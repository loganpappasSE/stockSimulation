import json

def load():
    with open("data.json", "r") as f :
        return json.load(f)

def save(data):
    with open("data.json","w") as f:
        json.dump(data,f,indent=4)
        print("saving market to market.json")
def load_market():
    with open("market.json", "r") as f :
        return json.load(f)

def save_market(data):
    with open("market.json","w") as f:
        json.dump(data,f,indent=4)
        print("saving market to market.json")