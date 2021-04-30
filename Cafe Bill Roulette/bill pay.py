# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# names_lists = [names]
number_lists = len(names)

play = random.randint(0,number_lists-1)

person = names[play]

print(person + " is going to pay the bill")

print(play)