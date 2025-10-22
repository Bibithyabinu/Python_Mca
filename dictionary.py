student = {
    "Anu" : 340,
    "Teena" : 458,
    "john" : 300
}
asc_by_name=dict(sorted(student.items()))
print("sorted by Name(Ascending):")
print(asc_by_name)
desc_by_name=dict(sorted(student.items(), reverse=True))
print("\n sorted by Name(Descening):")
print(desc_by_name)


'''sorted by Name(Ascending):
{'Anu': 340, 'Teena': 458, 'john': 300}

 sorted by Name(Descening):
{'john': 300, 'Teena': 458, 'Anu': 340}
'''