# Order Management App (Frappe)

## Features
- Customer Management
- Item Management
- Sales Order with Child Table
- Stock Validation
- Auto Calculation of Total
- Workflow (Draft → Confirmed → Cancelled)
- REST API for Orders
- Background Email Job
- Logging and Caching

## Installation

```bash
bench get-app order_management <repo_url>
bench --site yoursite install-app order_management
```

## API

GET Confirmed Orders:

/api/method/order_management.orders.get_orders

Create custome:

/api/method/order_management.customer.create_customer

Example:

http://localhost:8000/api/method/order_management.customer.create_customer?customer_name=Ram&email=ram@gmail.com&phone=9876543210

## Tech Used
- Frappe Framework
- Python
- MariaDB
