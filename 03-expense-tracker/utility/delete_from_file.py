import csv


def delete_from_file(path, index):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)  # list of dictionaries
        fieldnames = reader.fieldnames

    # delete the selected row
    del rows[index]

    # rewrite file
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()  # writes provided fieldnames as a header
        writer.writerows(rows)
