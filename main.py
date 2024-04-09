from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu, MenuItem
coffemaker=CoffeeMaker()
moneymachine=MoneyMachine()
menu1=Menu()
choose="on"
while(choose!="off"):
   choose=input("What would you like? (espresso/latte/cappuccino)\n")
   if (choose == "report"):
       coffemaker.report()
       moneymachine.report()
   if(coffemaker.is_resource_sufficient(choose)):
       drink=menu1.find_drink(choose)
       if(moneymachine.make_payment(drink.cost)):
           moneymachine.profit+=drink.cost
           print(f"money received: {moneymachine.money_received}$")
           coffemaker.make_coffee(drink)
