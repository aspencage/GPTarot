# tarot_deck.py 

import itertools
import random
from enum import Enum
from copy import deepcopy

lower_first = lambda s : s[0].lower() + s[1:]
upper_first = lambda s : s[0].upper() + s[1:]

class Arcana(Enum):

    MAJOR = "major"
    MINOR = "minor"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class Card:

    namify = lambda rank,suit: f"The {rank} of {suit}"

    def __init__(self,rank=None,suit=None,name=None):
        
        if name is not None:
            self.name = name
            self.arcana = Arcana.MAJOR
        else:
            self.rank = str(rank)
            self.suit = suit
            self.arcana = Arcana.MINOR
            self.name = Card.namify(rank,suit)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Deck:

    major_strings = [
        "The Fool","The Magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","Strength","The Hermit","The Wheel of Fortune","Justice","The Hanged Man","Death","Temperance","The Devil","The Tower","The Star","The Moon","The Sun","Judgement","The World"
    ]
    
    rank_map = {
        "2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten"
        }


    def __init__(self,n_drawn=None,major_only=False):
        
        self.major_arcana = [Card(name=card_name) for card_name in self.major_strings]

        self.cards = self.major_arcana

        if not major_only:
            
            ranks = ["Ace"] + [Deck.rank_map.get(str(i+1)) for i in range(1,10)] + ["Page","Knight","Queen","King"]
            suits = ["Wands","Cups","Pentacles","Swords"]
            self.minor_arcana = [Card(r,s) for r,s in itertools.product(ranks,suits)]
        
            self.cards.extend(self.minor_arcana)

        self.base_cards = deepcopy(self.cards)
        self.unshuffled_cards = self.base_cards
        self.shuffle()

        if n_drawn is not None:
            self.draw_random_cards(n_drawn)


    def shuffle(self,returns="self"):
    
        random.shuffle(self.cards)
        if returns=="cards":
            return self.cards
        elif returns=="self":
            return self
        
        
    def draw_random_cards(self,number:int):
        
        drawn = list()
        for _ in range(number):
            drawn_card = self.cards.pop(0)
            drawn.append(drawn_card)
        self.hand = drawn
        self.unshuffled_cards = [i for i in self.cards if i.name not in [drawn]]

        return drawn

    