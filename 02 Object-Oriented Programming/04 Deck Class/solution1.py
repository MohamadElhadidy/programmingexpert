import random
class Deck:
    valid_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ['H', 'D', 'C', 'S']
    def __init__(self):
        self.cards = [f'{value}{suit}' for suit in Deck.valid_suits for value in Deck.valid_values]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_cards(self):
        return self.cards[:]

    def __len__(self):
        return len(self.cards)

    def contains(self, card):
        if card in self.cards:
            return True
        return False

    def copy(self):
        new_obj = Deck()
        new_obj.cards = self.cards[:]
        return new_obj
    
    def deal(self, n):
        new_list = self.cards[-n:]
        for card in new_list:
            self.cards.remove(card)
        return new_list
        
    def sort_by_suit(self):
        def sort_cards(n):
            if 'H' in n:
                return  69
            if 'D' in n:
                return  79
            if 'C' in n:
                return 89
            if 'S' in n:
                return  99
            
        sort_cards = sorted(self.cards, key=sort_cards)
        self.cards = sort_cards
    
