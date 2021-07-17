from art import logo
from art import vs
import random
from game_data import data

print(logo)

a_account = random.choice(data)

print(a_account)


# dictu = [{
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'},
#            {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     }]
next_ques_a = 0
next_ques_b = 1

new_ques_a = 0
new_ques_b = 0

# for value in my_dict[0]:
# #     print(key
#     print(value)
# #     print(my_dict[0])

game = True

def question():
    
    
    
    
        
#     ques = 9
    next_ques_a
    next_ques_b
    new_ques_a
    new_ques_b
    game
    
    A_ques = print(f"Compare A: {data[next_ques_a].get('name')} , a {data[next_ques_a].get('description')} , from {data[next_ques_a].get('country')}")
    count_a = data[next_ques_a].get("follower_count")
    print(count_a)

    print(vs)

    B_ques = print(f"Compare B: {data[next_ques_b].get('name')} , a {data[next_ques_b].get('description')} , from {data[next_ques_b].get('country')}")

    count_b = data[next_ques_b].get("follower_count")
    print(count_b)




    def scoring():
        choice = input("Who has more followers? Type 'A' or 'B':")
        
        global next_ques_a
        global next_ques_b
        global New_ques_a
        global new_ques_b
        global game
        if choice == "A":
            if count_a > count_b:
                print("NEXT")
                new_ques_b = next_ques_b + 1
                next_ques_b = new_ques_b
            elif count_a < count_b:
                print("Lose")
            elif count_a == count_b:
                print("Draw")
                new_ques_b = next_ques_b + 1
                next_ques_b = new_ques_b
#                     continue_game == False
        elif choice == "B":
            if count_b > count_a:
                print("NEXT")
                new_ques_a = next_ques_a + 1
                next_ques_a = new_ques_a
#                 new_ques_b = next_ques_b + 1
#                 next_ques_b = new_ques_b
                print(new_ques_b)
#                     continue_game == True
            elif count_b < count_a:
                print("Lose")
            elif count_b == count_a:
                print("Draw")
                new_ques_b = next_ques_b + 1
                next_ques_b = new_ques_b
    scoring()
    
    # Next Question Logic
    

    #     print(ques)
        


while game:
    question()

# checking the most followers:
# if choice == "A":
#     ques = 5
# else:
#     print("You Lose")
# 
# print(ques)
    
# if A_count > B_count or A_count < B_count:
#     print("Next")
# else:
#     print("You Loose")
