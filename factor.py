num = int(input("enter the number:"))
i=1
print("factors of {num} are:")
while i<=num:
    if num % i==0:
        print(i,end=" ")
    i += 1


    '''enter the number:12
factors of {num} are:
1 2 3 4 6 12 '''