// FutureVisionMachines - Admin Panel JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Flash messages (same as main.js but repeated for admin context)
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(flash => {
        const closeBtn = flash.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                flash.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => flash.remove(), 300);
            });
        }
        
        setTimeout(() => {
            if (flash.parentElement) {
                flash.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => flash.remove(), 300);
            }
        }, 5000);
    });
    
    // Confirm delete actions
    const deleteForms = document.querySelectorAll('form[action*="delete"]');
    deleteForms.forEach(form => {
        if (!form.hasAttribute('onsubmit')) {
            form.addEventListener('submit', function(e) {
                if (!confirm('Are you sure you want to delete this item?')) {
                    e.preventDefault();
                }
            });
        }
    });
    
    // Auto-resize textareas
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
    
    // Highlight current nav link
    const currentPath = window.location.pathname;
    const sidebarLinks = document.querySelectorAll('.sidebar-link');
    sidebarLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.style.background = 'rgba(0, 229, 255, 0.2)';
            link.style.color = 'var(--color-primary)';
        }
    });
});
