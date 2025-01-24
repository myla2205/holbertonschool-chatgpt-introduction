#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program. Have a nice day!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
