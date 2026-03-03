import frappe

def send_order_email(order_name):
    order = frappe.get_doc("Sales Order", order_name)

    frappe.sendmail(
        recipients=["test@gmail.com"],
        subject=f"Order Confirmed: {order.name}",
        message=f"""
        Dear Customer,<br><br>
        Your order <b>{order.name}</b> has been confirmed.<br><br>
        Thank you.
        """
    )

    frappe.logger().info(f"Email sent for order {order.name}")