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

/api/method/order_management.api.get_orders

## Tech Used
- Frappe Framework
- Python
- MariaDB
