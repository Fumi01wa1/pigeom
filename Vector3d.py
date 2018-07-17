import numpy as np

np.seterr(all="raise")


class Vector3d:
    """3DVector."""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Constructor."""
        self.__v = np.zeros((3), dtype='double')
        self.__v[0] = x
        self.__v[1] = y
        self.__v[2] = z

    def get_x(self):
        """Return x."""
        return self.__v[0]

    def get_y(self):
        """Return y."""
        return self.__v[1]

    def get_z(self):
        """Return z."""
        return self.__v[2]

    def get_v(self):
        """Return z."""
        return self.__v

    def set_x(self, x):
        """Set x."""
        self.__v[0] = x
        return 0

    def set_y(self, y):
        """Set y."""
        self.__v[1] = y
        return 0

    def set_z(self, z):
        """Set z."""
        self.__v[2] = z
        return 0

    def set_xyz(self, x, y, z):
        """Set x, y and z."""
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        return 0

    def __add__(self, other):
        """Addition."""
        vec = Vector3d()
        vec.__v = self.__v + other.__v
        return vec

    def __sub__(self, other):
        """Subtraction."""
        vec = Vector3d()
        vec.__v = self.__v - other.__v
        return vec

    def __mul__(self, other):
        """Vector times scalar."""
        vec = Vector3d()
        vec.__v = self.__v * other
        return vec

    def __truediv__(self, other):
        """Vector divided by scalar."""
        try:
            vec = Vector3d()
            vec.__v = self.__v / other
        except FloatingPointError as e:
            print(e)
            print("Vector3d.__truediv__(self, other)")
            print("self = ")
            self.print_self()
            print("other = ")
            print(other)
        else:
            return vec

    def __pow__(self, other):
        """Inner product."""
        innerProd = np.dot(np.transpose(self.__v), other.__v)
        return innerProd

    def __xor__(self, other):
        """Outer product."""
        vec = Vector3d()
        vec.__v = np.cross(self.__v, other.__v)
        return vec

    def __rmul__(self, other):
        """Scalar times vector."""
        vec = Vector3d()
        vec.__v = self.__v * other
        return vec

    def __iadd__(self, other):
        """Addition."""
        self.__v += other.__v
        return self

    def __isub__(self, other):
        """Subtraction."""
        self.__v -= other.__v
        return self

    def __imul__(self, other):
        """Vector times scalar."""
        self.__v *= other
        return self

    def __itruediv__(self, other):
        """Vector divided by scalar."""
        try:
            self.__v /= other
        except FloatingPointError as e:
            print(e)
            print("Vector3d.__truediv__(self, other)")
            print("self = ")
            self.print_self()
            print("other = ")
            print(other)
        else:
            return self

    def norm(self):
        """Return norm"""
        return np.linalg.norm(self.__v)

    def normalize(self):
        """Return normalized vector"""
        tempNorm = self.norm()
        tempVec = self / tempNorm
        return tempVec

    def normalizeme(self):
        """Normalize itself."""
        vec = self.normalize()
        self.__v = vec.__v
        return self

    def rotate_x(self, deg):
        """Rotate vecor with respect to x axis."""
        rad = np.deg2rad(deg)

        valCos = np.cos(rad)
        valSin = np.sin(rad)

        mat = np.array([[1.0,    0.0,     0.0],
                        [0.0, valCos, -valSin],
                        [0.0, valSin, valCos]])

        vec = Vector3d()
        vec.__v = mat @ self.__v

        return vec

    def rotate_y(self, deg):
        """Rotate vecor with respect to y axis."""
        rad = np.deg2rad(deg)

        valCos = np.cos(rad)
        valSin = np.sin(rad)

        mat = np.array([[ valCos,  0.0, valSin],
                        [    0.0,  1.0,    0.0],
                        [-valSin,  0.0, valCos]])

        vec = Vector3d()
        vec.__v = mat @ self.__v

        return vec

    def rotate_z(self, deg):
        """Rotate vecor with respect to z axis."""
        rad = np.deg2rad(deg)

        valCos = np.cos(rad)
        valSin = np.sin(rad)

        mat = np.array([[valCos, -valSin, 0.0],
                        [valSin,  valCos, 0.0],
                        [   0.0,     0.0, 1.0]])

        vec = Vector3d()
        vec.__v = mat @ self.__v

        return vec

    def print_self(self):
        """Print each component."""
        print(self.__v)
