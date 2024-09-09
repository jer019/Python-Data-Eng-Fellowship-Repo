import random

"""
Rules:
1 for snake
-1 for water
0 for gun
"""

computer=random.choice([1,-1,0])

yourstr=input("Enter your choice: ")
yourDict={'s':1,'w':-1,'g':0}
reverseDict={1:'Snake',-1:'Water',0:'Gun'}

you=yourDict[yourstr]

print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")


if(you == computer):
    print("It's a draw!")
else:
    if(you == 1 and computer == -1):
        print("You won!")
    
    elif(you == 1 and computer == 0):
        print("Computer won!")

    elif(you == 0 and computer == 1):
        print("You won!")

    elif(you == 0 and computer == -1):
        print("Computer won!")

    elif(you == -1 and computer == 0):
        print("You won!")
        
    elif(you == -1 and computer == 1):
        print("Computer won!")

    else:
        print("Something went wrong")
    
