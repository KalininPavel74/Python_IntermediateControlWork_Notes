from interfaces.ICSV import ICSV
from interfaces.ILog import ILog
from util.Util import Util
from util.ExceptionProg import ExceptionProg
from os.path import exists


class CSV(ICSV):
    __SEPARATOR: str = ";"
    __REPLACEMENT: str = "REPLACEMENT_OF_SEPARATOR"

    def __init__(self, logger: ILog) -> None:
        self.__logger = logger

    def readFileCSV(self, fileName: str, charset: str) -> list:  # String[][]  throws ExceptionProg
        if fileName is None or len(fileName.strip()) == 0:
            raise ExceptionProg("Ошибка. Не указан CSV файл.")
        lst: list = list()
        if not exists(fileName):
            return lst
        try:
            with open(fileName, 'r', encoding=charset) as fileStream:
                for s in fileStream:
                    lst2: list = s.split(CSV.__SEPARATOR)
                    for i, s2 in enumerate(lst2):
                        lst2[i] = s2.replace(self.__REPLACEMENT, self.__SEPARATOR)
                    lst.append(lst2)
                return lst
        except Exception as e:
            raise ExceptionProg(f"Ошибка. Проблема с данными из файла {fileName} ({e})")

    def writeFileCSV(self, ss: tuple, fileName: str, charset: str) -> int:  # String[][] throws ExceptionProg
        if fileName is None or len(fileName.strip()) == 0:
            raise ExceptionProg("Ошибка. Не указан CSV файл.")
        if ss and len(ss) > 0:
            try:
                with open(fileName, 'w', encoding=charset) as fileStream:
                    for arS in ss:
                        sb: list = list()
                        for s in arS:
                            sb.append(s.replace(self.__SEPARATOR, self.__REPLACEMENT))
                            sb.append(CSV.__SEPARATOR)
                        del sb[len(sb) - 1]
                        sb.append('\n')
                        fileStream.write(''.join(Util.listToListOfStr(sb)))
                    fileStream.flush()
            except Exception as e:
                raise ExceptionProg(f"Ошибка. Сохранение данных в файла {fileName} ({e})")
            return len(ss)
        return 0
