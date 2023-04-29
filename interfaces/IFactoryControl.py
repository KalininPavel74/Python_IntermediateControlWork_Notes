from interfaces.ILog import ILog
from interfaces.ICSV import ICSV
from interfaces.IView import IView
from interfaces.INotes import INotes
from interfaces.IControl import IControl
from interfaces.IFactoryNote import IFactoryNote


class IFactoryControl:
    def create(self, view: IView, notes: INotes, fNote: IFactoryNote,
               csv: ICSV, dbFile: str, charset: str, logger: ILog) -> IControl:
        raise NotImplementedError("Не реализован интерфейсный метод create()")
