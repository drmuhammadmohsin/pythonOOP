class Distance:
    def __init__(self, x, y):
     self.x = x
     self.y = y
    
    def ecludiane(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

find = Distance(5, 2)
print(find.ecludiane(find))