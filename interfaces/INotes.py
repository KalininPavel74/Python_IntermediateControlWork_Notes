from interfaces.IGenerator import IGenerator
from interfaces.INote import INote


class INotes:

    def getGenerator(self) -> IGenerator:
        raise NotImplementedError("Не реализован интерфейсный метод getGenerator()")

    def getListNotes(self) -> tuple:  # List<INote>
        raise NotImplementedError("Не реализован интерфейсный метод getListNotes()")

    def add(self, note: INote) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод note()")

    def update(self, idn: str, body: str) -> bool:
        raise NotImplementedError("Не реализован интерфейсный метод update()")

    def searchByIdn(self, idn: int) -> INote:
        raise NotImplementedError("Не реализован интерфейсный метод searchByIdn()")

    def searchByIdnToStr(self, idn: int) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод searchByIdnToStr()")

    def searchByDate(self, beginDate: float, endDate: float) -> tuple:  # List<INote>
        raise NotImplementedError("Не реализован интерфейсный метод searchByDate()")

    def searchByDateToStr(self, beginDate: float, endDate: float) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод searchDateToStr()")

    def view(self, idn: int) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод view()")

    def delete(self, idn: int) -> bool:
        raise NotImplementedError("Не реализован интерфейсный метод delete()")

    def getLastNotes(self, n: int) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод getLastNotes()")

    def getArrayNotes(self) -> tuple:  # String[][]
        raise NotImplementedError("Не реализован интерфейсный метод getArrayNotes()")

    def setSaveDate(self, saveDate: float) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод setSaveDate()")

    def isSaveDate(self) -> bool:
        raise NotImplementedError("Не реализован интерфейсный метод isSaveDate()")
