# Task 1

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def new_ticket(tickets, ticket_id, customer, issue, status):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"customer": customer, "issue": issue, "status": status}
        print(f"Service ticket {ticket_id} added...")
    else:
        print(f"Service ticket with id {ticket_id} already exists...")

def update_ticket(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"{ticket_id}'s status has been updated to {status}")
    else:
        print(f"Ticket ID {ticket_id} not found in the system...")

def display_tickets():
    for key, value in service_tickets.items():
        print(f"{key}: {value}")

new_ticket(service_tickets, "Ticket004", "George", "Sucks at his job", "open")
update_ticket(service_tickets, "Ticket002", "open")
display_tickets()
