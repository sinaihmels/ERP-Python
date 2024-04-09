from .models import Customer

def add_customers():
    customers_data = [
        {"name": "John Doe", "email": "john@example.com", "address": "123 Main St, Anytown, USA", "phone": 1234567890},
        {"name": "Jane Smith", "email": "jane@example.com", "address": "456 Elm St, Othertown, USA", "phone": 9876543210},
        {"name": "Alice Johnson", "email": "alice@example.com", "address": "789 Oak St, Anothertown, USA", "phone": 1112223333},
        {"name": "Bob Brown", "email": "bob@example.com", "address": "321 Pine St, Newtown, USA", "phone": 4445556666},
        {"name": "Emily Davis", "email": "emily@example.com", "address": "654 Cedar St, Sometown, USA", "phone": 7778889999},
        {"name": "Michael Wilson", "email": "michael@example.com", "address": "987 Birch St, Thistown, USA", "phone": 9998887777},
        {"name": "Sarah Martinez", "email": "sarah@example.com", "address": "1010 Maple St, Yourtown, USA", "phone": 3332221111},
        {"name": "Daniel Garcia", "email": "daniel@example.com", "address": "1313 Elm St, Hometown, USA", "phone": 6665554444},
        {"name": "Olivia Rodriguez", "email": "olivia@example.com", "address": "1515 Oak St, Everytown, USA", "phone": 2223334444},
        {"name": "James Lopez", "email": "james@example.com", "address": "1717 Pine St, Whosville, USA", "phone": 5554443333},
        {"name": "Sophia Gonzalez", "email": "sophia@example.com", "address": "1919 Cedar St, Thatplace, USA", "phone": 8889990000},
        {"name": "William Perez", "email": "william@example.com", "address": "2020 Birch St, Thisplace, USA", "phone": 1110009999},
        {"name": "Ava Ramirez", "email": "ava@example.com", "address": "2121 Maple St, Yourplace, USA", "phone": 4449996666},
        {"name": "Alexander Torres", "email": "alexander@example.com", "address": "2323 Elm St, Anyplace, USA", "phone": 7778881111},
        {"name": "Mia Flores", "email": "mia@example.com", "address": "2525 Oak St, Everyplace, USA", "phone": 2223335555},
        {"name": "Ethan Washington", "email": "ethan@example.com", "address": "2727 Pine St, Nowhere, USA", "phone": 5556667777},
        {"name": "Charlotte Diaz", "email": "charlotte@example.com", "address": "2929 Cedar St, Somewhere, USA", "phone": 8889991111},
        {"name": "Amelia Stewart", "email": "amelia@example.com", "address": "3030 Birch St, Anywhere, USA", "phone": 1112223333},
    ]

    for data in customers_data:
        customer = Customer.objects.create(
            name=data["name"],
            email=data["email"],
            address=data["address"],
            phone=data["phone"]
        )
        print(f"Added customer: {customer.name}")