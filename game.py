from random import shuffle
from collections import deque


class BaseEntity(object):
    def __init__(self, name, attack, life, mana):
        self.life = life
        self.name = name
        self.attack = attack
        self.life = life
        self.mana = mana
        self.alive = True
    
    def battle(self, other):
        self.life -= other.attack
        if self.life <= 0:
            self.life = False
    
        other.life -= self.attack
        if other.life <= 0:
            other.alive = False


class Card(BaseEntity):
    def __init__(self, name, attack, life, mana):
        BaseEntity.__init__(self, name, attack, life, mana)

    def __str__(self):
        return "(%s) %s [%s/%s]" % (self.mana, self.name, self.attack, self.life)


class Hero(BaseEntity):
    def __init__(self, name, attack, life, deck, mana=0):
        BaseEntity.__init__(self, name, life, attack, mana)
        self.field = list()
        self.hand = list()
        self.deck = deck

    def heal(self, entity, life=0):
        entity.life += life

    def pull(self):
        # remove card from deck, and add to hand
        self.hand.append(
            self.deck.cards.pop()
        )


    def summon(self, card):
        # remove card from hand, and add to field
        self.mana -= card.mana
        self.field.append(
            self.hand.pop(card)
            )


class Deck(object):
    def __init__(self, *card):
        self.cards = [c for c in card]
  
    def shuffle(self):
        shuffle(self.cards)



c1 = Card(name="Cartman", attack=2, life=4, mana=2)
c2 = Card(name="Butters", attack=1, life=1, mana=1)
c3 = Card(name="Slave", attack=1, life=4, mana=3)
c4 = Card(name="Chef", attack=4, life=2, mana=3)
c5 = Card(name="Kyle", attack=2, life=2, mana=2)
c6 = Card(name="Sten", attack=4, life=2, mana=4)
c7 = Card(name="Token", attack=4, life=5, mana=5)
c8 = Card(name="Randy", attack=6, life=5, mana=6)
c9 = Card(name="Garrison", attack=1, life=8, mana=5)
c0 = Card(name="Kenny", attack=7, life=3, mana=6)

d1 = Deck(c1,c2,c3,c4,c5,c6,c7,c8,c9,c0)
d2 = Deck(c1,c2,c3,c4,c5,c6,c7,c8,c9,c0)

h1 = Hero(name="Warrior", attack=1, life=15, deck=d1)
h2 = Hero(name="Priest", attack=1, life=15, deck=d2)


def turn(hero, mana_turn):
    hero.mana = mana_turn
    hero.pull()


def match(h1, h2):
    mana_turn = 1
    while True:        
        turn(h1, mana_turn)
        turn(h2, mana_turn)
        mana_turn += 1


if __name__ == "__main__":

    h1.deck.shuffle()
    h2.deck.shuffle()
