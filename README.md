# Healthcare-Backend-

A secure RESTful backend system for a healthcare application, built with Django, Django REST Framework (DRF), PostgreSQL, and JWT authentication.

---

## 🚀 Features

- 🔐 User registration and JWT login
- 🧑 Patient management (CRUD)
- 👨‍⚕️ Doctor management (CRUD)
- 🔗 Patient–Doctor assignment mapping
- ✅ JWT Authentication with `djangorestframework-simplejwt`
- 🐘 PostgreSQL integration using Django ORM
- 📦 Environment-based config management with `python-decouple`

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT
- Python Decouple

---

## 📁 Project Structure


---

## 🧪 API Endpoints

### 🔐 Authentication

| Method | Endpoint              | Description           |
|--------|-----------------------|-----------------------|
| POST   | `/api/auth/register/` | Register new user     |
| POST   | `/api/auth/login/`    | JWT token login       |

### 🧑 Patient APIs (Auth required)

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | `/api/patients/`     | List all user patients   |
| POST   | `/api/patients/`     | Create a new patient     |
| GET    | `/api/patients/<id>/`| Get specific patient     |
| PUT    | `/api/patients/<id>/`| Update patient           |
| DELETE | `/api/patients/<id>/`| Delete patient           |

### 👨‍⚕️ Doctor APIs (Auth required)

| Method | Endpoint             | Description         |
|--------|----------------------|---------------------|
| GET    | `/api/doctors/`      | List all doctors    |
| POST   | `/api/doctors/`      | Add new doctor      |
| GET    | `/api/doctors/<id>/` | Doctor details      |
| PUT    | `/api/doctors/<id>/` | Update doctor       |
| DELETE | `/api/doctors/<id>/` | Delete doctor       |

### 🔗 Mapping APIs (Auth required)

| Method | Endpoint                    | Description                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/api/mappings/`            | List all patient-doctor mappings       |
| POST   | `/api/mappings/`            | Assign a doctor to a patient           |
| GET    | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient    |
| DELETE | `/api/mappings/<id>/`       | Remove a doctor from a patient         |

---

## 🧰 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-healthcare-backend.git
cd django-healthcare-backend

```

### 2. Set up virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL database
```bash
Create a PostgreSQL database named healthcare_db. Then update your .env file:
DB_NAME=healthcare_db
DB_USER=your_pg_username
DB_PASS=your_pg_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply migrations and create a superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
Visit http://localhost:8000 to view the app.
```




