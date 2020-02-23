import math


class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point ({self.x}, {self.y}, {self.z})'

    def __repr__(self):
        return f'Point ({self.x}, {self.y}, {self.z})'

    def __sub__(self, other):
        if not isinstance(other, Point3d):
            raise TypeError
        return Vector3d(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )


class Vector3d:
    def __init__(self, nx, ny, nz):
        self.nx = nx
        self.ny = ny
        self.nz = nz

    def __str__(self):
        return f'Vector ({self.nx}, {self.ny}, {self.nz})'

    def __repr__(self):
        return f'Vector ({self.nx}, {self.ny}, {self.nz})'

    def __pow__(self, other, modulo=None):
        if not isinstance(other, Vector3d):
            raise TypeError
        return Vector3d(
            self.ny * other.nz - self.nz * other.ny,
            self.nz * other.nx - self.nx * other.nz,
            self.nx * other.ny - self.ny * other.nx
        )

    def __sub__(self, other):
        if not isinstance(other, Vector3d):
            raise TypeError
        return Vector3d(
            self.nx - other.nx,
            self.ny - other.ny,
            self.nz - other.nz,
        )

    def __mul__(self, other):
        if not isinstance(other, Vector3d):
            raise TypeError
        return sum(
            [
                self.nx * other.nx,
                self.ny * other.ny,
                self.nz * other.nz,
            ]
        )

    def length(self):
        return math.sqrt(self.nx ** 2 + self.ny ** 2 + self.nz ** 2)


class Line:
    def __init__(self, x, y, z, nx, ny, nz, multiplier=None):
        self.p = Point3d(x, y, z)
        self.v = Vector3d(nx, ny, nz)
        self.multiplier = multiplier

    def __str__(self):
        return f'Line: ' \
               f'x={self.p.x}+{self.v.nx}t, ' \
               f'y={self.p.y}+{self.v.ny}t, ' \
               f'z={self.p.z}+{self.v.nz}t) '

    def __repr__(self):
        return f'Line: ' \
               f'x={self.p.x}+{self.v.nx}t, ' \
               f'y={self.p.y}+{self.v.ny}t, ' \
               f'z={self.p.z}+{self.v.nz}t) '

    def perpendicular_line(self, other):
        n = self.v ** other.v
        n2 = other.v ** n

        if not self.v * n2:
            raise BadData

        wagedpoint = other.p - self.p
        multiplier = (n2 * wagedpoint) / (self.v * n2)
        print(multiplier)

        return Point3d(
            self.p.x + multiplier * other.v.nx,
            self.p.y + multiplier * other.v.ny,
            self.p.z + multiplier * other.v.nz
        )


class BadData(Exception):
    pass


def unpack_data(line):
    x, y, z, nx, ny, nz = line
    return Line(x, y, z, nx, ny, nz)


def line_distance(l1, l2):
    line1 = unpack_data(l1)
    line2 = unpack_data(l2)

    c1 = line1.perpendicular_line(line2)
    c2 = line2.perpendicular_line(line1)
    print(c1)
    print(c2)

    vec = c2 - c1
    print(vec*vec)
    return vec.length()


if __name__ == '__main__':
    line_1 = (2, 2, 3, 0, 0, -1)
    line_2 = (0, -1, 2, 0, -2, 4)

    print(line_distance(line_1, line_2))
