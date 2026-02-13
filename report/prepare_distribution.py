#!/usr/bin/env python3
"""
Prepare distribution package for end users
Creates a folder with the executable and setup instructions
"""

import os
import shutil
from pathlib import Path
import json

# Create distribution folder
dist_base = Path('/Users/janani/Desktop/sitapp/budgetapp/report/dist')
release_folder = dist_base / 'Spending-Report-System-Distribution'

if release_folder.exists():
    shutil.rmtree(release_folder)

release_folder.mkdir(parents=True, exist_ok=True)

# Copy the standalone executable
exe_path = dist_base / 'Spending-Report-System'
if exe_path.exists():
    shutil.copy2(exe_path, release_folder / 'Spending-Report-System')
    print(f"✓ Copied executable ({exe_path.stat().st_size / 1024 / 1024:.1f}MB)")

# Create README for users
readme = """# 💰 Spending Report & Analysis System

## What This App Does
Automatically categorizes your spending, generates reports, and answers natural language questions about your finances - all locally on your computer. No cloud uploads. No API fees. 100% private.

## Installation

### System Requirements
- **macOS 10.13+** (Intel or Apple Silicon)
- **2GB free disk space**
- **500MB RAM available**

### Step 1: Download & Extract
1. Download the `Spending-Report-System-Distribution.zip` file
2. Extract it to a location of your choice
3. You should have a folder with `Spending-Report-System` inside

### Step 2: Prepare Your Bank Statements (First Time Only)
1. Export your bank transactions as **CSV file**
   - From your bank's website, usually: Download → CSV format
   - Must have columns: Date, Description, Amount
   
2. Save the CSV file as `statement.csv` in the same folder

### Step 3: Run the App
Double-click `Spending-Report-System` to launch the menu

## 📋 What You Can Do

### 1. Generate Spending Report
- Creates an Excel report with all transactions
- Automatically categorizes each expense
- Shows spending by category with charts
- Generates vendor analysis

### 2. Natural Language Queries (Optional)
- Ask questions like "How much did I spend on food?"
- Get spending comparisons and analysis
- Requires Ollama (local AI) - setup guide included
- **Note:** First time setup takes ~10 minutes, then instant queries

### 3. Manage Categories & Rules
- Customize spending categories
- Create your own rules for auto-categorization
- Override categories for specific vendors
- Save your custom rules

### 4. View Category Hierarchy
- See all categories and subcategories
- Understand organizational structure
- Modify hierarchy if needed

### 5. Export Rules
- Backup your custom rules
- Transfer rules to another computer
- Share rules with team members

## ⚡ Quick Start

1. Place your bank statement CSV in the same folder as the executable
2. Run the app
3. Select Option 1: Generate Spending Report
4. Wait for Excel file to be created
5. Open the Excel file to see your report

## 🤖 AI Features (Optional)

To use natural language queries:

### First Time: Install Ollama
1. Visit: https://ollama.ai
2. Download and install Ollama (takes 5 minutes)
3. Run the app again
4. Select Option 6 to install a language model (takes 10 minutes)
5. You're ready to ask questions!

### Usage
- Option 2: Ask questions about your spending
- Example: "What's my highest spending category?"
- The response is instant - model runs locally on your computer

## 📊 File Locations

Your files are stored in:
```
macOS → ~/Library/Preferences/SpenditApp/
        or same folder as the executable
```

**No data is uploaded to cloud. Everything stays on your computer.**

## ❓ FAQ

**Q: Is my financial data private?**
A: Yes! All data stays on your computer. No cloud upload.

**Q: Do I need internet?**
A: No, except for first-time setup. Everything runs locally.

**Q: Can I share my data?**
A: Yes, you have full control. Export features available in menu.

**Q: What if I don't want AI features?**
A: You don't need them. Reports work great without AI.

**Q: Can I use my own custom categories?**
A: Yes! Option 3 in the menu allows full customization.

## 🆘 Troubleshooting

**App won't start:**
- Try running from Terminal: `./Spending-Report-System`
- Check you have 500MB RAM available

**CSV import fails:**
- Verify CSV has: Date, Description, Amount columns
- Date format should be: YYYY-MM-DD

**AI responses are slow:**
- First query trains the model (takes 30 seconds)
- Subsequent queries are instant
- Internet not required

## 📝 Version

Version 2.0 - Built February 2026

## 💬 Support

This is a standalone application. No external support needed.
All code is open source - check the documentation folder.

---

**Made with ❤️ for financial privacy**
"""

with open(release_folder / 'README.txt', 'w') as f:
    f.write(readme)

print(f"✓ Created README.txt ({len(readme)} bytes)")

