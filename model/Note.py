from interfaces.INote import INote
from interfaces.IView import IView
from util.Util import Util
from datetime import datetime


class Note(INote):

    def __init__(self, idn: int, head: str, body: str, create: float = 0,
                 update: float = 0) -> None:
        self.__idn: int = idn
        self.__head: str = head
        self.__body: str = body
        self.__create: float = create if create > 0.001 else datetime.now().timestamp()
        self.__update: float = update
        self.__delete: float = 0.0

    def getIdn(self) -> int:
        return self.__idn

    def getHead(self) -> str:
        return self.__head

    def getBody(self) -> str:
        return self.__body

    def setBody(self, text: str) -> None:
        self.__body = text
        self.__update = datetime.now().timestamp()
        self.__delete = 0.0

    def getCreate(self) -> float:
        return self.__create

    def getUpdate(self) -> float:
        return self.__update

    def getDelete(self) -> float:
        return self.__delete

    def setDelete(self) -> None:
        self.__delete = datetime.now().timestamp()

    def isDelete(self) -> bool:
        return self.__delete >= 0.001

    def view(self) -> str:
        sb: list = list()
        sb.append("Запись: ")
        sb.append("Идентификатор: ")
        sb.append(self.__idn)
        sb.append("\n")
        sb.append("Заголовок: ")
        sb.append(self.__head)
        sb.append("\n")
        sb.append("Текст: ")
        sb.append(self.__body)
        sb.append("\n")
        sb.append("Дата создания: ")
        sb.append(datetime.fromtimestamp(self.__create).strftime(IView.OUTPUT_DATETIME_FORMAT_FULL))
        sb.append("\n")
        sb.append("Дата изменения: ")
        if self.__update:
            sb.append(datetime.fromtimestamp(self.__update).strftime(IView.OUTPUT_DATETIME_FORMAT_FULL))
        else:
            sb.append("не изменялась")
        sb.append("\n")
        sb.append("Дата удаления: ")
        if self.__delete:
            sb.append(datetime.fromtimestamp(self.__delete).strftime(IView.OUTPUT_DATETIME_FORMAT_FULL))
        else:
            sb.append("не удалена")
        sb.append("\n")
        return ''.join(Util.listToListOfStr(sb))

    def toString(self) -> str:
        sb: list = list()
        sb.append("№ ")
        sb.append(self.__idn)
        sb.append("; ")
        sb.append(self.__head)
        sb.append("; ")
        if len(self.__body) > 20:
            sb.append(self.__body[:20])
            sb.append(" ...; ")
        else:
            sb.append(self.__body)
            sb.append("; ")
        sb.append(datetime.fromtimestamp(self.__create).strftime(IView.OUTPUT_DATETIME_FORMAT))
        if self.__update:
            sb.append("; ")
            sb.append(datetime.fromtimestamp(self.__update).strftime(IView.OUTPUT_DATETIME_FORMAT))
        if self.__delete:
            sb.append("; Удалена.")
        sb.append("\n")
        return ''.join(Util.listToListOfStr(sb))
