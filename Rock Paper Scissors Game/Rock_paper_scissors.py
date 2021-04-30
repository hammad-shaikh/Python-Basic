import random
play = int(input("Welcome to 0 - Rock, 1 - paper and 2 - scissor game\n"))




# print(play)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
 '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



ascii_images = [rock, paper, scissors]
 

print(ascii_images[play])
# if play == 0:
#     print(rock)
# elif play == 1:
#     print(paper)
# elif play == 2:
#     print(scissors)
# else:
#     print("Enter correct Number")


#------------------------------------------------
comp = random.randint(0,2)

# if comp == 0:
#     print(rock)
# elif comp == 1:
#     print(paper)
# elif comp == 2:
#     print(scissors)

print(ascii_images[comp])

if play >= 0 and play <=2: 
#     print("Play it Right Man")


# Win or lose section --------------------------
if play == comp:
    print("Draw")

elif play == 0 and comp == 1:
    print("LOSE")
        
elif play == 0 and comp == 2:
    print("WIN")
    
elif play == 1 and comp == 0:
    print("WIN")
        
elif play == 1 and comp == 2:
    print("LOSE")
    
elif play == 2 and comp == 0:
    print("LOSE")
        
elif play == 2 and comp == 1:
    print("WIN")
else:
    print("Logic Failed")
# 
#     Rock wins against scissors.
#     Scissors win against paper.
#     Paper wins against rock.
#-----------------------------



#