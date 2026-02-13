#!/usr/bin/env python3
"""
Spending Report System - Quick Launcher
Simple entry point that checks requirements and launches the main app
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.7+"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required")
        print(f"   Current version: {sys.version}")
        return False
    return True

def check_required_files():
    """Check if required files exist"""
    base_dir = os.path.dirname(__file__)
    required_files = [
        "generate_reports_email.py",
        "natural_language_query.py",
        "manage_rules.py",
        "spending_lm.py",
        "categories.csv",
        "category_rules.csv",
    ]
    
    missing = []
    for f in required_files:
        filepath = os.path.join(base_dir, f)
        if not os.path.exists(filepath):
            missing.append(f)
    
    if missing:
        print("❌ Missing required files:")
        for f in missing:
            print(f"   • {f}")
        return False
    
    return True

def check_dependencies():
    """Check if required Python packages are installed"""
    required = ["pandas", "openpyxl", "xlsxwriter", "requests"]
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("⚠️  Missing Python packages:")
        for pkg in missing:
            print(f"   • {pkg}")
        print("\n📦 Installing missing packages...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install"] + missing, 
                         check=True, capture_output=True)
            print("✅ Packages installed successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to install packages: {e}")
            print("\n   Try manually:")
            print(f"   pip3 install {' '.join(missing)}")
            return False
    
    return True

def main():
    """Main launcher"""
    print("\n" + "="*70)
    print("🚀 SPENDING REPORT SYSTEM LAUNCHER")
    print("="*70 + "\n")
    
    # Check requirements
    print("📋 Checking system requirements...\n")
    
    if not check_python_version():
        sys.exit(1)
    print("✅ Python version OK")
    
    if not check_required_files():
        sys.exit(1)
    print("✅ All required files present")
    
    if not check_dependencies():
        sys.exit(1)
    print("✅ All dependencies available")
    
    # Launch main app
    print("\n" + "─"*70)
    print("🎯 Starting application...\n")
    
    try:
        app_path = os.path.join(os.path.dirname(__file__), "app.py")
        result = subprocess.run([sys.executable, app_path])
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error launching app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
