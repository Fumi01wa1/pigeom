class Quadrilateral:
    """Quadrilateral."""
    def __init__(self, vertex0, vertex1, vertex2, vertex3):
        """Constructor."""
        self.__vertex = []
        self.__vertex.append(vertex0)
        self.__vertex.append(vertex1)
        self.__vertex.append(vertex2)
        self.__vertex.append(vertex3)

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
        for i in range(4):
            print("----")
            self.__vertex[i].print_self()

#    def isconsistent(vertex0, vertex1, vertex2):
#        """Check consistency."""
