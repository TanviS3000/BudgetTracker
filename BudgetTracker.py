import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="budget_tracker"
        )
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
        return None

def init_db():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS expenses (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(255), amount FLOAT)")
        db.close()

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if not category or not amount:
        messagebox.showwarning("Incomplete Data", "Please fill in both fields.")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showwarning("Invalid Data", "Amount must be a number.")
        return

    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO expenses (category, amount) VALUES (%s, %s)", (category, float(amount)))
        db.commit()
        db.close()

        # Clear the input fields for new entries
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        # Refresh the displayed expenses
        display_expenses()

def display_expenses():
    db = connect_db()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

        # Clear existing data in the listbox
        expense_listbox.delete(0, tk.END)

        for row in rows:
            expense_listbox.insert(tk.END, f"{row[0]}: {row[1]} - ${row[2]}")

        db.close()

# Initialize database
init_db()

# Initialize Tkinter window
root = tk.Tk()
root.title("Mint: Budgeting and Expense Tracking")

category_label = tk.Label(root, text="Category:")
category_label.pack()
category_entry = tk.Entry(root)
category_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

expense_listbox = tk.Listbox(root)
expense_listbox.pack()

# Initially display expenses
display_expenses()

root.mainloop()
