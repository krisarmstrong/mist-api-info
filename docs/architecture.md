# Architecture

## Overview

Mist API Info is a Python 3.9+ tool for retrieving network information from the Mist API. It provides both synchronous and asynchronous implementations for fetching device data, WLAN configurations, beacons, clients, and RF statistics.

## System Design

### Core Components

1. **Synchronous Client** (`client.py`)
   - HTTP requests using `requests` library
   - Device information retrieval
   - WLAN configuration queries
   - Beacon and client data
   - RF statistics collection

2. **Async Client V1** (`async_client_v1.py`)
   - Asynchronous HTTP with `asyncio`
   - Concurrent API requests
   - Performance-optimized data retrieval

3. **Async Client V2** (`async_client_v2.py`)
   - Enhanced async implementation
   - Improved error handling
   - Advanced concurrency patterns

### Technology Stack

- **Python 3.9+**: Core language
- **requests**: Synchronous HTTP client
- **asyncio**: Asynchronous I/O framework
- **aiohttp**: Async HTTP client (for async versions)
- **json**: JSON parsing and generation

### Data Flow

```
API Configuration (Token, URL, Site ID)
    ↓
HTTP Request to Mist API
    ↓
JSON Response Parsing
    ↓
Data Processing
    ↓
Console Output / File Export
```

## Module Dependencies

### External Libraries
- **requests**: HTTP library for synchronous requests
- **asyncio**: Async I/O support (Python stdlib)
- **aiohttp**: Async HTTP client (for async versions)
- **json**: JSON operations (Python stdlib)
- **logging**: Logging framework (Python stdlib)

### Internal Modules
- **src/mist_api_info/client.py**: Synchronous API client
- **src/mist_api_info/async_client_v1.py**: Async client version 1
- **src/mist_api_info/async_client_v2.py**: Async client version 2
- **src/mist_api_info/__main__.py**: CLI entry point

## API Integration

### Authentication
- API token-based authentication
- Bearer token in request headers
- Secure credential handling

### Endpoints
- `/api/v1/sites/{site_id}/devices` - Device information
- `/api/v1/sites/{site_id}/wlans` - WLAN configurations
- `/api/v1/sites/{site_id}/beacons` - Beacon data
- `/api/v1/sites/{site_id}/clients` - Client information
- `/api/v1/sites/{site_id}/stats/rf` - RF statistics

## Synchronous vs Asynchronous

### Synchronous Client
- Sequential API calls
- Simple error handling
- Lower resource usage
- Easier debugging

### Asynchronous Client
- Concurrent API calls
- Faster data retrieval
- Higher throughput
- Complex error handling

## Error Handling

- API authentication failures
- Network connectivity errors
- Invalid API responses
- Rate limiting
- Timeout handling
- JSON parsing errors

## Logging

- Request/response logging
- Error tracking
- Performance metrics
- Debug information

---

Author: Kris Armstrong
