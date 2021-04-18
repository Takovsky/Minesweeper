class NumberToColor():
    def __init__(self):
        self.__numberToColorDictionary = {
            1: "blue",
            2: "green",
            3: "yellow",
            4: "purple",
            5: "maroon",
            6: "darkblue",
            7: "black",
            8: "grey",
            "M": "red",
            "O": "pink"
        }

    def getDictionary(self):
        return self.__numberToColorDictionary

    __numberToColorDictionary = []