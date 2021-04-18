class Coordinates():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getCoordinates(self):
        return self.__x, self.__y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    __x = None
    __y = None
