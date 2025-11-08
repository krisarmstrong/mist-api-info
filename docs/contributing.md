# Contributing Guide

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/mist_api_Info.git
cd mist_api_Info
pip install -e ".[dev]"
pytest -q
```

## Development Workflow

1. **Branch**: `git checkout -b feature/your-feature`
2. **Code**: Follow PEP 8, add type hints
3. **Test**: `pytest -q --cov`
4. **Commit**: `git commit -m "feat: description"`
5. **Push**: `git push origin feature/your-feature`
6. **PR**: Open pull request

## Code Standards

- Python 3.9+
- PEP 8 compliant
- Type hints required
- Docstrings for all functions
- Tests for new features

## Project Structure

```
mist_api_Info/
├── src/
│   └── mist_api_info/
│       ├── __init__.py
│       ├── __main__.py
│       ├── client.py           # Sync client
│       ├── async_client_v1.py  # Async v1
│       └── async_client_v2.py  # Async v2
├── tests/
├── docs/
│   ├── architecture.md
│   ├── api.md
│   └── contributing.md
└── CONTRIBUTING.md
```

## API Testing

### Mocking Mist API

Use `responses` library to mock HTTP requests:

```python
import responses
from mist_api_info.client import get_devices

@responses.activate
def test_get_devices():
    responses.add(
        responses.GET,
        'https://api.mist.com/api/v1/sites/site-id/devices',
        json={'devices': []},
        status=200
    )

    headers = {'Authorization': 'Bearer token'}
    result = get_devices(headers, 'https://api.mist.com', 'site-id')
    assert 'devices' in result
```

### Integration Testing

Create test site in Mist sandbox:
- Use test API token
- Verify API endpoints
- Test rate limiting
- Check error handling

## Async Development

### Testing Async Code

```python
import pytest
from mist_api_info.async_client_v1 import get_devices_async

@pytest.mark.asyncio
async def test_async_get_devices():
    # Mock async HTTP calls
    result = await get_devices_async(headers, url, site_id)
    assert result is not None
```

### Performance Testing

- Measure request latency
- Test concurrent requests
- Monitor resource usage
- Compare sync vs async performance

## Security Guidelines

### API Token Handling

- Never commit API tokens
- Use environment variables
- Implement token rotation
- Log token usage (not values)

### Credential Storage

```python
# Good
token = os.environ.get('MIST_API_TOKEN')

# Bad
token = "hardcoded-token-value"
```

## Documentation

### Adding New API Endpoints

1. Document endpoint in `api.md`
2. Add function docstring
3. Include usage example
4. Update architecture diagram

### Code Examples

Provide complete, runnable examples:

```python
"""
Example: Retrieve all devices

This script demonstrates how to retrieve device
information from the Mist API.
"""
from mist_api_info.client import get_devices

headers = {'Authorization': f'Bearer {token}'}
devices = get_devices(headers, mist_url, site_id)
print(devices)
```

---

Author: Kris Armstrong
