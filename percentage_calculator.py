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

def main():
    choice = input("What calculator?  1.) What is X% of Y? 2.) What % of X is Y? 3.) What is the % increase or decrease?") 

    if choice == '1':
        what_is_X_percent_of_Y()
    elif choice == '2':
        X_is_what_percent_of_Y()
    elif choice == '3':
        percentage_increase_drecrease()
    else:
        print("Invalid choice.  Try again.")

main()
