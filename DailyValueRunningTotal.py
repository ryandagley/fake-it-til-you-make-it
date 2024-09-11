'''
Script Name: DailyValueRunningTotal.py

Description:
This Python script generates a sequence of daily values from 1 through 31, where each value corresponds to its respective day number. 
The script also maintains a running total that accumulates the sum of the values as the days progress. For example, on Day 1, the value is 1, 
and the running total is 1. On Day 2, the value is 2, and the running total is 1 + 2 = 3. This continues through Day 31, providing both the 
daily value and the cumulative running total for each day.

'''

# Initialize variables
running_total = 0

# Loop through days 1 to 31
for day in range(1, 32):
    running_total += day  # Add the current day to the running total
    print(f"Day {day}: Value = {day}, Running Total = {running_total}, Couple Running Total = {running_total*2}"
        )
