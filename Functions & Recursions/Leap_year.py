# A function to find if a given year is a leap year or not

def leapyear(year):
    if (year % 4 == 0):
        if(year % 400 == 0):
            return "is a leap year"
        else:
            return "is not a leap year"
        
    return "is not a leap year"

year=int(input("Entar a year to find if it'd leap year or not: "))

print(f"Year {year} {leapyear(year)}")
