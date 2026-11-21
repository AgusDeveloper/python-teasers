def create_discount_policy(threshold: float, rate: float):
    # Define the inner function here
    def apply_discount(amount):
    # It should accept 'amount' and use 'threshold' and 'rate'
        if amount > threshold:
            amount = amount * rate
            
        return amount
    
    return apply_discount
    # Return the inner function

# Create the policies
holiday_sale = create_discount_policy(100.0, 0.8)  # 20% discount for amounts over $100
student_discount = create_discount_policy(50.0, 0.9)  # 10% discount for amounts over $50

# Test cases
cart_1 = 150.0
cart_2 = 60.0

print(f"Holiday Sale on $150: {holiday_sale(cart_1)}")
print(f"Student Discount on $60: {student_discount(cart_2)}")

print(hash("Carlos"))
print(hash(100))
print(hash((1, 2, 3)))

print(hash([1, 2, 3]))