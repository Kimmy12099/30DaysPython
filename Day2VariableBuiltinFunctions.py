#Day 2: 30 Days of Python Programming 
first_name = 'Ian'
last_name = 'Kim' 
Full_name  = 'Ian Kim'

country = 'Canada'
city = 'Unknown' #For privacy 
age = 21
year = 2024 

is_married = False 
is_true = True 

is_light_on = False 

first_name, last_name, country, age = "Ian", "Kim", "Canada", 21 

print(type(first_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))

print("First name length: ",len(first_name))
print("Last name length: ", len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one/num_two
remainder = num_one % num_one
exp = num_one** num_two
floor_division = num_one//num_two

radius = 30 
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

user_radius = input("Please input the radius of a circle: ")
circle_area = 3.14 * int(user_radius) ** 2 

first_name = input("Please enter a first name ")
last_name = input("Please enter a last name: ")
country = input("Please enter what country you are from ")
age = input("Please enter your age ")
