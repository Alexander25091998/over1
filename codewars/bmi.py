# def bmi(weight, height):
#     BMI = weight // (height*height)
#     if BMI <= 18.5:
#         return print("Underweight")
#
#     if BMI <= 25.0 :
#         return print("Normal")
#
#     if BMI <= 30.0:
#         return print("Overweight")
#
#     if BMI > 30:
#         return print("Obese")

def bmi(weight, height):
    b = weight / height ** 2
    return print(['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)])

bmi(50, 1.80)