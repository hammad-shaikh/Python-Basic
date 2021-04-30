
even_number = 0

for even in range (1, 101):
    if even % 2 == 0:
        even_number += even
print(f"Result using approach 1: {even_number}")


even_number2 = 0
for even in range (2,101,2):
    even_number2 += even
print(f"Result using approach 2: {even_number2}")
    

    