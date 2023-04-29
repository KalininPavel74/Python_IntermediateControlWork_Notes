from interfaces.ILog import ILog
from util.ExceptionProg import ExceptionProg
from datetime import datetime


class Log(ILog):

    def __init__(self, fileName: str = ILog.FILE_NAME, charset: str = ILog.UTF_8) -> None:
        self.__charset = charset
        self.__fileName = fileName
        self.__fileStream = None  # создать (объявить)
        self.open(self.__fileName, self.__charset)  # инициализировать

    def open(self, fileName: str = ILog.FILE_NAME, charset: str = ILog.UTF_8) -> None:
        if self.__fileStream is not None and not self.__fileStream.closed:
            self.close()
        self.__fileStream = open(self.__fileName, 'a', encoding=self.__charset)

    def write(self, text: str, className: str = '', methodName: str = '') -> None:
        if self.__fileStream.closed:
            raise ExceptionProg('Лог файл закрыт')
        self.__fileStream.write(f'{str(datetime.now())} {className} {methodName} {text}\n')
        self.__fileStream.flush()

    def close(self) -> None:
        if not self.__fileStream.closed:
            self.__fileStream.close()
