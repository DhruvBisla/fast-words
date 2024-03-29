import time
import numpy as np

from . import utils
from . import letterpool

class Game():
    """Main class that captures high level functionality of the game"""

    def __init__(self):
        """Initializes instance variables

        Attributes:
            length (np.float64): Length of game in minutes
            m_letterPool (letterpool.LetterPool): Letter pool instance
            score (int): Game score
        """

        self.length : np.float64
        self.m_letterPool : letterpool.LetterPool = letterpool.LetterPool()
        self.score : int = 0

    def chooseLength(self) -> None:
        """Performs action to ask user for desired game length in minutes"""

        try:
            self.length = float(input("Please enter the desired game time in minutes: "))
        except ValueError:
            print("Please enter a number only.")
            self.chooseLength()
        except KeyboardInterrupt:
            exit()

    def runCycle(self) -> list[str]:
        """Runs the primary cycle of the game involving prompting the player to form a word and appropriately adding to score

        Returns:
            list[str]: Validated word formed by the player as a list of characters
        """

        print(utils.Utils.Text.formatListToString(self.m_letterPool.bank.getBank()), "\t\t\t", f"Score: {self.score}")
        entered : str
        while True:
            try:
                entered = input("").lower()
            except KeyboardInterrupt:
                exit()
            if (self.checkInput(entered)):
                break
            else:
                print(f"{entered.title()} is not a word or includes a letter not in the word bank. Try something else.")
        self.score += len(entered)
        return [char for char in entered]

    def checkInput(self, word : list[str]) -> bool:
        """Performs a check on word validity and that the used characters were all from the word bank

        Args:
            word (list[str]): Word formed by player

        Returns:
            bool: Whether given list of characters is an English word and uses only the characters in the word bank
        """

        # Idiomatic one-liner below, but it does not satisfy all 3c. and 3d. requirements
        # return (utils.Utils.Text.isEnglishWord("".join(word)) and all(character in self.m_letterPool.bank.getBank() for character in word))
        allInBank : bool = True
        if (word == self.m_letterPool.bank.getBank()):
            pass
        else:
            for character in word:
                if (not(self.m_letterPool.bank.getBank().count(character))):
                    allInBank = False
                    break
        if (allInBank):
            if (utils.Utils.Text.isEnglishWord("".join(word))):
                return True
            else:
                return False
        else:
            return False

    def prepNext(self, word : list[str]) -> None:
        """Removes used characters and replaces with random from letter pool

        Args:
            word (list[str]): English word formed by player
        """

        # Emulate do-while loop behavior of loop as none exists in Python
        self.m_letterPool.bank.removeCharacters(word)
        self.m_letterPool.bank.addCharacters(self.m_letterPool.getRandom(len(word)))
        # Ensure free 8 points not given to player by providing word bank that already forms 8 letter word
        while (self.checkInput(self.m_letterPool.bank.getBank())):
            self.m_letterPool.bank.removeCharacters(self.m_letterPool.bank.getBank())
            self.m_letterPool.bank.addCharacters(self.m_letterPool.getRandom(len(word)))

    def play(self) -> None:
        """Puts together the main components of the game"""

        print("Welcome to fast-words!")
        self.chooseLength()
        print(f"Press any key to begin a game of {self.length} minute(s)")
        utils.Utils.Keyboard.blockTillAnyKey()
        timeout : float = time.time() + (60*self.length)
        while time.time() < timeout:
            self.prepNext(self.runCycle())
        print(f"{self.length} minute(s) over. You scored {self.score} points!")
