import random

# TODO Rewrite this comment to make clear sense.
'''
Generates 2 lists of random numbers.  Then outputs how many times the loop
ran before finding 10 matching numbers(match_amount).
'''

list1 = []
list2 = []
x = 0  # counter for the loop
combined_nums_count = 0  # the matching numbers
match_amount = 10  # how many numbers have to match

while combined_nums_count < match_amount:
    combined_nums = set(list1).intersection(list2)
    combined_nums_count = len(combined_nums)
    x = x + 1
    for i in range(10):
        random_num1 = random.randint(10, 35)
        random_num2 = random.randint(1, 23)
        list1.append(random_num1)
        list2.append(random_num2)

print "It takes " + str(x) + " runs to find a match!"
