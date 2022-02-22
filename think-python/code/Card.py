import random

class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit: int=0, rank: int=2) -> None:
        
        self.suit = suit
        self.rank = rank
    
    def __str__(self) -> str:
        return f"{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}"
    
    def __lt__(self, other) -> bool:
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # If suits are the same we check the ranks
        return self.rank < other.rank 

class Deck:

    def __init__(self) -> None:
        
        self.cards = []

        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self) -> str:

        res = [str(card) for card in self.cards]
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
    
    def move_cards(self, other, num: int):
        """Move cards from self to other. If called by a class that inherits from Deck,
        other can be a Hand or a Deck.
        """
        
        for i in range(num):
            card = self.pop_card()
            other.add_card(card)

class Hand(Deck):

    def __init__(self, label: str="") -> None:
        
        self.cards = []
        self.label = label

if __name__ == '__main__':

    d = Deck()
    print(d)
    print("\n\n\n")

    d.shuffle()
    print(d)
    print("\n\n\n")
    
    d.sort()
    print(d)
