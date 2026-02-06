from feats.show_expenses import show_expenses
from feats.add_expense import add_expense
from utility.modify_expense import modify_expense
from utility.modify_from_file import modify_from_file


def update_expense(expenses, path):
    shown_expenses = show_expenses(expenses=expenses, path=path)
    total_length = len(shown_expenses)
    expenses_length = len(expenses)
    file_count = total_length - expenses_length

    if not show_expenses:
        print("There is no expense to show")

    while True:
        user_input = input("Enter number to update: ")

        if not user_input.isdigit():
            print("Invalid input")
            continue

        index = int(user_input) - 1

        # check is user_input in range?
        if index < 0 or index >= total_length:
            print("Index does not exist")
            continue

        # is expense in_file or in_memory
        if index >= file_count:
            print("in memory")
            expenses[index - file_count] = modify_expense(index)
        else:
            print("in file")
            modify_from_file(path=path, index=index)

        break
