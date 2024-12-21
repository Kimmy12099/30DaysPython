numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_nums = [num for num in numbers if num >= 0 ]
print(filtered_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist in list_of_lists for row in sublist for number in row]
#for sublist in list_of_lists loops over the outer list; for row in sublist loops into the inner list; number for row extracts individual numbers 
print(flattened_list)
print("")

table = [[n] + [n**k for k in range(6)] for n in range(11)]

for row in table:
    print(tuple(row))

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_list = [country for sublist  in countries for country in sublist]
result = [[country.upper(), country[:3].upper(), capital.upper()] for country, capital in flat_list]
print(result)

list_of_dict = [{'country': country.upper(), 'city': city.upper()} for country, city in flat_list]
print(list_of_dict)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

results = [f"{first} {last}" for sublist in names for first, last in sublist]

print(results)
