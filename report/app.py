#!/usr/bin/env python3
"""
Main Application Menu
Central hub for all spending management features
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def print_banner():
    """Print application banner"""
    print("\n" + "="*70)
    print("💰 SPENDING REPORT & ANALYSIS SYSTEM")
    print("="*70)
    print("Manage your finances with AI-powered insights\n")

def print_menu():
    """Print main menu options"""
    print("\n" + "─"*70)
    print("📋 MAIN MENU - SELECT AN OPTION")
    print("─"*70 + "\n")
    
    options = [
        ("1", "📊 Generate Spending Report", 
         "Create Excel report from bank statements"),
        ("2", "🤖 Natural Language Queries",
         "Ask questions about your spending"),
        ("3", "⚙️  Manage Categories & Rules",
         "Customize categories and categorization rules"),
        ("4", "📈 View Category Hierarchy",
         "See parent-child category relationships"),
        ("5", "📤 Export Custom Rules",
         "Export your custom categories and rules"),
        ("6", "ℹ️  Help & Documentation",
         "View help and feature guides"),
        ("0", "❌ Exit",
         "Close the application"),
    ]
    
    for num, title, desc in options:
        print(f"  {num}  {title}")
        print(f"     {desc}\n")
    
    print("─"*70)

def menu_reports():
    """Generate spending reports"""
    print("\n" + "="*70)
    print("📊 SPENDING REPORT GENERATOR")
    print("="*70)
    print("\nStarting report generation...\n")
    
    try:
        import subprocess
        result = subprocess.run(
            ["python3", "generate_reports_email.py"],
            cwd=os.path.dirname(__file__)
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def menu_nlq():
    """Natural language queries"""
    print("\n" + "="*70)
    print("🤖 NATURAL LANGUAGE ANALYZER")
    print("="*70)
    print("\nStarting natural language query tool...\n")
    
    try:
        import subprocess
        result = subprocess.run(
            ["python3", "natural_language_query.py"],
            cwd=os.path.dirname(__file__)
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def menu_manage_rules():
    """Manage categories and rules"""
    print("\n" + "="*70)
    print("⚙️  CATEGORY & RULE MANAGER")
    print("="*70)
    print("\nStarting rule manager...\n")
    
    try:
        import subprocess
        result = subprocess.run(
            ["python3", "manage_rules.py"],
            cwd=os.path.dirname(__file__)
        )
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def menu_hierarchy():
    """View category hierarchy"""
    print("\n" + "="*70)
    print("📈 CATEGORY HIERARCHY")
    print("="*70 + "\n")
    
    try:
        import pandas as pd
        
        categories_file = os.path.join(os.path.dirname(__file__), "categories.csv")
        if not os.path.exists(categories_file):
            print("❌ categories.csv not found")
            return False
        
        df = pd.read_csv(categories_file)
        
        # Print root categories (no parent)
        print("📂 ROOT CATEGORIES:")
        print("─"*70)
        root_cats = df[df['ParentCategory'].isna()]
        for _, row in root_cats.iterrows():
            print(f"  • {row['CategoryName']}")
            
            # Print sub-categories
            sub_cats = df[df['ParentCategory'] == row['CategoryName']]
            if not sub_cats.empty:
                for _, sub_row in sub_cats.iterrows():
                    marker = "✨" if sub_row.get('IsUserDefined') == 'Yes' else "  "
                    print(f"    {marker} ↳ {sub_row['CategoryName']}")
        
        print("\n✨ = Custom user-defined category")
        print("\nTotal categories: " + str(len(df)))
        print("User-defined: " + str(len(df[df.get('IsUserDefined') == 'Yes'])))
        
        return True
        
    except ImportError:
        print("❌ pandas not installed. Install with: pip3 install pandas")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def menu_export():
    """Export custom rules"""
    print("\n" + "="*70)
    print("📤 EXPORT CUSTOM RULES")
    print("="*70 + "\n")
    
    try:
        import pandas as pd
        
        rules_file = os.path.join(os.path.dirname(__file__), "category_rules.csv")
        if not os.path.exists(rules_file):
            print("❌ category_rules.csv not found")
            return False
        
        df = pd.read_csv(rules_file)
        custom_rules = df[df.get('IsCustom', 'No') == 'Yes']
        
        if custom_rules.empty:
            print("ℹ️  No custom rules found")
            return True
        
        print(f"📋 CUSTOM RULES ({len(custom_rules)} total)\n")
        print("─"*70)
        
        for _, row in custom_rules.iterrows():
            print(f"\nRule ID: {row['RuleID']}")
            print(f"  Category: {row['Category']}")
            print(f"  Pattern: {row['VendorPattern']}")
            print(f"  Priority: {row['Priority']}")
            print(f"  Created: {row.get('CreatedDate', 'Unknown')}")
            if pd.notna(row.get('Explanation')):
                print(f"  Note: {row['Explanation']}")
        
        # Ask to export
        print("\n" + "─"*70)
        export = input("\n📥 Export to CSV file? (y/n): ").strip().lower()
        
        if export == 'y':
            filename = input("Enter filename (default: custom_rules_export.csv): ").strip()
            if not filename:
                filename = "custom_rules_export.csv"
            
            filepath = os.path.join(os.path.dirname(__file__), filename)
            custom_rules.to_csv(filepath, index=False)
            print(f"✅ Exported to: {filename}")
            return True
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def menu_help():
    """Show help and documentation"""
    print("\n" + "="*70)
    print("ℹ️  HELP & DOCUMENTATION")
    print("="*70 + "\n")
    
    help_options = [
        ("1", "Quick Start Guide", "README.md"),
        ("2", "Spending Report Guide", "README.md"),
        ("3", "Natural Language Query Guide", "LLM_NATURAL_LANGUAGE_GUIDE.md"),
        ("4", "Custom Categories Guide", "ADVANCED_CUSTOMIZATION_GUIDE.md"),
        ("5", "LLM Setup & Troubleshooting", "LLM_README.md"),
        ("0", "Back to main menu", None),
    ]
    
    print("Available documentation:\n")
    for num, title, _ in help_options:
        print(f"  {num}  {title}")
    
    print("\n" + "─"*70)
    choice = input("Select option (0-5): ").strip()
    
    if choice == "0":
        return True
    
    doc_map = {
        "1": "README.md",
        "2": "README.md",
        "3": "LLM_NATURAL_LANGUAGE_GUIDE.md",
        "4": "ADVANCED_CUSTOMIZATION_GUIDE.md",
        "5": "LLM_README.md",
    }
    
    doc_file = doc_map.get(choice)
    if not doc_file:
        print("❌ Invalid option")
        return False
    
    filepath = os.path.join(os.path.dirname(__file__), doc_file)
    if not os.path.exists(filepath):
        print(f"❌ File not found: {doc_file}")
        return False
    
    try:
        import subprocess
        subprocess.run(["less", filepath])
    except:
        # Fallback to cat if less not available
        try:
            with open(filepath, 'r') as f:
                print(f.read())
        except Exception as e:
            print(f"❌ Error reading file: {e}")
    
    return True

def interactive_menu():
    """Main interactive menu loop"""
    print_banner()
    
    menu_actions = {
        "1": ("Reports", menu_reports),
        "2": ("Natural Language", menu_nlq),
        "3": ("Manage Rules", menu_manage_rules),
        "4": ("View Hierarchy", menu_hierarchy),
        "5": ("Export Rules", menu_export),
        "6": ("Help", menu_help),
        "0": ("Exit", None),
    }
    
    while True:
        print_menu()
        choice = input("👉 Enter your choice (0-6): ").strip()
        
        if choice not in menu_actions:
            print("\n❌ Invalid choice. Please select 0-6")
            continue
        
        title, action = menu_actions[choice]
        
        if choice == "0":
            print("\n" + "="*70)
            print("👋 Thank you for using Spending Report System!")
            print("="*70 + "\n")
            break
        
        if action:
            try:
                success = action()
                if success:
                    print("\n✅ Operation completed successfully")
                input("\n Press Enter to return to menu...")
            except KeyboardInterrupt:
                print("\n\n⏹️  Operation cancelled")
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\n Press Enter to return to menu...")

def main():
    """Main entry point"""
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
