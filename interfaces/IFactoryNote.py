from interfaces.INote import INote


class IFactoryNote:
    def create(self, head: str, body: str) -> INote:
        raise NotImplementedError("Не реализован интерфейсный метод create()")
