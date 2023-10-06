class Number:
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)
    
    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)
    
    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other 
        