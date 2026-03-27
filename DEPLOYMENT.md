# 🚀 FutureVisionMachines - Deployment Guide

## Deploy TODAY - Production Ready

This guide will get your site live in under 30 minutes.

---

## Option 1: Quick Deploy to Render (RECOMMENDED)

### Step 1: Prepare Your Repository

```powershell
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit - FutureVisionMachines complete system"

# Push to GitHub
# Create a new repository on GitHub first, then:
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Render

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: futurevisionmachines
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn "app:create_app('production')"`
   - **Instance Type**: Free (to start)

### Step 3: Add Environment Variables

In Render dashboard, add these environment variables:

```
SECRET_KEY=<generate-a-strong-secret-key>
FLASK_ENV=production
DATABASE_URL=<render-will-provide-if-using-postgres>
ADMIN_PASSWORD=<your-secure-admin-password>

MAIL_SERVER=mail.smtp2go.com
MAIL_PORT=2525
MAIL_USERNAME=<your-smtp2go-username>
MAIL_PASSWORD=<your-smtp2go-password>
MAIL_DEFAULT_SENDER=noreply@futurevisionmachines.com
```

### Step 4: Add PostgreSQL Database (Optional but recommended)

1. In Render dashboard, create a new PostgreSQL database
2. Copy the "Internal Database URL"
3. Set it as `DATABASE_URL` in your web service environment variables

### Step 5: Deploy!

Click "Create Web Service" and wait ~5 minutes for deployment.

Your site will be live at: `https://futurevisionmachines.onrender.com`

---

## Option 2: Deploy to DigitalOcean

### Requirements
- DigitalOcean account
- Domain name (optional but recommended)

### Steps

1. **Create Droplet**
   - Ubuntu 22.04 LTS
   - $6/month plan minimum
   - Add SSH key

2. **SSH into server**
```bash
ssh root@your-server-ip
```

3. **Setup server**
```bash
# Update system
apt update && apt upgrade -y

# Install Python and dependencies
apt install python3 python3-pip python3-venv nginx postgresql -y

# Create app user
adduser fvm
usermod -aG sudo fvm
su - fvm
```

4. **Deploy application**
```bash
# Clone repository
git clone <your-repo-url>
cd FutureVisionMachines-Website

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
nano .env
# Add all environment variables

# Setup PostgreSQL
sudo -u postgres psql
CREATE DATABASE fvm;
CREATE USER fvmuser WITH PASSWORD 'secure-password';
GRANT ALL PRIVILEGES ON DATABASE fvm TO fvmuser;
\q

# Update DATABASE_URL in .env
DATABASE_URL=postgresql://fvmuser:secure-password@localhost/fvm
```

5. **Setup Gunicorn service**
```bash
sudo nano /etc/systemd/system/fvm.service
```

Add:
```ini
[Unit]
Description=FutureVisionMachines
After=network.target

[Service]
User=fvm
WorkingDirectory=/home/fvm/FutureVisionMachines-Website
Environment="PATH=/home/fvm/FutureVisionMachines-Website/venv/bin"
ExecStart=/home/fvm/FutureVisionMachines-Website/venv/bin/gunicorn -w 4 -b 127.0.0.1:5000 "app:create_app('production')"

[Install]
WantedBy=multi-user.target
```

6. **Setup Nginx**
```bash
sudo nano /etc/nginx/sites-available/fvm
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /home/fvm/FutureVisionMachines-Website/app/static;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/fvm /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

7. **Start services**
```bash
sudo systemctl start fvm
sudo systemctl enable fvm
```

---

## Email Setup (SMTP2GO)

### Required for Lead Notifications

1. Sign up at [SMTP2GO](https://www.smtp2go.com/)
2. Verify your email
3. Get SMTP credentials from dashboard
4. Add to environment variables
5. Test by submitting a contact form

---

## Domain Setup

### Point Domain to Your Site

#### For Render:
1. In Render dashboard, go to your web service
2. Add custom domain
3. Update your domain's DNS:
   - Add CNAME record pointing to your Render URL

#### For DigitalOcean:
1. In your domain registrar (Cloudflare, etc.):
   - Add A record pointing to your droplet IP
   - Wait for DNS propagation (5-30 minutes)

---

## SSL Certificate (HTTPS)

### Render
- Automatically provided when you add a custom domain

### DigitalOcean
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Post-Deployment Checklist

- [ ] Site loads correctly
- [ ] All pages accessible
- [ ] Contact form works and sends emails
- [ ] Admin panel accessible at /admin
- [ ] Can log into admin with your password
- [ ] Can create/edit/delete content via admin
- [ ] Newsletter subscription works
- [ ] Email notifications working
- [ ] SSL certificate active (HTTPS)
- [ ] Update admin password to something strong
- [ ] Test on mobile devices

---

## Monitoring & Maintenance

### Check Site Health
- Monitor uptime
- Check error logs regularly
- Test contact form weekly
- Backup database regularly

### Updates
```bash
# Pull latest changes
git pull origin main

# Restart service
sudo systemctl restart fvm
```

---

## Troubleshooting

### Site not loading
- Check service status: `sudo systemctl status fvm`
- Check logs: `sudo journalctl -u fvm -n 50`
- Check Nginx: `sudo nginx -t`

### Database errors
- Verify DATABASE_URL is correct
- Check PostgreSQL is running: `sudo systemctl status postgresql`

### Email not sending
- Verify SMTP2GO credentials
- Check email quotas in SMTP2GO dashboard
- Test with a different email address

---

## Going Live Workflow

1. ✅ Complete deployment (Render recommended for speed)
2. ✅ Configure email (SMTP2GO)
3. ✅ Test all features
4. ✅ Add custom domain
5. ✅ Enable HTTPS
6. ✅ Update company email signature with website link
7. ✅ Start driving traffic!

---

**Need Help?**
- Email: anthony@futurevisionmachines.com
- Check logs first
- Google the error message
- Post on Stack Overflow

---

**You're ready to launch! 🚀**
