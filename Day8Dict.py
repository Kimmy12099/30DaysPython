dog = {
    "Name": "Nala",
    "Color": "Beige",
    "Breed": "Golden Retriver",
    "Legs": 4,
    "Age": 7 
}

student = {
    "First Name": "Ian",
    "Last Name": "Kim",
    "Gender": "Male",
    "Age": 21, 
    "Marital Status": False, 
    "Skills": ["Python", "SQL","Powerbi", "Tableau", "Excel"],
    "Country": "Canada",
    "City": "Private",
    "Address": "Private hehe"
}

print(len(student))
print(type(student["Skills"]))
student["Skills"].append("Java")
print(student["Skills"])

print(student.keys())
print(student.values())

tpl = tuple(student)
print(tpl)
print("")
print("")

del student["Address"]
print(student)

del student