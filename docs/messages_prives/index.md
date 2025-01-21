# Messages Prive Microservice Documentation

## Production Deployment

@TODO

## Developer Guide

### Prerequisites

- Docker, Please refer to the installation instructions for Docker.
- Python
- WSL (for Windows users)

### Workflows

### Project Architecture

The Messages Prive Microservice is structured as follows:

```
/messages_prives
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── services.py
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_models.py
│   └── test_services.py
├── data
│   └── sample_data.json
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```