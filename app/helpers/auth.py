from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    """Decorator to require admin authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_authenticated'):
            flash('Please log in to access the admin panel.', 'error')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

def check_admin_password(password, correct_password):
    """Simple password check for V1 admin gate"""
    return password == correct_password
