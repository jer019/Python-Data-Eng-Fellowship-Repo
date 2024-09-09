# Function to add first n natural numbers using recursion

def Sum(n):
    if(n == 1):
        return 1
    else:
        return n + Sum(n-1)


n=int(input("Enter a natural number: "))
print(f"Sum of upto natural number provided is: {Sum(n)}")