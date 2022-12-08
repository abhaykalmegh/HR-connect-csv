"""
TASK 1:
Write a program to get details of employees whose salary is > 9000.
The output should
be in following format
{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}
"""

import csv

data = []
with open('my_utils/employees.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

employee = {}
for emp in data:
    for key, value in emp.items():
        if key == 'SALARY':
            if int(value) >= 9000:
                fst_name = emp["FIRST_NAME"]
                lst_name = emp["LAST_NAME"]
                name = f"{fst_name} {lst_name}"
                email = emp["EMAIL"]
                phone_number = emp["PHONE_NUMBER"]
                employee.update({"name": name})
                employee.update({"email": email})
                employee.update({"Phone_Number": phone_number})
                print(employee)

