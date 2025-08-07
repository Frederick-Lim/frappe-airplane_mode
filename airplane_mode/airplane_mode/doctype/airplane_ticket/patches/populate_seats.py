import frappe

def execute():
    tickets = frappe.db.get_all("Airplane Ticket")
    for t in tickets:
        ticket = frappe.get_doc("Airplane Ticket", t)
        if not ticket.seat:  # Check if seat is already set
            ticket.set_seat()
            ticket.save()

    frappe.db.commit()