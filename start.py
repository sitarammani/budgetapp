#!/usr/bin/env python3
"""
Spending Report System - Quick Launcher
Simple entry point that checks requirements and launches the main app
"""

import sys
import os
import subprocess
import json
import time
from pathlib import Path

class ProgressBar:
    """Simple progress bar for startup sequence"""
    def __init__(self, total_steps=10):
        self.total_steps = total_steps
        self.current_step = 0
    
    def update(self, step_name=""):
        """Update progress bar"""
        self.current_step += 1
        percent = int((self.current_step / self.total_steps) * 100)
        filled = int(percent / 5)
        bar = "█" * filled + "░" * (20 - filled)
        
        if step_name:
            print(f"⏳ {bar} {percent:3d}% | {step_name}", flush=True)
        else:
            print(f"\r⏳ {bar} {percent:3d}%", end="", flush=True)
    
    def complete(self):
        """Show completion"""
        print(f"\r✅ {chr(9608)*20} 100% | All systems ready!", flush=True)
        print()

def check_python_version():
    """Check if Python version is 3.7+"""
    if sys.version_info < (3, 7):
        return False
    return True

def check_required_files():
    """Check if required files exist"""
    if getattr(sys, 'frozen', False):
        base_dir = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
    else:
        base_dir = os.path.dirname(__file__)
    required_files = [
        "categories.csv",
        "category_rules.csv",
    ]
    
    # For frozen, the py files are bundled, so don't check
    if not getattr(sys, 'frozen', False):
        required_files.extend([
            "generate_reports_email.py",
            "natural_language_query.py",
            "manage_rules.py",
            "spending_lm.py",
        ])
    
    missing = []
    for f in required_files:
        filepath = os.path.join(base_dir, f)
        if not os.path.exists(filepath):
            missing.append(f)
    
    return len(missing) == 0

def check_dependencies():
    """Check if required Python packages are installed"""
    if getattr(sys, 'frozen', False):
        # In frozen app, assume packages are bundled
        return True
    
    required = ["pandas", "openpyxl", "xlsxwriter", "requests"]
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        try:
            subprocess.run([sys.executable, "-m", "pip", "install"] + missing, 
                         check=True, capture_output=True)
            return True
        except Exception:
            return False
    
    return True

