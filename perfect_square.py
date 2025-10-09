start_range=int(input("enter the starting range (4 digit min):"))
end_range=int(input("enter the ending range (4 digit max):"))
evendigit=[]
for num in range(start_range,end_range+1):
    if all(int(digit)%2==0 for digit in str(num)):
        sqrt = int(num**0.5)
        if sqrt* sqrt==num:
            evendigit.append(num)
if evendigit !=[]:
    print("no with all even digits and are perfact squares:")
    print(evendigit)
else:
    print("no with no even digits and are perfact squares:")

'''enter the starting range (4 digit min):1000
enter the ending range (4 digit max):9999
no with all even digits and are perfact squares:
[4624, 6084, 6400, 8464]
'''