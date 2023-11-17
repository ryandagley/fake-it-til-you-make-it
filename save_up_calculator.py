item_price = 4000
monthly_savings = 300


def months_calc():
    how_many_months = item_price / monthly_savings
    print(
        f'it will take you {how_many_months} months to save up for that item.')


months_calc()

new_monthly_savings = float(
    input('What would you like the new monthly savings to be?'))

# Update the monthly_savings variable with the new value
monthly_savings = new_monthly_savings

months_calc()  # Call the months_calc function again to recalculate and print the result
