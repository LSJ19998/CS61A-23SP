class Number:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, self.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[self.type_tag, other.type_tag]
        return cross_fn(self, other)

    adders = {
        ('com', 'rat'): add_complex_and_rational,
        ('rat', 'com'): add_ration_and_compelx
    }

    multipliers = {
        ('com', 'rat'):
        mul_complex_and_rational,
        ('rat', 'com'):
        mul_ration_and_complex
    }
