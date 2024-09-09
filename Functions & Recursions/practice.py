#  Recursive function to find factorial of a given number
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    

# n=int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")


# Function to find greatest of 3 numbers

def greatest(a,b,c):
    
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a=19
b=44
c=10

# print(greatest(a,b,c))

    