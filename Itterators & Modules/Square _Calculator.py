# A module that has iterator in it that calculates the square of numbers from 1 till 20. 
# Name this module as square_calculator.py import it in new file and apply.

class SquareCalculator:
    def __init__(self,limit=20):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.current > self.limit):
            raise StopIteration
        
        else:
            square= self.current * self.current
            self.current+=1
            return square
        

square= SquareCalculator()

for i in square:
    print(i)