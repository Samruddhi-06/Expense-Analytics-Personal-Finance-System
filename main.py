from src.expense_manager import *

transactions = load_transactions()

while True:
    print("================================")
    print("EXPENSE MANAGER")
    print("================================")
    print()

    print(" 1. Add Expense\n 2. View Expense\n 3. Update Expense\n 4. Delete Expense\n 5. Exit")
    print()
    
    choice = get_integer_input("Enter your choice :")
    print()

    if choice == 1:
        date = get_date_input("Enter Date :")
        category = get_category_input("Enter Category :")
        description = input("Enter Description :")
        amount = get_float_input("Enter Amount :")
        payment_method = input("Enter Payment Method :")
        add_expense(transactions, date, category, description, amount, payment_method)

    elif choice == 2:
        view_transactions(transactions)

    elif choice == 3:
        transaction_id = get_integer_input("Enter transaction id :")
        update_expense(transactions, transaction_id)

    elif choice == 4:
        transaction_id = get_integer_input("Enter transaction id :")
        delete_expense(transactions, transaction_id)

    elif choice == 5:
        break

    else:
        print("Invalid choice!")