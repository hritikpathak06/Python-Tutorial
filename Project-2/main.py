# Guess The Number
import random
num = random.choice(range(1,10))

print(num)
user_input = int(input("Enter the number: "))


if(user_input == num):
    print("You Won the match")
elif(user_input > num):
    print("Please choose the small number")
else:
    print("Please choose the larger number")