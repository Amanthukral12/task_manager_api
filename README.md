# Task Manager API Task

## Live API URL

**Deployed URL**: [https://task-manager-api-29og.onrender.com](https://task-manager-api-29og.onrender.com)

## Tech Stack

- **Language**: Python
- **Backend Library**: Flask
- **Database**: MongoDB (via PyMongo / Flask-PyMongo)
- **Authentication**: JWT (JSON Web Token)
- **Deployment**: Render
- **Documentation**: Postman

---

## Features

- User registration and login with hashed passwords
- JWT-based authentication
- CRUD operations on tasks
- Authorization for accessing user-specific tasks
- RESTful API structure

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Amanthukral12/task_manager_api.git
cd task-manager-api
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

```bash
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
MONGO_URI=mongodb+srv://your_mongo_connection_string
```

### 5. Run the server

```bash
python app.py
```

## API Documentation (via Postman)

Postman Collection: [Click to View & Import](https://www.postman.com/amanthukral0412/aman-workspace/collection/v05ardl/task-manager?action=share&creator=10144580)

```
{
  "info": {
    "_postman_id": "17c0c6fe-1787-47ad-8cc1-8417077418e9",
    "name": "task-manager",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "10144580"
  },
  "item": [
    {
      "name": "register",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n  \"email\": \"test@example.com\",\r\n  \"password\": \"securepassword123\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/api/auth/register",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "auth", "register"]
        }
      },
      "response": [
        {
          "message": "User registered successfully!",
          "user": {
            "id": "67f5ad20ab46bdfa4b242861",
            "email": "test@example.com",
            "created_at": "2025-04-08T23:11:28.580221+00:00"
          }
        }
      ]
    },
    {
      "name": "login",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n  \"email\": \"test@example.com\",\r\n  \"password\": \"securepassword123\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/api/auth/login",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "auth", "login"]
        }
      },
      "response": [
        {
          "message": "Login successful!",
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
          "user": {
            "id": "67f5ad20ab46bdfa4b242861",
            "email": "test@example.com",
            "created_at": "2025-04-08T23:11:28.580000"
          }
        }
      ]
    },
    {
      "name": "Create new Task",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "POST",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
            "type": "text"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\r\n  \"title\": \"Complete API project\",\r\n  \"description\": \"Finish the task manager API assignment\",\r\n  \"status\": \"in-progress\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/api/tasks/",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "tasks", ""]
        }
      },
      "response": [
        {
          "message": "Task created successfully!",
          "task": {
            "id": "67f5aff18958a95c11f6d2ef",
            "title": "Complete API project",
            "description": "Finish the task manager API assignment",
            "status": "in-progress",
            "user_id": "67f5ad20ab46bdfa4b242861",
            "created_at": "2025-04-08T23:23:29.166000",
            "updated_at": "2025-04-08T23:23:29.166000"
          }
        }
      ]
    },
    {
      "name": "Get all tasks for user",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "GET",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
            "type": "text"
          }
        ],
        "url": {
          "raw": "http://localhost:5000/api/tasks/",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "tasks", ""]
        }
      },
      "response": [
        {
          "tasks": [
            {
              "id": "67f5af57f0f83c16eb1fc7cf",
              "title": "Complete API project",
              "description": "Finish the task manager API assignment",
              "status": "in-progress",
              "user_id": "67f5ad20ab46bdfa4b242861",
              "created_at": "2025-04-08T23:20:55.958000",
              "updated_at": "2025-04-08T23:20:55.958000"
            },
            {
              "id": "67f5af70c8e50cc8ecb630ad",
              "title": "Complete API project",
              "description": "Finish the task manager API assignment",
              "status": "in-progress",
              "user_id": "67f5ad20ab46bdfa4b242861",
              "created_at": "2025-04-08T23:21:20.664000",
              "updated_at": "2025-04-08T23:21:20.664000"
            },
            {
              "id": "67f5aff18958a95c11f6d2ef",
              "title": "Complete API project",
              "description": "Finish the task manager API assignment",
              "status": "in-progress",
              "user_id": "67f5ad20ab46bdfa4b242861",
              "created_at": "2025-04-08T23:23:29.166000",
              "updated_at": "2025-04-08T23:23:29.166000"
            }
          ],
          "count": 3
        }
      ]
    },
    {
      "name": "Get Single Task By ID",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "GET",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
            "type": "text"
          }
        ],
        "url": {
          "raw": "http://localhost:5000/api/tasks/67f5af70c8e50cc8ecb630ad",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "tasks", "67f5af70c8e50cc8ecb630ad"]
        }
      },
      "response": [
        {
          "task": {
            "id": "67f5af70c8e50cc8ecb630ad",
            "title": "Complete API project",
            "description": "Finish the task manager API assignment",
            "status": "in-progress",
            "user_id": "67f5ad20ab46bdfa4b242861",
            "created_at": "2025-04-08T23:21:20.664000",
            "updated_at": "2025-04-08T23:21:20.664000"
          }
        }
      ]
    },
    {
      "name": "Update a task",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "PUT",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
            "type": "text"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"status\": \"completed\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://localhost:5000/api/tasks/67f5af70c8e50cc8ecb630ad",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "tasks", "67f5af70c8e50cc8ecb630ad"]
        }
      },
      "response": [
        {
          "message": "Task updated successfully!",
          "task": {
            "id": "67f5af70c8e50cc8ecb630ad",
            "title": "Complete API project",
            "description": "Finish the task manager API assignment",
            "status": "completed",
            "user_id": "67f5ad20ab46bdfa4b242861",
            "created_at": "2025-04-08T23:21:20.664000",
            "updated_at": "2025-04-08T23:21:20.664000"
          }
        }
      ]
    },
    {
      "name": "Delete a task",
      "request": {
        "auth": {
          "type": "noauth"
        },
        "method": "DELETE",
        "header": [
          {
            "key": "Authorization",
            "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQxNTc5NzgsImlhdCI6MTc0NDE1NDM3OCwic3ViIjoiNjdmNWFkMjBhYjQ2YmRmYTRiMjQyODYxIn0.kxmpIOjGQdwHNZhNoQ1sQ7n-Hn6_NembPw7oEdkai8o",
            "type": "text"
          }
        ],
        "url": {
          "raw": "http://localhost:5000/api/tasks/67f5af70c8e50cc8ecb630ad",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "tasks", "67f5af70c8e50cc8ecb630ad"]
        }
      },
      "response": [
        {
          "message": "Task deleted successfully!"
        }
      ]
    }
  ]
}

```

## Deployment (Render)

- Platform: Render
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn wsgi:app
- Environment Variables
  - SECRET_KEY
  - JWT_SECRET_KEY
  - MONGO_URI
  - JWT_ACCESS_TOKEN_EXPIRES

## Author

Built by Aman Thukral
