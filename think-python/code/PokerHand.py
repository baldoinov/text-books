
from Card import Hand, Deck, Card


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def classify(self):

        poker_hands = ['straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pair', 'pair']
        classifiers = [self.has_straight_flush, self.has_four_of_a_kind, self.has_full_house, self.has_flush, self.has_straight, self.has_three_of_a_kind, self.has_twopair, self.has_pair]

        for label, metho in zip(poker_hands, classifiers):
            
            if metho():
                self.label = label
                break

    def rank_hist(self):
        """Builds a histogram of the rank that appear in the hand.
        
        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
    
    def suit_rank_hist(self):
        """Builds a histogram of suit and rank frequency that appear in the hand.

        Store the result in attribute suit_rank
        """

        self.suit_rank = {}

        for card in self.cards:
            self.suit_rank[(card.suit, card.rank)] = self.suit_rank.get((card.suit, card.rank), 0) + 1

    def hand_frequency(self, hist: dict, val: int) -> bool:
        """Check if the frequency of ranks or suits in a Hand is >= than val."""

        for i in hist.values():
            
            if i >= val:
                return True
        
        return False
    
    def has_flush(self) -> bool:
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        return self.hand_frequency(self.suits, 5)

    def has_pair(self) -> bool:
        """Returns True if the hand has a pair, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        return self.hand_frequency(self.ranks, 2)
    
    def has_twopair(self) -> bool:
        """Returns True if the hand has two pairs, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        counter = 0

        for val in self.ranks.values():
            if val >= 2:
                counter += 1
        
        if counter >= 2:
            return True
        
        return False
    
    def has_three_of_a_kind(self) -> bool:
        """Returns True if the hand has three cards with the same rank, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.rank_hist()
        return self.hand_frequency(self.ranks, 3)
    
    def has_straight(self) -> bool:
        """Returns True if the hand has five cards with the ranks in sequence, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        cards = [card for card in self.cards]
        ranks = [card.rank for card in cards]
        
        # https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/
        
        if ranks[0] == 1:
            return checkConsecutive(ranks[:2])

        elif ranks[-1] == 1:
            return checkConsecutive(ranks[:-1])            
        
        else:
            return checkConsecutive(ranks)
    
    def has_full_house(self):
        """Returns True if the hand has three cards with one rank and two
        cards with another, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        
        self.rank_hist()
        counter_3 = 0
        counter_2 = 0

        for val in self.ranks.values():
            if val == 3:
                counter_3 += 1
            elif val == 2:
                counter_2 += 1
        
        if counter_2 >= 1 and counter_3 >= 1:
            return True
        
        return False
    
    def has_four_of_a_kind(self) -> bool:   
        """Returns True if the hand has four cards with the same rank, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """        
        
        self.rank_hist()
        return self.hand_frequency(self.ranks, 4)

    def has_straight_flush(self) -> bool:
        """Returns True if the hand has five cards in sequence and with the same suit, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        cards = [card for card in self.cards]
        ranks = [card.rank for card in cards]
        
        if self.hand_frequency(self.suits, 5):
            if ranks[0] == 1:
                return checkConsecutive(ranks[:2])

            elif ranks[-1] == 1:
                return checkConsecutive(ranks[:-1])            
            
            else:
                return checkConsecutive(ranks)
        else:
            return False


def checkConsecutive(l: list) -> bool:
    return sorted(l) == list(range(min(l), max(l)+1))


occurences = {}
def probabilities() -> dict:
    """Creates a Deck, shuffles it, classify the Hands in this Deck
    and counts the number of times various classifications appear,
    
    Stores the result in the dict occurences.
    """

    deck = Deck()
    deck.shuffle()

    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        hand.classify()
        
        occurences[hand.label] = occurences.get(hand.label, 0) + 1



if __name__ == '__main__':

    for i in range(10000):
        probabilities()
    
    print(occurences, end="\n\n")

    total = sum([value for value in occurences.values()])

    for label, value in occurences.items():
        print(f"A {label} has the {value / total} chance of appearing.")
