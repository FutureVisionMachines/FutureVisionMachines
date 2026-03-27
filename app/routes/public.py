from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db, limiter
from app.models import Lead, SaaSProduct, BlogPost, Subscriber
from app.helpers.email_helper import send_lead_notification, send_lead_response
from datetime import datetime

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def index():
    """Home page"""
    return render_template('public/index.html')

@public_bp.route('/about')
def about():
    """About page"""
    return render_template('public/about.html')

@public_bp.route('/services')
def services():
    """Services page"""
    return render_template('public/services.html')

@public_bp.route('/saas')
def saas_hub():
    """SaaS products hub"""
    products = SaaSProduct.query.filter_by(status='active').order_by(
        SaaSProduct.featured.desc(), 
        SaaSProduct.order.asc()
    ).all()
    return render_template('public/saas_hub.html', products=products)

@public_bp.route('/contact', methods=['GET', 'POST'])
@limiter.limit("5 per hour")
def contact():
    """Contact form"""
    if request.method == 'POST':
        try:
            # Create lead
            lead = Lead(
                name=request.form.get('name', '').strip(),
                email=request.form.get('email', '').strip(),
                business=request.form.get('business', '').strip(),
                phone=request.form.get('phone', '').strip(),
                problem_description=request.form.get('problem_description', '').strip(),
                source='website'
            )
            
            # Validation
            if not lead.name or not lead.email or not lead.problem_description:
                flash('Please fill in all required fields.', 'error')
                return render_template('public/contact.html')
            
            # Save to database
            db.session.add(lead)
            db.session.commit()
            
            # Send notifications
            send_lead_notification(lead)
            send_lead_response(lead)
            
            flash('Thank you for reaching out! We\'ll get back to you within 24-48 hours.', 'success')
            return redirect(url_for('public.index'))
            
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'error')
            return render_template('public/contact.html')
    
    return render_template('public/contact.html')

@public_bp.route('/blog')
def blog():
    """Blog listing"""
    posts = BlogPost.query.filter_by(status='published').order_by(
        BlogPost.published_at.desc()
    ).all()
    return render_template('public/blog.html', posts=posts)

@public_bp.route('/blog/<slug>')
def blog_post(slug):
    """Individual blog post"""
    post = BlogPost.query.filter_by(slug=slug, status='published').first_or_404()
    
    # Increment view count
    post.views += 1
    db.session.commit()
    
    return render_template('public/blog_post.html', post=post)

@public_bp.route('/subscribe', methods=['POST'])
@limiter.limit("3 per hour")
def subscribe():
    """Newsletter subscription"""
    email = request.form.get('email', '').strip()
    
    if not email:
        flash('Please enter a valid email address.', 'error')
        return redirect(request.referrer or url_for('public.index'))
    
    # Check if already subscribed
    existing = Subscriber.query.filter_by(email=email).first()
    if existing:
        if existing.status == 'active':
            flash('You\'re already subscribed!', 'info')
        else:
            existing.status = 'active'
            existing.subscribed_at = datetime.utcnow()
            db.session.commit()
            flash('Welcome back! You\'re subscribed again.', 'success')
    else:
        subscriber = Subscriber(email=email)
        db.session.add(subscriber)
        db.session.commit()
        flash('Successfully subscribed to our newsletter!', 'success')
    
    return redirect(request.referrer or url_for('public.index'))

# Legal pages
@public_bp.route('/terms')
def terms():
    """Terms of Service"""
    return render_template('public/legal/terms.html')

@public_bp.route('/privacy')
def privacy():
    """Privacy Policy"""
    return render_template('public/legal/privacy.html')

@public_bp.route('/security')
def security():
    """Security Policy"""
    return render_template('public/legal/security.html')

@public_bp.route('/cookies')
def cookies():
    """Cookie Policy"""
    return render_template('public/legal/cookies.html')
