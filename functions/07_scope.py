counter = 1

while counter <= 10:
    text = f"Iteration {counter}"
    print(text)
    counter += 1

print(f"Outside: {text}")


def greet_somebody(name):
    greeting = f"Hello {name}"
    return greeting

print(greet_somebody("Gábor"))




