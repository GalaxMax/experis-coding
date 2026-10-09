def index(array, n):
    return array[n]**(n) if n < len(array) else -1

print(index([1, 2, 3, 4, 5], 3))  # Output: 9