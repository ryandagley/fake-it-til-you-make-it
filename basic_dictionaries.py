#sensor dictionary

sensors = {1: 'temp',
           2: 'air quality',
           3: 'acidity'}

print "Prints the dictionary: \n" + str(sensors)

print "\nLoops through the dictionary " \
      "and prints keys."
for i in sensors:
    print(i)


print "\nLoops through the dictionary " \
      "and print values."
for i in sensors:
    print(sensors[i])