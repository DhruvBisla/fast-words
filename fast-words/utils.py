from getch import getch
from nltk.corpus import words
from nltk import download

class Utils():
    class Keyboard():
        @staticmethod
        def blockTillAnyKey() -> str:
            return getch()
        @staticmethod
        def blockTillYesNo() -> bool:
            input : str = getch()
            return (input == "y") or False
    class Text():
        @staticmethod
        def formatListToString(rawList : list[str]) -> str:
            return " ".join(rawList)
        @staticmethod
        def isEnglishWord(word : str) -> bool:
            try:
                wordSet = set(words.words())
            except LookupError:
                download("words")
            return (word in wordSet)
