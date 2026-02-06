# FLOW: show all expense with numbering, ask user input to delete nth number of dict of a list, match number, delete from expenses list.
from feats.show_expenses import show_expenses
from feats.save_expense import save_expense
from utility.delete_from_file import delete_from_file

def delete_expense(expenses, path):
    shown_expenses = show_expenses(expenses, path)
    total_length = len(shown_expenses)
    expenses_length = len(expenses)
    file_count = total_length - expenses_length

    if not shown_expenses:
        return

    while True:
        user_input = input("Enter number to delete: ")

        if not user_input.isdigit():
            print("Invalid input")
            continue

        index = int(user_input) - 1

        if index < 0 or index >= total_length:
            print("Index does not exist")
            continue

        # check where is expense in_file or in_memory?
        if index >= file_count:
            print("in memory")
            del expenses[index - file_count]
            print(expenses)
        else:
            delete_from_file(path, index)         
                    
        break
