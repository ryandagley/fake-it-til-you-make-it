def what_is_X_percent_of_Y():
    print("This will tell you what is X percent of Y.")

    total = int(input("What is the total? y = \n"))
    progress = int(input("How much have you completed? x = \n"))

    print(str(progress/total*100) + " percent of " + str(total) + " is " +  (str(progress)))

def X_is_what_percent_of_Y():
    print("This will tell you what percent X is of Y.")
    total = int(input("What is the total? y = \n"))
    progress = int(input("What is X? x = \n"))

    print(str(progress) + " is " + str(progress/total*100) + " percent of " + str(total))

def percentage_increase_drecrease():
    print("This will tell you the percentage increase or decrease from X to Y.")
    start_value = int(input("What is the starting percentage?  x = \n"))
    end_value = int(input("What is the second value? y = \n"))
    value_diff = int(start_value-end_value)
    if value_diff < 0:
        direction = "increase"
    elif value_diff > 0:
        direction = "decrease"
    else: 
        direction = "changed"
    print(str(abs((value_diff)/start_value) * 100) + "% " + direction)

def add_percentage_to_X():
    print("This will add Y% to X.")
    start_value = int(input("What is the starting value? x = \n"))
    percentage_increase = int(input("What percentage are you adding to " + str(start_value) + "? "))
    percentage_increase = (percentage_increase/100)
    print(str((start_value * percentage_increase) + start_value))

def subtract_percentage_from_X():
    print("This will subtract Y% from X.")
    start_value = int(input("What is the starting value? x = \n"))
    percentage_decrease = int(input("What percentage are you subtracting from " + str(start_value) + "? "))
    percentage_decrease = (percentage_decrease/100)
    print(str(start_value - (start_value * percentage_decrease)))

def pareto():
    print("This will calculate the 80/20% split of X.")
    start_value = int(input("What is the starting value? x = \n"))
    eighty = round(start_value * .8,2)
    twenty = round(start_value * .2,2)
    print(str(eighty) + "/" + str(twenty) + ".  80% of " + str(start_value) + " is " + str(eighty) + ".  20% of " + str(start_value) + " is " + str(twenty) + ".")

def main():
    choice = input("""
    Which calculator? \n 
    1.) What is X% of Y? \n 
    2.) What % of X is Y? \n 
    3.) What is the % increase or decrease? \n
    4.) What is X + Y%? \n
    5.) What is X - Y%? \n
    6.) What is the 80/20 of X? \n
                    
                    
    Choice: """) 

    if choice == '1':
        what_is_X_percent_of_Y()
    elif choice == '2':
        X_is_what_percent_of_Y()
    elif choice == '3':
        percentage_increase_drecrease()
    elif choice == '4':
        add_percentage_to_X()
    elif choice == '5':
        subtract_percentage_from_X()
    elif choice == '6':
        pareto()
    else:
        print("Invalid choice.  Try again.")

main()



