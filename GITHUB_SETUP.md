# 🚀 GitHub Setup Guide

## Before pushing to GitHub

### 1. Check .gitignore

Make sure `.gitignore` is properly configured:
```bash
cat .gitignore
```

Should include:
- `venv/` - virtual environment
- `.env` - API keys
- `__pycache__/` - Python cache
- `*.pyc` - compiled Python files

### 2. Remove sensitive data

**IMPORTANT:** Never commit your API key!

Check if `.env` is ignored:
```bash
git status
```

If you see `.env` in the list, add it to `.gitignore`:
```bash
echo ".env" >> .gitignore
```

### 3. Create .env.example

Already created! This file shows the structure without actual keys:
```bash
cat .env.example
```

---

## Pushing to GitHub

### First time setup

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Check what will be committed
git status

# Make sure .env is NOT in the list!

# Commit
git commit -m "Initial commit: Solodit API Client"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push
git push -u origin main
```

### Subsequent updates

```bash
# Add changes
git add .

# Commit
git commit -m "Your commit message"

# Push
git push
```

---

## For users cloning your repo

### Setup instructions for others

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API key:
```bash
# Copy example file
cp .env.example .env

# Edit .env and add your API key
nano .env  # or use any text editor
```

5. Test:
```bash
python scripts/quick_test.py
```

---

## What gets committed to GitHub

✅ **Will be committed:**
- Source code (`src/`)
- Scripts (`scripts/`)
- Examples (`examples/`)
- Documentation (`docs/`, `*.md`)
- Configuration files (`requirements.txt`, `.gitignore`)
- `.env.example` (without real API key)

❌ **Will NOT be committed:**
- `venv/` - virtual environment
- `.env` - your API key
- `__pycache__/` - Python cache
- `*.pyc` - compiled files
- `*.log` - log files
- IDE settings (`.vscode/`, `.idea/`)

---

## Security checklist

Before pushing:

- [ ] `.env` is in `.gitignore`
- [ ] `.env` is NOT in `git status`
- [ ] `.env.example` exists (without real key)
- [ ] No API keys in code
- [ ] No sensitive data in comments
- [ ] `venv/` is ignored
- [ ] `__pycache__/` is ignored

---

## If you accidentally committed .env

If you already committed `.env` with your API key:

### 1. Remove from git (keep local file)
```bash
git rm --cached .env
git commit -m "Remove .env from git"
git push
```

### 2. Change your API key
Go to https://solodit.cyfrin.io and generate a new API key!

### 3. Update .gitignore
```bash
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to .gitignore"
git push
```

---

## GitHub repository settings

### Recommended settings:

1. **Add description:**
   "Python client for Cyfrin Solodit Findings API - search and analyze smart contract security vulnerabilities"

2. **Add topics:**
   - python
   - api-client
   - security
   - smart-contracts
   - blockchain
   - audit
   - vulnerabilities
   - cyfrin
   - solodit

3. **Add README badges** (optional):
   ```markdown
   ![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
   ![License](https://img.shields.io/badge/license-MIT-green.svg)
   ```

---

## Example README for GitHub

Update your `README.md` to include setup instructions:

```markdown
# Solodit API Client

Python client for working with Cyfrin Solodit Findings API.

## Quick Start

1. Clone and setup:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key from https://solodit.cyfrin.io
   ```

3. Test:
   ```bash
   python scripts/quick_test.py
   ```

See [START_HERE.md](START_HERE.md) for detailed instructions.
```

---

## Useful git commands

```bash
# Check status
git status

# See what's ignored
git status --ignored

# Check if file is tracked
git ls-files | grep .env

# Remove file from git but keep locally
git rm --cached filename

# See commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

---

## Questions?

- Check `.gitignore` is working: `git status`
- Verify `.env` is not tracked: `git ls-files | grep .env` (should be empty)
- Test clone in new directory to verify setup works

---

## Ready to push!

```bash
git add .
git commit -m "Initial commit: Solodit API Client"
git push -u origin main
```

Good luck! 🚀
