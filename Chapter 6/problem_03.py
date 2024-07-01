# write a program that detects spam keywords in comments

p1="make alot of money"
p2="subscribe this"
p3="buy now"
p4="click this"

comment=input("Enter the comment: ")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("It is a spam comment/message!")

else:
    print("Message/Comment is not spam!")
