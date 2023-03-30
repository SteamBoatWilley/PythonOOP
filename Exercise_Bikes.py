# Make a program that runs continuously
# Program will consist of Bicycles 
# Program will allow you to choose how many wheels you have on your bicycle and the brand to choose from

class Bicycles():
    TerrainType = "Road" # The most popular type of terrain to ride your bike one

class MountainBike(Bicycles):  # Subclass type of Bicycles
    def __init__(self): # Allowing the function to be ran
        self.__numberOfWheels = 2 # number of wheels a bicycle has
        self.__numberOfPedals = 2 # number of pedals a bicycle has
        self.__mostPopularBrand = "Specialized"
        self.__secondMostPopularBrand = "Trek"

    def checkWheels(self):
        print("Your mountain bike has {} wheels ".format(self.__numberOfWheels))

    def checkPedals(self):
        print("Your mountain bike has {} pedals ".format(self.__numberOfPedals))

    def BikeType(self, brand):
        self.brandtype = brand
        print("{} is your favotire type of mountain bike, while {} is the most popular bike brand out there followed by {}".format(self.brandtype, self.__mostPopularBrand, self.__secondMostPopularBrand))

    def WheelChoice(self):
        if self.__numberOfWheels > 0:
            self.__numberOfWheels = self.__numberOfWheels +- 1 # need to fix this so that when they select 3 they are able to either choose to add or subtract a Wheel
            print("Your bike has {} wheels".format(self.__numberOfWheels))
        else:
            print("Your bike has no wheels!")

    def PedalChoice(self):
        if self.__numberOfPedals > 0:
            self.__numberOfPedals = self.__numberOfPedals +- 1 # need to fix this so that when they select 4 they are able to either choose to add or subtract a Pedal
            print("Your bike has {} pedals".format(self.__numberOfPedals))
        else:
            print("Your bike has no pedals!")
        


bike = MountainBike()

while True:
    print("1: Pick your favorite Mountain Bike Brand")
    print("2: Check how many wheels/pedals your bike has")
    print("3: Add or get rid of a wheel")
    print("4: Add or get rid of a pedal")
    print("5: Exit")
    choice = int(input())
    if choice == 1:
        print("What is your favorite Mountain Bike brand out there?")
        bike.BikeType(input())
    elif choice == 2:
        bike.checkWheels()
        bike.checkPedals()
    elif choice == 3:
        bike.WheelChoice()
    elif choice == 4:
        bike.PedalChoice()
    elif choice == 5:
        exit()
    else:
        print("Pick a value shown above of 1 through 5 so this program runs properly!")





