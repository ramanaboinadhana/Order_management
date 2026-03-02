import frappe


frappe.enqueue(
    "order_management.tasks.send_email",
    doc_name=self.name
)

def send_email(doc_name):
    doc = frappe.get_doc("Sales Order", doc_name)

    frappe.sendmail(
        recipients=["test@gmail.com"],
        subject="Order Confirmed",
        message=f"Order {doc.name} confirmed"
    )