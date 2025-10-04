age=int(input("enter your age:"))
print("age",age)
if age<10:
    print("ticket rate is 7")
elif age>=10 and age<60:
    print("ticket rate is 10")
elif age>=60:
    print("ticket rate is 5")
else:
    print("invalid")

    '''enter your age:18
age 18
ticket rate is 10'''