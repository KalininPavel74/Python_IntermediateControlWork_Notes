from interfaces.ICSV import ICSV
from interfaces.ILog import ILog


class IFactoryUtil:

    def createLog(self, fileName: str = ILog.FILE_NAME, charset: str = ILog.UTF_8) -> ILog:
        raise NotImplementedError("Не реализован интерфейсный метод createLog()")

    def createCSV(self, logger: ILog) -> ICSV:
        raise NotImplementedError("Не реализован интерфейсный метод createCSV()")
