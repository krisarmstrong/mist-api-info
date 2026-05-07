# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

### How to Report

1. **Do NOT open a public issue** for security vulnerabilities
2. Email security concerns to the maintainer
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment** within 48 hours
- **Initial assessment** within 7 days
- **Resolution timeline** communicated based on severity

## Security Considerations

### API Keys

This tool interacts with the Mist API. Please ensure:

- API tokens are stored securely
- Never commit API keys to version control
- Use environment variables or secure vaults for credentials
- Rotate API keys periodically

### Best Practices

- Keep dependencies updated
- Review API permissions and scopes
- Use HTTPS for all API communications
- Monitor for suspicious API activity
