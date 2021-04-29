# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are slightly overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese.

bmi = (round(float(weight)/float(height**height)))

print(bmi)

if bmi < 18.5:
  print("Your BMI IS " + str(bmi) + " Underweigh")
elif bmi >= 18.5:
  print("Normal weight")
elif bmi <= 25:
    print("Normal weight")
elif bmi >= 25:
  print("Slighly Over weight")
elif bmi <= 30:
  print("Slightly Over weight")
elif bmi >=30:
  print("Obese")
elif bmi <=35:
  print("Over obese")
else:
    print("Clinically Obsses")


# print("Normal Weight")
#         elif <= 25:
#           print("Normal weight")
#             elif <= 30:
#               print("Normal weight")
#                 elif >= 30:
#                   print("Normal weight")
#                     elif >= 35: 