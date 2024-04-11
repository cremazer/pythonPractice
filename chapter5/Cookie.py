class Cookie:
    def __init__(self, sugar, flour):
        self.sugar = sugar
        self.flour = flour

    def __str__(self):
        return f'Cookie with {self.sugar}g of sugar and {self.flour}g of flour'

    def __repr__(self):
        return f'Cookie({self.sugar}, {self.flour})'

    def __add__(self, other):
        return Cookie(self.sugar + other.sugar, self.flour + other.flour)

    def __sub__(self, other):
        return Cookie(self.sugar - other.sugar, self.flour - other.flour)

    def __mul__(self, other):
        return Cookie(self.sugar * other, self.flour * other)

    def __truediv__(self, other):
        return Cookie(self.sugar / other, self.flour / other)

    def __floordiv__(self, other):
        return Cookie(self.sugar // other, self.flour // other)

    def __mod__(self, other):
        return Cookie(self.sugar % other, self.flour % other)

    def __pow__(self, other):
        return Cookie(self.sugar ** other, self.flour ** other)

    def __eq__(self, other):
        return self.sugar == other.sugar and self.flour == other.flour

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.sugar + self.flour < other.sugar + other.flour

    def __le__(self, other):
        return self.sugar + self.flour <= other.sugar + other.flour

    def __gt__(self, other):
        return self.sugar + self.flour > other.sugar + other.flour

    def __ge__(self, other):
        return self.sugar + self.flour >= other.sugar + other.flour

    def __len__(self):
        return self.sugar + self.flour

    def __getitem__(self, item):
        if item == 0:
            return self.sugar
        elif item == 1:
            return self.flour
        else:
            raise IndexError('Index out of range')

    def __setitem__(self, key, value):
        if key == 0:
            self.sugar