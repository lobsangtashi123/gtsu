# Deploy Django to PythonAnywhere - Complete Guide

## ✅ No Credit Card Required!

---

## Step 1: Sign Up for PythonAnywhere

1. Go to https://www.pythonanywhere.com/registration/register/beginner/
2. Create a **free Beginner account**
3. Confirm your email address
4. Log in to your dashboard

---

## Step 2: Upload Your Code to GitHub

If you haven't already, push your code to GitHub:

```bash
cd /Users/lobsangtashi/Desktop/ngo-main

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit for deployment"

# Create a new repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## Step 3: Clone Your Code on PythonAnywhere

1. Go to your PythonAnywhere dashboard
2. Click on **"Consoles"** tab
3. Start a **Bash console**
4. Run these commands:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Go to project directory
cd YOUR_REPO_NAME

# Create virtual environment
python3.10 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 4: Set Up Database

```bash
# Still in the bash console, with venv activated
python manage.py migrate
python manage.py createsuperuser
```

---

## Step 5: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

---

## Step 6: Configure Web App

1. Go to **"Web"** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **Python 3.10**
5. Click **Next**

---

## Step 7: Configure WSGI File

1. On the Web tab, find **"Code"** section
2. Click on **WSGI configuration file** link
3. Delete everything and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'ngo.settings'

# Activate virtual environment
activate_this = '/home/YOUR_USERNAME/YOUR_REPO_NAME/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values!**

---

## Step 8: Configure Virtualenv

1. Still on the **Web** tab
2. Find **"Virtualenv"** section
3. Enter path: `/home/YOUR_USERNAME/YOUR_REPO_NAME/venv`
4. The virtualenv path should turn green

---

## Step 9: Configure Static Files

1. On the **Web** tab, find **"Static files"** section
2. Click **"Enter URL"** and add:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/YOUR_REPO_NAME/staticfiles`

3. Add another one:
   - URL: `/media/`
   - Directory: `/home/YOUR_USERNAME/YOUR_REPO_NAME/media`

---

## Step 10: Update Settings for PythonAnywhere

In your PythonAnywhere bash console:

```bash
cd /home/YOUR_USERNAME/YOUR_REPO_NAME
nano ngo/settings.py
```

Update these settings:

```python
# Add your PythonAnywhere domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com', 'localhost', '127.0.0.1']

# Update STATIC_ROOT
STATIC_ROOT = '/home/YOUR_USERNAME/YOUR_REPO_NAME/staticfiles'

# Update MEDIA_ROOT
MEDIA_ROOT = '/home/YOUR_USERNAME/YOUR_REPO_NAME/media'
```

Save and exit (Ctrl+X, then Y, then Enter)

---

## Step 11: Reload Your Web App

1. Go back to the **Web** tab
2. Click the big green **"Reload"** button at the top
3. Wait for it to finish reloading

---

## Step 12: Visit Your Site! 🎉

Your Django app is now live at:
**https://YOUR_USERNAME.pythonanywhere.com**

---

## Troubleshooting

### If you see an error:

1. Click **"Error log"** link on Web tab
2. Check for errors
3. Common fixes:
   - Make sure paths in WSGI file are correct
   - Verify virtualenv path
   - Check ALLOWED_HOSTS in settings.py
   - Make sure you ran `collectstatic`

### Update your code:

```bash
# In PythonAnywhere bash console
cd /home/YOUR_USERNAME/YOUR_REPO_NAME
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Then reload web app from Web tab
```

---

## Important Notes

**Free Tier Limitations:**
- Your domain: `YOUR_USERNAME.pythonanywhere.com`
- App sleeps after 3 months of inactivity
- Limited CPU seconds per day
- SQLite database only
- No scheduled tasks

**Perfect for:**
- Small projects
- Portfolio sites
- Testing/demo apps
- Learning Django deployment

---

## Need Help?

- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- PythonAnywhere Help: https://help.pythonanywhere.com/

---

**Your app is now deployed! 🚀**
