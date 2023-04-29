from interfaces.IGenerator import IGenerator
from threading import Lock


class Generator(IGenerator):

    def __init__(self, begin: int) -> None:
        self.__maxIdn: int = begin
        self.__lock = Lock()

    def getNewIdn(self) -> int:  # synchronized
        with self.__lock:
            self.__maxIdn += 1
            return self.__maxIdn

#        self.lock.acquire()
#        try:
#            self.__maxIdn += 1
#            return self.__maxIdn
#        finally:
#            self.lock.release()
