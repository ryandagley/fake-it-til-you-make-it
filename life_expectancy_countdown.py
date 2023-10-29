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


while True:
    # Calculate the current time
    current_datetime = datetime.datetime.now()

    # Calculate the time remaining until your 76th birthday
    time_remaining = target_datetime - current_datetime

    # Calculate years, months, days, hours, minutes, and seconds
    days_remaining = time_remaining.days
    seconds_remaining = time_remaining.seconds
    years_remaining = days_remaining // 365
    days_remaining %= 365
    months_remaining = days_remaining // 30
    days_remaining %= 30
    hours_remaining, remainder = divmod(seconds_remaining, 3600)
    minutes_remaining, seconds_remaining = divmod(remainder, 60)

    # Calculate the number of weeks remaining
    weeks_remaining = days_remaining // 7

    # Calculate the total number of weeks from today until your 76th birthday
    total_weeks = (target_datetime - current_datetime).days // 7

    # Calculate periods for the years you've lived and have left
    years_lived = 76 - years_remaining

    # Clear the previous line and print the countdown and total weeks
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print(f" Final days:  {target_datetime}") #final days
    print(f" {'.' * years_lived} {years_lived} years lived \n {'.' * years_remaining} {years_remaining} years left \n" , end="")
    print(f" | Countdown: {years_remaining} years, {months_remaining} months, {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes, {seconds_remaining} seconds",  end="" )
    print(f" ({total_weeks} weeks left)", end="\r")  # Print on the same line
    time.sleep(1)
