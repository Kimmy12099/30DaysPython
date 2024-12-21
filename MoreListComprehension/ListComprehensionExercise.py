# Resources used
# https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/
# https://www.w3schools.com/python/python_lists_comprehension.asp

numbers_divis_by_7 = [x for x in range(1001) if x % 7 == 0]
print(numbers_divis_by_7)
print("")

numbers_with_three = [i for i in range(1001) if "3" in str(i)]
print(numbers_with_three)

# for i in range(1001): 
#     if "3" in str(i): 
#         numbers_with_three.append(i)
# print(numbers_with_three)

str_example = "  hello  "
count = 0
# count = 0
# for i in range(len(str_example)):
#     if str_example[i] == " ": 
#         count += 1

# print(count)

spaces_in_string = sum([1 for i in str_example if i ==" "])
print(spaces_in_string)

str_example2 = "Hello my name is Ian, I am a Python Programmer"
remove_vowels = [i for i in str_example2 if i.lower() not in "aeiou"]
remove_vowels = "".join(remove_vowels)
print(remove_vowels)

str_example3 = "Hello my name is Ian, I am a Python Programmer"
str_example3 = str_example3.split(" ")
words_in_string = [word for word in str_example3 if len(word) < 4]
print(words_in_string)