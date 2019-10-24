def square(x):
    y = pow(x,2)
    return y
    print("i will never run")

def noReturn():
    print("all functions return *something*, even if it's None")


toSquare = 10

result = square(toSquare)

print("The result of ", toSquare, " squared is ", result)

nothingToSee = noReturn()
print(nothingToSee)
