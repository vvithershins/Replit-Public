import datetime,pytz

MyTime = datetime.datetime.now(pytz.timezone("America/New_York"))
#print(MyTime)
st = str(MyTime)
formatTime = f"{st[5:7]}/{st[8:10]}/{st[0:4]} {st[11:19]}"
print(formatTime)

# Convert formatTime back to a datetime object
datetime_object = datetime.datetime.strptime(formatTime, "%m/%d/%Y %H:%M:%S")
print(datetime_object)
