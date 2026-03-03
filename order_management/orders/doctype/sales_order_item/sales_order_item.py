# Copyright (c) 2026, Dhana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesOrderItem(Document):
    def validate(self):
        if self.qty <= 0:
            frappe.throw("Quantity must be greater than zero")