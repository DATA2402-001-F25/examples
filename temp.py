class A:

    def __init__(self, x):
        self.x = x
        print(x)
        
class B(A):

    def __init__(self, y):
        self.y = y
        super().__init__(5)

    def method(self):
        print(self.x)

class C(B):

    def __init__(self, z):
        super().__init__(z)
        print(self.y)

obj1 = A(5)
obj2 = C(10)
obj2.method()
