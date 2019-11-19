letter_count = {}
for letter in "mississippi":
    letter_count[letter] = letter_count.get(letter, 0)+1
print(letter_count)

#combined items and sort to get items in alphabetical orderings
letter_items = list(letter_count.items())
letter_items.sort()
print(letter_items)
