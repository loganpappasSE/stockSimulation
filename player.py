import market
class Player:
    def __init__(self,name):
        self.player = {
        }
    def create_player(self,name):
        self.player[name] = {
            "money":10000,
            "portfolio":{}
        }
    def add_stock(self, stock,player):
        portfolio = self.player[player]["portfolio"]
        if stock in portfolio:
            portfolio +=1
        else:
            portfolio[stock]=1
    def delete_stock(self, stock,player):
        portfolio = self.player[player]["portfolio"]
        if stock in portfolio:
            portfolio -=1
    def buy_stock(self,stock,player,market):
        price = market.stocks[stock]["price"]
        self.player[player]["money"] -= price
        self.add_stock(stock,player)
    def sell_stock(self,stock,player,market):
        price = market.stocks[stock]["price"]
        self.delete_stock()
        self.player[player]["money"] += price
    def display(self,player,market):
        print(f"In {player}'s portfolio, you have ")
        
        for item,amount in self.player["portfolio"].items:
            condition,percent = market.percentchange(item)
            if condition:
                saying=  "has gone up ", percent , "%"
            else:
               saying = "has gone down ", percent , "%"
            print(item, ":",amount,"shares,  the price today is", 
                  market.stocks[item]["price"], saying )

