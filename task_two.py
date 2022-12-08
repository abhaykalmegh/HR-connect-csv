"""
Write a program to get "HIRE DATE" of employee whose department is within range 30
to 110 AND whose salary is > 4200.
The output should be in following format.
{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}

{ "21-JUN-07" [Hermann Baer]}
"""

import csv
from typing import Union

data = []
with open('my_utils/employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

employee = {}
for emp in data:
    for key, value in emp.items():
        if (30 > int(emp["DEPARTMENT_ID"]) < 110) and int(emp["SALARY"]) > 4200:
            hire_date = emp["HIRE_DATE"]
            fst_name = emp["FIRST_NAME"]
            lst_name = emp["LAST_NAME"]
            name = f"{fst_name} {lst_name}"
            employee.update({"HIRE DATE":hire_date})
            employee.update({"Full Name":name})
    print(employee)