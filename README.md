# Coffee Machine Program

This Python program simulates a coffee machine with the following features:

1. **Prompt user for drink selection**: Users are prompted to select a drink (espresso/latte/cappuccino). The prompt appears after each completed action to serve the next customer.

2. **Turn off the Coffee Machine**: Users and maintainers can turn off the machine by entering "off" as the input. The program ends execution when this happens.

3. **Print Report**: Users can request a report of the current resource values by entering "report" as the input. The report includes the current levels of water, milk, coffee, and money.

4. **Check Resources**: The program checks if there are sufficient resources to make the selected drink. If any resource is depleted, it prints a message indicating the shortage.

5. **Process Coins**: If there are sufficient resources, the program prompts the user to insert coins and calculates the monetary value of the coins inserted.

6. **Check Transaction**: The program checks if the user has inserted enough money to purchase the selected drink. It also handles cases where the user has inserted too much money, offering change if necessary.

7. **Make Coffee**: If the transaction is successful and there are enough resources, the program deducts the ingredients required to make the drink and informs the user that their drink is ready.

## Instructions for Running the Program

1. Clone the repository to your local machine:

git clone https://github.com/ShoshiBnayahu/Python-CoffeeMachine.git

2. Navigate to the project directory:

cd Python-CoffeeMachine


3. Run the program:

python main.py


4. Follow the prompts to interact with the coffee machine.

## Additional Notes

- This program is written in Python and follows the requirements specified in the Coffee Machine Program Requirements.

- The program is designed to be user-friendly and provides clear prompts and messages for better user interaction.

- Resource management and transaction handling are implemented to ensure smooth operation of the coffee machine.

- The code is well-documented and organized for readability and maintainability.

Feel free to explore the code and modify it as needed for your specific use case or requirements. If you encounter any issues or have any questions, please don't hesitate to contact me. Enjoy your coffee!
