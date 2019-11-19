inventory = {"apples":430, "bananas": 230, "oranges":132}
for k in inventory.keys():
    print("got key", k, "which maps to ", inventory[k])
#k is implicity what is returned, aka you get the keys

#values are the values in your dictionary. you can map this over to a list if you need to
print(inventory.values())

myList= list(inventory.values())
print(
    myList[0])

#you can also get out a tuple for each pair
myListofTuples = list(inventory.items())
print(myListofTuples)

#you can also test to see if an item is in a dictionary by using in and not in
if("apple" in inventory):
    print(inventory("apple"))

if("orange" not in inventory):
    print("there are no oranges in my inventory")
#looking up a non-exsistant key will produce a key error

