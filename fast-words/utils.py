'''
Py-Getch Package
Source: https://github.com/joeyespo/py-getch
Credit: Contributors of py-getch, https://github.com/joeyespo/py-getch/graphs/contributors
'''
from getch import getch
'''
Natural Language Toolkit Package
Source: https://github.com/nltk/nltk
Credit: Contributors of NLTK, https://github.com/nltk/nltk/graphs/contributors
'''
from nltk import download
from nltk.corpus import words

class Utils():
    """Class containing utility methods"""

    class Keyboard():
        """Class containing keyboard specific methods"""

        @staticmethod
        def blockTillAnyKey() -> str:
            """Blocks main thread till any key is pressed

            Returns:
                str: Key code for character pressed
            """

            return getch()

    class Text():
        """Class containing text specific methods"""

        @staticmethod
        def formatListToString(rawList : list[str]) -> str:
            """Prettifies list in string form

            Args:
                rawList (list[str]): Given list

            Returns:
                str: Formatted string
            """

            return " ".join(rawList)

        @staticmethod
        def isEnglishWord(word : str) -> bool:
            """Checks whether given string is an English word

            Args:
                word (str): Given string

            Returns:
                bool: Whether string is a word
            """

            try:
                wordSet = set(words.words())
            except LookupError:
                download("words")
            return ((word in wordSet) and (len(word) > 1))
