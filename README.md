# Veridex Student Verification API

A simple REST API built with Django and Django REST Framework for the Veridex Student Verification Program.

## Setup

```bash
# 1. Clone the repo and navigate into it
git clone <your-repo-url>
cd veridex_api

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

---

## API Endpoints

### 1. Register a Student
**POST** `/api/students/register/`

**Request body:**
```json
{
  "full_name": "Peace Okonkwo",
  "email": "peace@example.com",
  "institution": "University of Lagos"
}
```

**Response (201):**
```json
{
  "id": 1,
  "full_name": "Peace Okonkwo",
  "email": "peace@example.com",
  "institution": "University of Lagos",
  "registered_at": "2025-01-01T10:00:00Z"
}
```

---

### 2. Submit a Task
**POST** `/api/students/<student_id>/submit/`

**Request body:**
```json
{
  "github_url": "https://github.com/peace/veridex-api",
  "description": "My Django REST API submission for Veridex verification."
}
```

**Response (201):**
```json
{
  "id": 1,
  "github_url": "https://github.com/peace/veridex-api",
  "description": "My Django REST API submission for Veridex verification.",
  "status": "pending",
  "submitted_at": "2025-01-01T12:00:00Z"
}
```

---

### 3. Get Student Profile
**GET** `/api/students/<student_id>/profile/`

**Response (200):**
```json
{
  "id": 1,
  "full_name": "Peace Okonkwo",
  "email": "peace@example.com",
  "institution": "University of Lagos",
  "registered_at": "2025-01-01T10:00:00Z",
  "submission": {
    "id": 1,
    "github_url": "https://github.com/peace/veridex-api",
    "description": "My Django REST API submission for Veridex verification.",
    "status": "pending",
    "submitted_at": "2025-01-01T12:00:00Z"
  }
}
```

> If no submission has been made yet, `"submission"` will be `null`.

---

## Project Structure

```
veridex_api/
├── manage.py
├── requirements.txt
├── README.md
├── veridex_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── students/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── migrations/
        └── __init__.py
```

## Notes

- The database used is SQLite (suitable for development/submission). 
- Each student can only have **one** submission.
- Submission `status` is managed server-side (`pending`, `reviewed`, `verified`, `rejected`).