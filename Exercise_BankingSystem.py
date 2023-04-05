import random # use the import function to import the random function so i can have a random number generated


class Bank: # Creating a savings account in a bank 
    def __init__(self): # Making the function run
        self.accounts = [] # Array representing all of the accounts

    def run(self):
        while True:
            print("Would you like to Login to a current savings account, Signup for a new one or Exit?")
            userInput = input()
            if userInput == "Login":
                self.accessSavingsAccount()
            elif userInput == "Signup":
                self.createSavingsAccount()
            elif userInput == "Exit":
                exit
            else:
                print("please type in either Login or Singup!")
    
    def createSavingsAccount(self): # New user - making an account for them
        accountNumber = random.randint(10000, 99999) # have the account number equal to the random function but add randint with the values i want the random value to be produced between
        print("Our system has successfully created an account number for you of {}, please use this when signing in!".format(accountNumber)) # Print the new account number that will be assigned as their savings account
        print("Please enter your name so that we can attach your name to your account number") # Have their account number equal to their name
        userName = input()
        print("Thank you {}, you have now successfully created your bank account, the only thing left is to deposit money into your account! So how much would you like to deposit?".format(userName))
        initialDeposit = int(input())
        print("Congratulations {}, your account is now fully functional with ${} in your account that you can access at anytime!".format(userName, initialDeposit))

        self.accounts.append({"accountNumber": accountNumber, "accountName": userName, "balance": initialDeposit})



    def accessSavingsAccount(self):  # Exisitng user - trying to access their account
        print("Please enter your Name.")
        name = input()
        print("Please enter your Account Number.")
        accNum = int(input())
        loggedIn = False
        for account in self.accounts:           # Dealing with the array of all account numnbers in the system
            if accNum == account["accountNumber"] and name == account["accountName"]:
                loggedIn = True
                while True:
                    print("Withdraw\nDeposit\nShow Balance\nExit")
                    userInput = input()
                    if userInput == "Withdraw":
                        self.handleWithdraw(account)
                    elif userInput == "Deposit":
                        self.handleDeposit(account)
                    elif userInput == "Show Balance":
                        self.handleBalance(account)
                    elif userInput == "Exit":
                        break
                    else:
                        print("Please enter one of three choices above!")
        if not loggedIn:
            print("The credentials you have entered do not match anything in our system, please try again!")
                        

    def handleWithdraw(self, acct):
        print("how much would you like to withdraw?")
        withdraw = float(input())
        if acct["balance"] - withdraw <0:
            print("You have insufficient funds for this withdraw, proceeding will result in an overdraft fee of $50, would you like to proceed, Yes or No?")
            userInput = input()
            if userInput == "Yes":
                withdraw += 50
            else:
                withdraw = 0
        acct["balance"] -= withdraw
        self.handleBalance(acct)    

    def handleDeposit(self, acct):
        print("How much would you like to Deposit?")
        userInput = float(input())
        acct["balance"] += userInput
        self.handleBalance(acct)

    def handleBalance(self, acct):
        print("Your current balance in your account is ${}".format(acct["balance"]))



bank = Bank()

bank.run()





            

                                         


