class Raypath:
    """Raypath."""
    def __init__(self, initray):
        """Constructor."""
        self.__optray = []
        self.__optray.append(initray)

    def getoptray(self, iRay):
        """Return optray."""

        nRay = len(self.__optray)

        if nRay <= iRay:
            print('nRay = {0}'.format(nRay))
            print('iRay = {0}'.format(iRay))
            raise IndexError
        else:
            return self.__optray[iRay]

    def appendoptray(self, optray):
        """append optray to raypath."""
        self.__optray.append(optray)
        return 0
