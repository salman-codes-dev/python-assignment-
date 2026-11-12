# Simple Shopping Cart

# 1. Takes the customers name as input 
customer_name = input("Enter your name: ")

# 2. Takes the names and prices of products as input
product1_name = input("Enter product 1 name: ")
product1_price = float(input(f"Enter  price for {product1_name}: "))

product2_name = input("Enter product 2 name: ")
product2_price = float(input(f"Enter  price for {product2_name}: "))

product3_name = input("Enter product 3 name: ")
product3_price = float(input(f"Enter  price for {product3_name}: "))

# 3. Calculates subtotal 
subtotal = product1_price + product2_price + product3_price

# 4. Determine the discount rate based on subtotal
if subtotal >= 5000:
    discount_rate = 0.20  # 20% discount
elif subtotal >= 3000:
    discount_rate = 0.10  # 10% discount
elif subtotal >= 1000:
    discount_rate = 0.50  #  5% discount
else:
    discount_rate = 0.0   # No discount
    
    # Formula for discont and final total
discount_amount = subtotal * discount_rate
final_total = subtotal - discount_amount

# 5. Displays the shopping summary using f-strings (f-strings)
print("\n---Shopping Summary ---")
print(f"Customer: {customer_name}")
print(f"product 1: {product1_name} ")
print(f"price: {product1_price} \n")
print(f"product 2: {product2_name} ")
print(f"price: {product2_price} \n")
print(f"product 3: {product3_name} ")
print(f"price: {product3_price} \n")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount_amount}")
print(f"Final Total: {final_total}")
