"""
"Classic" example of LCP violation is Square - Rectangle problem.
"""


class Reactange:
    height = None
    width = None

    def set_height(self, height: int) -> None:
        self.height = height

    def set_width(self, width: int) -> None:
        self.width = width


class Square(Reactange):
    # what happens when we change the height? Second side should be updated as well
    def set_height(self, height: int) -> None:
        self.height = height
        self.width = height

    def set_width(self, width: int) -> None:
        self.width = width
        self.height = width


# === CORRECT BEHAVIOR:
#
# width=2, height=4
r = Reactange()
r.set_width(2)
r.set_height(4)

# this code will pass
assert r.width == 2
assert r.height == 4


# === INCORRECT BEHAVIOR:
#
# Now let's use the same code, but change Reactange to Square.
# according to LSP - Square class should behave similarly to his parent class Reactange
s = Square(2)
s.set_width(2)
s.set_height(4)  # it also overrides width to be 4

# but he we will have a failure
assert r.width == 2, f"Expected: square.width=2, Actual: {s.width=}"
assert r.height == 4


"""
What can we do in this case? 
There is no clear solution for this specific example. 🧐R. Martin states the following:

    The only way to defend against this kind of LSP violation is to add mechanisms
    to the User (such as an if statement) that detects whether the Rectangle is, in
    fact, a Square. Since the behavior of the User depends on the types it uses, those
    types are not substitutable.

"""
