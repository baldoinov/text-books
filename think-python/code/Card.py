from multiprocessing.sharedctypes import Value
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
        """Compares this card to other, first by suit, then rank.
        
        returns: boolean
        """

        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # If suits are the same we check the ranks
        return self.rank < other.rank
    
    def __eq__(self, other) -> bool:
        """Checks whether self and other have the same rank and suit.
        
        returns: boolean
        """
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    """Represents a standard deck with 52 cards.
    
    attributes:
        cards: list of Card objects
    """

    def __init__(self) -> None:
        
        self.cards = []

        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self) -> str:

        res = [str(card) for card in self.cards]
        return '\t'.join(res)
    
    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)
    
    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        
        card: Card
        """
        self.cards.remove(card)

    def add_card(self, card):
        """Adds a card to the Deck."""
        self.cards.append(card)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)
    
    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()
    
    def move_cards(self, other, num: int):
        """Moves the given number of cards from the deck into the Hand.
        
        hand: destination Hand object
        num: integer number of cards to move
        """
        
        for i in range(num):
            other.add_card(self.pop_card())
    
    def deal_hands(self, n_hands: int, n_cards: int) -> list:
        """Creates hands with the given number of cards and return them inside a list.
        
        n_hands: number of hands
        n_cards: number of cards in each hand
        """
        
        if n_hands * n_cards > len(self.cards):
            raise ValueError("There's not enough cards in this Deck for this kind of game!")
        
        hands = []
        
        for i in range(n_hands):
            h = Hand()    
            self.move_cards(h, n_cards)

            hands.append(h)
        
        return hands


class Hand(Deck):
    """Represents a hand of playing cards"""

    def __init__(self, label: str="") -> None:
        
        self.cards = []
        self.label = label

if __name__ == '__main__':

    d = Deck()
    d.shuffle()
    hands = d.deal_hands(4, 5)
    
    for h in hands:
        print(h, end='\n\n')
