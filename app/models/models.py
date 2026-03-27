from datetime import datetime
from extensions import db

class Lead(db.Model):
    """CRM Lead Model - Core of the business system"""
    __tablename__ = 'leads'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    business = db.Column(db.String(150))
    phone = db.Column(db.String(20))
    problem_description = db.Column(db.Text, nullable=False)
    
    # Status tracking
    status = db.Column(db.String(20), default='new')  # new, contacted, qualified, closed_won, closed_lost
    source = db.Column(db.String(50), default='website')  # website, referral, direct, etc.
    
    # Internal notes and tags
    notes = db.Column(db.Text)
    tags = db.Column(db.String(200))  # Comma-separated tags
    
    # Follow-up tracking
    last_contact = db.Column(db.DateTime)
    next_followup = db.Column(db.DateTime)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Lead {self.name} - {self.status}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'business': self.business,
            'phone': self.phone,
            'problem_description': self.problem_description,
            'status': self.status,
            'source': self.source,
            'notes': self.notes,
            'tags': self.tags,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class SaaSProduct(db.Model):
    """SaaS Product Model - Managed products displayed on SaaS Hub"""
    __tablename__ = 'saas_products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(200))
    
    # URLs
    demo_url = db.Column(db.String(200))
    site_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    
    # Pricing
    price_monthly = db.Column(db.Float)
    price_yearly = db.Column(db.Float)
    
    # Metadata
    version = db.Column(db.String(20))
    status = db.Column(db.String(20), default='active')  # active, coming_soon, beta, archived
    featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)  # Display order
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<SaaSProduct {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'short_description': self.short_description,
            'demo_url': self.demo_url,
            'site_url': self.site_url,
            'image_url': self.image_url,
            'price_monthly': self.price_monthly,
            'price_yearly': self.price_yearly,
            'version': self.version,
            'status': self.status,
            'featured': self.featured
        }


class BlogPost(db.Model):
    """Blog Post Model - SEO and authority building"""
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    
    # SEO
    meta_description = db.Column(db.String(160))
    meta_keywords = db.Column(db.String(200))
    
    # Publishing
    status = db.Column(db.String(20), default='draft')  # draft, published, archived
    published_at = db.Column(db.DateTime)
    
    # Analytics
    views = db.Column(db.Integer, default=0)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<BlogPost {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'excerpt': self.excerpt,
            'status': self.status,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'views': self.views
        }


class Subscriber(db.Model):
    """Email Subscriber Model - Newsletter system"""
    __tablename__ = 'subscribers'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100))
    
    # Subscription management
    status = db.Column(db.String(20), default='active')  # active, unsubscribed
    source = db.Column(db.String(50), default='website')
    
    # Segmentation
    tags = db.Column(db.String(200))
    
    # Timestamps
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)
    unsubscribed_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return f'<Subscriber {self.email}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'status': self.status,
            'subscribed_at': self.subscribed_at.isoformat() if self.subscribed_at else None
        }
