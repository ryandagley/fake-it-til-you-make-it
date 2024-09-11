# Initialize variables
running_total = 0

# Loop through days 1 to 31
for day in range(1, 32):
    running_total += day  # Add the current day to the running total
    print(f"Day {day}: Value = {day}, Running Total = {running_total}")
