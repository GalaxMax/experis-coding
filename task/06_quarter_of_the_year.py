def quarter_of_the_year(month):
    if month in [1, 2, 3]:
        return 1
    elif month in [4, 5, 6]:
        return 2
    elif month in [7, 8, 9]:
        return 3
    elif month in [10, 11, 12]:
        return 4
    else:
        return print("Month must be between 1 and 12")

print(quarter_of_the_year(5))  # Output: 2