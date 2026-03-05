import player, market
import sys
players = player()
daMarket = market()
name = input("Enter your name:")
if name not in players.players:
    players.create_player(name)
daily = daMarket.dailythree
players.display(name,daMarket)
print("todays market looks like: ")
for stock in daily:
    price = daMarket.stocks[stock]["price"]
    print(stock, "-",price)
choice = input("would you like to buy or sell or leave?")
if choice == "buy":
    schoice = input("which stock?")
    players.buy_stock(schoice,name,daMarket)
elif choice == "sell":
    sell = input("which stock?")
    players.sell_stock(sell,name,daMarket)
else:
    sys.exit

