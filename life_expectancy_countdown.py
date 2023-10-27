import datetime
import time
import os

# Prompt the user to enter their birthdate
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Calculate your 76th birthday
target_year = birthdate.year + 76
target_birthday = datetime.date(target_year, birthdate.month, birthdate.day)

# Calculate the time remaining until your 76th birthday
current_datetime = datetime.datetime.now()
target_datetime = datetime.datetime(target_year, birthdate.month, birthdate.day, 0, 0, 0)
time_remaining = target_datetime - current_datetime

# Calculate years, months, days, hours, minutes, and seconds
days = time_remaining.days
seconds = time_remaining.seconds
years = days // 365
days %= 365
months = days // 30
days %= 30
hours, remainder = divmod(seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Calculate the number of weeks remaining
weeks_remaining = days // 7

# Calculate the total number of weeks from today until your 76th birthday
total_weeks = (target_datetime - current_datetime).days // 7

while True:
    # Calculate the current time
    current_datetime = datetime.datetime.now()

    # Calculate the time remaining until your 76th birthday
    time_remaining = target_datetime - current_datetime

    # Calculate years, months, days, hours, minutes, and seconds
    days = time_remaining.days
    seconds = time_remaining.seconds
    years = days // 365
    days %= 365
    months = days // 30
    days %= 30
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Calculate the number of weeks remaining
    weeks_remaining = days // 7

    # Calculate the total number of weeks from today until your 76th birthday
    total_weeks = (target_datetime - current_datetime).days // 7

    # Calculate periods for the years you've lived and have left
    years_lived = years
    years_left = 76 - years_lived

    # Clear the previous line and print the countdown and total weeks
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print(f" {'.' * years_left} {years_left} years lived \n {'.' * years_lived} {years_lived} years left \n" , end="")
    print(f" | Countdown: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds",  end="" )
    print(f" ({total_weeks} weeks in total)", end="\r")  # Print on the same line
    time.sleep(1)