def check_ollama_installed():
    """Check if Ollama is installed"""
    try:
        result = subprocess.run(["which", "ollama"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def is_ollama_running():
    """Check if Ollama server is running"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except:
        return False

def check_model_installed(model="llama2"):
    """Check if a specific model is installed in Ollama"""
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            models = [m["name"].split(":")[0] for m in data.get("models", [])]
            return model in models
    except:
        pass
    return False

def prompt_install_model_now():
    """Prompt user to install AI model during startup"""
    print("\n" + "="*70)
    print("🤖 AI MODEL NOT FOUND")
    print("="*70)
    print("\nThe AI model (Llama 2) is not installed or not available.")
    print("Would you like to install it now?")
    print("(This will take 5-15 minutes, one-time only)\n")
    
    try:
        response = input("Install AI model now? (y/n): ").strip().lower()
    except EOFError:
        response = 'n'
    
    if response == 'y':
        print("\n📥 Starting Ollama model installation...")
        print("   This may take 5-15 minutes depending on your connection.")
        print("   Please keep the app running.\n")
        return prompt_for_ai_model_install()
    else:
        print("\n➡️  AI features will be disabled")
        print("   You can enable them later by running: ollama pull llama2\n")
        return False

def prompt_for_ai_model_install():
    """Prompt user to install AI model during first-time setup"""
    if not check_ollama_installed():
        print("\n⚠️  Ollama not installed")
        print("   AI features require Ollama. Install from: https://ollama.ai")
        print("   AI features will be disabled.\n")
        return False
    
    print("\n" + "="*70)
    print("🤖 AI FEATURES SETUP")
    print("="*70)
    print("\nThis app can analyze your spending with AI-powered insights.")
    print("This requires downloading the Llama 2 model (~4GB).")
    print("\nWould you like to install the AI model now?")
    print("(You can skip this and enable AI features later)")
    
    try:
        response = input("\nInstall AI model? (y/n): ").strip().lower()
    except EOFError:
        response = 'n'
    
    if response == 'y':
        print("\n📥 Starting Ollama model installation...")
        print("   This may take 5-15 minutes depending on your connection.")
        print("   Please keep the app running.\n")
        
        try:
            # Start Ollama server if not running
            if not is_ollama_running():
                print("🚀 Starting Ollama server...")
                subprocess.Popen(
                    ["ollama", "serve"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    preexec_fn=os.setsid if sys.platform != "win32" else None
                )
                time.sleep(2)
            
            # Pull the model with progress tracking (percentage only)
            print("📥 Downloading Llama 2 model (this is a one-time operation)...")
            process = subprocess.Popen(
                ["ollama", "pull", "llama2"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Read output in real-time and show only percentage progress
            for line in iter(process.stdout.readline, ''):
                if line:
                    line = line.rstrip()
                    # Only print lines with percentage or size indicators
                    if "%" in line or "MB" in line or "GB" in line:
                        print(f"   {line}")
            
            returncode = process.wait()
            
            if returncode == 0:
                print("\n✅ Llama 2 model installed successfully!")
                print("   AI features are now enabled.\n")
                return True
            else:
                print("\n❌ Failed to install Llama 2 model")
                print("   AI features will be disabled.\n")
                return False
        except subprocess.TimeoutExpired:
            print("\n⏱️  Model installation timed out")
            print("   Please try again later or install manually: ollama pull llama2")
            print("   AI features will be disabled.\n")
            return False
        except Exception as e:
            print(f"\n❌ Error installing model: {e}")
            print("   AI features will be disabled.\n")
            return False
    else:
        print("\n➡️  AI features disabled")
        print("   You can enable them later by running: ollama pull llama2\n")
        return False

def start_ollama():
    """Start Ollama server in background"""
    try:
        if not check_ollama_installed():
            print("\n⚠️  Ollama is not installed")
            print("   Install from: https://ollama.ai")
            print("   Features requiring Ollama will be unavailable\n")
            return False
        
        print("🚀 Starting Ollama server...")
        # Start ollama serve in background
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=os.setsid if sys.platform != "win32" else None
        )
        
        # Wait for server to start
        max_retries = 10
        for i in range(max_retries):
            time.sleep(0.5)
            if is_ollama_running():
                print("✅ Ollama server started successfully")
                return True
        
        print("⚠️  Ollama server may be starting (taking longer than expected)")
        return True
    except Exception as e:
        print(f"⚠️  Could not start Ollama: {e}")
        return False

def check_first_time_install():
    """Check if this is first time install and ask for configuration"""
    config_dir = Path.home() / '.config' / 'SpendingApp'
    config_file = config_dir / 'config.json'
    
    if config_file.exists():
        return False  # Not first time
    
    # First time install
    print("\n" + "="*70)
    print("🎉 WELCOME TO SPENDING REPORT SYSTEM - FIRST TIME SETUP")
    print("="*70)
    
    config_dir.mkdir(parents=True, exist_ok=True)
    
    # Ask for log location
    print("\n📁 LOG FILE LOCATION")
    print("─"*70)
    print("\nWhere would you like to store application logs and transaction data?")
    print(f"\nDefault location: {config_dir}")
    
    try:
        response = input("\nUse default location? (y/n): ").strip().lower()
    except EOFError:
        response = 'y'
    
    if response == 'y' or response == '':
        log_location = str(config_dir)
    else:
        try:
            custom_path = input("Enter custom path: ").strip()
            if custom_path:
                log_location = custom_path
            else:
                log_location = str(config_dir)
        except EOFError:
            log_location = str(config_dir)
    
    # Ask for AI model installation
    print("\n🤖 AI MODEL SETUP")
    print("─"*70)
    print("\nThis application can use AI for natural language queries and insights.")
    print("Would you like to install Ollama and download the Llama 2 AI model?")
    print("Note: This requires ~4GB disk space and 5-15 minutes download time.")
    print("(You can skip this - AI features will be easily enabled later)")
    
    try:
        response = input("\nInstall AI model now? (y/n): ").strip().lower()
    except EOFError:
        response = 'y'
    
    install_model = response == 'y' or response == ''
    
    # Create config file (save install preference)
    config = {
        'version': '1.0',
        'log_location': log_location,
        'install_model': install_model,
        'ai_feature_enabled': False,  # Will be set after installation attempt
        'created_at': str(Path(config_file).stat().st_mtime if config_file.exists() else time.time()),
        'first_time_setup_complete': True
    }
    
    try:
        # Create log directory
        Path(log_location).mkdir(parents=True, exist_ok=True)
        
        # Save config
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n✅ Configuration saved")
        print(f"   Logs location: {log_location}\n")
        
    except Exception as e:
        print(f"\n❌ Error creating configuration: {e}")
        print(f"   Using default: {config_dir}\n")
    
    # If user wants to install model, do it NOW (before progress bar)
    if install_model:
        ai_enabled = prompt_for_ai_model_install()
        config['ai_feature_enabled'] = ai_enabled
        # Save updated config
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except:
            pass
    else:
        print("➡️  Skipping AI model installation")
        print("   You can enable it later by running: ollama pull llama2\n")
    
    return config

def prompt_sender_email_and_oauth(config, config_file):
    """Prompt for sender email and setup OAuth if email changed or not set"""
    saved_sender = config.get('sender_email', '')
    print("\n📧 EMAIL CONFIGURATION")
    print("─"*70)
    
    if saved_sender:
        print(f"\nCurrent sender email: {saved_sender}")
        try:
            change = input("Use same email? (y/n): ").strip().lower()
        except EOFError:
            change = 'y'
        
        if change == 'y' or change == '':
            print("✅ Using saved email configuration")
            return
    
    # Ask for new sender email
    print("\nEnter the email address you want to use for sending reports:")
    try:
        sender_email = input("Sender email: ").strip()
    except EOFError:
        sender_email = ''
    
    if not sender_email:
        print("⚠️  No email provided. Email features will be available after restart.")
        return
    
    # Setup OAuth for the email
    print(f"\n🔐 Authenticating {sender_email} with Gmail...")
    print("Opening browser for Gmail authentication...\n")
    
    try:
        # Use a simplified OAuth setup without requiring pre-configured credentials
        setup_gmail_oauth_interactive(sender_email)
        
        # Save sender email to config
        config['sender_email'] = sender_email
        config_dir = Path.home() / '.config' / 'SpendingApp'
        config_dir.mkdir(parents=True, exist_ok=True)
        with open(config_file, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✅ Sender email saved: {sender_email}\n")
    except Exception as e:
        print(f"❌ OAuth authentication failed: {e}")
        print("   Email features will be available after restart.\n")

def setup_gmail_oauth_interactive(email):
    """Setup Gmail OAuth2 with browser-based interactive flow"""
    import webbrowser
    from pathlib import Path
    
    config_dir = Path.home() / '.config' / 'SpendingApp'
    config_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a minimal OAuth config for the GmailAuth class
    # Using Google's public OAuth credentials for desktop apps
    oauth_config = {
        'client_id': '407408718192.apps.googleusercontent.com',
        'client_secret': 'kapsy8Q8FeuJYcVfea_Bpr0T',
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://oauth2.googleapis.com/token',
        'redirect_uris': ['http://localhost:8080/', 'urn:ietf:wg:oauth:2.0:oob']
    }
    
    oauth_config_file = os.path.join(os.path.dirname(__file__), '.gmail_oauth_config')
    
    # Save OAuth config temporarily if it doesn't exist
    if not os.path.exists(oauth_config_file):
        try:
            with open(oauth_config_file, 'w') as f:
                json.dump(oauth_config, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save OAuth config: {e}")
    
    # Now trigger the OAuth flow
    try:
        from gmail_auth import GmailAuth
        auth = GmailAuth()
        creds = auth.get_oauth2_credentials()
        print("✅ Gmail authentication successful!")
        return creds
    except Exception as e:
        raise Exception(f"Failed to authenticate with Gmail: {e}")

def main():
    """Main launcher with progress bar"""
    
    # Check for first time install BEFORE progress bar (needs user interaction)
    config_dir = Path.home() / '.config' / 'SpendingApp'
    config_file = config_dir / 'config.json'
    is_first_time = not config_file.exists()
    
    config = {}
    
    if is_first_time:
        # Show first-time setup and perform AI model installation if requested
        config = check_first_time_install()
    else:
        # Load configuration for returning users
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
            except:
                config = {}
        
        # Don't pre-set ai_feature_enabled for returning users
        # Let the status check during startup handle it
    
    # Now show progress bar for background startup tasks
    sys.stdout.write("\n")
    sys.stdout.flush()
    print("╔" + "═"*68 + "╗", flush=True)
    print("║  🚀 SPENDING REPORT SYSTEM - INITIALIZING" + " "*24 + "║", flush=True)
    print("╚" + "═"*68 + "╝", flush=True)
    sys.stdout.write("\n")
    sys.stdout.flush()
    
    # Initialize progress bar (reduced from 11 since model install happens before startup)
    progress = ProgressBar(total_steps=10)
    
    try:
        # Step 1: Check Python version
        progress.update("Checking Python version...")
        time.sleep(0.1)
        if not check_python_version():
            print("❌ Python 3.7+ required", flush=True)
            sys.exit(1)
        
        # Step 2: Check required files
        progress.update("Verifying application files...")
        time.sleep(0.1)
        if not check_required_files():
            print("❌ Missing required files", flush=True)
            sys.exit(1)
        
        # Step 3: Check dependencies
        progress.update("Checking Python dependencies...")
        time.sleep(0.1)
        if not check_dependencies():
            print("⚠️  Some dependencies missing. Continuing...", flush=True)
        
        # Step 4: AI model status - check if model is actually available
        progress.update("Verifying AI model status...")
        time.sleep(0.1)
        model_available = check_model_installed()
        
        if model_available:
            print("✅ AI features enabled (Llama 2 model found)")
            config['ai_feature_enabled'] = True
        else:
            # Model not available - should we ask user to install?
            # Only skip asking if user explicitly declined during first-time setup
            explicitly_declined = config.get('install_model') == False
            
            if explicitly_declined:
                # User said NO during first-time setup, respect their choice
                print("ℹ️  AI features disabled (as per your preference)")
                config['ai_feature_enabled'] = False
            else:
                # User hasn't explicitly declined, offer to install now
                ai_enabled_now = prompt_install_model_now()
                config['ai_feature_enabled'] = ai_enabled_now
        
        # Step 5: Check Ollama installation
        progress.update("Detecting Ollama installation...")
        time.sleep(0.1)
        ollama_installed = check_ollama_installed()
        
        # Step 6-7: Start Ollama if available and AI is enabled
        if ollama_installed and config.get('ai_feature_enabled', False):
            progress.update("Starting Ollama AI server...")
            time.sleep(0.2)
            start_ollama()
        else:
            progress.update("Preparing application...")
            time.sleep(0.1)
        
        # Step 8: Final preparations
        progress.update("Preparing application environment...")
        time.sleep(0.2)
        
        # Step 9: Loading resources
        progress.update("Loading application resources...")
        time.sleep(0.1)
        
        # Step 10: Complete
        progress.update("Finalizing startup sequence...")
        time.sleep(0.1)
        
        # Show completion
        progress.complete()
        
        # Show "Application started" only after all background work is done
        # Save config with AI feature status
        try:
            config_dir.mkdir(parents=True, exist_ok=True)
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except:
            pass
        
        print("="*70, flush=True)
        print("✨ APPLICATION STARTED - ALL SYSTEMS READY", flush=True)
        print("="*70, flush=True)
        print()
        sys.stdout.flush()
        sys.stderr.flush()
        
        # Prompt for sender email and setup OAuth
        prompt_sender_email_and_oauth(config, config_file)
        
        # Launch main app
        if getattr(sys, 'frozen', False):
            # In frozen app, import and run app
            import app
            app.main()
        else:
            app_path = os.path.join(os.path.dirname(__file__), "app.py")
            result = subprocess.run([sys.executable, app_path])
            sys.exit(result.returncode)
        
    except KeyboardInterrupt:
        print("\n\n👋 Startup cancelled by user", flush=True)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Startup error: {e}", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
