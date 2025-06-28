# Creating a Base class
class Base:
    def __init__(self,val):
        self.val = val
    # Declaring public method
    def fun(self):
        print("Public method")

    # Declaring private method
    def __fun(self):
        print("Private method")

# Creating a derived class


class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        super().__init__(val=20)

    def call_public(self):

        # Calling public method of base class
        print("\nInside derived class",self.val)
        self.fun()

    def call_private(self):

        # Calling private method of base class
        self._Base__fun()


# Driver code
obj1 = Base(val=10)

# Calling public method
obj1.fun()
obj1._Base__fun()

obj2 = Derived()
obj2.call_public()
obj2.call_private()

# Uncommenting obj1.__fun() will
# raise an AttributeError

# Uncommenting obj2.call_private()
# will also raise an AttributeError
