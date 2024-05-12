import requests

site = "https://api.quotable.io/quotes/random"
stuff = requests.get(site)
data = stuff.json()
print(data[0]["content"])
print(data[0]["author"])
