class IView:

    INPUT_DATETIME_FORMAT: str = '%d.%m.%Y %H:%M'
    OUTPUT_DATETIME_FORMAT: str = '%d.%m.%Y %H:%M'
    OUTPUT_DATETIME_FORMAT_FULL: str = '%Y.%m.%d %H:%M:%S.%f'

    def viewText(self, text: str) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод create()")

    def request(self, description: str) -> str:  # throws ExceptionExit
        raise NotImplementedError("Не реализован интерфейсный метод create()")

    def requestMenu(self, description: str, symbols: tuple) -> str:  # throws ExceptionExit
        raise NotImplementedError("Не реализован интерфейсный метод create()")

    def clearScreen(self) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод clearScreen()")
