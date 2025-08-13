# 🚀 Deployment Guide for DSA Problem Solver

This guide will help you deploy your Flask application to various free hosting platforms.

## 🌟 **Option 1: Render (Recommended)**

### Step 1: Prepare Your Repository
1. Make sure all changes are committed and pushed to GitHub
2. Your repository should have these files:
   - `app.py` (main Flask app)
   - `requirements.txt` (with gunicorn)
   - `render.yaml` (deployment config)
   - `gunicorn.conf.py` (production config)

### Step 2: Deploy to Render
1. Go to [render.com](https://render.com) and sign up with GitHub
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select your `dsa-problem-solver` repository
5. Configure the service:
   - **Name**: `dsa-problem-solver`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click "Create Web Service"
7. Wait for deployment (usually 2-5 minutes)

### Step 3: Set Environment Variables
1. In your Render dashboard, go to your service
2. Click "Environment" tab
3. Add environment variable:
   - **Key**: `GROQ_API_KEY`
   - **Value**: Your actual Groq API key
4. Click "Save Changes"
5. Your service will automatically redeploy

### Step 4: Access Your Website
- Your website will be available at: `https://your-app-name.onrender.com`
- Render automatically provides HTTPS and handles scaling

---

## 🚄 **Option 2: Railway**

### Step 1: Deploy to Railway
1. Go to [railway.app](https://railway.app) and sign up with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will automatically detect it's a Python app
5. Add environment variable `GROQ_API_KEY` with your API key
6. Deploy!

---

## 🐍 **Option 3: PythonAnywhere**

### Step 1: Sign Up
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account

### Step 2: Upload Your Code
1. Go to "Files" tab
2. Upload your `app.py` and other files
3. Or clone from GitHub using the "Bash" console

### Step 3: Set Up Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.11 dsa-solver
pip install -r requirements.txt
```

### Step 4: Configure Web App
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Flask" and Python 3.11
4. Set source code directory to your project folder
5. Set WSGI configuration file to point to your app
6. Add environment variable for `GROQ_API_KEY`

---

## 🔧 **Production Considerations**

### Environment Variables
Make sure to set these in your hosting platform:
- `GROQ_API_KEY`: Your Groq API key
- `FLASK_ENV`: Set to `production`

### Security
- Never commit API keys to your repository
- Use environment variables for sensitive data
- Enable HTTPS (most platforms do this automatically)

### Performance
- Your app will sleep after inactivity on free tiers
- First request after sleep may take 10-30 seconds
- Consider upgrading to paid plans for production use

---

## 📱 **Custom Domain (Optional)**

### Render
1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain and follow DNS instructions

### Other Platforms
Most platforms support custom domains in their paid tiers.

---

## 🆘 **Troubleshooting**

### Common Issues:
1. **Import Errors**: Make sure all dependencies are in `requirements.txt`
2. **Port Issues**: Most platforms set `PORT` environment variable automatically
3. **API Key Errors**: Check environment variables are set correctly
4. **Build Failures**: Check build logs for specific error messages

### Getting Help:
- Check platform-specific documentation
- Look at build/deployment logs
- Ensure your app runs locally with `gunicorn app:app`

---

## 🎯 **Quick Start (Render)**

1. **Push your code to GitHub** (already done!)
2. **Go to [render.com](https://render.com)**
3. **Connect your GitHub account**
4. **Deploy your repository**
5. **Set `GROQ_API_KEY` environment variable**
6. **Wait for deployment**
7. **Access your website!**

Your DSA Problem Solver will be live on the internet! 🌐✨
