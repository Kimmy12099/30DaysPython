days = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
coding = 'Coding' + 'For' + 'All'

company = "Coding For All"
print(company)
print(len(company))

print(company.upper())
print(company.lower())

companys = "coding for all"
print(companys.capitalize())
print(companys.title())

print(companys[6:])

print(companys.index("coding"))

companys = companys.replace("coding", "Coding For All")
print(companys)

a = "Python For Everyone"
a = a.replace("Python For Everyone", "Python For All")
print(a)

split = companys.split(" ")
print(split)

business = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
business_Split = business.split(",")
print(business_Split)

print(companys[0])
print(companys[-1])
print(companys[10])


py = "Python For Everyone"
acronym = py.replace("Python For Everyone","PFE")
print(acronym)

acro = company.replace("Coding For All", "CFA")
print(acro)

company = "Coding For All"
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))
print("")

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))
print(sentence.replace("because",""))

print(company.startswith("coding"))
print(company.startswith("Coding"))

white = '   Coding For All      ' 
white = white.strip(" ")
print(white)

word1 = "30DaysOfPython"
word2 = "thirty_days_of_python"
print(word1.isidentifier())
print(word2.isidentifier())

library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join = "#".join(library)
print(join)

print("I am enjoying this challenge. \nI just wonder what is next.")

print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius {} is {} meters square.".format(radius,area))
print(f"The area of a circle with radius {radius} is {area} meters square.")

num1 = 8
num2 = 6 

print(f"{num1} + {num2} = {num1+num2}")
print("{} - {} = {}".format(num1, num2, num1-num2))
print(f"{num1} * {num2} = {num1*num2}")
print("{} / {} = {:.2f}".format(num1,num2,num1/num2))
print(f"{num1} % {num2} = {num1%num2}")
print("{} // {} = {}".format(num1,num2,num1//num2))
print(f"{num1} ** {num2} = {num1**num2}")
