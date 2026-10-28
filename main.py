from bank_account import BankAccount


# Ask for a dollar amount until the customer types a valid positive number
def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt + "\n"))
            if amount > 0 and amount < 1000000000:
                return round(amount, 2)          # keep whole cents only
            print("Please enter an amount greater than $0.00.")
        except ValueError:
            print("Please enter a number, like 25 or 19.99.")


# Option 1: deposit money into the account
def make_deposit(account):
    amount = get_amount("How much would you like to deposit?")
    account.deposit(amount)
    print(f"Deposited ${amount:,.2f}. New balance: ${account.balance:,.2f}")


# Option 2: withdraw money, refusing if it's more than the balance
def make_withdrawal(account):
    amount = get_amount("How much would you like to withdraw?")
    if account.withdraw(amount):
        print(f"Withdrew ${amount:,.2f}. New balance: ${account.balance:,.2f}")
    else:
        print(f"Insufficient funds. Your balance is only ${account.balance:,.2f}.")


# Option 3: show name, account number and balance
def view_account(account):
    print(account.get_info())


# Print the menu options
def show_menu():
    print("\nPlease choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")


# Main program
print("Welcome to Abe's Bank!")
customer_name = input("Please enter your name:\n").strip()
while customer_name == "":                      
    customer_name = input("Name cannot be blank. Please enter your name:\n").strip()
customer_account = BankAccount(customer_name)

choice = ""
while choice != "4":
    show_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        make_deposit(customer_account)
    elif choice == "2":
        make_withdrawal(customer_account)
    elif choice == "3":
        view_account(customer_account)
    elif choice != "4":
        print("Invalid choice. Please try again.")

print("Thank you for your business!")
