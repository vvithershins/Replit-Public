import requests, json, datetime, pytz

# Replace 'America/New_York'/'EST' with your desired timezone

timezone = pytz.timezone('EST')

current_date = datetime.datetime.now(timezone)


dayslist = [(current_date + datetime.timedelta(days=i)).strftime("%A") for i in range(7)]


def getcode(code):
  if code == 0:
    return "Clear sky."
  elif code == 1: 
    return "Mainly clear."
  elif code == 2:
    return "Partly cloudy."
  elif code == 3:
    return "Overcast."
  elif code == 45:
    return "Fog."
  elif code == 48:
    return "Depositing rime fog."
  elif code == 51:
    return "Light drizzle."
  elif code == 53:
    return "Moderate drizzle."
  elif code == 55:
    return "Dense drizzle."
  elif code == 56:
    return "Light freezing drizzle"
  elif code == 57:
    return "Dense freezing drizzle."
  elif code == 61:
    return "Slight rain."
  elif code == 63:
    return "Moderate rain."
  elif code == 65:
    return "Heavy rain."
  elif code == 66:
    return "Light freezing rain."
  elif code == 67:
    return "Heavy freezing rain."
  elif code == 71:
    return "Slight snow fall."
  elif code == 73:
    return "Moderate snow fall."
  elif code == 75:
    return "Heavy snow fall."
  elif code == 77:
    return "Snow grains"
  elif code == 80:
    return "Slight rain showers."
  elif code == 81:
    return "Moderate rain showers."
  elif code == 82:
    return "Violent rain showers"
  elif code == 85:
    return "Slight snow showers."
  elif code == 86:
    return "Heavy snow showers."
  elif code == 95:
    return "Thunderstorm."
  elif code == 96:
    return "Thunderstorm with slight hail."
  elif code == 98:
    return "Thunderstorm with heavy hail."


#Adjust timezone and lat and long here.

timezone = "EST"
latitude = 37.0708
longitude = -76.4844

result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

user = result.json()
#print(json.dumps(user, indent=2))

for i in range(7):
  print(dayslist[i])
  
  date = f"{user['daily']['time'][i][5:7]}-{user['daily']['time'][i][8:10]}-{user['daily']['time'][i][0:4]}"
  print(date)
  #print(user["daily"]["time"][i])
  


  weathercode = (user["daily"]["weathercode"][i])


  print(f"{getcode(weathercode)}")
  max = (user["daily"]["temperature_2m_max"][i])
  min = (user["daily"]["temperature_2m_min"][i])

  maxf = (max * 1.8) + 32
  minf = (min * 1.8) + 32
  maxf = round(maxf, 2)
  minf = round(minf, 2)

  print("The high", dayslist[i], "will be", maxf, "°F and the low will be", minf, "°F")
  print()


