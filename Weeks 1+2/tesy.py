class Vector:

    def init (self, d):

        self. coords = [0]*d

    def len (self):

        return len(self. coords)

    def getitem (self, j):

        return self. coords[j]

    def setitem (self, j, val):

        self. coords[j] = val

    def add (self, other):

        if len(self) != len(other): # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def eq (self, other):

        return self. coords == other. coords

    def ne (self, other):

        return not self == other # rely on existing eq definition

    def str (self):

        return "<" + str(self. coords)[1:-1] + ">" # adapt list representation

    def __neg__ (self):
        final = self.len()
        for i in range (len(self)):
            final[i] = -self[i]
        return final
