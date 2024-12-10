
def capitalize_items(capital): 
    for i in range(len(capital)):
        capital[i] = capital[i].upper()
    return capital 

print(capitalize_items(["akali","katarina","fiora","anivia","jayce"]))
print("")

def add_item(list,item):
    list = list.append(item)