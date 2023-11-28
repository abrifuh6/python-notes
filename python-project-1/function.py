# Function to calculate total price with tax
def calculate_total_price(items, tax_rate=0.1):
    """Calculate the total price of items including tax."""
    subtotal = sum(items)
    tax = subtotal * tax_rate 
    total_price = subtotal + tax 
    return total_price 

# Example of items in the shooping cart
shopping_cart_items = [10, 20, 30, 40]

# Calculating and printing the total prices
total_price = calculate_total_price(shopping_cart_items)
print(f"The toatal price is: ${total_price:.2f}")


# Function to output hello world!! 

def str_text (string1, string2):
    new_str = string1 + string2 
    return new_str

print(str_text("hello ", "world!!" ))
     