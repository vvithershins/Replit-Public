import time, os, pytz
from datetime import datetime


def countdown(target_date_str, ent_tz, event):
  """Counts down to a given target date in the specified timezone."""

  # Parse the target date string
  target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")
 
  timezone = pytz.timezone(ent_tz)
  target_date = timezone.localize(target_date)

  while True:
    # Get the current time in America/New_York timezone
    current_time = datetime.now(timezone)

    # Calculate the time difference
    time_difference = target_date - current_time

    # Check if the countdown is over
    if time_difference.total_seconds() < 0:
      print("Countdown finished!")
      break

    # Calculate remaining time in days, hours, minutes, and seconds
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Display the countdown
    print(f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d} until {event}", end="\r")

    # Wait for one second
    time.sleep(1)

# Get the target date from the user
event = input("Which event are you counting down to?\n-> ")
ent_tz = input("Enter your timezone\n-> ")
if ent_tz == "":
  print("Since no time_zone was entered, UTC time will be used")
  ent_tz = "UTC"
target_date_str = input("Enter target date (YYYY-MM-DD HH:MM:SS) ")

# Start the countdown
os.system("clear")
print("\033[?25l",end="")
if event == "Halloween":
  print("\033[43m",end="")
elif event == "Christmas":
  print("\033[42m",end="")
countdown(target_date_str,ent_tz,event)
