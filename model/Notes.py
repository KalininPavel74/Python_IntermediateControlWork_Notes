from interfaces.IGenerator import IGenerator
from interfaces.INote import INote
from interfaces.INotes import INotes
from interfaces.ILog import ILog
from interfaces.IView import IView

from util.ExceptionProg import ExceptionProg
from util.Util import Util
from model.Generator import Generator
from model.FactoryNote import FactoryNote
from datetime import datetime


class Notes(INotes):

    def __init__(self, ss: tuple, logger: ILog) -> None:  # String[][]  throws ExceptionProg
        self.__saveDate: float = 0
        self.__notes: list = list()  # new ArrayList<INote>()
        self.__logger: ILog = logger
        if ss is None or len(ss) == 0:
            self.__generator: IGenerator = Generator(0)
        else:
            set1: set = set()
            maxIdn: int = 0
            for arS in ss:
                try:
                    idn: int = int(arS[0])
                    if idn > maxIdn:
                        maxIdn = idn
                    set1.add(idn)
                    self.__notes.append(FactoryNote.createStatic(idn, arS[1], arS[2], float(arS[3]), float(arS[4])))
                except ValueError as e:
                    raise ExceptionProg(f'Ошибка в номере записи или датах {e}')

            if len(set1) != len(ss):
                raise ExceptionProg(f'В записях присутствуют дубли по номеру. {len(set1)} <> {len(ss)}')
            self.__generator: IGenerator = Generator(maxIdn)

    def getGenerator(self) -> IGenerator:
        return self.__generator

    def getListNotes(self) -> tuple:  # List<INote>
        return tuple(self.__notes)

    def add(self, note: INote) -> None:
        self.__notes.append(note)

    def update(self, idn: int, body: str) -> bool:
        note: INote = self.searchByIdn(idn)
        if note is not None:
            note.setBody(body)
            return True
        return False

    def searchByDate(self, beginDate: float, endDate: float) -> tuple:  # List<INote>
        al: list = list()
        for note in self.__notes:
            if note.getDelete() <= 0.001 or note.getDelete() > self.__saveDate:
                create: float = note.getCreate()
                if beginDate <= create <= endDate:
                    al.append(note)
        return tuple(al)

    def searchByDateToStr(self, beginDate: float, endDate: float) -> str:
        tpl: tuple = self.searchByDate(beginDate, endDate)
        sb: list = list()
        for note in tpl:
            if not note.isDelete() or note.getDelete() > self.__saveDate:
                sb.append(note.view())
                sb.append("\n")
        return ''.join(Util.listToListOfStr(sb))

    def searchByIdn(self, idn: int) -> INote:
        for note in self.__notes:
            if note.getIdn() == idn:
                return note
        return None

    def searchByIdnToStr(self, idn: int) -> str:
        note: INote = self.searchByIdn(idn)
        if note:
            return note.view()
        return "Запись не найдена."

    def view(self, idn: int) -> str:
        note: INote = self.searchByIdn(idn)
        if note:
            return note.view()
        return "Запись не найдена."

    def delete(self, idn: int) -> bool:
        note: INote = self.searchByIdn(idn)
        if note:
            note.setDelete()
            return True
        return False

    def getLastNotes(self, n: int) -> str:
        sb: list = list()
        i: int = len(self.__notes) - 1
        count: int = n
        while i >= 0 and count > 0:
            if self.__notes[i].getDelete() <= 0.001 or self.__notes[i].getDelete() > self.__saveDate:
                sb.append(self.__notes[i].toString())
                count -= 1
            i -= 1
        return ''.join(Util.listToListOfStr(sb))

    def getArrayNotes(self) -> tuple:  # String[][]
        qty: int = 0
        for note in self.__notes:
            if not note.isDelete():
                qty += 1
        if not qty:
            return tuple()

        ss: list = list()
        i: int = 0
        for note in self.__notes:
            if not note.isDelete():
                lst: list = list()
                lst.append(str(note.getIdn()))
                lst.append(note.getHead())
                lst.append(note.getBody())
                lst.append(str(note.getCreate()))
                lst.append(str(note.getUpdate()))
                ss.append(lst)
                i += 1
        return tuple(ss)

    def setSaveDate(self, saveDate: float) -> None:
        self.__saveDate = saveDate
        self.__logger.write(
            f'время сохранения {datetime.fromtimestamp(self.__saveDate).strftime(IView.OUTPUT_DATETIME_FORMAT)}')

    def isSaveDate(self) -> bool:
        return self.__saveDate >= 0.001
