from cmath import sqrt
from decimal import Decimal


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        try:
            if len(self.coordinates) != len(v.coordinates):
                raise ValueError
            
            for x in range(len(self.coordinates)):

                print(self.coordinates[x] + v.coordinates[x])

        except ValueError:
            raise ValueError('Plus: The Two vectors does not have the same length')
        

    def minus(self, v):
        try:
            if len(self.coordinates) != len(v.coordinates):
                raise ValueError
            
            for x in range(len(self.coordinates)):

                print(self.coordinates[x] - v.coordinates[x])

        except ValueError:
            raise ValueError('Minus: The Two vectors does not have the same length')

    def scale(self, num):
        try:
            for item in self.coordinates:
                print(item * num)

        except TypeError:
            raise TypeError('scale: please enter a digit as number to multiply')


    def magnitude(self):
        sum = 0
        for item in self.coordinates:
            sum += item * item
        
        magnitude = round(sqrt(round(sum,3)).real, 3)
        
        return magnitude


    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            for item in self.coordinates:
                print(round((1/magnitude) * item, 3))


print('Plus')        
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
v1.plus(v2)

print('Minus===========================')
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])
v1.minus(v2)

print('scale===========================')
v = Vector([1.671, -1.012, -0.318])
v.scale(7.41)

print('Magnitude=======================')
v = Vector([-0.221, 7.437])
print('Magnitude= ' + str(v.magnitude()))

v = Vector([8.813, -1.331, -6.247])
print ('Magnitude= ' + str(v.magnitude()))

print('Normalize=======================')
v = Vector([5.581, -2.136])
v.normalize()

v = Vector([1.996, 3.108, -4.554])
v.normalize()