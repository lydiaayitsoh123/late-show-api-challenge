# 🎭 Late Show API — Flask + PostgreSQL Project

This project is a RESTful API built with **Flask**, **PostgreSQL**, and **SQLAlchemy**, using **Flask-Migrate** for handling database migrations. It simulates a late-night talk show database, managing users, bookings, and show information.

---

## 📦 Features

- User registration & login (JWT authentication)
- Role-based access (admin, guests)
- Book and manage late show slots
- PostgreSQL database with schema migrations via Alembic

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/late-show-api.git
cd late-show-api

    **Login to PostgreSQL
sudo -i -u postgres
psql


  Migrations (Using Flask-Migrate)
Run the following commands to set up and apply database migrations:


flask db init
flask db migrate -m "initial migration"
flask db upgrade