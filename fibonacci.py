n=int(input("enter the limit:"))
a=0
b=1
print("fibonacci series upto",n,"terms")
for i in range(n):
    print (a,end=" ")
    temp=a
    a=b
    b=temp+b


 '''enter the limit:10
fibonacci series upto 10 terms
0 1 1 2 3 5 8 13 21 34 '''