# MAX:
input_list = [0, 1, -23, 11, 256]

print("input list:", input_list)

import math
def my_max(input_list):
  max_number = -math.inf
  # let's iterate through all the numbers:
  for number in input_list:
    # if it's bigger than what we had ...
    if number > max_number: 
      max_number = number # <- remember it

  return number

value = my_max(input_list)
print(value)


# ODD NUMBERS:
input_list = [0, 1, -23, 11, 256]

print("input list:", input_list)

def my_odd_numbers(input_list):
  new_list = []
  for number in input_list:
    # check if it's odd
    if number % 2 == 1:
      # if it is, add it to my new list:
      new_list.append(number)

  # return the whole list
  return new_list

odd_only = my_odd_numbers(input_list)
print(odd_only)