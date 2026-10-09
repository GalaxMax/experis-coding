def string_repeat(string, n):
    return string * n
print(string_repeat("Hello", 3))  # Output: HelloHelloHello

def no_space(x):
    return x.replace(" ", "")
print(no_space("Hello World"))  # Output: HelloWorld

def number_to_string(num):
    return str(num)
print(number_to_string(123))  # Output: "123"

def boolean_to_string(b):
    return str(b)
print(boolean_to_string(True))  # Output: "True"

def abbrev_name(name):
    parts = name.split()
    return f"{parts[0][0].upper()}.{parts[1][0].upper()}"
print(abbrev_name("John Doe"))  # Output: "J.D"

def name_length(name):
    parts = name.split()
    return f"{parts[0]} {len(parts[0])}, {parts[1]} {len(parts[1])}"
print(name_length("John Doe"))  # Output: "John 4, Doe 3"

def remove_orders(orders):
    order_list = orders.split(", ")
    order_list.pop(0)
    order_list.pop(-1)
    return str.join(", ", order_list)
print(remove_orders("Pizza, Burger, Salad, Pasta"))  # Output: "Burger, Salad"

def food_menu(foods):
    for i in range(0, len(foods)):
        foods[i] = f"{i+1}. {foods[i]}"
    return foods
print(food_menu(["Pizza", "Burger", "Salad", "Pasta"]))  # Output: ["1. Pizza", "2. Burger", "3. Salad", "4. Pasta"]