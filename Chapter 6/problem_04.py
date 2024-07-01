# write a program to find whether the given username contains less than 10 characters or not

u=input("Enter your username: ")

len=len(u)

if(len <= 10 and len >1 ):
    print("username is good to go")

elif(len>10):
    print("username is lengthy, make it under 10")

else:
    print("No username entered!")

