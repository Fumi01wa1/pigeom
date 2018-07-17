class Optray:
    """Ray of geometrical optics."""
    def __init__(self, vecQ_um, vecP_um, length_um, refractiveIndex):
        """Constructor."""
        self.__vecQ_um = vecQ_um
        self.__vecP_um = vecP_um
        self.__length_um = length_um
        self.__refractiveIndex = refractiveIndex

    def get_vecq(self):
        """Return vecQ."""
        return self.__vecQ_um

    def get_vecp(self):
        """Return vecP."""
        return self.__vecP_um

    def get_length(self):
        """Return length."""
        return self.__length_um

    def get_refractiveindex(self):
        """Return refractive index."""
        return self.__refractiveIndex

    def set_vecq(self, vecQ_um):
        """Set vecQ."""
        self.__vecQ_um = vecQ_um
        return 0

    def set_vecp(self, vecP_um):
        """Set vecP."""
        self.__vecP_um = vecP_um
        return 0

    def set_length(self, length_um):
        """Set length."""
        self.__length_um = length_um
        return 0

    def set_refractiveindex(self, refractiveindex):
        """Set refractive index."""
        self.__refractiveindex = refractiveindex
        return 0

    def print_self(self):
        print("----")
        self.__vecQ_um.print_self()
        print("----")
        self.__vecP_um.print_self()
        print("----")
        print(self.__length_um)
        print("----")
        print(self.__refractiveIndex)
        print("----")