# Create setup instructions
setup_guide = """# SETUP INSTRUCTIONS FOR END USERS

## BEFORE YOU START
Make sure you have:
✓ This executable file
✓ Your bank statement as CSV file
✓ macOS 10.13 or later
✓ At least 2GB free disk space

## STEP 1: PREPARE YOUR CSV FILE

Your bank statement CSV must have these columns (in any order):
  • Date (format: YYYY-MM-DD or MM/DD/YYYY)
  • Description or Merchant (the merchant/payee name)
  • Amount (the transaction amount, can be positive or negative)

Example CSV:
```
Date,Description,Amount
2026-01-05,Amazon,45.99
2026-01-05,Whole Foods,78.50
2026-01-06,Electric Bill,125.00
```

To get your CSV:
  1. Log into your bank's website
  2. Find "Download" or "Export Transactions"
  3. Select CSV format
  4. Save as: statement.csv
  5. Place in same folder as the executable

## STEP 2: RUN THE APP

Double-click: Spending-Report-System

You'll see the main menu with options:
  1. Generate Spending Report
  2. Natural Language Queries
  3. Manage Categories & Rules
  4. View Category Hierarchy
  5. Export Custom Rules
  6. Help & Documentation

## STEP 3: GENERATE YOUR FIRST REPORT

Select Option 1: Generate Spending Report
  → Follow the prompts
  → Select your CSV file
  → Wait for processing (20-60 seconds)
  → You'll get an Excel file with your report!

## OPTIONAL: AI FEATURES

If you want to ask questions like "How much did I spend on groceries?"

1. Install Ollama (free, local):
   → Visit: https://ollama.ai
   → Download and install
   → It creates a personal AI on your computer

2. In the app, select:
   Option 6: Help & Documentation
   → Follow LLM setup instructions

3. Then use Option 2: Natural Language Queries
   → Ask any question about your spending!

## IMPORTANT NOTES

✓ No Internet Required (except initial Ollama download)
✓ No Account Needed
✓ No Data Uploaded
✓ All Data Stays On Your Computer
✓ Free & Open Source

---
Questions? Check README.txt
"""

with open(release_folder / 'SETUP_GUIDE.txt', 'w') as f:
    f.write(setup_guide)

print(f"✓ Created SETUP_GUIDE.txt")

# Create a quick reference
quick_ref = """QUICK REFERENCE

LAUNCH: Double-click "Spending-Report-System"

MENU OPTIONS:
1) Generate Report ........... Create Excel with spending analysis
2) Natural Language .......... Ask "How much on food?" (needs Ollama)
3) Manage Rules .............. Create custom categories & rules
4) View Hierarchy ............ See your category structure
5) Export Rules .............. Backup your custom rules
6) Help ...................... View all documentation
0) Exit ...................... Close the app

KEYBOARD:
  Type the number and press Enter to select an option
  Type 'exit' or '0' anytime to quit

REQUIRED FILES:
  • Spending-Report-System (the executable)
  • statement.csv (your bank statement)

OUTPUT FILES CREATED:
  • Spending_Report_[Date].xlsx (your report)
  • categories.csv (your categories)
  • category_rules.csv (your rules)

TIPS:
→ First time? Start with Option 1
→ Want AI? Follow Option 6 for Ollama setup
→ Stuck? Check README.txt
→ Need help? All code is open source

VERSION: 2.0 (February 2026)
"""

with open(release_folder / 'QUICK_REFERENCE.txt', 'w') as f:
    f.write(quick_ref)

print(f"✓ Created QUICK_REFERENCE.txt")

# Create system requirements
sysreq = """SYSTEM REQUIREMENTS

MINIMUM:
  • macOS 10.13 (2017) or later
  • Apple Silicon (M1/M2/M3) or Intel processor
  • 500 MB RAM free
  • 2 GB disk space

RECOMMENDED:
  • macOS 12 (2021) or later
  • 2GB RAM free
  • 5GB disk space (for reports and AI model)

OPTIONAL (for AI features):
  • Ollama: https://ollama.ai
  • 4GB free disk space (for language model)
  • 2GB RAM available (while running queries)

WHAT YOU DON'T NEED:
  ✗ Python (bundled in executable)
  ✗ Internet connection (except Ollama download)
  ✗ Cloud account
  ✗ Admin privileges

SUPPORTED BANK STATEMENTS:
  ✓ CSV format (any bank)
  ✓ Excel exports (if saved as CSV)
  ✓ Any format with: Date, Description, Amount

UNSUPPORTED:
  ✗ PDF statements (save as CSV first)
  ✗ OFX/QFX (convert to CSV)
  ✗ Screenshots (won't work)
"""

with open(release_folder / 'SYSTEM_REQUIREMENTS.txt', 'w') as f:
    f.write(sysreq)

print(f"✓ Created SYSTEM_REQUIREMENTS.txt")

# Create info.json
info = {
    "app": "Spending Report & Analysis System",
    "version": "2.0",
    "date_built": "February 13, 2026",
    "platform": "macOS",
    "size_mb": 25.7,
    "files_included": [
        "Spending-Report-System (executable)",
        "README.txt (main guide)",
        "SETUP_GUIDE.txt (step-by-step)",
        "QUICK_REFERENCE.txt (quick help)",
        "SYSTEM_REQUIREMENTS.txt (system specs)"
    ],
    "features": [
        "Spending report generation (Excel)",
        "Automatic transaction categorization",
        "Natural language queries (optional AI)",
        "Custom category creation",
        "Transaction rule management",
        "Category hierarchy",
        "Rule export/backup"
    ],
    "requirements": {
        "os": "macOS 10.13+",
        "ram_mb": 500,
        "disk_space_gb": 2
    }
}

with open(release_folder / 'INFO.json', 'w') as f:
    import json
    json.dump(info, f, indent=2)

print(f"✓ Created INFO.json")

print("\n" + "="*60)
print("✅ Distribution package ready!")
print("="*60)
print(f"\nLocation: {release_folder}")
print(f"\nFiles included:")
for item in sorted(release_folder.iterdir()):
    if item.is_file():
        size = item.stat().st_size / 1024 / 1024
        print(f"  ✓ {item.name} ({size:.1f}MB)")

print("\n📦 READY TO DISTRIBUTE")
print("\nZip this folder to create:")
print("  → Spending-Report-System-Distribution.zip")
print("\nThen share with users!")
