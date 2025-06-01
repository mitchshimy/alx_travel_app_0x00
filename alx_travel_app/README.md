# 🧳 ALX Travel App

A simple Django-based travel booking API and frontend interface, created as part of the **ALX Software Engineering** program.

## 🚀 Features

- List travel properties (listings) with details like title, description, price, location, etc.
- Book a listing by specifying start and end dates
- View listings via a basic HTML template
- REST API for listings and bookings
- Admin interface for managing data
- Swagger/OpenAPI documentation

---

## 🛠 Tech Stack

- **Backend**: Django 5, Django REST Framework
- **Database**: SQLite (default, can switch to PostgreSQL)
- **Docs**: drf-yasg (Swagger)

---

## 📦 Project Structure

```bash
alx_travel_app_0x00/
├── alx_travel_app/        # Main Django project config
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   └── ...
├── listings/              # Listings app (models, views, serializers)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── templates/
│       └── listings/
│           └── home.html
├── manage.py
└── requirements.txt
