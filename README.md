# FutureVisionMachines Website

**Enterprise-grade software solutions, made accessible to everyone.**

A complete dual-system platform featuring a public marketing site and internal admin panel with CRM, SaaS management, blog system, and email integration.

---

## 🚀 Quick Start

### 1. Setup Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and configure:

```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=development

# Database (start with SQLite, upgrade to PostgreSQL later)
DATABASE_URL=sqlite:///fvm.db

# Admin Password (CHANGE THIS!)
ADMIN_PASSWORD=your-secure-admin-password

# Email (SMTP2GO)
MAIL_SERVER=mail.smtp2go.com
MAIL_PORT=2525
MAIL_USERNAME=your-smtp2go-username
MAIL_PASSWORD=your-smtp2go-password
MAIL_DEFAULT_SENDER=noreply@futurevisionmachines.com
```

### 3. Initialize Database

```powershell
# The database will be created automatically on first run
python run.py
```

### 4. Access the Application

- **Public Site**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin

**Default Admin Password**: Set in your `.env` file (ADMIN_PASSWORD)

---

## 📁 Project Structure

```
FutureVisionMachines-Website/
├── app/
│   ├── __init__.py           # App factory
│   ├── models/
│   │   └── models.py         # Database models
│   ├── routes/
│   │   ├── public.py         # Public routes
│   │   └── admin.py          # Admin routes
│   ├── helpers/
│   │   ├── auth.py           # Authentication helpers
│   │   ├── email_helper.py   # Email functions
│   │   └── utils.py          # Utility functions
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── public/           # Public pages
│   │   ├── admin/            # Admin pages
│   │   └── emails/           # Email templates
│   └── static/
│       ├── css/              # Stylesheets
│       └── js/               # JavaScript
├── config.py                 # Configuration
├── extensions.py             # Flask extensions
├── run.py                    # Application entry point
└── requirements.txt          # Dependencies
```

---

## 🎨 Brand System

### Colors
- **Primary**: Cyan (#00E5FF)
- **Secondary**: Electric Purple (#7B61FF)
- **Background**: True Black (#050505)
- **Surface**: #0A0A0A / #111
- **Text**: #EAEAEA / #A0A0A0

### Design Language
- Glassmorphism panels
- Subtle neon glows
- Micro-animations
- Grid-based layouts

---

## 📊 Core Features

### Public Site
- ✅ Home page with hero section
- ✅ About page
- ✅ Services page
- ✅ SaaS products hub
- ✅ Blog system
- ✅ Contact form → CRM integration
- ✅ Newsletter subscription
- ✅ Legal pages (Terms, Privacy, Security, Cookies)

### Admin Panel
- ✅ Dashboard with key metrics
- ✅ **CRM System** (Lead management)
  - View all leads
  - Filter by status
  - Update lead information
  - Add notes and tags
  - Track follow-ups
- ✅ **SaaS Manager** (Create/Edit/Delete products)
- ✅ **Blog Manager** (Create/Edit/Delete posts)
- ✅ **Subscriber Management**
- ✅ Email notifications (SMTP2GO integration)

---

## 📧 Email Setup (SMTP2GO)

1. Sign up at [SMTP2GO](https://www.smtp2go.com/)
2. Get your SMTP credentials
3. Add to `.env` file
4. Test by submitting a contact form

### Email Templates
- Lead notification (to admin)
- Auto-response (to lead)

---

## 🗄️ Database Models

### Lead (CRM)
```python
- id, name, email, business, phone
- problem_description
- status (new, contacted, qualified, closed_won, closed_lost)
- notes, tags
- timestamps
```

### SaaSProduct
```python
- id, name, slug, description
- demo_url, site_url, image_url
- pricing (monthly/yearly)
- version, status
```

### BlogPost
```python
- id, title, slug, content
- meta_description, meta_keywords
- status (draft, published, archived)
- views, timestamps
```

### Subscriber
```python
- id, email, name
- status (active, unsubscribed)
- timestamps
```

---

## 🚢 Deployment

### Development
```powershell
python run.py
```

### Production - Render (RECOMMENDED)

**✨ Auto-deployment enabled!** Every `git push` to master automatically deploys.

#### Quick Deploy

1. **Connect Repository to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - New → Blueprint
   - Connect your GitHub repository
   - Render auto-detects `render.yaml`

2. **Set Sensitive Environment Variables**
   ```bash
   ADMIN_PASSWORD=your-secure-password
   MAIL_USERNAME=your-smtp-username
   MAIL_PASSWORD=your-smtp-password
   ```

3. **Deploy!**
   - Click "Apply"
   - Render creates database & web service
   - Auto-deployment configured

#### Database Setup
PostgreSQL database included in `render.yaml`:
- **Name**: futurevisionmachines-db
- **Region**: Oregon
- **Plan**: Free
- Auto-linked to web service

#### After First Deployment
Initialize database tables via Render Shell:
```python
from app import create_app, db
app = create_app('production')
with app.app_context():
    db.create_all()
```

📖 **Full Guide**: See [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md) for complete instructions.

### Production (Manual - Gunicorn)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app('production')"
```

### Production Checklist
- [x] ✅ Render deployment configured
- [x] ✅ PostgreSQL database set up
- [x] ✅ Auto-deployment enabled (git push)
- [ ] Set strong `ADMIN_PASSWORD`
- [ ] Initialize database tables
- [ ] Test email sending (SMTP2GO)
- [ ] Configure custom domain (optional)
- [ ] Enable HTTPS (auto on Render)

### Hosting Options
- **Render** ⭐ (Recommended - Auto-deployment, free tier)
- **DigitalOcean** (Full VPS control)
- **Heroku** (Simple but paid)

### Auto-Deployment Workflow
```bash
# Make changes
git add .
git commit -m "Update features"
git push origin master

# Render automatically:
# 1. Detects push
# 2. Runs build script
# 3. Deploys new version
# 4. Zero downtime deployment
```

---

## 🔐 Security Notes

### V1 Admin Authentication
Currently using simple password gate. For production:
- Use a **strong, unique password**
- Consider adding IP whitelist
- Plan to implement full user auth system in future

### Important
- Never commit `.env` file
- Rotate secrets regularly
- Monitor admin access logs

---

## 📈 Roadmap

### Phase 1 (DONE ✅)
- Home, About, Services, Contact
- CRM system
- Basic admin panel

### Phase 2 
- SaaS product launches
- Blog content creation
- Email campaigns

### Phase 3
- Analytics dashboard
- Advanced CRM features
- Multi-user admin access

### Phase 4
- API development
- Automation workflows
- Advanced reporting

---

## 🛠️ Development

### Adding a New Page
1. Create route in `app/routes/public.py` or `admin.py`
2. Create template in `app/templates/`
3. Add navigation link in `base.html`

### Adding a Database Model
1. Add model to `app/models/models.py`
2. Run migrations:
```powershell
flask db migrate -m "Description"
flask db upgrade
```

---

## 📞 Support

For questions or issues:
- **Email**: anthony@futurevisionmachines.com
- **Location**: Edmonton, Alberta, Canada

---

## 📄 License

Copyright © 2026 FutureVisionMachines. All rights reserved.

---

**Built with Flask | Designed for Scale | Ready to Launch**
