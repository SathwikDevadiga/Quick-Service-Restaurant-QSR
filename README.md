
# 🍔 QuickBite POS Backend

A Django REST API backend for QuickBite, a Quick Service Restaurant (QSR) Point of Sale (POS) system.  
It helps manage menu items, take orders, and analyze sales — all via RESTful endpoints.

---

## 📦 Tech Stack

- Django
- Django REST Framework
- django-filter
- SQLite (default)

---

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

# Apply migrations
python manage.py migrate

# Create superuser (for Django admin)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

---

## 🔐 Django Admin

Visit: http://127.0.0.1:8000/admin/  
Use it to:
- Manage `MenuItems`
- View and update `Orders` and `OrderItems`

---

## 📖 API Endpoints

### 🍽️ Menu Items (/menu_items/)

| Method | Endpoint                      | Description                        |
|--------|-------------------------------|------------------------------------|
| GET    | /menu_items/                  | List all menu items                |
| GET    | /menu_items/<id>/             | Retrieve a specific menu item      |
| GET    | /menu_items/available/        | List available menu items only     |
| POST   | /menu_items/                  | Create menu items		      |
| DELETE | /menu_items/<id>/             | Delete a specific menu item        |

#### 🔁 Place Order Sample Payload:
{
    "name" : "Burger",
    "price" : 120.00,
    "availability" : True
}

{
    "name" : "Pizza",
    "price" : 180.00,
    "availability" : True
}

{
    "name" : "momos",
    "price" : 150.00,
    "availability" : False
}

---

### 🧾 Orders (/orders/)

| Method | Endpoint                              | Description                         |
|--------|----------------------------------------|-------------------------------------|
| GET    | /orders/                               | List all orders                     |
| GET    | /orders/?status=pending                | Filter orders by status             |
| POST   | /orders/                               | Place a new order                   |
| GET    | /orders/<id>                           | Retrieve order details              |
| PUT    | /orders/<id>  	                  | Update order details                |		
| DELETE | /orders/<id>                           | Delete order details                |
| GET    | /orders/average-daily-sales/           | Daily average revenue (last 4 weekdays) |

#### 🔁 Place Order Sample Payload:

{
  "status": "pending",
  "order_items": [
    {"menu_item": 1, "quantity": 2},
    {"menu_item": 2, "quantity": 1}
  ]
}

---

### 🧾 Order Items (/order_items/)

| Method | Endpoint          | Description             |
|--------|-------------------|-------------------------|
| GET    | /order_items/     | List all order items    |

---

## ⚠️ Features & Rules

- ✅ Prevents placing orders with **unavailable** items.
- ✅ Supports **filtering orders** by status.
- ✅ Admin interface for full data management.
- ✅ Calculates **average daily sales** based on **completed orders** for last 4 weekdays.

---


## 📄 License

MIT License
