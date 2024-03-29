leapyear = input("Is it a leap year? ").strip().lower()

if leapyear[0] == "n":
  year = 365
  leap = False
elif leapyear[0] == "y":
  year = 366
  leap = True

if leap == False:
  leapmonths = {"JAN" : 31, "FEB" : 28, "MAR" : 31, "APR" : 30, "MAY" : 31, "JUN" : 30, "JUL" : 31, "AUG" : 31, "SEP" : 30, "OCT" :31, "NOV" : 30}
  
elif leap == True:
  leapmonths = {"JAN" : 31, "FEB" : 29, "MAR" : 31, "APR" : 30, "MAY" : 31, "JUN" : 30, "JUL" : 31, "AUG" : 31, "SEP" : 30, "OCT" :31, "NOV" : 30}
  
month = input("What is the month? ex JAN,FEB,MAR,APR\n>").strip().upper()

date = int(input("What is the date? ex 1-31\n>"))


if month[0:3] == "JAN":
  answer = (100 / year) * date
  
elif month[0:3] == "FEB":
  answer = (100 / year) * (leapmonths["JAN"] + date)

elif month[0:3] == "MAR":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + date)

elif month[0:3] == "APR":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + date)

elif month[0:3] == "MAY":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + date)

elif month[0:3] == "JUN":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + date)

elif month[0:3] == "JUL":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + date)

elif month[0:3] == "AUG":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + leapmonths["JUL"] + date)

elif month[0:3] == "SEP":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + leapmonths["JUL"] + leapmonths["AUG"] + date)

elif month[0:3] == "OCT":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + leapmonths["JUL"] + leapmonths["AUG"] + leapmonths["SEP"] + date)

elif month[0:3] == "NOV":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + leapmonths["JUL"] + leapmonths["AUG"] + leapmonths["SEP"] + leapmonths["OCT"] + date)

elif month[0:3] == "DEC":
  answer = (100 / year) * (leapmonths["JAN"] + leapmonths["FEB"] + leapmonths["MAR"] + leapmonths["APR"] + leapmonths["MAY"] + leapmonths["JUN"] + leapmonths["JUL"] + leapmonths["AUG"] + leapmonths["SEP"] + leapmonths["OCT"] + leapmonths["NOV"] + date)


print(f"The year is {answer}% over,")

percentleft = (100 - answer)

print(f"Meaning there is {percentleft}% left until the end of the year.")
