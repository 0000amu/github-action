import csv

with open('data/employee.csv', 'r', newline='') as file:
    data = csv.DictReader(file)

    print("Validating employee data...")

    for row_number, row in enumerate(data, start=2):

        employee_id = row['id'].strip()
        salary = row['salary'].strip()

        # Check Employee ID
        if not employee_id:
            raise ValueError(
                f"Row {row_number}: Employee ID is missing."
            )

        try:
            int(employee_id)
        except ValueError:
            raise ValueError(
                f"Row {row_number}: Employee ID must be numeric."
            )

        # Check Salary
        try:
            salary = float(salary)
        except ValueError:
            raise ValueError(
                f"Row {row_number}: Salary must be numeric."
            )

        if salary < 0:
            raise ValueError(
                f"Row {row_number}: Salary cannot be negative."
            )

print("Employee data validation completed successfully.")