from control.FactoryControlMenu import FactoryControlMenu

from model.FactoryNotes import FactoryNotes
from model.FactoryNote import FactoryNote

from view.FactoryView import FactoryView

from util.FactoryUtil import FactoryUtil

from interfaces.ILog import ILog
from interfaces.IFactoryUtil import IFactoryUtil
from interfaces.ICSV import ICSV
from interfaces.INotes import INotes
from interfaces.IFactoryNotes import IFactoryNotes
from interfaces.IFactoryNote import IFactoryNote
from interfaces.IView import IView
from interfaces.IFactoryView import IFactoryView
from interfaces.IFactoryControl import IFactoryControl
from interfaces.IControl import IControl
import traceback


class Main:
    __DB_FILE: str = "notes.csv"  # Файл с базой данных.
    __DB_CHARSET: str = "UTF-8"  # Кодировка файла с базой данных.

    @staticmethod
    def main() -> None:  # throws ExceptionProg {

        # Фабрика для объектов утилит. Для доступа к классу для работы с файлами csv, лог
        fUtil: IFactoryUtil = FactoryUtil()
        logger: ILog = fUtil.createLog(ILog.FILE_NAME, ILog.UTF_8)  # логирование
        try:
            csv: ICSV = fUtil.createCSV(logger)
            ss: list = csv.readFileCSV(Main.__DB_FILE, Main.__DB_CHARSET)  # String[][]

            # Фабрика для получения объекта Заметки - модель (MCV)
            fNotes: IFactoryNotes = FactoryNotes()
            notes: INotes = fNotes.create(ss, logger)
            # Фабрика для получения объекта Заметка
            # отделена, для того чтобы передать ее в контроллер (MCV)
            # Контроллер будет создавать Записи через фабрику.
            fNote: IFactoryNote = FactoryNote(notes.getGenerator())

            # Фабрика для получения объекта визуализации (MCV)
            fv: IFactoryView = FactoryView()
            # Выход из программы по кнопке q или из меню контроллера.
            view: IView = fv.create("", ILog.UTF_8, ('Q', 'q'), logger)

            # Фабрика для получения объекта контроллер (MCV)
            fc: IFactoryControl = FactoryControlMenu()
            control: IControl = fc.create(view, notes, fNote, csv, Main.__DB_FILE, Main.__DB_CHARSET, logger)

            control.run()  # запуск цикла работы

        except Exception as e:
            logger.write(str(e))
            logger.write(str(traceback.format_exc()))
            raise Exception(e)
        finally:
            logger.close()  # закрыть лог файл


Main.main()
