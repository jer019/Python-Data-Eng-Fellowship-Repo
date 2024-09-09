# Problem:
# Write a Python function is_leap_year that takes an integer year as input and returns True if the year is a leap year, and False otherwise. A year is a leap year if it is:

# 1. Divisible by 4, and
# 2. Not divisible by 100, unless
# 3. It is also divisible by 400.3

def leap_year(year):

    if(year%4 == 0 and year%100 != 0):
        print(year," is a leap year")
    else:
        print(year," is not a leap year")

y=int(input("Enter year to check if it's leap or not: "))

leap_year(y)
