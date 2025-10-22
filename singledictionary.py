contact1= {
    "Anu": "8086131712"
    "Teena"  "9074458770"
}
contact2= {
    "John" : "9846175316"
    "priya" "9876543210"
}
print("contact 1:",contact1)
print("contact 2:",contact2)
merged_contacts=contact1.copy()
merged_contacts.update(contact2)
print("merged contacts:")
print("merged_contacts")


"""contact 1: {'Anu': '8086131712Teena9074458770'}
contact 2: {'John': '9846175316priya9876543210'}
merged contacts:
merged_contacts"""