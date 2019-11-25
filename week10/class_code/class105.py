class Point:
    """ point class for representing and maninpulating x and y coors."""

    def __init__(self, intx, inty):

        self.x = intx
        self.y = inty

    def addUp(self):
        return self.x+self.y


p = Point(11,12)
q = Point(23,46)


num = q.addUp();
print(p.x, q.x, num)
