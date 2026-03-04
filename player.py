import market
class Player:
    def __init__(self,name):
        self.player = {
            name: {"portfolio" : {},
                     "money":10000
                     }
        }
    def add_stock(self, stock,player):
        portfolio = self.player[player]["portfolio"]
        if stock in portfolio:
            portfolio +=1
        else:
            portfolio[stock]=1