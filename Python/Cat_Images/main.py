import requests


request = requests.get("https://api.thecatapi.com/v1/images/search")

stuff = (eval(request.text))

print(stuff[0]["url"])
cat = stuff[0]["url"]

image = requests.get(cat)

f = open("catimage.png","wb")
f.write(image.content)
f.close()
