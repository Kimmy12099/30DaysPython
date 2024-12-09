from countries import countries 

for x in range(1,11):
    print(x)

a = 0
while a < 11:
    print(a)
    a += 1


for x in range(10,-1,-1):
    print(x)

a = 10
while a != -1:
    print(a)
    a -= 1

for x in range(1,8): 
    print("#" * x)
print("")
print("")

rows = 8
cols = 7
for _ in range (rows): 
    print("# " * cols)

print("")
print("")

for x in range(0,11): 
    print("{} x {} = {}".format(x,x,x*x))

print("")
print("")

lang = ['Python', 'Numpy','Pandas','Django', 'Flask']

for language in lang: 
    print(language)

print("")
print("")

for a in range(1,101): 
    if a % 2 == 0: 
        print(a)

print("")
print("")

for a in range(1,101):
    if a % 2 != 0:
        print(a)

print("")

sum = 0 
for b in range(1,101):
    sum += b
print(sum)

print("")

evens = 0 
odds = 0 

for c in range(1,101): 
    if c % 2 != 0: 
        odds += c 
    else: 
        evens += c 
print(f"The sum of all evens is {evens}. And the sum of all odds is {odds}")

for i in range(len(countries)): 
    if 'land' in countries[i].lower(): 
        print(countries[i])

print("")
fruits = ['banana', 'orange', 'mango', 'lemon']
sorted_fruits = []
for _ in range(len(fruits)): 
    sorted_fruits.append(fruits[-1])
    fruits.pop()

print(sorted_fruits)
print("")

