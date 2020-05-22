print("This will tell you X is what percent of Y.")

total = int(input("What is the total? y = \n"))
progress = int(input("How much have you completed? x = \n"))

print(str(progress) + " is " + str(progress/total*100) + " percent of " + str(total))
