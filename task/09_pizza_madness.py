def string_repeat(string, n):
    return string * n

def no_space(x):
    return x.replace(" ", "")

def number_to_string(num):
    return str(num)

def boolean_to_string(b):
    return str(b)

def abbrev_name(name):
    parts = name.split()
    return f"{parts[0][0].upper()}.{parts[1][0].upper()}"

def name_length(name):
    parts = name.split()
    return f"{parts[0]} {len(parts[0])}, {parts[1]} {len(parts[1])}"

def remove_orders(orders):
    order_list = orders.split(", ")
    order_list.pop(0)
    order_list.pop(-1)
    return str.join(", ", order_list)

def food_menu(foods):
    for i in range(0, len(foods)):
        foods[i] = f"{i+1}. {foods[i]}"
    return foods

print(food_menu(["Pizza", "Burger", "Salad", "Pasta"]))