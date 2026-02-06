import csv
from utility.modify_expense import modify_expense


def modify_from_file(path, index):
    # read file
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    # update a row
    rows[index] = modify_expense(index)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # writes provided fieldnames as a header
        writer.writerows(rows)
