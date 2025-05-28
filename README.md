# 🍔 QuickBite POS Backend

A Django REST API backend for QuickBite, a Quick Service Restaurant (QSR) Point of Sale (POS) system.
It helps manage menu items, take orders, analyze sales,caching with redis and authenticate users via JWT.

---

## 📦 Tech Stack

* Django
* Django REST Framework (DRF)
* PostgreSQL
* Redis

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

# Configure the Database
# Update your .env file with the following values:
DB_NAME={database_name}
DB_USER={database_user}
DB_PASSWORD={database_password}

EMAIL_HOST_USER={your-email}
EMAIL_HOST_PASSWORD={your-app-password}

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

---

## 📬 Email Notifications via Signals

The system uses **Django custom signals** to send an order confirmation email after an order and its items are saved.

### ✉️ Setup

- Add to `.env`:
  ```
  EMAIL_HOST_USER=your_email@gmail.com
  EMAIL_HOST_PASSWORD=your_app_password
  ```

- Add to `settings.py`:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
  EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
  ```

- Define a custom signal `order_created` and connect it to a receiver that sends an email with order details.

- Trigger `order_created.send(sender=Order, order=order)` **after saving** the order and its items.

- refrence for email part : https://www.geeksforgeeks.org/setup-sending-email-in-django-project/

---

## 📊 API Documentation

* **Swagger UI**: [`/api/schema/swagger-ui/`](http://127.0.0.1:8000/api/schema/swagger-ui/)
* **ReDoc**: [`/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/)
* **Schema**: [`/api/schema/`](http://127.0.0.1:8000/api/schema/)

---

## ⚙️ Performance Profiling

`drf-silk` is enabled. Visit [`/silk/`](http://127.0.0.1:8000/silk/) after making API requests to view performance metrics.

---

## ⚠️ Features & Rules

* Prevents placing orders with unavailable items
* Environment-based secret management (`.env`)
* Filter orders by status
* Admin panel for full data control
* Daily sales analytics (last 4 weekdays)
* JWT authentication
* Swagger + ReDoc API docs
* drf-silk profiling

---

## 📄 License

MIT License
