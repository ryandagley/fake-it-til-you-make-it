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

def main():
    choice = input("What calculator?  1.) What is X% of Y? 2.) What % of X is Y? ") 

    if choice == '1':
        what_is_X_percent_of_Y()
    elif choice == '2':
        X_is_what_percent_of_Y()
    else:
        print("Invalid choice.  Try again.")

main()
