def add_expense(expenses):
    """
    Creates expense instance collect details by user input
    Puts expense instance in expenses list
    """
    e_name = input("Enter expense name here: ").strip()
    e_amount = input("Enter expense amount here: ").strip()
    e_category = input("Enter expense category here: ").strip()

    # check input validation here later.................

    expense = {"name": e_name, "amount": e_amount, "category": e_category}
    expenses.append(expense)
