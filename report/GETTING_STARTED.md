# Starting the Application

Your spending report system now has a **central menu hub** for all features!

## Quick Start

### Method 1: Smart Launcher (Recommended)
```bash
python3 start.py
```

Automatically checks requirements and launches the app.

### Method 2: Direct Launch
```bash
python3 app.py
```

### Method 3: Full Path
```bash
cd /Users/janani/Desktop/sitapp/budgetapp/report
python3 app.py
```

## Main Menu Options

When you start the app, you'll see:

```
======================================================================
💰 SPENDING REPORT & ANALYSIS SYSTEM
======================================================================

📋 MAIN MENU - SELECT AN OPTION

  1  📊 Generate Spending Report
     Create Excel report from bank statements

  2  🤖 Natural Language Queries
     Ask questions about your spending

  3  ⚙️  Manage Categories & Rules
     Customize categories and categorization rules

  4  📈 View Category Hierarchy
     See parent-child category relationships

  5  📤 Export Custom Rules
     Export your custom categories and rules

  6  ℹ️  Help & Documentation
     View help and feature guides

  0  ❌ Exit
     Close the application
```

## What Each Option Does

### 1️⃣ Generate Spending Report
Creates an Excel file (.xlsx) from your bank statements.
- Process multiple CSV/PDF files
- Categorize transactions automatically
- Generate category breakdown
- Identify large transactions
- Optional: Email report via Gmail

**Output:** `Spending_Report_MM_YYYY.xlsx`

### 2️⃣ Natural Language Queries
Ask questions about your spending in plain English.
- "How much on education?"
- "What's my highest category?"
- "Analyze my spending patterns"
- All processed locally with AI (no APIs)

**Requires:** Ollama running (`ollama serve` in another terminal)

### 3️⃣ Manage Categories & Rules
Customize how transactions are categorized.
- Add custom categories
- Create custom rules
- Set priorities
- Manage overrides
- View all relationships

**Changes:** Saved to `categories.csv` and `category_rules.csv`

### 4️⃣ View Category Hierarchy
See all categories and their parent-child relationships.
- ✨ = Custom user-defined categories
- Shows 9 total categories (8 built-in + custom)
- Visual tree structure

### 5️⃣ Export Custom Rules
Export your custom categories and rules to CSV file.
- Name your export file
- Share with others
- Backup your customizations

**Output:** CSV file with your custom rules

### 6️⃣ Help & Documentation
Browse full documentation:
- Quick Start Guide
- Spending Report Guide
- Natural Language Query Guide
- Custom Categories Guide
- LLM Setup Guide

Opens in your default viewer (less, cat, etc.)

### 0️⃣ Exit
Cleanly exit the application.

## Workflow Example

### Daily/Weekly Use
```
1. Run: python3 app.py
2. Select: Option 2 (Natural Language Queries)
3. Ask: "How much did I spend this week?"
4. Get: Instant analysis
5. Exit
```

### Monthly Reports
```
1. Run: python3 app.py
2. Select: Option 1 (Generate Report)
3. Enter: Directory with statements, month/year
4. Get: Excel file with full analysis
5. Exit
```

### Customizing Categories
```
1. Run: python3 app.py
2. Select: Option 3 (Manage Rules)
3. Add: Custom category (e.g., "Education")
4. Create: Rules for new category
5. Use: In reports automatically
6. Exit
```

## Features by Menu Option

| Option | Feature | Time | Requirements |
|--------|---------|------|--------------|
| 1 | Reports | 1-2 min | CSV/PDF files |
| 2 | NLQ | Instant | Ollama running |
| 3 | Rules | 5-10 min | None |
| 4 | Hierarchy | 10 sec | None |
| 5 | Export | 1 min | Custom rules |
| 6 | Help | Variable | None |

## Requirements Checklist

### For Report Generation (Option 1)
- ✅ pandas
- ✅ openpyxl
- ✅ xlsxwriter
- ✅ pdfplumber
- ✅ Bank statements (CSV/PDF)

### For Natural Language (Option 2)
- ✅ requests
- ✅ Ollama installed
- ✅ Ollama server running
- ✅ Mistral model downloaded

### For Rule Management (Option 3)
- ✅ pandas
- ✅ CSV files (auto-created)

### For all options
- ✅ Python 3.7+
- ✅ Current directory files

## Troubleshooting

### "Missing Python packages"
The start.py launcher automatically installs them. Or:
```bash
pip3 install pandas openpyxl xlsxwriter pdfplumber requests
```

### "Ollama is not running" (Option 2)
In another terminal:
```bash
ollama serve
```

### "Model not found" (Option 2)
```bash
python3 natural_language_query.py --download
```

### "File not found"
Make sure you're in the correct directory:
```bash
cd /Users/janani/Desktop/sitapp/budgetapp/report
```

### Menu doesn't appear
Try the launcher:
```bash
python3 start.py
```

## Tips & Tricks

### Run Option Without Menu
If you know which option you want:
```bash
# Just generate reports
python3 generate_reports_email.py

# Just ask questions
python3 natural_language_query.py

# Just manage rules
python3 manage_rules.py
```

### Keyboard Shortcuts in Menu
- Press Enter after typing choice number
- Type 0 to exit at any time
- Press Ctrl+C to cancel (returns to menu)

### Keep Files Organized
All files stay in one directory:
```
/Users/janani/Desktop/sitapp/budgetapp/report/
├── app.py                              # Main menu
├── start.py                            # Smart launcher
├── generate_reports_email.py           # Report generator
├── natural_language_query.py           # LLM queries
├── manage_rules.py                     # Rule manager
├── categories.csv                      # Your categories
├── category_rules.csv                  # Your rules
└── Spending_Report_01_2026.xlsx       # Generated reports
```

## Next Steps

1. **First Time?**
   - Start with Option 6 (Help) to read guides
   - Then try Option 4 (View Hierarchy) to see structure
   - Finally test Option 1 (Generate Report)

2. **Have Statements Ready?**
   - Gather CSV/PDF bank files
   - Start with Option 1 (Generate Report)
   - Place files in a directory when prompted

3. **Want to Customize?**
   - Start with Option 3 (Manage Rules)
   - Add custom categories
   - Create patterns

4. **Want AI Analysis?**
   - Make sure Ollama is running
   - Start with Option 2 (Natural Language Queries)
   - Ask questions about your spending

## System Files

You don't need to edit these; they're managed by the app:

- **categories.csv** - All categories (8 built-in + custom)
- **category_rules.csv** - 52+ rules for auto-categorization
- **category_map.csv** - Legacy format (for compatibility)

## Questions?

See the documentation in Option 6, or run:
```bash
python3 app.py --help
```

---

**Ready to start?** 

```bash
python3 start.py
```

or

```bash
python3 app.py
```

Enjoy! 💰📊
