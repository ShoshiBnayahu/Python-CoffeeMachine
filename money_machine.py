class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
         "quarters": 0.25,
         "dimes": 0.10,
         "nickles": 0.05,
         "pennies": 0.01
        
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print (f"money:{self.profit}$")


    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("insert coins:")
        quarters = float(input("insert quarters\n"))
        dimes = float(input("insert dimes\n"))
        nickles = float(input("insert nickles\n"))
        pennies = float(input("insert pennies"))
        totalSum = (quarters * self.COIN_VALUES['quarters'] + dimes * self.COIN_VALUES['dimes']
               + nickles * self.COIN_VALUES['nickles'] + pennies * self.COIN_VALUES['pennies'])
        return totalSum

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        print(f"payment: {cost}")
        pay=self.process_coins()
        if(pay>=cost):
            if(pay>=cost):
                self.money_received=(float)(pay-cost)
            return True
        print(f"Sorry there is not enough coins,good bye.")
        return False