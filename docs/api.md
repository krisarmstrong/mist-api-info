# API Reference

## Command-Line Interface

### mist-api-info

Retrieve information from Mist API.

**Syntax:**
```bash
python -m mist_api_info [OPTIONS]
```

**Configuration:**
- Set API token in environment or config file
- Specify Mist API URL
- Provide site ID

**Examples:**
```bash
# Basic usage
python -m mist_api_info

# With config file
python -m mist_api_info --config config.json

# Async version
python src/mist_api_info/async_client_v1.py
```

---

## Module: mist_api_info.client

### Functions

#### `get_devices(headers: dict, mist_url: str, site_id: str) -> dict`

Retrieve device information from Mist API.

**Parameters:**
- `headers` (dict): HTTP headers with authentication
- `mist_url` (str): Mist API base URL
- `site_id` (str): Site identifier

**Returns:**
- dict: Device information

**Raises:**
- `requests.HTTPError`: If API request fails

#### `get_wlans(headers: dict, mist_url: str, site_id: str) -> dict`

Retrieve WLAN configurations.

**Parameters:**
- `headers` (dict): HTTP headers with authentication
- `mist_url` (str): Mist API base URL
- `site_id` (str): Site identifier

**Returns:**
- dict: WLAN configuration data

#### `get_beacons(headers: dict, mist_url: str, site_id: str) -> dict`

Retrieve beacon information.

**Parameters:**
- `headers` (dict): HTTP headers with authentication
- `mist_url` (str): Mist API base URL
- `site_id` (str): Site identifier

**Returns:**
- dict: Beacon data

#### `get_clients(headers: dict, mist_url: str, site_id: str) -> dict`

Retrieve client information.

**Parameters:**
- `headers` (dict): HTTP headers with authentication
- `mist_url` (str): Mist API base URL
- `site_id` (str): Site identifier

**Returns:**
- dict: Client data

#### `get_rf_stats(headers: dict, mist_url: str, site_id: str) -> dict`

Retrieve RF statistics.

**Parameters:**
- `headers` (dict): HTTP headers with authentication
- `mist_url` (str): Mist API base URL
- `site_id` (str): Site identifier

**Returns:**
- dict: RF statistics

---

## Configuration

### Environment Variables

```bash
export MIST_API_TOKEN="your-api-token"
export MIST_API_URL="https://api.mist.com"
export MIST_SITE_ID="your-site-id"
```

### config.json

```json
{
  "api_token": "your-api-token",
  "mist_url": "https://api.mist.com",
  "site_id": "your-site-id",
  "timeout": 30,
  "retry_count": 3
}
```

---

## Response Formats

### Device Response

```json
{
  "devices": [
    {
      "id": "device-id",
      "name": "AP-01",
      "model": "AP43",
      "status": "connected",
      "ip": "192.168.1.10"
    }
  ]
}
```

### WLAN Response

```json
{
  "wlans": [
    {
      "id": "wlan-id",
      "ssid": "Corporate-WiFi",
      "security": "wpa2",
      "enabled": true
    }
  ]
}
```

### Client Response

```json
{
  "clients": [
    {
      "mac": "aa:bb:cc:dd:ee:ff",
      "hostname": "laptop-01",
      "ip": "192.168.1.100",
      "connected_ap": "AP-01"
    }
  ]
}
```

---

## Error Handling

### HTTP Error Codes

- `401 Unauthorized`: Invalid API token
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Site or resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Server Error`: Mist API error

### Exception Types

```python
try:
    data = get_devices(headers, url, site_id)
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.Timeout:
    print("Request timeout")
except requests.ConnectionError:
    print("Connection error")
```

---

## Async API

### Async Client Usage

```python
import asyncio
from mist_api_info import async_client_v1

async def main():
    data = await async_client_v1.get_all_data()
    print(data)

asyncio.run(main())
```

---

Author: Kris Armstrong
