#!/usr/bin/env python3
"""
Natural Language Query Tool for Spending Data
Uses local LLM (Ollama) - no API required
"""

from spending_lm import SpendingLM
import sys
import os

def print_banner():
    """Print welcome banner"""
    print("\n" + "="*70)
    print("💰 NATURAL LANGUAGE SPENDING ANALYZER")
    print("="*70)
    print("Query your spending data using plain English!")
    print("Running completely locally - no external APIs needed")
    print("="*70 + "\n")

def quick_start():
    """Print quick start instructions"""
    print("""
QUICK START:
───────────────────────────────────────────────────────────────────────

1. FIRST TIME SETUP:
   
   # Download a model (one-time, takes 5-10 minutes)
   python3 natural_language_query.py --download

2. START OLLAMA SERVER:
   
   # In a new terminal:
   ollama serve

3. INTERACTIVE QUERIES:
   
   # Ask questions about your spending
   python3 natural_language_query.py

EXAMPLES OF QUESTIONS YOU CAN ASK:
───────────────────────────────────────────────────────────────────────
  ✓ "How much did I spend on education?"
  ✓ "What was my highest spending category last month?"
  ✓ "How many transactions were over $200?"
  ✓ "Compare my shopping vs restaurant spending"
  ✓ "What percentage of my budget went to utilities?"
  ✓ "Show me all transactions categorized as entertainment"
  ✓ "Analyze my spending patterns and suggest areas to save"

COMMAND LINE OPTIONS:
───────────────────────────────────────────────────────────────────────
  python3 natural_language_query.py
    └─ Interactive mode (ask multiple questions)
  
  python3 natural_language_query.py "How much on groceries?"
    └─ Single query mode
  
  python3 natural_language_query.py --analyze
    └─ Generate automatic spending analysis
  
  python3 natural_language_query.py --download
    └─ Download the Mistral model
  
  python3 natural_language_query.py --list-models
    └─ Show installed models
  
  python3 natural_language_query.py --model llama2 "question"
    └─ Use a different model

MODELS AVAILABLE:
───────────────────────────────────────────────────────────────────────
  • llama2 (7B, fast, recommended) ⭐
  • llama2 (7GB, slower, more powerful)
  • neural-chat (4GB, optimized for chat)
  • dolphin-mixtral (26GB, very powerful)

REQUIREMENTS:
───────────────────────────────────────────────────────────────────────
  ✓ Ollama installed (via: brew install ollama)
  ✓ Python 3.7+
  ✓ requests library (auto-installed)
  ✓ spending data files in current directory

GETTING HELP:
───────────────────────────────────────────────────────────────────────
  python3 natural_language_query.py --help
    └─ Show all options

""")

def check_ollama_setup():
    """Check if Ollama is properly set up"""
    import requests
    
    try:
        # Check if Ollama is running
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            models = [m["name"].split(":")[0] for m in data.get("models", [])]
            
            if not models:
                print("⚠️  Ollama is running but no models found")
                print("   Download a model with: ollama pull llama2")
                return False
            
            if "llama2" not in models:
                print(f"⚠️  Found models: {', '.join(set(models))}")
                print(f"   Recommended: ollama pull llama2")
                return False
            
            return True
        else:
            print("⚠️  Ollama server not responding properly")
            return False
    except requests.exceptions.ConnectionError:
        print("⚠️  Ollama is not running!")
        print("   Start it with: ollama serve")
        return False
    except Exception as e:
        print(f"⚠️  Error checking Ollama: {e}")
        return False

def main():
    print_banner()
    
    # Check Ollama setup
    if not check_ollama_setup():
        print("\n❌ Ollama setup incomplete. Fix the issues above and try again.\n")
        return
    
    print("✅ Ollama and model ready!\n")
    
    # Check if this is first time
    if len(sys.argv) == 1:
        print("ℹ️  Starting in interactive mode...")
        print("(For help, run: python3 natural_language_query.py --help)\n")
        
        lm = SpendingLM()
        lm.load_spending_data()
        lm.interactive_session()
    else:
        # Pass through to spending_lm
        from spending_lm import main
        main()

if __name__ == "__main__":
    main()
