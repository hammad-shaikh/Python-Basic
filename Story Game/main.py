
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


input("Where would you like to go "Left" or "Right"")

if input == "Left".lower():
  print("Good! How do you go?")
  if input("What do you want to do Swim or Wait?") == "Wait":
    print("Now you got there doors, which one would you like to choose")
  if input("Which door") == "Yellow":
    print("You Win")
  else:
    print("Game over")
else:
  print("Game Over")   
            
  
  #if step_2 == "Wait" or step_2.lower() == "wait":
   # print("Wow, now you got two doors, which one do you get?")
  

