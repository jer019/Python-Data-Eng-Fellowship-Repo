# Module that will give us the next power of 2 in each iteration. Power exponent starts from zero up to a user set number,

class PowTwo:

    def __init__(self,max):
        self.max=max
        

    def __iter__(self):
        self.current=0
        return self
    
    def __next__(self):

        if(self.current <= self.max):
            result= 2 ** self.current
            self.current += 1
            return result
          
        
        else:
             raise StopIteration 

numb=int(input("Enter a number to find squares upto it: "))

print("Squares of number upto given number:")

power=PowTwo(numb)

for i in power:
    print(i)