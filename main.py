
import json
from bank_account import BankAccount


file_name = "accounts.json"

# Load all accounts if the file exists
try:
    with open(file_name, "r") as file:
        all_accounts = json.load(file)
except FileNotFoundError:
    all_accounts = {}

print("Welcome to Simple Bank System 🏦")

# User login or create new account
name = input("Enter your name: ").strip()

# Validate name
while not name.replace(" ", "").isalpha() or len(name) <= 2:
    print("Name must contain only letters and be longer than 2 characters 🔄")
    name = input("Enter your name: ").strip()

if name in all_accounts:
    balance = all_accounts[name]["balance"]
    print(f"Welcome back {name}! Your balance: {balance} 💵")
else:
    balance_input = input("Enter initial balance (or press Enter for 0): ").strip()
    balance = float(balance_input) if balance_input else 0
    print(f"Account created for {name} with balance {balance} ✅")

# Create BankAccount object
account = BankAccount(name, balance)

# Add user to dictionary if not already present
if account.get_account_holder() not in all_accounts:
    all_accounts[account.get_account_holder()] = {}

all_accounts[account.get_account_holder()]["balance"] = account.get_balance()

# Save data after account creation
with open(file_name, "w") as file:
    json.dump(all_accounts, file, indent=4)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check balance\n4. Exit")
    choice = input("Choose: ").strip()

    user = account.get_account_holder()

   # Deposit
    if choice == "1":
        amount = float(input("Deposit amount: "))
        account.deposit(amount)
        print(f"Deposit successful! New balance: {account.get_balance()} 💵")
    
    # Withdraw
    elif choice == "2":
        amount = float(input("Withdraw amount: "))
        try:
            account.withdraw(amount)
            print(f"Withdrawal successful! ✅ New balance: {account.get_balance()} 💸")
        except Exception as e:
            print(f"Error: {e} ")
    
    # Check balance
    elif choice == "3":
        print(f"Current balance: {account.get_balance()} 📊")

    # Exit
    elif choice == "4":
        print(f"Thank you, {account.get_account_holder()}! Final Balance: {account.get_balance()} 👋")
        break
# Invalid choice
    else:
        print("Invalid choice, please try again 🔄")

    # تحديث الرصيد في JSON بعد كل عملية
    if user not in all_accounts:
        all_accounts[user] = {}
    all_accounts[user]["balance"] = account.get_balance()

    with open(file_name, "w") as file:
        json.dump(all_accounts, file, indent=4)
