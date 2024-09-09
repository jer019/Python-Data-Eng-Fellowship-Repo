# Write a test class for the Car class above.  You are required to do the followings:
# a.	Create an object of type Car.
# b.	Assign any valid values to the instance variables of the object created in ‘A’.
# c.	Use the method getPriceAfterUse on the object created in ‘A’ then output the result to the screen.
# d.	Use the method updateMilage on the object created in ‘A’ by passing a valid value.
# e.	Do part ‘C’ again.
# f.	Use the method outputDetails on the object created in ‘A’.




class Car:
    def __init__(self, brandName, priceNew, color, odometer):
        self.brandName = brandName
        self.priceNew = priceNew
        self.color = color
        self.odometer = odometer

    def getPriceAfterUse(self):
        return self.priceNew * (1 - (self.odometer / 6000000))

    def updateMilage(self, traveledDistance):
        self.odometer += traveledDistance

    def outputDetails(self):
        print(f"Brand Name: {self.brandName}")
        print(f"Price New: {self.priceNew}")
        print(f"Price Used: {self.getPriceAfterUse()}")
        print(f"Color: {self.color}")
        print(f"Odometer: {self.odometer}")

car = Car("Toyota", 20000, "Red", 50000)
print(f"Price After Use: {car.getPriceAfterUse()}")
car.updateMilage(10000)
car.outputDetails()
car.outputDetails()
