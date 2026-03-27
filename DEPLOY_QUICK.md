# Quick Deployment Commands

## Initial Setup (First Time Only)

### 1. Connect to Render
```bash
# Push code to GitHub
git add .
git commit -m "Initial commit"
git push origin master

# Go to Render Dashboard
# - New → Blueprint
# - Connect GitHub repo
# - Render detects render.yaml
# - Click "Apply"
```

### 2. Set Environment Variables in Render Dashboard
```
ADMIN_PASSWORD=5199152396aA!
MAIL_USERNAME=futurevisionmachines.com
MAIL_PASSWORD=icMsHW8b2hU7p2PT
```

### 3. Initialize Database (After First Deploy)
```python
# In Render Shell:
from app import create_app, db
app = create_app('production')
with app.app_context():
    db.create_all()
    print("✅ Database initialized!")
```

---

## Daily Deployment (Auto)

```bash
# 1. Make your changes locally
# 2. Commit and push
git add .
git commit -m "Your update message"
git push origin master

# 3. Render automatically deploys!
# - Watches master branch
# - Builds on push
# - Deploys with zero downtime
```

---

## Useful Commands

### Check Deployment Status
```bash
# View in Render Dashboard
# - Go to your service
# - Click "Logs" tab
# - See real-time deployment
```

### Access Render Shell
```bash
# From Render Dashboard:
# - Your Service → Shell
# - Opens Python/Bash terminal
# - Run commands directly
```

### Database Migration (When Changing Models)
```bash
# In Render Shell:
flask db migrate -m "Description of changes"
flask db upgrade
```

### View Logs
```bash
# Render Dashboard → Your Service → Logs
# Shows all application output
```

---

## Troubleshooting

### Build Failed
```bash
# Check Render logs for error
# Usually missing dependency or syntax error
# Fix locally, commit, push again
```

### Database Connection Error
```bash
# Verify DATABASE_URL is set
# Should auto-link from render.yaml
# Check database is running in Render
```

### Email Not Sending
```bash
# Verify environment variables:
MAIL_USERNAME=futurevisionmachines.com
MAIL_PASSWORD=icMsHW8b2hU7p2PT
MAIL_SERVER=mail.smtp2go.com
MAIL_PORT=2525
```

---

## Database Credentials

**PostgreSQL (Render)**
```
Host: dpg-d70b1rndiees73dhghvg-a.oregon-postgres.render.com
Database: fvm
User: fvm_user
Password: mWHJYbI4NWvNMCIeN9WHzNagyw9X6Mpy
Connection String: 
postgresql://fvm_user:mWHJYbI4NWvNMCIeN9WHzNagyw9X6Mpy@dpg-d70b1rndiees73dhghvg-a.oregon-postgres.render.com/fvm
```

**SMTP2GO Email**
```
Server: mail.smtp2go.com
Port: 2525
Username: futurevisionmachines.com
Password: icMsHW8b2hU7p2PT
Sender: info@futurevisionmachines.com
```

**Admin Access**
```
Password: 5199152396aA!
Path: /admin/login
```

---

## Quick Links

- 🌐 **Your App**: https://futurevisionmachines-website.onrender.com (after deploy)
- 📊 **Render Dashboard**: https://dashboard.render.com
- 📧 **SMTP2GO Dashboard**: https://app.smtp2go.com
- 🗃️ **Database**: Render → Databases → futurevisionmachines-db

---

## Rollback (If Needed)

```bash
# In Render Dashboard:
# - Go to your service
# - Click "Manual Deploy"
# - Select previous deployment
# - Click "Deploy"
```

---

## Custom Domain Setup

```bash
# 1. In Render Dashboard:
#    Settings → Custom Domains → Add Custom Domain
#    
# 2. Add DNS records at your domain registrar:
#    Type: CNAME
#    Name: www
#    Value: futurevisionmachines-website.onrender.com
#
# 3. Enable "Force HTTPS" in Render
```

---

## Success Checklist

After deployment, verify:
- [ ] Site loads at Render URL
- [ ] Database tables created
- [ ] Admin login works (/admin)
- [ ] Contact form submits
- [ ] Email sends (check SMTP2GO dashboard)
- [ ] Newsletter signup works
- [ ] All pages accessible

---

**Need Help?** Check [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md) for detailed guide.
