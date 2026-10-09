products = [
    {"name": "Green Tea", "price": 2.99, "quantity": 100, "Location": "Store A"},
    {"name": "Black Tea", "price": 3.49, "quantity": 50, "Location": "Store B"},
    {"name": "White Tea", "price": 4.99, "quantity": 30, "Location": "Store A"},
    {"name": "Oolong Tea", "price": 5.99, "quantity": 20, "Location": "Store D"}
]

unique_locations = set()
for product in products:
    unique_locations.add(product["Location"])

print(unique_locations)