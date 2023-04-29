from interfaces.IFactoryNote import IFactoryNote
from interfaces.IGenerator import IGenerator
from interfaces.INote import INote
from model.Note import Note


class FactoryNote(IFactoryNote):

    def __init__(self, generator: IGenerator) -> None:
        self.__generator: IGenerator = generator

    def create(self, head: str, body: str) -> INote:
        return Note(self.__generator.getNewIdn(), head, body)

    @staticmethod
    def createStatic(idn: int, head: str, body: str, create: float, update: float) -> INote:
        return Note(idn, head, body, create, update)
