import random
import storage
class Market:
    def __init__ (self):
        self.stocks = storage.load_market()
    def set_previous(self):
       for stock in self.stocks:
          self.stocks[stock]["previous"]=self.stocks[stock]["price"]
    def change_price(self):
        factor = random.uniform(.1,.9)
        for stock in self.stocks.values():
         price = stock["price"]
         risk = stock["risk"]
         change = random.uniform(.01, risk *.2)
         if risk < factor:
            price = price * (1+change)
         else:
            price = price * (1-change)
         stock["price"] = round(price,2)
      
    def moon(self):
       lucky_day=random.randint(1,10)
       if lucky_day in range(1,4):
           symbol = random.choice(list(self.stocks.keys()))
           self.stocks[symbol]["price"] *=8
           return symbol + " is going to the moon!!!!!!!!!!!!"
    def new_day(self):
       self.set_previous()
       self.change_price()
       storage.save_market(self.stocks)
    def percentchange(self,stock):
       change = round((self.stocks[stock]["price"]-self.stocks[stock]["previous"]) / self.stocks[stock]["previous"]*100,2)
       if self.stocks[stock]["price"] > self.stocks[stock]["previous"]:
          return True, change
       else:
          return False, change
    def dailythree(self):
       return random.sample(list(self.stocks.keys()),3)
