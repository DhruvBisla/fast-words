import time
import numpy as np

from . import utils
from . import letterpool

class Game():
    def __init__(self):
        self.length : np.float64
        self.m_letterPool = letterpool.LetterPool()
        self.score : int = 0

    def chooseLength(self):
        try:
            self.length = float(input("Please enter the desired game time in minutes: "))
        except ValueError:
            print("Please enter a number only.")
            self.chooseLength()
        except KeyboardInterrupt:
            exit()

    def runCycle(self) -> list[str]:
        print(utils.Utils.Text.formatListToString(self.m_letterPool.bank.getBank()), "\t\t\t", f"Score: {self.score}")
        entered : str
        while True:
            entered = input("").lower()
            if (self.checkInput(entered)):
                break
            else:
                print(f"{entered.title()} is not a word. Try something else.")
        self.score += len(entered)
        return [char for char in entered]

    def checkInput(self, entered : list[str]) -> bool:
        return (utils.Utils.Text.isEnglishWord("".join(entered)) and all(character in self.m_letterPool.bank.getBank() for character in entered))

    def prepNext(self, word : list[str]):
        self.m_letterPool.bank.removeCharacters(word)
        self.m_letterPool.bank.addCharacters(self.m_letterPool.getRandom(len(word)))

    def play(self):
        print("Welcome to fast-words!")
        self.chooseLength()
        print(f"Press any key to begin a game of {self.length} minute(s)")
        utils.Utils.Keyboard.blockTillAnyKey()
        timeout : float = time.time() + (60*self.length)
        while time.time() < timeout:
            self.prepNext(self.runCycle())
        print(f"{self.length} minute(s) over. You scored {self.score} points!")
