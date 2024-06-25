# Print largest number among 4 numbers entered by the user

n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
n4=int(input("Enter number 4: "))

if(n1>n2 and n1>n3 and n1>n4):
    print("Largest number is n1: ",n1)

elif(n2>n1 and n2>n3 and n2>n4):
    print("Largest number is n2: ",n2)

elif(n3>n1 and n3>n2 and n3>n4):
    print("Largest number is n3: ",n3)

else:
    print("Largest number is n1: ",n4)