employees = {'Antony': 55000, 'Susan': 45000, 'Kiran': 60000}
categorized_employees = {name: 'high' if salary > 50000 else 'low' for name, salary in employees.items()}
print(categorized_employees)
