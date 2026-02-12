# 🚀 GitHub Pages Deployment - Step by Step

## Step 1: Create GitHub Repository

### Option A: Using Web Browser (Easiest)

1. Go to **https://github.com/new**
2. Fill in details:
   - **Repository name:** `budget-app`
   - **Description:** `Budget App - Track and analyze expenses with CSV import`
   - **Visibility:** Public (required for free GitHub Pages)
   - **Initialize repository:** Leave unchecked (we already have code)
3. Click **"Create repository"**

### Option B: Using GitHub CLI

```bash
# If you have GitHub CLI installed
gh repo create budget-app --public --source=. --remote=origin --push
```

---

## Step 2: Connect Local Repository to GitHub

Copy one of these commands from your GitHub repo page after creating it:

```bash
cd /Users/janani/Desktop/sitapp/budgetapp

# Add GitHub as remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/budget-app.git

# Rename default branch to main
git branch -M main

# Push code to GitHub
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/janani/budget-app.git
git branch -M main
git push -u origin main
```

---

## Step 3: Enable GitHub Pages

1. Go to your repository: `https://github.com/USERNAME/budget-app`
2. Click **Settings** (gear icon)
3. Left sidebar → Click **Pages**
4. Under "Build and deployment":
   - **Source:** Select "Deploy from a branch"
   - **Branch:** Select `main`
   - **Folder:** Select `/ (root)`
5. Click **Save**

---

## Step 4: Deploy Web App

The Flutter web app is already built. Now we need to move it to make GitHub Pages serve it:

```bash
cd /Users/janani/Desktop/sitapp/budgetapp

# Create docs folder (GitHub Pages default)
mkdir -p docs

# Copy built web app to docs folder
cp -r budgetui/build/web/* docs/

# Add, commit, and push
git add docs/
git commit -m "Deploy Budget App web version to GitHub Pages"
git push origin main
```

---

## Step 5: Access Your Live App

After pushing, wait **1-2 minutes** then visit:

```
https://USERNAME.github.io/budget-app/
```

**Example:**
```
https://janani.github.io/budget-app/
```

✅ Your app is now live!

---

## Step 6: (Optional) Custom Domain

To use your own domain instead:

1. In **Settings → Pages**
2. Under "Custom domain" enter your domain: `budget.example.com`
3. Add DNS records (instructions provided by GitHub)

---

## 📋 Complete Command Sequence

Run these commands in order:

```bash
cd /Users/janani/Desktop/sitapp/budgetapp

# 1. Create docs folder and copy web build
mkdir -p docs
cp -r budgetui/build/web/* docs/

# 2. Add web app files
git add docs/

# 3. Commit changes
git commit -m "Deploy Budget App web version to GitHub Pages"

# 4. Add GitHub remote (if not already added)
git remote add origin https://github.com/USERNAME/budget-app.git
git branch -M main

# 5. Push to GitHub
git push -u origin main
```

---

## ✅ Verify Deployment

```bash
# Check if files were pushed
git log --oneline

# Verify docs folder exists locally
ls -la docs/
```

---

## 🔄 Update Live App Later

To push updates:

```bash
# Rebuild web app
flutter clean
flutter pub get
flutter build web --release

# Copy to docs
cp -r budgetui/build/web/* docs/

# Push to GitHub
git add docs/
git commit -m "Update Budget App v1.0.1"
git push origin main
```

Wait 1-2 minutes, then refresh your app at: `https://USERNAME.github.io/budget-app/`

---

## 🆘 Troubleshooting

### "404 Not Found"
- Wait 2-3 minutes after pushing (GitHub needs time to publish)
- Check Pages is enabled in Settings
- Verify branch is set to `main` and folder is `/ (root)` in Pages settings

### "Docs folder not showing"
```bash
# List files
ls -la /Users/janani/Desktop/sitapp/budgetapp/

# Verify docs exists
ls -la /Users/janani/Desktop/sitapp/budgetapp/docs/
```

### "Push rejected"
```bash
# Update local repo with remote changes
git pull origin main

# Try push again
git push origin main
```

---

## 📊 Deployment Status

Track your deployment:

1. Go to **Actions** tab in your GitHub repo
2. Watch the workflow run
3. It should complete in ~30 seconds
4. Your app is live after it finishes!

---

**Ready?** Start with Step 1 above! 🎉
