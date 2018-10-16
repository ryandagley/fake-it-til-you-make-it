#BMI calculator

name1 = "Denny"
height1 = 70
weight1 = 204

def bmi_calculator(name, height, weight):
    bmi = float(weight) / (height ** 2) * 703
    print("bmi: ")
    print(bmi)
    if bmi < 18.0:
        return name + " is underweight"
    elif bmi < 25:
        return name + " is normal weight"
    elif bmi < 30:
        return name + " is overweight"
    else:
        return name + " is obese"

result = bmi_calculator(name1, height1, weight1)
print result