# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
# 🚨 Don't change the code above 👆


#Write your code below this row
# student = int(student_heights)
# student = int(student_heights)
total = 0

for height in student_heights:
    total += height
print(total)

number = 0

for numb in student_heights:
    number += 1
    
print(number)

average = round(total/number)

print(average)
    

    
    