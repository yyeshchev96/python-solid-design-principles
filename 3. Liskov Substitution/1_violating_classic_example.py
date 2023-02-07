"""
Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable 
with objects of its subclasses without breaking the application. 

In other words, what we want is to have the objects of our subclasses 
behaving the same way as the objects of our superclass

"Classic" example of LCP violation is Square-Rectangle problem
"""


class Reactange:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def set_a(self, new_a: int) -> None:
        self.a = new_a


class Square(Reactange):
    def __init__(self, a: int, b=None) -> None:
        # well, since all sides of square are the same, pass "a"
        super().__init__(a, a)

    # what happens when we change the size of one side?
    # second side should be updated as well
    def set_a(self, new_a: int) -> None:
        self.a = new_a
        self.b = new_a


# === CORRECT BEHAVIOR:
#
# side a=2, side b=4
reactange = Reactange(2, 4)

# We changed a to be 3. Side b should still have 4:
reactange.set_a(3)
assert reactange.a == 3
assert reactange.b == 4


# === INCORRECT BEHAVIOR:
#
# first of all, the init is slightly different, as both sides must be  are equal
square = Square(2)

# We changed a to be 3. According to Reactange Base Class logic, it should not affect "b"
square.set_a(3)
assert square.a == 3
# but here we have an error, as side "b" is also changed to 3
assert square.b == 4, f"Expected: square.b=4, Actual: {square.b=}"
