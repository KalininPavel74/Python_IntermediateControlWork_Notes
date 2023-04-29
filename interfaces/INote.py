class INote:
    def getIdn(self) -> int:
        raise NotImplementedError("Не реализован интерфейсный метод getIdn()")

    def getHead(self) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод getHead()")

    def getBody(self) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод getBody()")

    def setBody(self, text: str) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод setBody()")

    def getCreate(self) -> float:
        raise NotImplementedError("Не реализован интерфейсный метод getCreate()")

    def getUpdate(self) -> float:
        raise NotImplementedError("Не реализован интерфейсный метод getUpdate()")

    def getDelete(self) -> float:
        raise NotImplementedError("Не реализован интерфейсный метод getDelete()")

    def setDelete(self) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод setDelete()")

    def isDelete(self) -> bool:
        raise NotImplementedError("Не реализован интерфейсный метод isDelete()")

    def view(self) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод view()")

    def toString(self) -> str:
        raise NotImplementedError("Не реализован интерфейсный метод toString()")
