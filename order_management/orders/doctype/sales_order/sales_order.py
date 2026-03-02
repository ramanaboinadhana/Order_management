# Copyright (c) 2026, Dhana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesOrder(Document):
    def validate(self):
        self.validate_items()
        self.calculate_total()

    
    def validate_items(self):
        if not self.items:
            frappe.throw("Order must have at least one Item")
        for i in self.items:
            item = frappe.get_doc("Item", i.item)
            print(item,"HHHHHHHH")

            if i.qty >item.stock_qty:
                frappe.trow(f"Not enough stock for {i.item}")
            if not i.rate:
                i.rate = item.price
            i.amount = i.qty*i.rate
    def calculate_total(self):
        total = 0
        for i in self.items:
            total += i.amount
            
        
        self.total_amount = total



    def on_update(self):
        if self.status == "Confirmed":
            self.reduce_stock()

    def reduce_stock(self):
        for row in self.items:
            item = frappe.get_doc("Item", row.item)

            if row.qty > item.stock_qty:
                frappe.throw(f"Insufficient stock for {row.item}")

            item.stock_qty -= row.qty
            item.save()

        frappe.logger().info(f"Order {self.name} confirmed")