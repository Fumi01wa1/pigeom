class Tetrahedron:
    """Tetrahedron."""
    def __init__(self, triangle0, triangle1, triangle2):
        """Constructor."""
        self.__face = []
        self.__face.append(triangle0)
        self.__face.append(triangle1)
        self.__face.append(triangle2)

    def get_face(self, idx):
        """Getter."""
        if 0 <= idx <= 3:
            return self.__face[idx]
        else:
            print("idx = {0}".format(idx))
            print("Must be 0 <= idx <= 3.")
            raise IndexError

    def set_face(self, triangle, idx):
        """Setter."""
        if 0 <= idx <= 3:
            self.__face[idx] = triangle
        else:
            print("idx = {0}".format(idx))
            print("Must be 0 <= idx <= 3.")
            raise IndexError

    def print_self(self):
        """Print each component."""
        for i in range(3):
            print("----")
            self.__face[i].print_self()

#    def isconsistent(face0, face1, face2):
#        """Check consistency."""
