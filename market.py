import random

class Market:
    def __init__ (self):
        self.stocks - {
            "AAPL": {"price": 180, "risk": 0.2,"previous":0},
            "MSFT": {"price": 320, "risk": 0.2,"previous":0},
            "GOOG": {"price": 140, "risk": 0.3,"previous":0},
            "AMZN": {"price": 130, "risk": 0.4,"previous":0},
            "META": {"price": 310, "risk": 0.5,"previous":0},

            "TSLA": {"price": 240, "risk": 0.8,"previous":0},
         "NVDA": {"price": 450, "risk": 0.7,"previous":0},
            "AMD": {"price": 120, "risk": 0.6,"previous":0},
            "INTC": {"price": 40, "risk": 0.4,"previous":0},
            "ORCL": {"price": 110, "risk": 0.3,"previous":0},

            "NFLX": {"price": 430, "risk": 0.6,"previous":0},
            "DIS": {"price": 95, "risk": 0.4,"previous":0},
            "UBER": {"price": 65, "risk": 0.7,"previous":0},
            "SHOP": {"price": 75, "risk": 0.8,"previous":0},
            "SQ": {"price": 70, "risk": 0.7,"previous":0},

            "COIN": {"price": 95, "risk": 0.9,"previous":0},
            "SNAP": {"price": 20, "risk": 0.8,"previous":0},
            "ROKU": {"price": 60, "risk": 0.7,"previous":0},
            "PLTR": {"price": 25, "risk": 0.6,"previous":0},
            "RIVN": {"price": 18, "risk": 0.9,"previous":0}

        }
    def set_previous(self):
       for stock in self.stocks.values:
          stock["previous"]=stock["price"]
    def change_price(self):
        factor = random.uniform(.1,.9)
        lucky_day=random.randint(1,10)
        for stock in self.stocks.values:
         price = stock["price"]
         risk = stock["risk"]
         change = random.uniform(.01, risk *.2)
         if risk < factor:
            price = price * (1+change)
         else:
            price = price * (1-change)
         stock["price"] = round(price,2)
        if lucky_day == 2:
           symbol = random.choice(list(self.stocks.keys()))
           self.stocks[symbol]["price"] *=8
    
    def new_day(self):
       self.set_previous()
       self.change_price()
    def percentchange(self):
       
      
