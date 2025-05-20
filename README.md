# 🍔 QuickBite POS Backend

A Django REST API backend for QuickBite, a Quick Service Restaurant (QSR) Point of Sale (POS) system.
It helps manage menu items, take orders, analyze sales, and authenticate users via JWT.

---

## 📦 Tech Stack

* Django
* Django REST Framework (DRF)
* drf-spectacular (for API schema and Swagger docs)
* drf-silk (for performance profiling)
* SQLite (default)

---
## Base URL

`http://127.0.0.1:8000/`

## 🚀 Getting Started

### 🔧 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/SathwikDevadiga/Quick-Service-Restaurant-QSR.git
cd quickbite

# Create virtual environment (optional)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#Configure the Database
Update your .env file with the following values:
DB_NAME=quickbite_db
DB_USER=root
DB_PASSWORD=root

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for Django admin)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

---

## 🔐 Django Admin

Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
Use it to:

* Manage `MenuItems`
* View and update `Orders` and `OrderItems`
* Manage users

---

## 📖 API Endpoints

### 🍽️ Menu Items (`/menu_items/`)

| Method | Endpoint                | Description                    |
| ------ | ----------------------- | ------------------------------ |
| GET    | /menu_items/           | List all menu items            |
| GET    | /menu_items/{id}/      | Retrieve a specific menu item  |
| GET    | /menu_items/available/ | List available menu items only |
| POST   | /menu_items/           | Create menu items              |
| DELETE | /menu_items/{id}/      | Delete a specific menu item    |

#### 🔁 Sample Payload:

```json
{
  "name": "Burger",
  "price": 120.00,
  "availability": true
}
```

---

### 🧾 Orders (`/orders/`)

| Method | Endpoint                     | Description                             |
| ------ | ---------------------------- | --------------------------------------- |
| GET    | /orders/                     | List all orders                         |
| GET    | /orders/?status=pending      | Filter orders by status                 |
| POST   | /orders/                     | Place a new order                       |
| GET    | /orders/{id}/                | Retrieve order details                  |
| PUT    | /orders/{id}/                | Update order details                    |
| DELETE | /orders/{id}/                | Delete order                            |
| GET    | /orders/average-daily-sales/ | Daily average revenue (last 4 weekdays) |

#### 🔁 Place Order Sample Payload:

```json
{
  "status": "pending",
  "order_items": [
    {"menu_item": 1, "quantity": 2},
    {"menu_item": 2, "quantity": 1}
  ]
}
```

---

### 📦 Order Items (`/order_items/`)

| Method | Endpoint       | Description          |
| ------ | -------------- | -------------------- |
| GET    | /order_items/ | List all order items |

---

## 👤 User Authentication & Management (`/auth/`)

| Method | Endpoint                 | Description                         |
| ------ | ------------------------ | ----------------------------------- |
| GET    | /auth/                   | List all users (admin only)         |
| POST   | /auth/                   | Create user                         |
| GET    | /auth/{id}/              | Retrieve a specific user            |
| POST   | /auth/api/token/         | Obtain JWT access and refresh token |
| POST   | /auth/api/token/refresh/ | Refresh JWT access token            |

#### 🔐 Create User Example
```json
POST /auth/api/token/
    {
        "id": 5,
        "username": "khushi",
        "email": "khushi@example.com",
        "password": "12345",
        "phone_number": "7028252987",
        "address": "A-308  Vinayak C.H.S"
    }
```

#### 🔐 Token Obtain Example
```json
POST /auth/api/token/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

#### 🔁 Response

```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

---

## 📊 API Documentation

Interactive docs are available at:

* **Swagger UI**: [`/api/schema/swagger-ui/`](http://127.0.0.1:8000/api/schema/swagger-ui/)
* **ReDoc**: [`/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/)
* **Schema**: [`/api/schema/`](http://127.0.0.1:8000/api/schema/)

Generated using `drf-spectacular`.

---

## ⚙️ Performance Profiling

`drf-silk` is enabled to help you analyze and optimize your API performance.
Visit [`/silk/`](http://127.0.0.1:8000/silk/) after making API requests.

---

## ⚠️ Features & Rules

* ✅ Prevents placing orders with **unavailable** items
* ✅ .env file for handling secrete keys
* ✅ Supports **filtering orders** by status
* ✅ Admin interface for full data management
* ✅ Calculates **average daily sales** for last 4 weekdays
* ✅ JWT-based **authentication** and **authorization**
* ✅ Clean **interactive API documentation**
* ✅ Route performance profiling via `drf-silk`

---

## 📄 License

MIT License
