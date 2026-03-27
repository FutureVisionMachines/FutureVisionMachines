from flask_mail import Message
from flask import render_template, current_app
from extensions import mail

def send_email(subject, recipients, text_body, html_body):
    """Send email using Flask-Mail"""
    try:
        msg = Message(subject, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.error(f"Email send error: {str(e)}")
        return False

def send_lead_notification(lead):
    """Send notification when new lead is received"""
    subject = f"New Lead: {lead.name} from {lead.business or 'Unknown Business'}"
    
    text_body = f"""
New lead received:

Name: {lead.name}
Email: {lead.email}
Business: {lead.business or 'Not provided'}
Phone: {lead.phone or 'Not provided'}

Problem Description:
{lead.problem_description}

View in CRM: {current_app.config['COMPANY_EMAIL']}
"""
    
    html_body = render_template('emails/lead_notification.html', lead=lead)
    
    return send_email(
        subject=subject,
        recipients=[current_app.config['COMPANY_EMAIL']],
        text_body=text_body,
        html_body=html_body
    )

def send_lead_response(lead):
    """Send automated response to lead"""
    subject = "Thanks for reaching out to FutureVisionMachines"
    
    text_body = f"""
Hi {lead.name},

Thank you for reaching out to FutureVisionMachines. We've received your inquiry and will review it shortly.

We'll get back to you within 24-48 hours to discuss how we can help solve your challenges.

Best regards,
Anthony Dinunzio
Founder, FutureVisionMachines

---
FutureVisionMachines
Enterprise-grade software solutions, made accessible to everyone.
Edmonton, Alberta, Canada
"""
    
    html_body = render_template('emails/lead_response.html', lead=lead)
    
    return send_email(
        subject=subject,
        recipients=[lead.email],
        text_body=text_body,
        html_body=html_body
    )

def render_campaign_template(template_id, subscriber, content):
    """Render campaign email template"""
    template_map = {
        'newsletter': 'emails/campaign_newsletter.html',
        'product_launch': 'emails/campaign_product_launch.html',
        'special_offer': 'emails/campaign_special_offer.html',
        'company_update': 'emails/campaign_company_update.html',
        'custom': 'emails/campaign_custom.html'
    }
    
    template_file = template_map.get(template_id, 'emails/campaign_custom.html')
    
    return render_template(template_file, 
                         subscriber=subscriber,
                         content=content)

def send_campaign_email(subscriber, subject, template_id, content):
    """Send campaign email to subscriber"""
    try:
        html_body = render_campaign_template(template_id, subscriber, content)
        
        # Generate text version
        text_body = f"""
{content.get('title', 'Update from FutureVisionMachines')}

{content.get('content', '')}

{content.get('cta_text', 'Learn More')}: {content.get('cta_url', '')}

---
You're receiving this because you subscribed to FutureVisionMachines updates.
Unsubscribe: [Your unsubscribe link]

FutureVisionMachines
Enterprise-grade software solutions
"""
        
        return send_email(
            subject=subject,
            recipients=[subscriber.email],
            text_body=text_body,
            html_body=html_body
        )
    except Exception as e:
        current_app.logger.error(f"Campaign email error: {str(e)}")
        return False
