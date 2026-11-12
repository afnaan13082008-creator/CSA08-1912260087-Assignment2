
# Q5: Functions, Parameters and Scope
# Register Number: 1912260087

# PART 1: Mutable default argument bug

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


print("===== MUTABLE DEFAULT ARGUMENT BUG =====")

print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print("\nDefault values stored in function:")
print(add_item_buggy.__defaults__)


# PART 2: Corrected function using None

def add_item(item, order=None):

    if order is None:
        order = []

    order.append(item)
    return order


print("\n===== CORRECTED FUNCTION =====")

print(add_item("Tea"), add_item("Vada"))


# PART 3: Three independent customers

print("\n===== THREE CUSTOMERS =====")

customer1 = add_item("Tea")
customer1 = add_item("Vada", customer1)

customer2 = add_item("Coffee")
customer2 = add_item("Samosa", customer2)

customer3 = add_item("Juice")
customer3 = add_item("Sandwich", customer3)

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# PART 4: Positional, keyword and default parameters

def calculate_bill(price, quantity=1, gst=0.05):

    subtotal = price * quantity
    tax = subtotal * gst
    total = subtotal + tax

    return total, tax


print("\n===== FUNCTION PARAMETERS =====")

# Positional arguments
total1, gst1 = calculate_bill(100, 2, 0.05)

# Keyword arguments
total2, gst2 = calculate_bill(price=200, quantity=2, gst=0.05)

# Default arguments
total3, gst3 = calculate_bill(150)

print("Positional - Total:", total1, "GST:", gst1)
print("Keyword - Total:", total2, "GST:", gst2)
print("Default - Total:", total3, "GST:", gst3)


# PART 5: Local and global scope

count = 10

def local_global_example():

    local_count = 5

    print("Local variable:", local_count)
    print("Global variable accessed:", count)


print("\n===== LOCAL AND GLOBAL SCOPE =====")
local_global_example()
print("Global count outside function:", count)


# PART 6: Changing a global variable

def change_global():

    global count
    count = 20


change_global()
print("Global count after modification:", count)


# PART 7: Nonlocal scope

def outer():

    value = 10

    def inner():

        nonlocal value
        value = 30

    inner()
    print("Nonlocal value:", value)


print("\n===== NONLOCAL SCOPE =====")
outer()