print("BMI calculator ")
height = float(input("what is your height in m?\n"))
weight = float(input("what is your weight in kg?\n"))
BMI =round(weight / (height**2),2)
print(f"BMI is {BMI}")
if BMI < 18.5:
    print("you are underweight")
elif BMI < 25:
    print("you have a normal weight")
elif BMI <30:
    print("you are overweight")
elif BMI <35:
    print("you are obese")
else:
    print("you are clinically obese")
