# 🔒 Security & Privacy Policy

## Data Privacy First

BudgetApp is designed with privacy as a core principle:

### ✅ What We DON'T Do
- ❌ Don't collect usage statistics
- ❌ Don't send data to external servers
- ❌ Don't track user behavior
- ❌ Don't share data with third parties
- ❌ Don't store credentials in the code
- ❌ Don't have telemetry

### ✅ What We DO Do
- ✅ Process all data locally on your machine
- ✅ Store credentials in secure locations
- ✅ Use OAuth2 for secure Gmail authentication
- ✅ Allow user control of data storage location
- ✅ Support local-only AI analysis (Ollama)

---

## Credential Security

### Gmail OAuth2
```
✅ Secure Authorization Flow
├─ Uses OAuth2 protocol (industry standard)
├─ Secrets stored in ~/.config/SpendingApp/
├─ Not committed to version control
├─ Can be revoked anytime from Google account
└─ No passwords stored locally
```

### Gmail SMTP (Optional)
```
✅ Password Security
├─ Requested via secure input (terminal hidden)
├─ Not stored anywhere
├─ Not logged or cached
├─ Used only for current session
└─ Use Gmail app-specific passwords recommended
```

### Configuration Files
```
Sensitive Files Location: ~/.config/SpendingApp/
├─ .gmail_oauth_config - OAuth tokens
├─ token.json - Google API token
├─ config.json - User preferences
└─ logs/ - Application logs (no PII)
```

---

## Data Handling

### Bank Statement Data
- **Scope**: Local processing only
- **Storage**: User-defined location
- **Retention**: Under user control
- **Sharing**: User's discretion
- **Encryption**: Use file system encryption for sensitive data

### Application Logs
```
Location: ~/.config/SpendingApp/logs/
Contents: Performance metrics, LLM queries (non-PII)
Exclusions: No transaction values, no account numbers
Retention: User can delete anytime
```

### What's NOT Logged
- ❌ Bank account numbers
- ❌ Transaction amounts (only metrics)
- ❌ Personal identification info (PII)
- ❌ Gmail credentials or tokens
- ❌ OAuth secrets

---

## Security Best Practices

### For Users

1. **Keep Data Safe**
   ```bash
   # Use file system encryption
   # macOS: Enable FileVault
   # Linux: Use LUKS
   # Windows: Use BitLocker
   ```

2. **Gmail App Passwords (Recommended)**
   - Use Gmail app-specific passwords instead of your main password
   - Generate at: https://myaccount.google.com/apppasswords
   - Can be revoked independently

3. **Regular Backups**
   ```bash
   # Back up your reports
   # Protect your config: ~/.config/SpendingApp/
   ```

4. **Delete Unused OAuth**
   ```bash
   rm ~/.config/SpendingApp/.gmail_oauth_config
   # Then run setup_gmail_oauth.py again if needed
   ```

### For Developers

1. **Never commit sensitive files**
   ```bash
   # Check .gitignore includes:
   #   .gmail_oauth_config
   #   token.json
   #   .config/
   #   *.key
   ```

2. **Environment variables for config**
   ```python
   # Don't: config = {'api_key': 'sk-xyz'}
   # Do: config = {'api_key': os.getenv('API_KEY')}
   ```

3. **Logging sanitization**
   ```python
   # Don't: logger.info(f"User: {email}, Pass: {password}")
   # Do: logger.info(f"User authentication attempt: {user_id}")
   ```

---

## Third-Party Services (Optional)

### Gmail API
- **Privacy**: Google's privacy policy applies
- **Transparency**: You control what data is shared
- **Revocation**: Easy to revoke at any time
- **Usage**: Only for email sending (no read access)

### Ollama (Local LLM)
- **Privacy**: Fully local, no cloud connection
- **Data**: All analysis happens on your machine
- **Model**: Llama 2 (open source, downloadable)
- **Network**: No internet required after model download

---

## Incident Reporting

🔒 Found a security issue?

```
Email: sitarammani@gmail.com
Include:
  - Description of the issue
  - Steps to reproduce
  - Affected version
  - Suggested fix (if any)
```

Please avoid public disclosure until the issue is fixed.

---

## Compliance

- ✅ GDPR: All data stays on user's machine
- ✅ CCPA: User has full control of data
- ✅ Privacy by Design: Core principle
- ✅ No tracking: Completely anonymous usage

---

## Security Updates

- Check GitHub for security advisories
- Update dependencies: `pip install -r requirements.txt --upgrade`
- Rebuild executable for latest security patches

---

Last Updated: February 18, 2026
