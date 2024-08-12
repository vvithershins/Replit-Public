import requests, os

while True:
  animal = input("Enter an animal name > ").strip()
  my_secret = os.environ['MyAPI']
  api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
  response = requests.get(api_url, headers={'X-Api-Key': my_secret})
  if response.status_code == requests.codes.ok:
    re = eval(response.text)
    #print(re)
    try:
      re2 = re[0]
      #print(re2)
      for key, value in re2.items():
        if key == "name":
          print("\033[32m",end="")
          print(key.title(),":", value,"\033[0m")
        elif key == "taxonomy":
          print("\033[33m",end="")
          print(key.title())
          for i, j in value.items():
            print(i.title(),":",j)
          print("\033[0m",end="")
        elif key == "locations":
          print("\033[34m",end="")
          print(key.title(),end=" : ")
          for loc in value:
            print(loc,end=" ")
          print("\033[0m ")
        elif key == "characteristics":
          print('\033[35m',end="")
          print(key.title(),)
          for i, j in value.items():
            print(i.title(),":",j)
          print("\033[0m")
    except Exception as err:
      print(err)
      '''if isinstance(value,dict):
        print(key, "is dict")
      elif isinstance(value,list):
        print(key, "is list")
      elif isinstance(value,str):
        print(key, "is string")'''
        
        
      
    
      
      
  else:
      print("Error:", response.status_code, response.text)