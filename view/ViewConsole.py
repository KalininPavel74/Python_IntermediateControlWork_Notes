from interfaces.IView import IView
from interfaces.ILog import ILog
from view.ExceptionExit import ExceptionExit


class ViewConsole(IView):

    def __init__(self, title: str, charset: str, exitLetters: tuple, logger: ILog) -> None:
        self.__exitLetters = exitLetters
        self.__logger = logger
        self.__printToConsoleAndLog(title)
        self.__printToConsoleAndLog('(Для выхода из программы вместо ответа нажмите кнопку: '
                                    + str(self.__exitLetters) + ")\n")

    def request(self, description: str) -> str:  # throws ExceptionExit
        strInputData: str = description + " Введите данные >>>"
        while True:
            s: str = input(strInputData)
            self.__logger.write("Пользователь ввел: '" + s + "'")
            s = s.strip()
            if s is None or len(s) == 0:
                self.__printToConsoleAndLog("!!! Ошибка. Получена пустая строка.")
                continue
            if self.__isExit(s):
                m: str = "Получен символ для выхода из программы."
                self.__logger.write(m)
                raise ExceptionExit(m)
            return s

    def requestMenu(self, description: str, symbols: tuple) -> str:  # throws ExceptionExit
        self.__printToConsoleAndLog(description)
        while True:
            s: str = input(" Введите данные >>>")
            self.__logger.write("Пользователь ввел: " + s)
            s = s.strip()
            if s is None or len(s) == 0:
                self.__printToConsoleAndLog("!!! Ошибка. Получена пустая строка.")
                continue
            if self.__isExit(s):
                m: str = "Получен символ для выхода из программы."
                self.__logger.write(m)
                raise ExceptionExit(m)
            if symbols is not None:
                for symbol in symbols:
                    if s == symbol:
                        return s
                self.__printToConsoleAndLog("!!! Ошибка. Требуется ввести один из пунктов меню.")
                continue
            return s

    def viewText(self, text: str) -> None:
        self.__printToConsoleAndLog(text)

    def __isExit(self, ch: str) -> bool:
        if ch is not None and len(ch) == 1:
            for c in self.__exitLetters:
                if c == ch:
                    return True
        return False

    def clearScreen(self) -> None:
        print("\033[H\033[J")
        self.__logger.write("Очистка экрана.")

    def __printToConsoleAndLog(self, text: str) -> None:
        self.__logger.write(text)
        print(text)
