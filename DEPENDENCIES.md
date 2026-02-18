# 📋 Dependencies & Licenses

## Python Package Dependencies

All Python dependencies are open source and compatible with the MIT license.

### Direct Dependencies

| Package | Version | License | Purpose |
|---------|---------|---------|---------|
| pandas | Latest | BSD-3-Clause | Data analysis, CSV/Excel processing |
| openpyxl | Latest | MIT | Excel file manipulation |
| xlsxwriter | Latest | BSD | Advanced Excel report formatting |
| pdfplumber | Latest | MIT | PDF bank statement extraction |
| google-api-python-client | Latest | Apache 2.0 | Gmail API integration |
| google-auth-httplib2 | Latest | Apache 2.0 | Google authentication |
| google-auth-oauthlib | Latest | Apache 2.0 | OAuth2 for Gmail |
| requests | Latest | Apache 2.0 | HTTP requests |
| psutil | Latest | BSD-3-Clause | System resource monitoring |
| PyInstaller | Latest | PyInstaller License (GPL-compliant) | Executable building |

## System Dependencies

### Ollama
- **License**: MIT
- **Purpose**: Local LLM server for AI features
- **Installation**: Homebrew (macOS), direct download (Windows/Linux)
- **Notice**: Optional - app works without it (AI features disabled)

### Llama 2 Model
- **License**: Meta's Llama Community License
- **Purpose**: AI model for spending analysis
- **Notice**: 
  - Open for research and commercial use under specific terms
  - Downloaded on-demand from Ollama repository
  - Verify usage terms for your use case at: https://github.com/meta-llama/llama

## License Compatibility

✅ **All licenses are compatible**:
- MIT ↔ BSD (compatible)
- MIT ↔ Apache 2.0 (compatible)
- MIT ↔ GPL (MIT is permissive)

## Data Privacy

- No telemetry or usage tracking
- All processing done locally
- No external API calls for data analysis
- User data never leaves the user's system

## Security Notes

### Credentials Management
- OAuth tokens stored locally in `~/.config/SpendingApp/`
- Not committed to version control (see `.gitignore`)
- User configurable location

### No Embedded Secrets
- ✅ No hardcoded API keys
- ✅ No hardcoded credentials
- ✅ No authentication tokens in source code

## Contributing

When adding new dependencies:
1. Choose OSS-licensed packages only
2. Verify license compatibility with MIT
3. Update this document
4. Add to `requirements.txt`

## Questions?

For license compliance questions, see:
- LICENSE file (MIT License text)
- CITATION.cff (Citation format)
- Individual package repositories
