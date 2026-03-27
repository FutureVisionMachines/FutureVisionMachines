import re
from datetime import datetime

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def format_datetime(dt, format='%B %d, %Y'):
    """Format datetime object"""
    if dt is None:
        return ''
    return dt.strftime(format)

def get_status_badge_class(status):
    """Get CSS class for status badges"""
    status_classes = {
        'new': 'badge-primary',
        'contacted': 'badge-info',
        'qualified': 'badge-success',
        'closed_won': 'badge-success',
        'closed_lost': 'badge-secondary',
        'active': 'badge-success',
        'draft': 'badge-warning',
        'published': 'badge-success',
        'archived': 'badge-secondary',
        'coming_soon': 'badge-info',
        'beta': 'badge-warning'
    }
    return status_classes.get(status, 'badge-secondary')
