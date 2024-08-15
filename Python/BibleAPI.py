import requests
verse = input("enter book and verse > ")
r = requests.get(f"https://bible-api.com/{verse}")
r = eval(r.text)
for key,value in r.items():
  if key == "text":
    print(value)
