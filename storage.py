import json

def load():
    with open("data.json", "r") as f :
        data =json.load(f)

def save():
    with open("data.json","w") as f:
        json.dump(data,f,indent=2)