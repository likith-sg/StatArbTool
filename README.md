# 📊 StatArb Tool - Crypto Statistical Arbitrage Dashboard API Documentation

## 1. Project Overview
The StatArb Tool is a powerful and real-time **Statistical Arbitrage Tool** for crypto traders, powered by Streamlit, copula analysis, z-score signals, and optional machine learning (RL) optimization.

## 2. API Endpoints

### GET /

* Description: Retrieve the dashboard statistics
* Request Examples:
```bash
GET / 
```
* Response:
```json
{
    "message": "Welcome to StatArb Tool",
    "stats": {
        "requests": 389,
        "avg_time": 557
    }
}
```

### GET /api/dashboard/stats

* Description: Retrieve the dashboard statistics
* Request Examples:
```bash
GET /api/dashboard/stats 
```
* Response:
```json
{
    "message": "Dashboard Statistics",
    "stats": {
        "requests": 178,
        "avg_time": 607
    }
}
```

### GET /api/endpoints/

* Description: Retrieve a list of available endpoints
* Request Examples:
```bash
GET /api/endpoints/ 
```
* Response:
```json
{
    "endpoints": [
        "/",
        "/api/dashboard/stats",
        "/api/endpoints/",
        "/api/endpoints/{uuid}",
        "/api/endpoints/drift"
    ]
}
```

### GET /api/endpoints/{uuid}

* Description: Retrieve an endpoint by UUID
* Request Examples:
```bash
GET /api/endpoints/abc 
```
* Response:
```json
{
    "endpoint": {
        "name": "Endpoint Name",
        "description": "Endpoint Description"
    }
}
```

### GET /api/endpoints/drift

* Description: Retrieve the drift statistics for endpoints
* Request Examples:
```bash
GET /api/endpoints/drift 
```
* Response:
```json
{
    "drifts": [
        {
            "endpoint": "/",
            "requests": 389,
            "avg_time": 557
        }
    ]
}
```

### POST /api/auth/signin

* Description: Authenticate user and retrieve token
* Request Examples:
```bash
POST /api/auth/signin 
{
    "username": "username",
    "password": "password"
}
```
* Response:
```json
{
    "token": "authentication_token"
}
```

### POST /api/github/repo

* Description: Create a new GitHub repository
* Request Examples:
```bash
POST /api/github/repo 
{
    "name": "Repository Name",
    "description": "Repository Description"
}
```
* Response:
```json
{
    "repo": {
        "id": 123,
        "name": "Repository Name"
    }
}
```

### OPTIONS /api/auth/signin

* Description: Retrieve the available authentication methods
* Request Examples:
```bash
OPTIONS /api/auth/signin 
```
* Response:
```json
{
    "methods": [
        "username/password",
        "github/oauth"
    ]
}
```

### GET /api/logs/

* Description: Retrieve the API logs
* Request Examples:
```bash
GET /api/logs/ 
```
* Response:
```json
{
    "logs": [
        {
            "timestamp": 1643723400,
            "method": "GET",
            "path": "/"
        }
    ]
}
```

### GET /api/logs/errors

* Description: Retrieve the API error logs
* Request Examples:
```bash
GET /api/logs/errors 
```
* Response:
```json
{
    "errors": [
        {
            "code": 404,
            "message": "Not Found"
        }
    ]
}
```

## 3. Real Usage Patterns from Production Traffic

| Endpoint | Average Requests | Average Time |
| --- | --- | --- |
| GET / | 389 | 557ms |
| GET /api/dashboard/stats | 178 | 607ms |
| GET /api/endpoints/ | 134 | 461ms |
| GET /api/endpoints/{uuid} | 134 | 461ms |
| GET /api/endpoints/drift | 104 | 438ms |

## 4. Error Responses and Edge Cases

* Error Code: 404 Not Found
* Error Message: "Not Found"
* Request Examples:
```bash
GET /non-existent-endpoint/
```
* Response:
```json
{
    "code": 404,
    "message": "Not Found"
}
```

## 5. Setup and Installation Instructions

1. Clone the repository using `git clone https://github.com/statarb-tool/statarb-tool.git`
2. Install dependencies using `npm install` or `pip install -r requirements.txt`
3. Run the application using `node index.js`

## 6. Environment Variables and Configuration

| Environment Variable | Description |
| --- | --- |
| `STATARB_TOKEN` | Authentication token for API access |
| `STATARB_GITHUB_OAUTH` | GitHub OAuth credentials for repository creation |

Note: The above Markdown is a complete API documentation output only, without preamble or explanation.