
import os
from dotenv import load_dotenv
from context import context
from validations import  validate_amount, validate_account_number
from agents import deposit_agent, withdraw_agent, check_balance_agent

load_dotenv()

def main():
    print("===Welcome to the Bank Agent System===")
    context["user_name"] = input("Enter your name:  ")

    while True:
        acc_num = input("Enter your account number:  ")

        if validate_account_number(acc_num):
            context["account_number"] = acc_num
            break

        else:
            print("Invalid account number. Please try again.")

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = input("Enter amount to deposit:  ")
             
            if validate_amount(amount):
                print(deposit_agent(int(amount)))

            else:
                print("❌ Invalid amount. Please enter a valid number.")

        elif choice == "2":
            amount = input("Enter withdraw amount: ")
            if validate_amount(amount):
                print(withdraw_agent(int(amount)))

            else:
                print("❌ Invalid amount. Please enter a valid number.")
        
        elif choice == "3":
            print(check_balance_agent())

        elif choice == "4":
            print("Thank you for using the Bank Agent System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()