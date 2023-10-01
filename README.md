# BudgetTracker

## Introduction:
"Mint: Budgeting and Expense Tracking" is a simple yet effective GUI-based application developed using Python's `tkinter` module. The app interfaces with a MySQL database to keep track of user expenses. With Mint, users can input their expenses under specific categories and then view the logged expenses.

## Features:
1. **Database Connection**: Connects to a MySQL database for persistent storage of expenses.
2. **Add Expense**: Users can input the category and amount for each expense.
3. **View Expenses**: The application displays a list of all expenses, including their ID, category, and amount.
4. **Data Validation**: Ensures that the amount entered by the user is valid and both fields are filled.

## Prerequisites:

### Software:
1. **Python**: Ensure you have Python installed.
2. **MySQL**: You need to have MySQL installed and running on your machine.

### Python Libraries:
Ensure the following Python libraries are installed:
1. `tkinter` - for the GUI interface.
2. `mysql-connector` - to interface with the MySQL database.

You can install them using `pip`:

```bash
pip install tk mysql-connector-python
```

(Note: `tkinter` is included with most standard Python installations.)

## Setting Up:

### Database:
1. The application expects a MySQL database named `budget_tracker`.
2. User credentials set in the code are `root` with the password `password`. Please change these credentials in the `connect_db` function as per your MySQL setup for security reasons.
3. The script will automatically create a table named `expenses` with the necessary columns if it doesn't already exist.

### Running the Application:
1. Save the provided code in a file named `BudgetTracker.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the command:
```bash
python BudgetTracker.py
```

## Usage:
1. **Adding an Expense**:
    - Fill in the category and amount fields.
    - Click the "Add Expense" button.

2. **Viewing Expenses**:
    - Expenses are automatically listed in the `Listbox` widget.
    - Each time you add an expense, the list updates to include it.

## Error Handling:
The application has robust error handling:
- In case of an unsuccessful database connection, an error message will pop up.
- If the user fails to fill in both the category and amount, a warning pops up.
- The application checks that the amount entered is a valid number.

## Future Enhancements:
1. **Delete & Update Expenses**: Future versions can include the ability to delete or update recorded expenses.
2. **Categorization & Filters**: Implementing filters to view expenses based on categories or date ranges.
3. **Security**: Improve database access security, such as implementing hashed passwords and using environment variables.

## Conclusion:
The "BudgetTracker" application offers a straightforward way to monitor and log expenses. It acts as a foundation for more complex budget tracking and financial management systems.
