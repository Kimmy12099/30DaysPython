age = 21 
height = 180.2 
complex = 1j 

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = base * height
print("Area of a triangle is ", area_of_triangle)

side_a = int(input("Enter side a "))
side_b = int(input("Enter side b "))
side_c = int(input("Enter side c "))
perimeter_of_triangle = side_a + side_b + side_c
print("Perimeter of a trangle is ", perimeter_of_triangle)

length = int(input("Enter a length "))
width = int(input("Enter a width "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2*length*width
print("The area of the rectangle is ", area_of_rectangle, " and the perimeter of a rectangle is ", perimeter_of_rectangle)

radius = int(input("Enter the radius of a circle: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("The area of a circle is ", area, "and the circumference of a circle is", circumference)

m = 2 #slope
b = -2 #y intercept 
x_intercept = -b/m 

qp1 = 2
qp2 = 2
rp1 = 6
rp2 = 10 
slope = (rp2-qp2)/(rp1-qp1)

if m == slope: 
    print("Wow the slopes are equal! ")
else:
    print("the slopes are not equal, here are the 2 values: ", m, " And ", slope)

#trying to find y-i = 0
for x in [-10, -5, 0, 2, -3]:
    y = x**2 + 6*x + 9 
    print(f"x = {x}, y = {y}")

print(len("Python") == len("Dragon"))
print("---")
print("on" in "Python" and "on" in "Dragon")
print("---")
print("jargon" in "I hope this course is not full of jargon")

#You can check if even numbers are divisible by 2 by using num % 2 == 0 

print("---")
print(7//3 == int(2.7))
print("---")
print(type("10") == type(10))
print("---")
print(type("9.8") == 10)
print("---")

hours = int(input("Enter hours: "))
rate_per_hour = float(input("Rate per hour "))
print("Your weekly earning is ", hours*rate_per_hour)
print("---")

years_lived = int(input("Enter the number of years you have lived "))
print("You have lived for ", years_lived*31536000, "Seconds")
print("---")

for n in range(1,6):
    print(f"{n:<3} {n**0:<3} {n:<3} {n**2:<5} {n**3:<5}")