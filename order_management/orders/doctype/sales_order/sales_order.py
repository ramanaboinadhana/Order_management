# Copyright (c) 2026, Dhana and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue


class SalesOrder(Document):

    def validate(self):
        self.validate_items()
        self.calculate_total()

    def validate_items(self):
        if not self.items:
            frappe.throw("Order must have at least one Item")

        for row in self.items:
            item = frappe.get_doc("Item", row.item)

            if row.qty > item.stock_qty:
                frappe.throw(f"Not enough stock for {row.item}")

            if not row.rate:
                row.rate = item.price

            row.amount = row.qty * row.rate

    def calculate_total(self):
        self.total_amount = sum(row.amount for row in self.items)

    def on_submit(self):
        self.reduce_stock()
        self.send_email_background()

    def reduce_stock(self):
        for row in self.items:
            item = frappe.get_doc("Item", row.item)

            if row.qty > item.stock_qty:
                frappe.throw(f"Insufficient stock for {row.item}")

            item.stock_qty -= row.qty
            item.save()

        frappe.logger().info(f"Order {self.name} confirmed")

    def send_email_background(self):
        enqueue(
            "order_management.tasks.send_order_email",
            order_name=self.name,
            queue="default"
        )

