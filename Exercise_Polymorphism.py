class Square:
    def __init__(self, side): # Make the function run with the __init__ function with self/side 
        self.side = side

    # Overload the exponent operator with the "__pow__() function"
    def __pow__(squareOne, squareTwo):
        # Return side of square one to the power of square two
        return squareOne.side ** squareTwo.side
    
    
squareOne = Square(4) # Each side is 4" in length
squareTwo = Square(6) # Each side is 6" in length
# Print the statement of square one to the power of square two - have to add the function at the end of the statement
print("Using the sides of the squares as an exponent of one another, SquareOne to the power of SquareTwo is ", squareOne ** squareTwo)

