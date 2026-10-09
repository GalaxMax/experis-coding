# def get_salary(person):
#     return person["salary"]

employees= [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 40000}
]

# sorted_employees = sorted(employees, key=get_salary)
sorted_employees = sorted(employees, key=lambda person: person["salary"])

print(sorted_employees)