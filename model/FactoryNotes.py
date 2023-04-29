from interfaces.IFactoryNotes import IFactoryNotes
from interfaces.INotes import INotes
from interfaces.ILog import ILog
from model.Notes import Notes


class FactoryNotes(IFactoryNotes):

    def create(self, ss: tuple, logger: ILog) -> INotes:  # String[][] throws ExceptionProg
        return Notes(ss, logger)
