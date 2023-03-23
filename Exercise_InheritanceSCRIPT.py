class Furniture: # Furniture is the template
    materials = "Teakwood" #Attribute of the furniture

    def furnitureDetails(self):
        print("Most furniture is made out of ", self.materials)

class Chair(Furniture): # Derivative of the template(Child Class)
    def __init__(self): # initialize will run this function
        print("What type of wood would you like your chair to be made out of?")
        self.WoodType = input() # Attribute of the chair
        __Legs = 4 # Attributre of the chair that is private so it cannot be altered outside of class
        print("Although most furniture is made out of Teakwood, in this example, the chair is a piece of furniture that is made out of {} and has {} legs.".format(self.WoodType, __Legs))



furniture = Furniture()
furniture.furnitureDetails() 
chair = Chair() #



