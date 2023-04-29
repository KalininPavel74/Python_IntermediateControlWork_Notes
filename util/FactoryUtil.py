from interfaces.IFactoryUtil import IFactoryUtil
from interfaces.ICSV import ICSV
from util.CSV import CSV
from interfaces.ILog import ILog
from util.Log import Log


class FactoryUtil(IFactoryUtil):

    def createLog(self, fileName: str = ILog.FILE_NAME, charset: str = ILog.UTF_8) -> ILog:
        return Log(fileName, charset)

    def createCSV(self, logger: ILog) -> ICSV:
        return CSV(logger)
