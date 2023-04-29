from interfaces.IFactoryView import IFactoryView
from interfaces.IView import IView
from interfaces.ILog import ILog
from view.ViewConsole import ViewConsole


class FactoryView(IFactoryView):

    def create(self, title: str, charset: str, exitLetters: tuple, logger: ILog) -> IView:
        return ViewConsole(title, charset, exitLetters, logger)
