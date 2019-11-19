#del will delete an item from a dictionary
inventory = {"apples":430, "bananas": 230, "oranges":132}
print(inventory)
del inventory["apples"]
print(inventory)

#change an assoiated pair
inventory["apples"] = 0

#adding to a value pair
inventory["bananas"] +=20

#you can still use len to get length
print(len(inventory))

