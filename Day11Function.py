def add_two_nums(num1, num2): 
    return num1 + num2 

print(add_two_nums(6,8))

def area_of_circle(r): 
    return 3.14*r*r

print(area_of_circle(5))

def add_all_nums(*nums):
    sum = 0
    for num in nums: 
        sum += num 
    return sum 

print(add_all_nums(1,2,3,4,5,6,7,8,9,10))

def convert_celsuis_to_fahrenheit(celsuis):
    return (celsuis*9/5) + 32 

print(convert_celsuis_to_fahrenheit(10)) 

def check_season(month): 
    month = month.capitalize()
    if month == "September" or month == "October" or month =="November":
        return "Autumn"
    elif month =="December" or month == "January" or month == "February":
        return "Winter"
    elif month == "March" or month == "May" or month == "June":
        return "Spring"
    else:
        return "Summer"

print("")
print(check_season("May"))
print("")

def calculate_slope(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)

print(calculate_slope(1,2,3,4))
print("")

def solve_quadratic_eqn(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x1, x2

print(solve_quadratic_eqn(1,5,6))
print("")    

def print_list(list):
    for i in range(len(list)):
        print(list[i])

print(print_list(["Apple","Peach","Pear","Orange"]))
print("")

def reverse_list(list):
    reversed_list = []
    for i in range(len(list)):
        reversed_list.append(list[-1])
        list.pop()
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))
print("")

def capitalize_items(capital): 
    for i in range(len(capital)):
        capital[i] = capital[i].upper()
    return capital 

print(capitalize_items(["akali","katarina","fiora","anivia","jayce"]))
print("")

def add_item(list,item):
    list.append(item) 
    return list 

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
print("")

def remove_item(list,item): 
    list.remove(item)
    return list 

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 
print("")

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i 
    return sum 

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
print("")

def sum_of_odds(num):
    sum = 0
    for i in range(num+1): 
        if i % 2 != 0:
            sum += i 
    return sum 

print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(100))
print("")

def sum_of_evens(num):
    sum = 0
    for i in range(num+1): 
        if i % 2 == 0:
            sum += i 
    return sum   

print(sum_of_evens(5))  
print(sum_of_evens(10)) 
print(sum_of_evens(100))
print("")

def even_and_odds(num):
    even = 0
    odd = 0 
    for i in range(num+1): 
        if i % 2 == 0: 
            even += 1
        else: 
            odd += 1 
    return even, odd 

print(even_and_odds(100))
print("")

def factorial(num1): 
    fac = 1
    for i in range(1, num1+1): 
        fac *= i 
    return fac 

print(factorial(5))

def is_empty(list):
    if list == []:
        return True 
    else:
        return False 

print(is_empty(["ABC"]))
print("")

def is_prime(number):
    for i in range(2,(number//2)+1):
        if number % i == 0: 
            return "Not a Prime Number"
    return "It is a prime number"

print(is_prime(20))
print(is_prime(5))

def unique_items(list): 
    sets = set(list)
    if len(list) == len(sets):
        return "They are all unique items"
    else: 
        return "They are not all unique items"

duplicates = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1, 9, 10, 4, 11]
without_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(unique_items(duplicates))
print(unique_items(without_duplicates))

list1 = [
    123,                  # Integer
    3.14,                 # Float
    "Hello",              # String
    True,                 # Boolean
    None,                 # NoneType
    [1, 2, 3],            # List
    (4, 5),               # Tuple
    {6, 7, 8},            # Set
    {"key1": "value1"},   # Dictionary
    b"abc"                # Bytes
]

list2 = [12,435,6,7,8,234,56,8,230]
def same_data_type(list):
    for i in range(len(list)):
        if type(list[0]) != type(list[i]):
            return False
    return True 

print(same_data_type(list1))
print(same_data_type(list2))

def valid_variable(variable):
    if variable.isidentifier() == True:
        return True
    return False

print("")
print(valid_variable("20943"))
print(valid_variable("HelloWorld"))
print(valid_variable("kgfij"))



