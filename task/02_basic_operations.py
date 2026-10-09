def basic_operations(a, operation, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "NAN"
    else:
        return "Error: Invalid operation"

print(basic_operations(5, "+", 3))
print(basic_operations(5, "-", 3))
print(basic_operations(5, "*", 3))
print(basic_operations(5, "/", 3))