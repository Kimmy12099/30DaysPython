empty = ()

brothers = ("Richard", "Squidward", "Doggo", "Cat")
sisters = ("Abc", "Def")

siblings = brothers + sisters

print(len(siblings))
siblings = list(siblings)
siblings.append("MyMother")
siblings.append("MyFather")
siblings = tuple(siblings)
print(siblings)

brother1, brother2, brother3, brother4, sister1, sister2, mother, father = siblings

fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "lettuce", "onion")
animal_products = ("meat", "milk", "egg")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

half = int(len(food_stuff_tp)/2)
print(food_stuff_tp[half], food_stuff_tp[half+1])
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-4:-1]
del food_stuff_tp
# print(food_stuff_tp) Causes error 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia = "Estonia" in nordic_countries
iceland = "Iceland" in nordic_countries
print(estonia)
print(iceland)