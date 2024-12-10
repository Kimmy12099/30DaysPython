age = int(input("Enter your age: "))

if age >= 18: 
    print("You are old enough to drive")
else: 
    print("You need {} more years to learn to drive".format(18-age))

my_age = 21
your_age = int(input("Enter your age: "))

if my_age > your_age and (my_age-your_age) != 1: 
    print("I am older than you by {} years".format(my_age-your_age))
elif my_age > your_age and (my_age-your_age) == 1: 
    print(f"I am older than you by {my_age-your_age} year")
elif your_age > my_age and (your_age-my_age) != 1: 
    print("You are older than me by {} years".format(your_age-my_age))
elif your_age < my_age and (your_age-my_age) == 1:
    print(f"You are older than me by {your_age-my_age} year")
elif my_age == your_age:
    print("We are the same age!!!")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print("{} is greater than {}".format(num1, num2))
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("{} is equal to {}".format(num1, num2))

grade = int(input("Input a grade: "))
if grade >= 80: 
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50: 
    print("D")
else:
    print("F")

season = input("Please enter a month: ").capitalize()
if season == "September" or season == "October" or season =="November":
    print("The season is Autumn")
elif season =="December" or season == "January" or season == "February":
    print("The season is winter")
elif season == "March" or season == "May" or season == "June":
    print("The season is spring")
else:
    print("The season is summer ")


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_input = input("Input a fruit: ")

if fruit_input not in fruits: 
    fruits.append(fruit_input)
    print(fruits)
else:
    print("That fruit already exists in the list")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# if person["skills"] != []:
if "skills" in person.keys():
    print(person['skills'])

if "skills" in person.keys() and "Python" in person["skills"]: 
    print("This guys got Python as a skill")

if "JavaScript" in person["skills"] and "React" in person["skills"]:
    print("he is a front end developer") 
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person['skills']:
    print("he is a backend developer")
elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB"in person["skills"]:
    print("He is a fullstack developer")
else:
    print("Unknown Title")

if person["is_married"] == True and person["country"] == "Finland" and person["is_married"] == True: 
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")