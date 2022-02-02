import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")
next(employee_file)

# ${:,.2f}.format([float]) this a hacky way of converting a float to have thousands seperators, a dollar sign, and two decimals.
for index in employee_file:
    print("First Name: " + index[1])
    print("Last Name: " + index[2])
    print("Salary:" + "${:,.2f}".format(float(index[3])))
    print("Bonus:" + index[4])
    Tpay = float(index[3]) * float(index[4]) + float(index[3])
    print("Total Pay:" + "${:,.2f}".format(float(Tpay)))

employees.close()
