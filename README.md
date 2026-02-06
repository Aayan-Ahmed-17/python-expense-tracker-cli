# 🧾 CLI Expense Tracker (Python)

A modular **command-line based Expense Tracker** built using Python.  
This project allows users to manage daily expenses with full **CRUD operations**, while storing data persistently in a CSV file.

The application is designed with a clean folder structure, separating features, utilities, and data handling logic.

---

## 🚀 Features

- Add new expense records
- View all saved expenses
- Update existing expenses
- Delete expense entries
- Persistent data storage using CSV files
- Modular and readable code structure
- Input validation and basic error handling

---

## 🗂️ Project Structure

# Project Structure

This project follows a standard directory structure:

## Project Structure

This project follows a modular directory structure to keep features, utilities, and data handling separate and maintainable:

* `main.py`: Entry point of the application.
* `feats/`: Contains feature-specific modules.
  * `add_expense.py`: Handles adding new expense records.
  * `delete_expense.py`: Handles deletion of existing expenses.
  * `save_expense.py`: Manages saving expense data to file.
  * `show_expenses.py`: Displays all stored expenses.
  * `update_expense.py`: Handles updating expense records.
* `utility/`: Contains helper functions and file operation logic.
  * `delete_from_file.py`: Deletes records from the CSV file.
  * `modify_expense.py`: Updates expense data in memory.
  * `modify_from_file.py`: Updates records directly in the file.
* `data/`: Auto-generated directory for persistent data storage.
  * `expenses.csv`: Stores expense records (created at runtime).
* `README.md`: Project documentation.



---

## ⚠️ Important Note About `data/` Folder

- The `data/` folder and `expenses.csv` file are **automatically generated**
- They are created **only when the user saves an expense**
- This folder is **not included in the repository** intentionally
- The project works without this folder initially

This approach keeps the repository clean and avoids committing generated data.

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.x installed on your system

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-expense-tracker-cli.git
2. Navigate to the project directory:
      cd python-expense-tracker-cli
3. Run the application:
      python main.py
4. Follow on-screen instructions to manage expenses 

---

🛠️ Technologies Used
Python
CSV file handling
Command Line Interface (CLI)

---

📌 Learning Outcomes
Gained hands-on experience with Python modular programming
Implemented real-world CRUD functionality
Learned file handling and persistent data storage using CSV
Improved logical thinking and code organization
Understood separation of concerns using feature and utility modules

---

👤 Author
Aayan Ahmed Tejani
GitHub: https://github.com/Aayan-Ahmed-17
LinkedIn: https://www.linkedin.com/in/aayan-ahmed-tejani/

---

📄 License
This project is for learning and educational purposes.


   

