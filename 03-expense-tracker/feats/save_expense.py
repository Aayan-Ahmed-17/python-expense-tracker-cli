import csv


def save_expense(expenses, path):
    """
    Takes expenses list of current main file section and save into .csv file
    Return: return success and failure message
    """

    if not expenses:
        print("Please insert data first then save into a file")
        return

    with open(path, "a", newline="", encoding="utf-8") as adcsv:
        csv_writer = csv.DictWriter(adcsv, fieldnames=["name", "amount", "category"])

        # if cursor on firstLine then only print the fieldname else no
        if adcsv.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerows(expenses)
