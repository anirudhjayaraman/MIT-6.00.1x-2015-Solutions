def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print Square(1)
print Square(2)
print Square(3)
print Square(4)
print Square(5)
print Square(6)
print Square(7)
print Square(8)
print Square(9)
print Square(10)
print Square(-3)
print Square(-100)
print Square(100)
print Square(0)

