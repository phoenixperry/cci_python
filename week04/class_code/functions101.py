
#note python must have a funciton definition before it can run a function
def run():
    print("run")

run()

def runFast(x,y):
    x = x/y
    print("run fast to", x, y)

runFast(10,10)

#we can't do this beause our function does math on x and y so they both need to be ints (integers said short hand)
#runFast("hello", 10)

x = input("what x position should I run to?")
#input returns a string type. To make it work with our function we will need to cast it
x = int(x)
y = x+x
runFast(x,y)
