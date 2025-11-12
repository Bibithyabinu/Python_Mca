import csv
field_name=['No','Company','Car model']
car=[
    {'No':1,'Company':'Ferrari','Car model':'GH'},
    {'No':2,'Company':'BMW','Car model':'X5'},
    {'No':3,'Company':'Maruti','Car model':'Swift'},
    {'No':4,'Company':'Audi','Car model':'RS7'},
    {'No':5,'Company':'Toyota','Car model':'Fortuner'},
]
with open('car.csv','w', newline='') as csvfile:
    write= csv.DictWriter(csvfile,fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('car.csv',newline='')as csvfile:
     d=csv.reader(csvfile)
     for r in d:
         print(','.join(r))
         print(r)

        '''No,Company,Car model
['No', 'Company', 'Car model']
1,Ferrari,GH
['1', 'Ferrari', 'GH']
2,BMW,X5
['2', 'BMW', 'X5']
3,Maruti,Swift
['3', 'Maruti', 'Swift']
4,Audi,RS7
['4', 'Audi', 'RS7']
5,Toyota,Fortuner
['5', 'Toyota', 'Fortuner']
'''