import random # use the import function to import the random function so i can have a random number generated


class Bank: # Creating a savings account in a bank 
    def __init__(self): # Making the function run
        self.accounts = [] # Array representing all of the accounts

        print("Would you like to acces a current savings account or create a new one?")
    
    def createSavingsAccount(self): # New user - making an account for them
        self.accountNumber = random.randint(10000, 99999) # have the account number equal to the random function but add randint with the values i want the random value to be produced between
        print("Our system has successfully created an account number for you of {}, please use this when signing in!".format(self.accountNumber)) # Print the new account number that will be assigned as their savings account
        print("Please enter your name so that we can attach your name to your account number") # Have their account number equal to their name
        self.userName = input()
        print("Thank you {}, you have now successfully created your bank account, the only thing left is to deposit money into your account! So how much would you like to deposit?".format(self.userName))
        self.initialDeposit = int(input())
        print("Congratulations {}, your account is now fully functional with ${} in your account that you can access at anytime!".format(self.userName, self.initialDeposit))


    def accessSavingsAccount(self):  # Exisitng user - trying to access their account
        print("Please enter your Name.")
        name = input()
        print("Please enter your Account Number.")
        accNum = input()
        for account in self.accounts:           # Dealing with the array of all account numnbers in the system
            if accNum == account.accountNumber and name == account.accountName:
                
            

                                         


