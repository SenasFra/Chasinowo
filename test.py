class A:
    def __init__(self):
        self.name = 'A'
    
    def change_value(self, other):
        other.name = self.name

class B:
    def __init__(self):
        self.name = 'B'
    
    def change_value(self, other):
        other.name = self.name

a = A()
b = B()

print(a.name) # Output: 'A'
print(b.name) # Output: 'B'

a.change_value(b)
print(b.name) # Output: 'A'

b.change_value(a)
print(a.name) # Output: 'B'
