class LetterBank():

    def __init__(self, bank):
        self.bank : list[str] = []
        self.initBank(bank)

    def initBank(self, bank : list[str]) -> None:
        self.bank = bank

    def removeCharacters(self, removeList : list[str]) -> None:
        # Using loop to individually iterate over removeList because do not want to remove duplicates, as list comprehension would
        for character in removeList:
            try:
                self.bank.remove(character)
            except:
                print("Trying to remove character not in bank.")

    def addCharacters(self, addList : list[str]) -> None:
        self.bank.extend(addList)

    def getBank(self) -> list[str]:
        return self.bank
