# Function to print * from n ties to 1

def pattern(n):
    if (n == 0):
        return 
    print("*" * n)
    pattern(n-1)

pattern(5)

