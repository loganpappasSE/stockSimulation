import market
import storage
class Player:
    def __init__(self):
        self.player = storage.load()
    def create_player(self,name):
        self.player[name] = {
            "money":10000,
            "portfolio":{}
        }
    
    def add_stock(self, stock,player):
        portfolio = self.player[player]["portfolio"]
        if stock in portfolio:
            portfolio[stock] +=1
        else:
            portfolio[stock]=1
    def delete_stock(self, stock,player):
        portfolio = self.player[player]["portfolio"]
        if stock in portfolio:
            portfolio[stock] -=1
    def buy_stock(self,stock,player,market):
        price = market.stocks[stock]["price"]
        self.player[player]["money"] -= price
        self.add_stock(stock,player)
        storage.save(self.player)
    def sell_stock(self,stock,player,market):
        # support selling all stocks at once
        if stock == "ALL":
            portfolio = self.player[player]["portfolio"]
            if not portfolio:
                print("You have no stocks to sell.")
                return
            total = 0
            for s, amt in list(portfolio.items()):
                price = market.stocks.get(s, {}).get("price", 0)
                total += price * amt
                del portfolio[s] 
            self.player[player]["money"] += total
            storage.save(self.player)
            print(f"Sold all stocks for ${round(total,2)}")
            return

        # sell a single share of the given stock
        portfolio = self.player[player]["portfolio"]
        if stock not in portfolio:
            print("You don't own that stock.")
            return
        price = market.stocks[stock]["price"]
        self.delete_stock(stock,player)
        self.player[player]["money"] += price
        if self.player[player]["portfolio"].get(stock, 0) == 0:
                del self.player[player]["portfolio"][stock]
        storage.save(self.player)
    def display(self,player,market):
        print(f"In {player}'s portfolio, you have ")
        print(round(self.player[player]["money"],2) , "$ \n-------------\n" \
            " your portfolio is ")
        for item,amount in self.player[player]["portfolio"].items():
            condition,percent = market.percentchange(item)
            if condition:
                saying=  "has gone up " + str(percent) + "%"
            else:
               saying = "has gone down "+ str(percent) + "%"
            print(item, ":",amount,"shares, risk factor:" ,
                  market.stocks[item]["risk"], "\nthe price today is", 
                  market.stocks[item]["price"], saying )

