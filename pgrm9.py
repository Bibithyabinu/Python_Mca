basic_pay=float(input("enter your basic pay: "))
hra=0.10*basic_pay
ta=0.05*basic_pay
salary=basic_pay+hra+ta
print("basic salary",basic_pay)
print("hra",hra)
print("ta",ta)
print("salary of employee",salary)