def form_the_minimum(array):
    array.sort()
    minimum_number = ""
    for number in array:
        minimum_number += f"{number}"
    return minimum_number

print(form_the_minimum([5, 3, 1, 4, 2]))  # Output: 12345