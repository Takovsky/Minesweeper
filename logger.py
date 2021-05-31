import datetime
import os
from pathlib import Path

class Logger():
    def __init__(self):
        super(Logger, self).__init__()
        self.__createDirectory()

    def __createDirectory(self):
        self.__mydir = os.getcwd()
        self.__mydir += "/logs"
        Path(self.__mydir).mkdir(parents=True, exist_ok=True)

    def removeFileIfExists(self, filename):
        if os.path.exists(self.__mydir + "/" + filename):
            os.remove(self.__mydir + "/" + filename)

    def createFile(self, filename):
        f = open(self.__mydir + "/" + filename, "w")
        f.close()

    def writeToFile(self, filename, what):
        f = open(self.__mydir + "/" + filename, "a")
        f.write(what)
        f.close()

    __mydir = None
