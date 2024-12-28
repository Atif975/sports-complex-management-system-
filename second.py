import datetime

# Prompt user for action
x = input("Choose an action (member, staff, bookings, payments, trainers, events, inventory, feedbacks): ").strip().lower()

# Data storage
members = []
staff = []
bookings = []
payments = []
trainers = []
events = []
inventory = []
feedbacks = []
membership_type = None

# Functions for management
def add_member():
    global membership_type
    name = input("Enter your name: ").strip()
    try:
        member_id = int(input("Enter your ID: "))
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input. ID and age must be numbers.")
        return
    membership_type = input("Enter your membership type (basic/standard/premium): ").strip().lower()
    members.append({"member_id": member_id, "name": name, "age": age, "membership_type": membership_type})

def add_staff():
    name = input("Enter your name: ").strip()
    try:
        staff_id = int(input("Enter your ID: "))
        salary = int(input("Enter your salary: "))
    except ValueError:
        print("Invalid input. ID and salary must be numbers.")
        return
    role = input("Enter your role: ").strip()
    staff.append({"staff_id": staff_id, "name": name, "role": role, "salary": salary})

def add_bookings():
    try:
        member_id = int(input("Enter your member ID: "))
        booking_id = int(input("Enter your booking ID: "))
        trainer_id = int(input("Enter your trainer ID: "))
    except ValueError:
        print("Invalid input. IDs must be numbers.")
        return
    booking_date = input("Enter Booking Date (YYYY-MM-DD): ").strip()
    bookings.append({"booking_id": booking_id, "member_id": member_id, "trainer_id": trainer_id, "booking_date": booking_date})

def add_payments():
    try:
        payment_id = int(input("Enter your payment ID: "))
        member_id = int(input("Enter your member ID: "))
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid input. Payment ID, member ID, and amount must be numbers.")
        return
    status = input("Enter the current status: ").strip()
    payments.append({"payment_id": payment_id, "member_id": member_id, "amount": amount, "status": status})

def add_trainers():
    name = input("Enter your name: ").strip()
    try:
        trainer_id = int(input("Enter your ID: "))
    except ValueError:
        print("Invalid input. ID must be a number.")
        return
    specialization = input("Enter your specialization: ").strip()
    schedule = input("Enter your schedule: ").strip()
    trainers.append({"trainer_id": trainer_id, "name": name, "specialization": specialization, "schedule": schedule})

def add_events():
    name = input("Enter the event name: ").strip()
    try:
        event_id = int(input("Enter the event ID: "))
        participants = int(input("Enter the number of participants: "))
    except ValueError:
        print("Invalid input. Event ID and participants must be numbers.")
        return
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    events.append({"event_id": event_id, "name": name, "date": date, "participants": participants})

def add_inventory():
    name = input("Enter the item name: ").strip()
    try:
        item_id = int(input("Enter the item ID: "))
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Invalid input. Item ID and quantity must be numbers.")
        return
    inventory.append({"item_id": item_id, "name": name, "quantity": quantity})

def add_feedbacks():
    feedback_id = input("Enter the feedback ID: ").strip()
    try:
        member_id = int(input("Enter your member ID: "))
    except ValueError:
        print("Invalid input. Member ID must be a number.")
        return
    comments = input("Enter your comments: ").strip()
    feedbacks.append({"feedback_id": feedback_id, "member_id": member_id, "comments": comments})

# Function to display records
def display_records(records, title):
    print(f"\n{title}:")
    if records:
        for record in records:
            for key, value in record.items():
                print(f"{key}: {value}", end=", ")
            print()
    else:
        print("No records available.")

# Main program
if __name__ == "__main__":
    if x == "member":
        add_member()
        print("Court 1: Swimming \nCourt 2: Squash\nCourt 3: GYM")
        try:
            court = int(input("Enter court number: "))
        except ValueError:
            print("Invalid input. Court number must be a number.")
            court = None

        if membership_type == "basic" and court == 1:
            print("OK, you can go.")
        elif membership_type == "standard" and court in (1, 2):
            print("OK, you can go.")
        elif membership_type == "premium" and court in (1, 2, 3):
            print("OK, you can go.")
        else:
            print("Sorry! You are not eligible.")
    elif x == "staff":
        add_staff()
    elif x == "bookings":
        add_bookings()
    elif x == "payments":
        add_payments()
    elif x == "trainers":
        add_trainers()
    elif x == "events":
        add_events()
    elif x == "inventory":
        add_inventory()
    elif x == "feedbacks":
        add_feedbacks()

    # Display records
    display_records(members, "Member Details")
    display_records(staff, "Staff Details")
    display_records(bookings, "Booking Details")
    display_records(payments, "Payment Details")
    display_records(trainers, "Trainer Details")
    display_records(events, "Event Details")
    display_records(inventory, "Inventory Details")
    display_records(feedbacks, "Feedback Details")
