# Copyright (c) 2026, Dhana and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Customer(Document):
	pass

import frappe


@frappe.whitelist()
def create_customer():
    doc = frappe.get_doc({
        "doctype": "Customer",
    "customer_name": "Test Customer",
    "email": "test@gmail.com",
    "phone": "9876543210",
    "status": "Active"
    })
    doc.insert(ignore_permissions=True)
    return {"message": f"{doc.customer_name} has been created successfully"}





