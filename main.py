import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

# Data structure to store items and their expiry dates
items = {}

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password123":
        notebook.tab(1, state="normal")  # Enable the Content Notifier tab
        notebook.select(1)  # Switch to the Content Notifier tab
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to add an item
def add_item():
    name = item_name_entry.get()
    expiry_date = expiry_date_entry.get()
    try:
        expiry_date_obj = datetime.strptime(expiry_date, "%Y-%m-%d")
        items[name] = expiry_date_obj
        messagebox.showinfo("Success", f"Item '{name}' added with expiry date {expiry_date}!")
        update_item_list()
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")

# Function to update the item list and check for nearing expiry
def update_item_list():
    item_list.delete(*item_list.get_children())
    now = datetime.now()
    for name, expiry in items.items():
        days_left = (expiry - now).days
        status = "Expired" if days_left < 0 else f"{days_left} days left"
        item_list.insert("", "end", values=(name, expiry.strftime("%Y-%m-%d"), status))
        if 0 <= days_left <= 3:
            messagebox.showwarning("Expiry Warning", f"Item '{name}' is expiring soon!")

# Create the main window
root = tk.Tk()
root.title("Content Expiry Notifier")
root.geometry("500x400")

# Create a Notebook (tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Tab 1: Login Page
login_tab = ttk.Frame(notebook)
notebook.add(login_tab, text="Login")

username_label = tk.Label(login_tab, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_tab)
username_entry.pack(pady=5)

password_label = tk.Label(login_tab, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(login_tab, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_tab, text="Login", command=login)
login_button.pack(pady=20)

# Tab 2: Content Notifier
notifier_tab = ttk.Frame(notebook)
notebook.add(notifier_tab, text="Content Notifier", state="disabled")

# Add Item Section
item_name_label = tk.Label(notifier_tab, text="Item Name:")
item_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
item_name_entry = tk.Entry(notifier_tab)
item_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

expiry_date_label = tk.Label(notifier_tab, text="Expiry Date (YYYY-MM-DD):")
expiry_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
expiry_date_entry = tk.Entry(notifier_tab)
expiry_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

add_item_button = tk.Button(notifier_tab, text="Add Item", command=add_item)
add_item_button.grid(row=2, column=0, columnspan=2, pady=10)

# Item List Section
item_list = ttk.Treeview(notifier_tab, columns=("Name", "Expiry Date", "Status"), show="headings")
item_list.heading("Name", text="Name")
item_list.heading("Expiry Date", text="Expiry Date")
item_list.heading("Status", text="Status")
item_list.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

notifier_tab.grid_rowconfigure(3, weight=1)
notifier_tab.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
