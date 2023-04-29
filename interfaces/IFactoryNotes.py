from interfaces.INotes import INotes
from interfaces.ILog import ILog


class IFactoryNotes:
    def create(self, ss: list, logger: ILog) -> INotes:  # String[][] ss   throws ExceptionProg
        raise NotImplementedError("Не реализован интерфейсный метод create()")
