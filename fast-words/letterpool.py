from random import choice
from . import letterbank

class LetterPool():
    
    def __init__(self):
        # Scrabble letter distribution
        self.pool = ['a','a','a','a','a','a','a','a','a','b','b','c','c','d','d','d','d','e','e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','g','h','h','i','i','i','i','i','i','i','i','i','j','k','l','l','l','l','m','m','n','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r','r','r','r','r','r','s','s','s','s','t','t','t','t','t','t','u','u','u','u','v','v','w','w','x','y','y','z']
        self.bank = letterbank.LetterBank(self.getRandom(8))

    def getRandom(self, quantity) -> list[str]:
        randomSelection : list[str] = []
        randomChoice : str
        for i in range(quantity):
            randomChoice = choice(self.pool)
            randomSelection.append(randomChoice)
        return randomSelection
