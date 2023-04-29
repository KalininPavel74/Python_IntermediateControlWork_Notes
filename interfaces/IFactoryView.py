from interfaces.IView import IView
from interfaces.ILog import ILog


class IFactoryView:
    def create(self, title: str, charset: str, exitLetters: tuple, logger: ILog) -> IView:
        raise NotImplementedError("Не реализован интерфейсный метод create()")
