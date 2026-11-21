inventory = [
    {"name": "Widget A", "price": 10.99, "stock": 50},
    {"name": "Widget B", "price": 5.50, "stock": 120},
    {"name": "Widget C", "price": 99.00, "stock": 5},
]

def sort_inventory(items: list, key_func) -> list:
    # Use the built-in sorted() function with the key_func
    return sorted(items, key=key_func)  # Sort in descending order
    
# Define your lambdas here
by_price = lambda item: item["price"]
by_stock = lambda item: item["stock"]

print("By Price:", sort_inventory(inventory, by_price))
print("By Stock:", sort_inventory(inventory, by_stock))