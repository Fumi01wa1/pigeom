import numpy as np
from Vector3d import Vector3d


class Triangle:
    """Triangle."""
    def __init__(self, vertex0, vertex1, vertex2):
        """Constructor."""
        if Triangle.isconsistent(vertex0, vertex1, vertex2) is True:
            self.__vertex = []
            self.__vertex.append(vertex0)
            self.__vertex.append(vertex1)
            self.__vertex.append(vertex2)
        else:
            raise ValueError

    def get_vertex(self, idx):
        """Getter."""
        if 0 <= idx <= 3:
            return self.__vertex[idx]
        else:
            print("idx = {0}".format(idx))
            print("Must be 0 <= idx <= 3.")
            raise IndexError

    def set_vertex(self, vertex, idx):
        """Setter."""
        if 0 <= idx <= 3:
            self.__vertex[idx] = vertex
        else:
            print("idx = {0}".format(idx))
            print("Must be 0 <= idx <= 3.")
            raise IndexError

    def print_self(self):
        """Print each component."""
        for i in range(3):
            print("----")
            self.__vertex[i].print_self()

    @staticmethod
    def isconsistent(vertex0, vertex1, vertex2):
        """Check consistency of given points."""
        vec01 = vertex1 - vertex0
        vec02 = vertex2 - vertex0

        norm01 = vec01.norm()
        norm02 = vec02.norm()

        eps = np.finfo(float).eps

        if (norm01 < eps) or (norm02 < eps):
            # At least two of three points are almost equivalent.
            ans = False
        else:
            innerprod = vec01 ** vec02

            if innerprod == norm01 * norm02:
                # Given points belong to common line.
                ans = False
            else:
                ans = True

        return ans


####
if __name__ == "__main__":
    vec0 = Vector3d(0.0, 0.0, 0.0)
    vec1 = Vector3d(1.0, 0.0, 0.0)
    vec2 = Vector3d(0.0, 1.0, 0.0)

    tri = Triangle(vec0, vec1, vec2)
    print(Triangle.isconsistent(vec0, vec1, vec2))
