# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 56

# Example Output

# You have 12410 days, 1768 weeks, and 408 months left.
age_1 = int(age)

age_remain = 90-age_1
days = age_remain*365
weeks = age_remain*52
months = age_remain*12


print(f"You have {days} days, {weeks} weeks, and {months} months left.")




