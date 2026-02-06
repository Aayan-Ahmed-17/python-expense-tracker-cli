def modify_expense(index):
    """
    PURPOSE: modifies / updates an expense in memory only
    CALL: gets called when user wants to update an expense present in_memory only
    """
    e_name = input("Enter updated name here: ").strip()
    e_amount = input("Enter updated amount here: ").strip()
    e_category = input("Enter updated category here: ").strip()

    # that index would modified like this:
    index = {"name": e_name, "amount": e_amount, "category": e_category}
    return index
