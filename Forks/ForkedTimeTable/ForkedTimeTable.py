#Forked from PythonDEVMaster / Country Time Table

# Import datetime and pytz modules
import datetime
import pytz

# Dictionary of countries, capitals, and time zones
countries = {
    "Afghanistan": {"Capital": "Kabul", "Timezone": "Asia/Kabul"},
    "Argentina": {"Capital": "Buenos Aires", "Timezone": "America/Argentina/Buenos_Aires"},
    "Australia": {"Capital": "Canberra", "Timezone": "Australia/Canberra"},
    "Bangladesh": {"Capital": "Dhaka", "Timezone": "Asia/Dhaka"},
    "Belgium": {"Capital": "Brussels", "Timezone": "Europe/Brussels"},
    "Brazil": {"Capital": "Brasília", "Timezone": "America/Sao_Paulo"},
    "Canada": {"Capital": "Ottawa", "Timezone": "America/Toronto"},
    "China": {"Capital": "Beijing", "Timezone": "Asia/Shanghai"},
    "Egypt": {"Capital": "Cairo", "Timezone": "Africa/Cairo"},
    "France": {"Capital": "Paris", "Timezone": "Europe/Paris"},
    "Germany": {"Capital": "Berlin", "Timezone": "Europe/Berlin"},
    "Greece": {"Capital": "Athens", "Timezone": "Europe/Athens"},
    "India": {"Capital": "New Delhi", "Timezone": "Asia/Kolkata"},
    "Indonesia": {"Capital": "Jakarta", "Timezone": "Asia/Jakarta"},
    "Italy": {"Capital": "Rome", "Timezone": "Europe/Rome"},
    "Japan": {"Capital": "Tokyo", "Timezone": "Asia/Tokyo"},
    "Kazakhstan": {"Capital": "Astana", "Timezone": "Asia/Almaty"},
    "Malaysia": {"Capital": "Kuala Lumpur", "Timezone": "Asia/Kuala_Lumpur"},
    "Netherlands": {"Capital": "Amsterdam", "Timezone": "Europe/Amsterdam"},
    "Pakistan": {"Capital": "Islamabad", "Timezone": "Asia/Karachi"},
    "Russia": {"Capital": "Moscow", "Timezone": "Europe/Moscow"},
    "South Africa": {"Capital": "Pretoria", "Timezone": "Africa/Johannesburg"},
    "Spain": {"Capital": "Madrid", "Timezone": "Europe/Madrid"},
    "Switzerland": {"Capital": "Bern", "Timezone": "Europe/Zurich"},
    "United Kingdom": {"Capital": "London", "Timezone": "Europe/London"},
    "US(New York)(Eastern)": {"Capital": "Washington, D.C.", "Timezone": "America/New_York"},
    "US(Central)(Chicago)" : {"Capital" : "Washington, D.C.", "Timezone" : "America/Chicago"},
    "US(Mountain)(Salt Lake City)" : {"Capital" : "Washington, D.C.", "Timezone" : "America/Denver"},
    "US(Pacific)" : {"Capital" : "Washington, D.C.", "Timezone" : "America/Los_Angeles"},
  "US(Alaska)" : {"Capital" : "Washington, D.C.", "Timezone" : "America/Anchorage"},
  "US(Hawaii)" : {"Capital" : "Washington, D.C.", "Timezone" : "Pacific/Honolulu"},
}

# Get the current UTC time
utc_time = datetime.datetime.utcnow()

# Sort countries based on the selected option
sorting_option = input("Enter sorting option (alphabetical/continent/time): ").lower()

if sorting_option == "alphabetical":
    sorted_countries = sorted(countries.items())
elif sorting_option == "continent":
    sorted_countries = sorted(countries.items(), key=lambda x: x[1]["Timezone"].split("/")[0])
  #-- New section.
elif sorting_option == "time":
  sorted_countries = sorted(countries.items(), key=lambda x: pytz.timezone(x[1]["Timezone"]).utcoffset(datetime.datetime.utcnow()))
# End new section. 

# Print the table
print("{:<20} {:<30} {:<30} {:<30}".format("Country", "Capital", "Time Zone", "Current Time"))
print("="*100)

for country, info in sorted_countries:
    time_zone = info["Timezone"]
    tz_object = pytz.timezone(time_zone)
    local_time = utc_time.astimezone(tz_object)
    current_time = local_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    print("{:<20} {:<30} {:<30} {:<30}".format(country, info["Capital"], time_zone, current_time))
    print()
