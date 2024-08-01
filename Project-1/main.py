import random
# Snake Water And Gun
# 1-> Snake
# -1->Water
# 0=>Gun

random_choices = [-1,1,0]

computer = random.choice(random_choices);

print("Computer Random Choice: ",computer)

you_str = input("Enter Your Choice: ")

your_dictionary = {
    "s":1,
    "w":-1,
    "g":0
}

you = your_dictionary[you_str]

print(you)

if(computer == you):
    print("Match Draw")

else:
  if(computer == -1 and you == 1):
    print("You win !")
  elif(computer == -1 and you == 0):
    print("You Lose")
  elif(computer == 1 and you == -1):
    print("You Lose")
  elif(computer == -1 and you == 0):
    print("You Win")
  elif(computer == 0 and you == -1):
    print("You Lose")
  else:
    print("Something went wrong")