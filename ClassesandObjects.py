# Check if an employee has achieved his weekly target or not

class Employee:
    name = "Ben"
    designation = "Sales Executive"
    SalesMadeThisWeek = 6
    def HasAchievedTarget(self):
        if self.SalesMadeThisWeek >= 5:
            print("Target has been achieved!")
        else:
            print("Target has not been achieved")

