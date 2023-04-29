from interfaces.ILog import ILog
from interfaces.ICSV import ICSV
from interfaces.INotes import INotes
from interfaces.IControl import IControl
from interfaces.INote import INote
from interfaces.IView import IView
from interfaces.IFactoryNote import IFactoryNote

from view.ExceptionExit import ExceptionExit
from util.Util import Util

from datetime import datetime


class ControlMenu(IControl):
    __messageStart: str = "\nПрограмма \"Заметки\"."
    __messageFinal: str = "Работа программы завершена."
    __CREATE: str = "1"
    __EDIT: str = "2"
    __SEARCH: str = "3"
    __VIEW: str = "4"
    __DELETE: str = "5"
    __SAVE: str = "6"
    __SHOW_ALL: str = "7"
    __SEARCH_BY_ID: str = "8"
    __SEARCH_BY_DATE: str = "9"
    __EXIT: str = "0"

    __MENU_SYMBOLS: tuple = (__CREATE, __EDIT, __SEARCH, __VIEW, __DELETE, __SAVE, __SHOW_ALL, __EXIT)
    __MENU: str = """
Меню:
1 - создать
2 - редактировать
3 - поиск
4 - детали
5 - удалить
6 - сохранить все изменения
7 - все заметки
0 - выход из программы
"""

    __SUBMENU_SYMBOLS: tuple = (__SEARCH_BY_ID, __SEARCH_BY_DATE, __EXIT)
    __SUBMENU: str = """
Меню:
8 - поиск по номеру
9 - поиск по дате
0 - вернуться в главное меню
"""
    __QTY_ROW_FOR_FAST_VIEW: int = 10

    def __init__(self, view: IView, notes: INotes, fNote: IFactoryNote,
                 csv: ICSV, dbFile: str, charset: str, logger: ILog) -> None:
        self.__view = view  # визуализатор (MCV)
        self.__notes = notes  # модель  (MCV)
        self.__fNote = fNote  # фабрика для создания заметки
        self.__csv = csv  # для работы с файлами csv
        self.__dbFile = dbFile  # имя файла с базой данных
        self.__charset = charset  # кодировка файла с базой данных
        self.__logger = logger  # кодировка файла с базой данных

    def run(self) -> None:  # throws ExceptionProg
        result: str = ""
        try:
            while True:
                # рисую меню, потом раздел с ответной информацией
                self.__view.clearScreen()
                self.__view.viewText(self.__messageStart)
                s: str = self.__MENU + "------------------------------\n" + result + "\n------------------------------"
                symbol: str = self.__view.requestMenu(s, self.__MENU_SYMBOLS)
                result = ""
                match symbol:
                    case self.__CREATE:  # создать запись
                        head: str = self.__view.request("Заголовок записи.")
                        body: str = self.__view.request("Текст записи.")
                        note: INote = self.__fNote.create(head, body)
                        self.__notes.add(note)
                        result = "Добавлена запись: " + note.toString()

                    case self.__EDIT:  # редактировать текст записи, если запись помечена к удалению - восстановится
                        idS: str = self.__view.request("Идентификатор записи.")
                        try:
                            idn = int(idS)
                        except ValueError as e:
                            result = "Ошибка. Требуется ввести число."
                            self.__logger.write(f"Вместо числа пользователь ввел '{e}'")
                            continue

                        note: INote = self.__notes.searchByIdn(idn)
                        if note is None:
                            result = f"Ошибка. Запись № {idn} не найдена."
                            self.__logger.write(result)
                            continue

                        body: str = self.__view.request("Текст записи.")
                        note.setBody(body)
                        result = "Запись отредактирована: " + note.toString()

                    case self.__SEARCH:  # отдельное меню для поисковых функций
                        self.runSubMenu()

                    case self.__VIEW:  # вывести полные данные по одной записи, которую нужно указать по номеру
                        idS: str = self.__view.request("Идентификатор записи.")
                        try:
                            idn: int = int(idS)
                        except ValueError as e:
                            result = "Ошибка. Требуется ввести число."
                            self.__logger.write(f"Вместо числа пользователь ввел '{e}'")
                            continue

                        note: INote = self.__notes.searchByIdn(idn)
                        if note is None:
                            result = f"Ошибка. Запись № {idn} не найдена."
                            self.__logger.write(result)
                            continue

                        result = note.view()

                    case self.__DELETE:  # пометить запись на удаление, при сохранении она не добавится в файл,
                        # но будет доступна для возвращения в рабочую, до перезапуска программы.
                        idS: str = self.__view.request("Идентификатор записи.")
                        try:
                            idn = int(idS)
                        except ValueError as e:
                            result = "Ошибка. Требуется ввести число."
                            self.__logger.write(f"Вместо числа пользователь ввел '{e}'")
                            continue

                        note: INote = self.__notes.searchByIdn(idn)
                        if note is None:
                            result = f"Ошибка. Запись № {idn} не найдена."
                            self.__logger.write(result)
                            continue

                        note.setDelete()
                        result = "Запись удалена. " + note.toString()

                    case self.__SAVE:  # сохранить записи в файл, кроме помеченных на удаление
                        qty: int = self.__csv.writeFileCSV(self.__notes.getArrayNotes(), self.__dbFile, self.__charset)
                        self.__notes.setSaveDate(datetime.now().timestamp())
                        if qty:
                            lst: list = list()
                            lst.append(qty)
                            lst.append(" Заметок сохранено в файл ")
                            lst.append(self.__dbFile)
                            lst.append("\n\nПоследние заметки:\n")
                            lst.append(self.__notes.getLastNotes(ControlMenu.__QTY_ROW_FOR_FAST_VIEW))
                            result = ''.join(Util.listToListOfStr(lst))
                        else:
                            result = 'Нет данных для сохранения.'

                    case self.__SHOW_ALL:  # вывести полную информацию по всем записям
                        tpl: tuple = self.__notes.getListNotes()  # List<INote>
                        sb: list = list()
                        for note in tpl:
                            sb.append(note.toString())
                            #sb.append("\n")
                        if len(sb):
                            result = ''.join(Util.listToListOfStr(sb))
                        else:
                            result = 'Нет данных для отображения'

                    case self.__EXIT:  # выход из программы
                        self.__view.viewText(self.__messageFinal)
                        return

                    case _:
                        self.__view.viewText("Не обработанный пункт меню " + symbol)
        except ExceptionExit:
            self.__view.viewText(self.__messageFinal)
            return

    # подменю, устроено по аналогии с основным
    def runSubMenu(self) -> None:  # throws ExceptionProg, ExceptionExit
        result: str = ""
        try:
            while True:
                self.__view.clearScreen()
                self.__view.viewText(self.__messageStart)
                s: str = self.__SUBMENU + "---------------------\n" + result + "\n----------------------"
                symbol: str = self.__view.requestMenu(s, self.__SUBMENU_SYMBOLS)
                result = ""
                match symbol:
                    case self.__SEARCH_BY_ID:  # поиск записи по номеру
                        # и вывод полной информации по указанной записи
                        idS: str = self.__view.request("Идентификатор записи.")
                        try:
                            idn = int(idS)
                        except ValueError as e:
                            result = "Ошибка. Требуется ввести число."
                            self.__logger.write(f"Вместо числа пользователь ввел '{e}'")
                            continue

                        note: INote = self.__notes.searchByIdn(idn)
                        if note is None:
                            result = "Ошибка. Запись не найдена."
                            continue

                        result = note.view()

                    case self.__SEARCH_BY_DATE:  # вывод полной информации по всем записям
                        # созданным в указанном диапазоне дат

                        beginDate: float = -1
                        i: int = 3  # чтобы не мучить пользователя - дается несколько попыток,
                        # чтобы указать дату в правильном формате
                        while i >= 0:
                            beginDateS: str = self.__view.request(
                                "Диапазон дат создания. Дата НАЧАЛА в формате 01.02.2023 01:59")
                            try:
                                beginDate = datetime.strptime(beginDateS, IView.INPUT_DATETIME_FORMAT).timestamp()
                                break
                            except ValueError as e:
                                self.__logger.write(
                                    f'Введенная пользователем дата не распозналась {beginDateS} {e}')
                                self.__view.viewText("Ошибка. Неправильный формат даты.")

                            i -= 1

                        if beginDate < 0:
                            result = "Ошибка. Неправильный формат даты."
                            continue

                        endDate: float = -1
                        i = 3  # чтобы не мучить пользователя - дается несколько попыток,
                        # чтобы указать дату в правильном формате
                        while i >= 0:
                            endDateS: str = self.__view.request(
                                "Диапазон дат создания. Дата ОКОНЧАНИЯ в формате 01.02.2023 01:59")
                            try:
                                endDate = datetime.strptime(endDateS, IView.INPUT_DATETIME_FORMAT).timestamp()
                                break
                            except ValueError as e:
                                self.__logger.write(
                                    f'Введенная пользователем дата не распозналась {endDateS} {e}')
                                self.__view.viewText("Ошибка. Неправильный формат даты.")
                            i -= 1

                        if endDate < 0:
                            result = "Ошибка. Неправильный формат даты."
                            continue

                        title: list = list()
                        title.append('Записи из диапазона дат: с ')
                        title.append(datetime.fromtimestamp(beginDate).strftime(IView.INPUT_DATETIME_FORMAT))
                        title.append(' по ')
                        title.append(datetime.fromtimestamp(endDate).strftime(IView.INPUT_DATETIME_FORMAT))
                        info: str = self.__notes.searchByDateToStr(beginDate, endDate)
                        if info is None or len(info.strip()) == 0:
                            title.append('\n')
                            title.append("В выбранном диапазоне записей нет")
                            result = ''.join(Util.listToListOfStr(title))
                            continue
                        title.append('\n\n')
                        title.append(info)
                        result = ''.join(Util.listToListOfStr(title))

                    case self.__EXIT:  # выход из подменю в основное меню
                        return

                    case _:
                        self.__view.viewText("Не обработанный пункт меню " + symbol)

        except ExceptionExit as e:
            raise ExceptionExit(str(e))
