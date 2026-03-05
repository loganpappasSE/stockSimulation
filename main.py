from player import Player
from market import Market
import sys
players = Player()
daMarket = Market()
name = input("Enter your name:")
if name not in players.player:
    players.create_player(name)
while True:
    daily = daMarket.dailythree()
    players.display(name,daMarket)
    print(daMarket.moon())
    print("todays market looks like: ")
    for stock in daily:
        price = daMarket.stocks[stock]["price"]
        risk = daMarket.stocks[stock]["risk"]
        print(stock, "-",price, " risk: ", risk)
    choice = input("would you like to buy or sell or leave?")
    if choice == "buy":
        schoice = input("which stock?")
        players.buy_stock(schoice,name,daMarket)
        daMarket.new_day()
    elif choice == "sell":
        sell = input("which stock?")
        players.sell_stock(sell,name,daMarket)
        daMarket.new_day()
    else:
        
        break

