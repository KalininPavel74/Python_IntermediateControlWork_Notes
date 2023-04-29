from interfaces.ILog import ILog
from interfaces.ICSV import ICSV
from interfaces.IView import IView
from interfaces.INotes import INotes
from interfaces.IControl import IControl
from interfaces.IFactoryNote import IFactoryNote
from interfaces.IFactoryControl import IFactoryControl

from control.ControlMenu import ControlMenu


class FactoryControlMenu(IFactoryControl):
    def create(self, view: IView, notes: INotes, fNote: IFactoryNote,
               csv: ICSV, dbFile: str, charset: str, logger: ILog) -> IControl:
        return ControlMenu(view, notes, fNote, csv, dbFile, charset, logger)
