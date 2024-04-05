# Step Tracker

### Overview
Step Count Tracker is a Python script designed to help individuals monitor their daily activity levels effortlessly. With its user-friendly interface and intuitive functionalities, users can easily input, store, visualize, and analyze their step data.

### Features
**Input Daily Step Counts**: Use the Add function to input your daily step counts.<br>
**Store Step Data**: The AddToDB function stores your step data within the system, providing options to input step counts for today's date or a specified date.<br>
**Visualize Step Trends**: Utilize functions like plot, plot_cumulative, and plot_within_range to visualize your step trends over time, aiding in better understanding of your activity patterns.<br>
**View Entries**: View step entries for specific days or date ranges to gain valuable insights into your progress.<br>
**Delete Entries**: Remove unwanted step entries to ensure data accuracy and integrity.<br>


### Dependencies
**matplotlib** *(For generating line graphs)*<br>
**replit**<br>
**flask >= 2** *(For saving to/loading from database)*

### Usage
Run the script and follow the prompts to input your daily step counts and perform various actions like visualization and deletion of entries.

### Accuracy

You can personalize Step Count Tracker to your timezone to ensure accuracy when adding today's steps.

`today_date = datetime.datetime.now(pytz.timezone("EST")).strftime("%-m/%d/%Y")`<br>
                                                                                        ^
Change EST to your time zone.

<a href = "https://www.timeanddate.com/time/zones/">🖱️Abbreviated Time Zones🖱️</a>

Is intended for use on replit.com
