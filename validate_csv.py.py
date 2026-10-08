import csv

with open('data/employee.csv', 'r', newline='') as file:
    data = csv.DictReader(file)
    print("data")

    for row_number, row in enumerate(data, start=2):
        employee_id = row['id']
        salary = row['salary']

    if float(employee_id):
        raise ValueError(f"Row {row_number}: Employee ID is missing or invalid.")
    if float(salary) < 0:
        raise ValueError(f"Row {row_number}: Salary cannot be negative.")

print("Employee data validation completed successfully.")
 