# ============================== Expense Tracker App Excel File Data Store ==========================================
"""
Add new expenses (name, amount, category)
Save all entries to a '.csv' file (UTF-8 encoded)
Display total expenses for the current month
Calculate how much budget remains
Show daily spending limit for the remaining days
Display a category-wise expense summary
View a full table of past entries in a neat layout
Feedback system to improve app experience
"""
# ========================================================================
from feats.add_expense import add_expense
from feats.show_expenses import show_expenses
from feats.save_expense import save_expense
from feats.delete_expense import delete_expense
from feats.update_expense import update_expense
import os


def main():
    "Contains logic and flow of whole app"
    expenses = [{"name": "dfjs", "amount": "dkjfh", "category": "djkfh"}]
    folder = "data"
    filename = "expenses.csv"
    path = os.path.join(folder, filename)

    os.makedirs(folder, exist_ok=True) # create directory if not exist

    print("*" * 30, "Welcome user", "*" * 30)
    print("Below are no of action you can perform.")

    feats = [
        "Add Expense",
        "Show All Expense",
        "Delete Expense",
        "Update All Expense",
        "Save Expenses in file",
        "Exit",
    ]  # all feature to show
    for i, feat in enumerate(feats):
        print(i + 1, feat)

    input_action = input("Type number corresponded to action: ").strip()

    # ? Check the conditions for valid user input_action value here later......

    match input_action:
        case "1":
            add_expense(expenses)
        case "2":
            show_expenses(expenses, path=path)
        case "3":
            delete_expense(expenses, path=path)
        case "4":
            update_expense(expenses, path=path)
        case "5":
            save_expense(expenses, path=path)
        # case 2:
        #     comment:
    # end match


main()
