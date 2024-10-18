# Zabbix Listener Project

## Overview

The Zabbix Listener Project is a Django-based application designed to interact with Zabbix monitoring systems using WebSockets for real-time notifications and a Celery worker for background tasks. This project leverages Django Channels for handling WebSocket connections, allowing the application to receive and broadcast monitoring alerts efficiently.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django Channels**: For handling asynchronous protocols like WebSockets.
- **Celery**: For managing background tasks.
- **Redis**: As a message broker for Celery.
- **Daphne**: ASGI server for handling HTTP and WebSocket requests.
- **PostgreSQL**: Database management system.
- **React**: Frontend framework for building dynamic user interfaces.

## Setup and Installation

### Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows
```

### Install Required Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Apply Migrations

```bash
python manage.py migrate
```

### Start Django Development Server

```bash
python manage.py runserver
```

### Run Daphne Server for ASGI

```bash
daphne backend.asgi:application
```

### Start Redis
Ensure Redis is running in the background for Channels WebSocket support:

```bash
redis-server
```

### Start React Development Server
Navigate to the frontend directory and start the React development server:

```bash
cd frontend
yarn start  # or npm start
```

## Celery Configuration

### Start Celery Worker

```bash
celery -A backend worker --loglevel=info
```

### Start Celery Beat Scheduler

```bash
celery -A backend beat --loglevel=info
```

###  WebSocket Setup
The WebSocket listens for messages sent by the Zabbix problem consumer. Example of sending a message through async_to_sync:

```python
async_to_sync(channel_layer.group_send)(
    "zabbix_problems",
    {
        "type": "zabbix_problem_message",
        "message": {"test": "Hello, WebSocket!"},
    },
)
```
