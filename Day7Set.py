it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["1","2","3"])
it_companies.remove("Facebook")
print(it_companies)

join = A.union(B)
print(join)
c = A.intersection(B)
print(c)

print(A.issubset(B))
print(A.isdisjoint(B))

AB = A.union(B)
BA = B.union(A)
print(AB)
print(BA)

sym_diff = A.symmetric_difference(B)
print(sym_diff)

del A
del B
# print(A, B) ERROR
print("")
print("")

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Len of age list", len(age))
print("Len of age set", len(age_set))
print("")

text = "I am a teacher and I love to inspire and teach people."
split = text.split(" ")
split_text = set(split)
print(len(split))