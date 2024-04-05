from replit import db
import os, time, datetime, pytz
import matplotlib.pyplot as plt

entries = []

totalvalues = 0

def Add():
  global addSteps
  addSteps = int(input("How many steps? > "))

def AddToDB():
  today = input("Enter steps for \n1. (T)oday  \n2. (A)nother date?\n------------------ \n-> ").strip().lower()
  time.sleep(1)
  os.system("clear")
  if today[0] == "1" or today[0] == "t":
    Add()
    today_date = datetime.datetime.now(pytz.timezone("EST")).strftime("%-m/%d/%Y")
    if today_date[1] == "/":
      today_date = f"0{today_date}"
      
    db[today_date] = addSteps
  elif today[0] == "2" or today[0] == "a":
    whatYear = input("What year (1234) -> ")
    whatMonth = input("What month (1-12) -> ")
    intMonth = int(whatMonth)
    if intMonth < 10:
      if whatMonth[0] != "0":
        whatMonth = f"0{whatMonth}"
    whatDay = input("What Day (1-31) -> ")
    intDay = int(whatDay)
    if intDay < 10:
      if whatDay[0] != "0":
        whatDay = f"0{whatDay}"
    date = f"{whatMonth}/{whatDay}/{whatYear}"
    Add()
    db[date] = addSteps
    #time.sleep(0.75)
    #os.system("clear")

def plot():
  dates = []
  steps = []
  keys = db.keys()
  for key in sorted(keys):
      dates.append(key)
      steps.append(db[key])
  plt.plot(dates, steps)
  plt.xlabel("Date")
  plt.ylabel("Steps")
  plt.title("Step Count Over Time")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("Graphs/step_count_over_time.png")  # Save plot as image
  plt.close()  # Close plot to avoid displaying it
  print("Plot saved as 'step_count_over_time.png'")

def plot_cumulative():
  cumulative_steps = []
  total_steps = 0
  dates = []
  keys = db.keys()
  for key in sorted(keys):
      total_steps += db[key]
      cumulative_steps.append(total_steps)
      dates.append(key)

  plt.plot(dates, cumulative_steps)
  plt.xlabel("Date")
  plt.ylabel("Cumulative Steps")
  plt.title("Cumulative Steps Over Time")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("Graphs/cumulative_step_count_over_time.png")  # Save plot as image
  plt.close()  # Close plot to avoid displaying it
  print("Plot saved as 'cumulative_step_count_over_time.png'")

def plot_within_range(start_date, end_date):
  dates = []
  steps = []
  cumulative_steps = []
  total_steps = 0

  sorted_items = sorted(db.items(), key=lambda x: datetime.datetime.strptime(x[0], "%m/%d/%Y"))

  for key, value in sorted_items:
      if start_date <= key <= end_date:
          dates.append(key)
          steps.append(value)
          total_steps += value
          cumulative_steps.append(total_steps)

  plt.plot(dates, steps)
  plt.xlabel("Date")
  plt.ylabel("Steps")
  plt.title("Step Count Over Time (Within Range)")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("Graphs/step_count_within_range.png")
  plt.close()

  plt.plot(dates, cumulative_steps)
  plt.xlabel("Date")
  plt.ylabel("Cumulative Steps")
  plt.title("Cumulative Steps Over Time (Within Range)")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("Graphs/cumulative_step_count_within_range.png")
  plt.close()

  print("Plots saved as 'step_count_within_range.png' and 'cumulative_step_count_within_range.png'")
  
