# Copyright (c) 2026, Dhana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Customer(Document):
	

    @frappe.whitelist(allow_guest=True)
    def create_customer(customer_name, email, phone, status="Active"):
        try:
            doc = frappe.get_doc({
                "doctype": "Customer",
                "customer_name": customer_name,
                "email": email,
                "phone": phone,
                "status": status
            })

            doc.insert(ignore_permissions=True)
            frappe.db.commit()

            return {
                "status": "success",
                "message": f"Customer {doc.customer_name} created successfully",
                "name": doc.name
            }

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Customer API Error")
            return {
                "status": "error",
                "message": str(e)
            }







