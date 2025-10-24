class Blackjack:
    def Deck(self):
        self.suits=('hearts','diamond','spades','clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'J':10,
                'Q':10, 'K':10, 'A':11}
        self.deck=[2,3,4,5,6,7,8,9,10,'A','A','A','A','J','J','J','J','k','k','k','k','Q','Q','Q','Q']
        self.dealerdeck=[]
        self.playerdeck=[]
    
    def dealcard(self,deck):
        self.Deck()
        import random
        
        card=random.choice(self.deck)
        self.dealerdeck.append(card)
        self.deck.remove(card)

    def total(self):
        total=0
        for card in self.dealerdeck:
            total+=self.values[card]
        return total

    def reveal_dealer(self):
        if len(self.dealerdeck)==2:
            return self.dealerdeck[0]
        elif len(self.dealerdeck)>2:
            return self.dealerdeck[0],self.dealerdeck[1]
        for _ in range(2):
            self.dealcard(self.dealerdeck)
            self.dealcard(self.playerdeck)
            