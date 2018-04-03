#coding=utf-8

class Card:
    def __init__(self,rem):
        self.rem = rem
        return

    def getRem(self):
        return self.rem

    def display(self):
        print('I\'m %s,my rem is %s.',(self.__class__.__name__,self.getRem()))

    def SwingCard(self,cost):
        return

class NoCard(Card):
    def SwingCard(self,cost):
        print('I have no discount.')
        self.rem = self.rem - cost

class SimpleCard(Card):
    def SwingCard(self,cost):
        self.rem = self.rem - cost * 0.2