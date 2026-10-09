def average(*args): # Positional
    return sum(args) / len(args)

print(average(1,2,5,8,10))


def greet(**kwargs): # Keyword args
    for key, value in kwargs.items():
        print(f"{key} {value}")

greet(name="Alice", age=25, city="New York")
greet(name="Bob", occupation="Engineer")


print("d", "e", "w", "q", sep="---")