def View():
  global totalvalues, entries
  keys = db.keys()
  if len(keys) > 0:
    howMany = input("Show \n1. (1) day \n2. (A)ll days \n3. (R)ange of days?\n------------------\n->  ").strip().lower()
    if howMany.startswith("a") or howMany.startswith('2'):
      # Show all entries
      time.sleep(1)
      os.system("clear")
      plot()
      plot_cumulative()
      sorted_items = sorted(db.items(), key=lambda x: datetime.datetime.strptime(x[0], "%m/%d/%Y"))
      i = 0
      max = 10
      total = len(sorted_items)
      lifetimesteps = 0
      while True:
        for key, value in sorted_items:
          entry = f"{key} -- {value}"
          if entry not in entries:
            print(entry)
            entries.append(entry)
            i += 1
            if i < total:
              if i < max:
                continue
              else:
                next = input("Show next? ")
                if next[0] == "y":
                  max += 10
                  time.sleep(0.75)
                  os.system("clear")
                  continue
                else:
                  entries = []
                  time.sleep(0.75)
                  os.system("clear")
                  AddOrView()
            else:
              entries = []
              for value in db.values():
                lifetimesteps += value
              input(f"{lifetimesteps} lifetime recorded accrued steps.\nPress enter to continue")
              if input:
                time.sleep(0.75)
                os.system("clear")
                AddOrView()

    elif howMany.startswith("1"):
      # Show entries for a single day
      time.sleep(1)
      os.system("clear")
      date_to_view = input("Enter the date (MM/DD/YYYY) -> ").strip()
      if date_to_view in keys:
        input(f"{date_to_view} -- {db[date_to_view]}\n------------------\nPress enter to continue")
        time.sleep(1)
        os.sytem("clear")
      else:
        input("No entries found for the specified date.\n----------------------------------------\nPress enter to continue")
        time.sleep(1)
        os.system("clear")


    elif howMany.startswith("r") or howMany.startswith("3"):
      # Show entries within a range of dates
      time.sleep(1)
      os.system("clear")
      start_date = input("Enter the start date (MM/DD/YYYY): ").strip()
      end_date = input("Enter the end date (MM/DD/YYYY): ").strip()
      plot_within_range(start_date, end_date)
      sorted_items = sorted(db.items(), key=lambda x: datetime.datetime.strptime(x[0], "%m/%d/%Y"))
      i = 0
      max = 10
      total = len(sorted_items)
      while i < total:
        for key, value in sorted_items:
          if start_date <= key <= end_date:
            entry = f"{key} -- {value}"
            if entry not in entries:
              print(entry)
              entries.append(entry)
              totalvalues += value
              i += 1
              if i < total and i % max == 0:
                next = input("Show next? ")
                if next.lower().startswith("y"):
                  max += 10
                  time.sleep(0.75)
                  os.system("clear")
                  continue
                else:
                  break
        else:
          input(f"{totalvalues} total steps within range.\nPress enter to continue")
          time.sleep(0.75)
          os.system("clear")
          break
      else:
          entries = []
          input(f"{totalvalues} total steps within range.\nPress enter to continue")
          time.sleep(0.75)
          os.system("clear")
          AddOrView()
    else:
      print("Invalid option. Please choose '1', 'all', or 'range'.")
  else:
    input("No entries to show, Press enter to return to menu")
    if input:
      time.sleep(0.75)
      os.system("clear")
      AddOrView()
      
def deleteEntries():
  deletewhich = input("Delete \n1. (1) entry \n2. (A)ll entries \n3. (R)ange of entries? ").strip().lower()
  if deletewhich[0] == "a" or deletewhich[0] == "2":
    time.sleep(1)
    os.system("clear")
    confirm = input("type CONFIRM in all caps to confirm deletion\nWARNING THIS ACTION CAN NOT BE UNDONE.")
    if confirm == "CONFIRM":
      for key in db.keys():
        del db[key]
      time.sleep(1.25)
      os.system("clear")
  elif deletewhich[0] == "1":
    time.sleep(1)
    os.system("clear")
    deleteYear = input("Enter year of date to delete >")
    deleteMonth = int(input("Enter the month of the date to delete > "))
    if deleteMonth < 10:
      deleteMonth = f"0{deleteMonth}"
    deleteDay = input("Enter the day of the date to delete >")
    date_to_delete = f"{deleteMonth}/{deleteDay}/{deleteYear}"
  
  
  
    if date_to_delete in db.keys():
      confirm = input("type CONFIRM in all caps to confirm deletion\nWARNING THIS ACTION CAN NOT BE UNDONE.\n ->")
      if confirm == "CONFIRM":
        del db[date_to_delete]
        input("Entry deleted.")
    else:
      input(f"Entry for {date_to_delete} not found")
    time.sleep(1)
    os.system("clear")
  elif deletewhich[0] == "r" or deletewhich[0] == "3":
    time.sleep(1)
    os.system("clear")
    start_date_delete = input("Enter the start date (MM/DD/YYYY): ").strip()
    end_date_delete = input("Enter the end date (MM/DD/YYYY): ").strip()
    
    for key in db.keys():
      if start_date_delete <= key <= end_date_delete:
        confirm = input("type CONFIRM in all caps to confirm deletion\nWARNING THIS ACTION CAN NOT BE UNDONE.")
        if confirm == "CONFIRM":
          del db[key]
          print("database deleted")
    else:
      print("Nothing to delete")
    time.sleep(1)
    os.system("clear")

def AddOrView():
  while True:
    which = input("1. (A)dd \n2. (V)iew \n3. (D)elete?\n------------\n-> ").strip().lower()
    time.sleep(1)
    os.system("clear")
    if which[0] == "a" or which[0] == "1":
      AddToDB()
      input("Press enter to continue")
      time.sleep(1)
      os.system("clear")
    elif which[0] == "v" or which[0] == "2":
      View()
    elif which[0] == "d" or which[0] == "3":
      deleteEntries()
      
AddOrView()