#BMI calculator
#Prompts for input!
import sys

name1 = raw_input("What is the name?")

def is_metric():
    yes = {'yes', 'y'}
    no = {'no','n'}

    m_choice = raw_input("Is your measurement metric?").lower()
    if m_choice in yes:
        return True
    elif m_choice in no:
        return False
    else:
        sys.stdout.write("Please use 'yes' or 'no'")

def metric_imperial_q():
    if is_metric == True:
        height1 = raw_input("What is the height in centimeters?")
        weight1 = raw_input("What is the weight in kilograms?")
        return height1, weight1
    else:
        height1 = raw_input("What is the height in inches?")
        weight1 = raw_input("What is the weight in pounds?")
        return height1, weight1

def bmi_calculator(name, height, weight, bmi_calc):
    if bmi_calc == True: #metric formula
        height = int(height)
        bmi = int(weight) / (float(height) ** 2) * 10000
    elif bmi_calc == False: #imperial formula
        bmi = float(int(weight)) / (int(height) ** 2) * 703
    print("bmi: ")
    print("%.2f" % bmi) #limited to two decimal places
    if bmi < 18.0:
        return name + " is underweight"
    elif bmi < 25:
        return name + " is normal weight"
    elif bmi < 30:
        return name + " is overweight"
    else:
        return name + " is obese"

is_metric = is_metric()
height1, weight1 = metric_imperial_q()
result = bmi_calculator(name1.title(), height1, weight1, is_metric)
print result
