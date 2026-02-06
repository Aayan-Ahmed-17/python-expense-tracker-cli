import csv

def show_expenses(expenses, path):
    output = []

    # 1️⃣ Read from CSV file
    try:
        with open(path, "r", encoding="utf-8") as rcsv:
            reader = csv.DictReader(rcsv)
            for row in reader:
                output.append(row)
    except FileNotFoundError:
        pass

    # 2️⃣ Add in-memory expenses
    if expenses:
        output.extend(expenses)

    # 3️⃣ No data
    if not output:
        print("No expense data found")
        return []

    # 4️⃣ Show with index (IMPORTANT)
    for i, expense in enumerate(output, start=1):
        print(f"{i}. {expense}")

    # 5️⃣ Return the SAME list that was shown
    return output
