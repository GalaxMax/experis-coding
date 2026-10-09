product = {
    "name": "Green Tea",
    "price": 2.99,
    "in_stock": True,
    "quantity": 100
}

print(f"Product Name: {product['name']}")
product["Description"] = """
A soothing green tea with a delicate flavor.
"""
print(f"Product Description: {product['Description']}")

for key, value in product.items():
    print(f"{key} -> {value}")