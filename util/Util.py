class Util:

    @staticmethod
    def listToListOfStr(lst: list) -> list:
        for i, elem in enumerate(lst):
            lst[i] = str(lst[i])
        return lst
