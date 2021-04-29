# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

T1 = lower_name1.count("t")
R1 = lower_name1.count("r")
U1 = lower_name1.count("u")
E1 = lower_name1.count("e")

True1 = T1 + R1 + U1 + E1

L2 = lower_name1.count("l")
O2 = lower_name1.count("o")
V2 = lower_name1.count("v")
E2 = lower_name1.count("e")

Love1 = L2 + O2 + V2 + E2

print(True1 + Love1)

T2 = lower_name2.count("t")
R2 = lower_name2.count("r")
U2 = lower_name2.count("u")
E2 = lower_name2.count("e")

True2 = T2 + R2 + U2 + E2

L3 = lower_name2.count("l")
O3 = lower_name2.count("o")
V3 = lower_name2.count("v")
E3 = lower_name2.count("e")

Love3 = L3 + O3 + V3 + E3

print(True2 + Love3)


