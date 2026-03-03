import frappe

@frappe.whitelist()
def get_orders():
    orders = frappe.get_all(
        "Sales Order",
        filters={"status": "Confirmed"},
        fields=["name", "customer", "total_amount"]
    )

    for order in orders:
        order["items"] = frappe.get_all(
            "Sales Order Item",
            filters={
                "parent": order["name"],
                "parenttype": "Sales Order"
            },
            fields=["item", "qty", "amount"]
        )

    return orders