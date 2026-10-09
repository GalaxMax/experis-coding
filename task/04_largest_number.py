def largest_number(a, b, c):
    return max(
        a + b + c,
        a + b * c,
        (a+b) * c,
        a * b * c,
        a * (b + c),
        (a * b) + c
    )

print(largest_number(4, 4, 4))