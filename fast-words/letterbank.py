class LetterBank():
    """Class containing word bank functionality"""

    def __init__(self, bank : list[str]):
        """Initializes instance variables

        Args:
            bank (list[str]): List of characters available to player to form words with
        
        Attributes:
            bank (list[str]): List of characters available to player to form words with
        """

        self.bank : list[str] = []
        self.setBank(bank)

    def setBank(self, bank : list[str]) -> None:
        """Sets word bank to a given list of characters

        Args:
            bank (list[str]): Given character list
        """

        self.bank = bank

    def removeCharacters(self, removeList : list[str]) -> None:
        """Removes characters in given list from word bank

        Args:
            removeList (list[str]): List containing characters to remove
        """

        # List comprehension would remove duplicates which is not desired; uses individual iteration instead
        for character in removeList:
            try:
                self.bank.remove(character)
            except:
                print("Trying to remove character not in bank.")

    def addCharacters(self, addList : list[str]) -> None:
        """Adds characters from given list to word bank

        Args:
            addList (list[str]): List containing characters to add
        """

        self.bank.extend(addList)

    def getBank(self) -> list[str]:
        """Returns word bank list instance variable

        Returns:
            list[str]: Word bank list
        """

        return self.bank
