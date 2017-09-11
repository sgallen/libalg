import math

class Vector:
    CANNOT_NORMALIZE_ZERO_VECTOR = 'Can\'t normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('Coordinates must not be empty')
        except TypeError:
            raise TypeError('Coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, rhs):
        return self.coordinates == rhs.coordinates

    def __add__(self, rhs):
        return Vector([sum(i) for i in zip(self.coordinates, rhs.coordinates)])

    def __sub__(self, rhs):
        return Vector([x - y for x, y in zip(self.coordinates, rhs.coordinates)])

    def scalar_multiply(self, multiplier):
        return Vector([multiplier*i for i in self.coordinates])

    def _magnitude(self, v):
        return math.sqrt(sum([i**2 for i in v.coordinates]))
        
    def magnitude(self):
        return self._magnitude(self)

    def normalize(self):
        try:
            return self.scalar_multiply(1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR)

    def dot(self, rhs):
        return sum([x * y for x, y in zip(self.coordinates, rhs.coordinates)])

    def angle(self, rhs, in_degrees=False):
        try:
            rads = math.acos(self.dot(rhs)/(self._magnitude(self)*self._magnitude(rhs)))
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR:
                raise Exception('Can\'t compute an angle with the zero vector.')
            else:
                raise e

        if not in_degrees:
            return rads
        return rads * (180 / math.pi)


def dot_product_angle_questions():
    print('-- Dot Product and Angle Questions --')

    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    print('Dot product of {} and {} is {}'.format(str(v1), str(v2), str(v1.dot(v2))))

    v3 = Vector([-5.955, -4.904, -1.874])
    v4 = Vector([-4.496, -8.755, 7.103])
    print('Dot product of {} and {} is {}'.format(str(v3), str(v4), str(v3.dot(v4))))

    v5 = Vector([3.183, -7.627])
    v6 = Vector([-2.668, 5.319])
    print('Angle between {} and {} is {}'.format(str(v5), str(v6), str(v5.angle(v6))))

    v7 = Vector([7.35, 0.221, 5.188])
    v8 = Vector([2.751, 8.259, 3.985])
    print('Angle between {} and {} is {}'.format(str(v7), str(v8), str(v7.angle(v8, True))))

def magnitude_direction_questions():
    print('-- Magnitude and Direction Questions --')

    v5 = Vector([-0.221, 7.437])
    print('Magnitude of {} is {}'.format(str(v5), str(v5.magnitude())))

    v6 = Vector([8.813, -1.331, -6.247])
    print('Magnitude of {} is {}'.format(str(v6), str(v6.magnitude())))

    v7 = Vector([5.581, -2.136])
    print('Direction of {} is {}'.format(str(v7), str(v7.normalize())))

    v8 = Vector([1.996, 3.108, -4.554])
    print('Direction of {} is {}'.format(str(v8), str(v8.normalize())))

def main():
    # q1 = Vector([8.218, -9.341]) + Vector([-1.129, 2.111])
    # print('Question 1: {}'.format(q1))

    # q2 = Vector([7.119, 8.215]) - Vector([-8.223, 0.878])
    # print('Question 2: {}'.format(q2))
    # 
    # q3 = Vector([1.671, -1.012, -0.318]).scalar_multiply(7.41)
    # print('Question 3: {}'.format(q3))

    # magnitude_direction_questions()
    dot_product_angle_questions()


if __name__ == '__main__':
    main()
