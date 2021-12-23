class parent(object):
    def __init__(self, valuea):
        self.a = valuea

class child(parent):
    def __init__(self, valuea, valueb):
        super().__init__(valuea)
        self.b = valueb
        self.a = valuea + 1
    def func(self):
        print(self.a, self.b)

c = child(0,9)
print(f"c.b {c.b}")
print(f"c.a {c.a}")
c.func()