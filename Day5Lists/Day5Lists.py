from countries import countries 

empty = []

item = ["Book", "Album", "Ruler", "Mouse", "Pencil"]
print(len(item))
print(item[0], item[2], item[4])

mixed_data_types = ["Ian", 21, 180, False, "123 fake address hahahalol"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[6])

it_companies[0] = "Facebookss"
print(it_companies)

it_companies.append("Netflix")
it_companies.insert(4, "Samsung")
print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)

joins = "#".join(it_companies)
print(joins)

does_exist = "Microsoft" in it_companies
does_not_exist = "qwerty" in it_companies
print(does_exist)
print(does_not_exist)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3])
print(it_companies[-4:-1])
print(it_companies[4:6])

print(it_companies.pop(0))
print(it_companies.pop(4))
print(it_companies.pop(-1))

it_companies = it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies) --> will result in error

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
both = front_end + back_end
# front_end.extend(back_end)

full_stack = both.copy()
full_stack.insert(5, "Python")
full_stack.insert(5,"SQL")
print(full_stack)

#Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Min age:", ages[0], "\nMax age:", ages[-1])

ages.append(ages[-1])
ages.append(ages[0])
ages.sort()
print(ages)
print("Median age:", (ages[6] + ages[7])/2)

average = sum(ages)/len(ages)
print(average)

range = ages[-1] - ages[0]
print(range)

a = abs(ages[0] - average)
b = abs(ages[-1] - average)

print(a)
print(b)

print(len(countries))
first_half_num = int(len(countries)/2 + 1)
print(first_half_num)
first_half = countries[0:first_half_num] 
second_half = countries[first_half_num:]

cn, rs, us, *Scan = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(cn)
print(rs)
print(us)
print(Scan)