class RentalCar: # Class is the big template
    def __init__(self, Cars):
        self.CarInventory = Cars # enterprise from below is the instance of this template or Avis (Each are a different version of the template)
        print(self.CarInventory) # Self.CarInventory is an attribute because that is just some data that instance has 

    def VehicleChoice(self): # A method is a function of an instance (Does something) 
        for car in self.CarInventory:
            print(car)
        print("Which vehicle would you like to rent?")
        UserChoice = input()
        if UserChoice in self.CarInventory:
            print("Great choice!")
            self.Fare(UserChoice) # Passing this data to the Fare funcation
        else:
            print("Sorry fuckhead, try again!")
            self.VehicleChoice() # Loops back and resets to the start of the function

    def Fare(self, SelectedCar): # Passing UserChoice as a parameter to the Fare Funcation
        print("How many days would you like the vehicle for?")
        NumberOfDays = int(input())
        if int(NumberOfDays) >0:
            print("Perfect, your total for {} days is going to be ".format(NumberOfDays), self.CarInventory[SelectedCar]*int(NumberOfDays))
        else:
            print("Pick a value greater than 0, fuckhead")
            self.Fare(SelectedCar) # Passing this data to the Fare funcation (Looping it back up)



         


EnterpriseAvailableCars = {"Hatchback": 30, "Sedan": 50, "SUV": 100}
Enterprise = RentalCar(EnterpriseAvailableCars) # Enterprise is taking the place of self (Spinning of an instance of the RentalCar class)
Enterprise.VehicleChoice() # Telling the Enterprise instance to do the method VehicleChoice 

AvisAvailableCars = {"Hatchback": 25, "Sedan": 40, "SUV": 85, "Premium": 120}
Avis = RentalCar(AvisAvailableCars) # AvisAvailableCars is the "Cars" parameter in the () to initialize the CarInventory attribute from the def __init__ piece above
Avis.VehicleChoice()










# A Class is like a template (a blank one)
# The one i put my name on is the instance of that template (aka instance (Kevin = memebership info)
# Self is where you want to take that instance and find more info on that instance