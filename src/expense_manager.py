import csv
from datetime import datetime


def load_transactions():
    with open('data/transactions.csv', 'r') as f:
        reader = csv.DictReader(f)

        transactions = []
        for r in reader:
            r["transaction_id"] = int(r["transaction_id"])
            r["amount"] = float(r["amount"])
            transactions.append(r)
        return transactions
    

def add_expense(transactions, date, category, description, amount, payment_method):
    ids = []
    for t in transactions:
        ids.append(t["transaction_id"])
    transaction_id = max(ids) + 1
    new_transaction = {
        "transaction_id" : transaction_id,
        "date" : date,
        "category" : category,
        "description" : description,
        "amount" : amount,
        "payment_method" : payment_method
    }
    transactions.append(new_transaction)
    save_transactions(transactions)
    print()
    print("New expense added.")
    print()
    


def save_transactions(transactions):
    headers = ['transaction_id', 'date', 'category', 'description', 'amount', 'payment_method']
    with open('data/transactions.csv', 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(transactions)

def view_transactions(transactions):
    print(f"transaction_id | date | category | description | amount | payment_method")
    for t in transactions:
        print(f"{t['transaction_id']} | {t['date']} | {t['category']} | {t['description']} | {t['amount']} | {t['payment_method']}")
        print()

def delete_expense(transactions, transaction_id):
    found = False
    
    for t in transactions:
        if t["transaction_id"] == transaction_id:
            transactions.remove(t)
            print()
            print(f"Transaction with id {transaction_id} has been removed.")
            print()
            found = True
            save_transactions(transactions)
            break
    if not found:
        print("No such id exists!!")
        print()

def update_expense(transactions, transaction_id):
    found = False
    for t in transactions:
        if t["transaction_id"] == transaction_id:
            while True:
                print()
                print("What do you want to update?")
                print()
                print(" 1. Date\n 2. Category\n 3. Description\n 4. Amount\n 5. Payment Method\n 6. Done\n")
                print()
                choice = get_integer_input("Enter your choice :")
                print()

                if choice == 1:
                    new_date = get_date_input("Enter new Date :")
                    t["date"] = new_date
                elif choice == 2:
                    new_category = get_category_input("Enter new Category :")
                    t["category"] = new_category
                elif choice == 3:
                    new_description = input("Enter new Description :")
                    t["description"] = new_description
                elif choice == 4:
                    new_amount = get_float_input("Enter new Amount :")
                    t["amount"] = new_amount
                elif choice == 5:
                    new_payment_method = input("Enter new payment_method :")
                    t["payment_method"] = new_payment_method
                elif choice == 6:
                    break
                else:
                    print("Invalid choice!!")
                
            found = True
            save_transactions(transactions)
            break

    if not found:
        print("No such id exists!!")

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number!!")
            continue
        return value

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Not a valid amount!!")
                continue
        except ValueError:
            print("Invalid input! Please enter a number!!")
            continue
        return value

def get_date_input(prompt):
    while True:
        try:
            date = datetime.strptime(input(prompt), "%Y-%m-%d")
        except ValueError:
            print("Invalid date!!")
            continue
        return date.strftime("%Y-%m-%d")


def get_category_input(prompt):
    while True:
        category = input(prompt).strip()
        if category == "":
            print("Enter a valid category!!")
            continue
        return category