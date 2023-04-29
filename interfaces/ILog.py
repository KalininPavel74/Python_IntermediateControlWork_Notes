class ILog:
    UTF_8: str = 'utf-8'
    FILE_NAME: str = 'log.txt'

    def open(self, fileName: str = FILE_NAME, charset: str = UTF_8) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод open()")

    def write(self, text: str, className: str = '', methodName: str = '') -> None:
        raise NotImplementedError("Не реализован интерфейсный метод write()")

    def close(self) -> None:
        raise NotImplementedError("Не реализован интерфейсный метод close()")
