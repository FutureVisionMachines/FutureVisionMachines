from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from extensions import db
from app.models import Lead, SaaSProduct, BlogPost, Subscriber
from app.helpers.auth import admin_required, check_admin_password
from app.helpers.utils import slugify
from datetime import datetime
from sqlalchemy import func

admin_bp = Blueprint('admin', __name__)

# Authentication
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login (V1 simple password gate)"""
    if request.method == 'POST':
        password = request.form.get('password', '')
        
        if check_admin_password(password, current_app.config['ADMIN_PASSWORD']):
            session['admin_authenticated'] = True
            session.permanent = True
            flash('Welcome to the admin panel!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid password.', 'error')
    
    return render_template('admin/login.html')

@admin_bp.route('/logout')
def logout():
    """Admin logout"""
    session.pop('admin_authenticated', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('public.index'))

# Dashboard
@admin_bp.route('/')
@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    """Admin dashboard with key metrics"""
    # Get stats
    stats = {
        'total_leads': Lead.query.count(),
        'new_leads': Lead.query.filter_by(status='new').count(),
        'active_products': SaaSProduct.query.filter_by(status='active').count(),
        'published_posts': BlogPost.query.filter_by(status='published').count(),
        'total_subscribers': Subscriber.query.filter_by(status='active').count()
    }
    
    # Recent leads
    recent_leads = Lead.query.order_by(Lead.created_at.desc()).limit(5).all()
    
    # Lead status breakdown
    lead_breakdown = db.session.query(
        Lead.status, func.count(Lead.id)
    ).group_by(Lead.status).all()
    
    return render_template('admin/dashboard.html', 
                         stats=stats, 
                         recent_leads=recent_leads,
                         lead_breakdown=lead_breakdown)

# CRM System
@admin_bp.route('/crm')
@admin_required
def crm():
    """CRM - Lead management"""
    status_filter = request.args.get('status', 'all')
    
    query = Lead.query
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
    
    leads = query.order_by(Lead.created_at.desc()).all()
    
    return render_template('admin/crm.html', leads=leads, current_status=status_filter)

@admin_bp.route('/crm/<int:lead_id>')
@admin_required
def crm_detail(lead_id):
    """CRM - Lead detail view"""
    lead = Lead.query.get_or_404(lead_id)
    return render_template('admin/crm_detail.html', lead=lead)

@admin_bp.route('/crm/<int:lead_id>/update', methods=['POST'])
@admin_required
def crm_update(lead_id):
    """CRM - Update lead"""
    lead = Lead.query.get_or_404(lead_id)
    
    lead.status = request.form.get('status', lead.status)
    lead.notes = request.form.get('notes', lead.notes)
    lead.tags = request.form.get('tags', lead.tags)
    lead.phone = request.form.get('phone', lead.phone)
    
    # Update contact tracking
    if request.form.get('mark_contacted'):
        lead.last_contact = datetime.utcnow()
    
    lead.updated_at = datetime.utcnow()
    db.session.commit()
    
    flash('Lead updated successfully!', 'success')
    return redirect(url_for('admin.crm_detail', lead_id=lead_id))

@admin_bp.route('/crm/<int:lead_id>/delete', methods=['POST'])
@admin_required
def crm_delete(lead_id):
    """CRM - Delete lead"""
    lead = Lead.query.get_or_404(lead_id)
    db.session.delete(lead)
    db.session.commit()
    
    flash('Lead deleted successfully.', 'success')
    return redirect(url_for('admin.crm'))

# SaaS Manager
@admin_bp.route('/saas')
@admin_required
def saas_manager():
    """SaaS product manager"""
    products = SaaSProduct.query.order_by(SaaSProduct.order.asc()).all()
    return render_template('admin/saas_manager.html', products=products)

@admin_bp.route('/saas/create', methods=['GET', 'POST'])
@admin_required
def saas_create():
    """Create new SaaS product"""
    if request.method == 'POST':
        product = SaaSProduct(
            name=request.form.get('name'),
            slug=slugify(request.form.get('name')),
            description=request.form.get('description'),
            short_description=request.form.get('short_description'),
            demo_url=request.form.get('demo_url'),
            site_url=request.form.get('site_url'),
            image_url=request.form.get('image_url'),
            price_monthly=float(request.form.get('price_monthly', 0) or 0),
            price_yearly=float(request.form.get('price_yearly', 0) or 0),
            version=request.form.get('version'),
            status=request.form.get('status', 'active'),
            featured=bool(request.form.get('featured'))
        )
        
        db.session.add(product)
        db.session.commit()
        
        flash('SaaS product created successfully!', 'success')
        return redirect(url_for('admin.saas_manager'))
    
    return render_template('admin/saas_form.html', product=None)

@admin_bp.route('/saas/<int:product_id>/edit', methods=['GET', 'POST'])
@admin_required
def saas_edit(product_id):
    """Edit SaaS product"""
    product = SaaSProduct.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.slug = slugify(request.form.get('name'))
        product.description = request.form.get('description')
        product.short_description = request.form.get('short_description')
        product.demo_url = request.form.get('demo_url')
        product.site_url = request.form.get('site_url')
        product.image_url = request.form.get('image_url')
        product.price_monthly = float(request.form.get('price_monthly', 0) or 0)
        product.price_yearly = float(request.form.get('price_yearly', 0) or 0)
        product.version = request.form.get('version')
        product.status = request.form.get('status', 'active')
        product.featured = bool(request.form.get('featured'))
        product.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('SaaS product updated successfully!', 'success')
        return redirect(url_for('admin.saas_manager'))
    
    return render_template('admin/saas_form.html', product=product)

@admin_bp.route('/saas/<int:product_id>/delete', methods=['POST'])
@admin_required
def saas_delete(product_id):
    """Delete SaaS product"""
    product = SaaSProduct.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    flash('SaaS product deleted successfully.', 'success')
    return redirect(url_for('admin.saas_manager'))

# Blog Manager
@admin_bp.route('/blog')
@admin_required
def blog_manager():
    """Blog post manager"""
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('admin/blog_manager.html', posts=posts)

@admin_bp.route('/blog/create', methods=['GET', 'POST'])
@admin_required
def blog_create():
    """Create new blog post"""
    if request.method == 'POST':
        post = BlogPost(
            title=request.form.get('title'),
            slug=slugify(request.form.get('title')),
            content=request.form.get('content'),
            excerpt=request.form.get('excerpt'),
            meta_description=request.form.get('meta_description'),
            meta_keywords=request.form.get('meta_keywords'),
            status=request.form.get('status', 'draft')
        )
        
        if post.status == 'published' and not post.published_at:
            post.published_at = datetime.utcnow()
        
        db.session.add(post)
        db.session.commit()
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('admin.blog_manager'))
    
    return render_template('admin/blog_form.html', post=None)

@admin_bp.route('/blog/<int:post_id>/edit', methods=['GET', 'POST'])
@admin_required
def blog_edit(post_id):
    """Edit blog post"""
    post = BlogPost.query.get_or_404(post_id)
    
    if request.method == 'POST':
        old_status = post.status
        
        post.title = request.form.get('title')
        post.slug = slugify(request.form.get('title'))
        post.content = request.form.get('content')
        post.excerpt = request.form.get('excerpt')
        post.meta_description = request.form.get('meta_description')
        post.meta_keywords = request.form.get('meta_keywords')
        post.status = request.form.get('status', 'draft')
        post.updated_at = datetime.utcnow()
        
        # Set published_at if changing to published
        if post.status == 'published' and old_status != 'published':
            post.published_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('admin.blog_manager'))
    
    return render_template('admin/blog_form.html', post=post)

@admin_bp.route('/blog/<int:post_id>/delete', methods=['POST'])
@admin_required
def blog_delete(post_id):
    """Delete blog post"""
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    
    flash('Blog post deleted successfully.', 'success')
    return redirect(url_for('admin.blog_manager'))

# Subscribers
@admin_bp.route('/subscribers')
@admin_required
def subscribers():
    """Subscriber management"""
    subs = Subscriber.query.order_by(Subscriber.subscribed_at.desc()).all()
    return render_template('admin/subscribers.html', subscribers=subs)

@admin_bp.route('/subscribers/<int:subscriber_id>/delete', methods=['POST'])
@admin_required
def subscriber_delete(subscriber_id):
    """Delete subscriber"""
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    db.session.delete(subscriber)
    db.session.commit()
    
    flash('Subscriber deleted successfully.', 'success')
    return redirect(url_for('admin.subscribers'))

# Email Campaigns
@admin_bp.route('/campaigns')
@admin_required
def campaigns():
    """Email campaign manager"""
    active_subscribers = Subscriber.query.filter_by(status='active').all()
    
    # Email templates available
    templates = [
        {
            'id': 'newsletter',
            'name': 'Newsletter Update',
            'description': 'Regular newsletter with company updates',
            'icon': '📰'
        },
        {
            'id': 'product_launch',
            'name': 'Product Launch',
            'description': 'Announce new product or feature',
            'icon': '🚀'
        },
        {
            'id': 'special_offer',
            'name': 'Special Offer',
            'description': 'Promotional email with special pricing',
            'icon': '💰'
        },
        {
            'id': 'company_update',
            'name': 'Company Update',
            'description': 'Share company news and milestones',
            'icon': '📢'
        },
        {
            'id': 'custom',
            'name': 'Custom Email',
            'description': 'Create fully custom email content',
            'icon': '✍️'
        }
    ]
    
    return render_template('admin/campaigns.html', 
                         subscribers=active_subscribers,
                         templates=templates)

@admin_bp.route('/campaigns/send', methods=['POST'])
@admin_required
def campaign_send():
    """Send email campaign to subscribers"""
    from app.helpers.email_helper import send_campaign_email
    
    # Get form data
    subject = request.form.get('subject', '').strip()
    template_id = request.form.get('template_id', 'custom')
    recipient_type = request.form.get('recipient_type', 'all')
    selected_ids = request.form.getlist('selected_subscribers')
    
    # Custom content (for custom template)
    custom_title = request.form.get('custom_title', '')
    custom_content = request.form.get('custom_content', '')
    custom_cta_text = request.form.get('custom_cta_text', '')
    custom_cta_url = request.form.get('custom_cta_url', '')
    
    # Template-specific content
    template_content = {
        'title': request.form.get('content_title', custom_title),
        'content': request.form.get('content_body', custom_content),
        'cta_text': request.form.get('cta_text', custom_cta_text),
        'cta_url': request.form.get('cta_url', custom_cta_url),
        'feature_1': request.form.get('feature_1', ''),
        'feature_2': request.form.get('feature_2', ''),
        'feature_3': request.form.get('feature_3', ''),
        'offer_details': request.form.get('offer_details', '')
    }
    
    # Validation
    if not subject:
        flash('Subject is required.', 'error')
        return redirect(url_for('admin.campaigns'))
    
    # Get subscribers based on selection
    if recipient_type == 'selected' and selected_ids:
        subscribers = Subscriber.query.filter(
            Subscriber.id.in_(selected_ids),
            Subscriber.status == 'active'
        ).all()
    else:
        subscribers = Subscriber.query.filter_by(status='active').all()
    
    if not subscribers:
        flash('No subscribers selected or available.', 'error')
        return redirect(url_for('admin.campaigns'))
    
    # Send emails
    success_count = 0
    fail_count = 0
    
    for subscriber in subscribers:
        try:
            result = send_campaign_email(
                subscriber=subscriber,
                subject=subject,
                template_id=template_id,
                content=template_content
            )
            if result:
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            current_app.logger.error(f"Campaign email failed for {subscriber.email}: {str(e)}")
            fail_count += 1
    
    # Flash result
    if success_count > 0:
        flash(f'Campaign sent successfully to {success_count} subscriber(s)!', 'success')
    if fail_count > 0:
        flash(f'{fail_count} email(s) failed to send.', 'error')
    
    return redirect(url_for('admin.campaigns'))

@admin_bp.route('/campaigns/preview', methods=['POST'])
@admin_required
def campaign_preview():
    """Preview campaign email"""
    from app.helpers.email_helper import render_campaign_template
    
    template_id = request.form.get('template_id', 'custom')
    subject = request.form.get('subject', 'Preview Email')
    
    template_content = {
        'title': request.form.get('content_title', ''),
        'content': request.form.get('content_body', ''),
        'cta_text': request.form.get('cta_text', ''),
        'cta_url': request.form.get('cta_url', ''),
        'feature_1': request.form.get('feature_1', ''),
        'feature_2': request.form.get('feature_2', ''),
        'feature_3': request.form.get('feature_3', ''),
        'offer_details': request.form.get('offer_details', '')
    }
    
    # Create preview subscriber
    preview_subscriber = type('obj', (object,), {
        'email': 'preview@example.com',
        'subscribed_at': datetime.utcnow()
    })
    
    html_content = render_campaign_template(
        template_id=template_id,
        subscriber=preview_subscriber,
        content=template_content
    )
    
    return render_template('admin/campaign_preview.html',
                         subject=subject,
                         html_content=html_content)
