import tkinter as tk
from tkinter import messagebox, ttk

from src.services.password_generator import generate_password
from src.services.vault_service import VaultService


vault = VaultService()


def clear_fields():
    title_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def show_entries(entries=None):
    for row in entry_table.get_children():
        entry_table.delete(row)

    if entries is None:
        entries = vault.view_entries()

    for entry in entries:
        entry_table.insert(
            "",
            tk.END,
            iid=entry.entry_id,
            values=(entry.title, entry.username, entry.password)
        )


def generate_new_password():
    try:
        length_text = length_entry.get().strip()

        if length_text:
            if not length_text.isdigit():
                raise ValueError("Password length must be a number.")

            password = generate_password(int(length_text))
        else:
            password = generate_password()

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError as error:
        messagebox.showerror("Error", str(error))


def create_entry():
    try:
        vault.create_entry(
            title_entry.get(),
            username_entry.get(),
            password_entry.get()
        )

        show_entries()
        clear_fields()

        messagebox.showinfo(
            "SecuraVault",
            "Password entry created."
        )

    except ValueError as error:
        messagebox.showerror("Error", str(error))


def update_entry():
    try:
        selected = entry_table.selection()

        if not selected:
            raise ValueError("Select an entry first.")

        entry_id = selected[0]

        vault.edit_entry(
            entry_id,
            title_entry.get(),
            username_entry.get(),
            password_entry.get()
        )

        show_entries()
        clear_fields()

        messagebox.showinfo(
            "SecuraVault",
            "Password entry updated."
        )

    except ValueError as error:
        messagebox.showerror("Error", str(error))


def delete_entry():
    try:
        selected = entry_table.selection()

        if not selected:
            raise ValueError("Select an entry first.")

        entry_id = selected[0]

        confirm = messagebox.askyesno(
            "Delete Entry",
            "Are you sure you want to delete this entry?"
        )

        if confirm:
            vault.delete_entry(entry_id)
            show_entries()
            clear_fields()

    except ValueError as error:
        messagebox.showerror("Error", str(error))


def search_entries():
    search_text = search_entry.get()

    if not search_text.strip():
        show_entries()
        return

    results = vault.search_entries(search_text)
    show_entries(results)


def select_entry(event):
    selected = entry_table.selection()

    if not selected:
        return

    entry = vault.find_entry(selected[0])

    clear_fields()

    title_entry.insert(0, entry.title)
    username_entry.insert(0, entry.username)
    password_entry.insert(0, entry.password)


window = tk.Tk()
window.title("SecuraVault Password Manager")
window.geometry("720x520")


form_frame = tk.Frame(window)
form_frame.pack(pady=10)


tk.Label(form_frame, text="Title").grid(
    row=0,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

title_entry = tk.Entry(form_frame, width=35)
title_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


tk.Label(form_frame, text="Username").grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

username_entry = tk.Entry(form_frame, width=35)
username_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


tk.Label(form_frame, text="Password").grid(
    row=2,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

password_entry = tk.Entry(form_frame, width=35)
password_entry.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)


tk.Label(form_frame, text="Password length").grid(
    row=3,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)

length_entry = tk.Entry(form_frame, width=10)
length_entry.grid(
    row=3,
    column=1,
    padx=5,
    pady=5,
    sticky="w"
)


generate_button = tk.Button(
    form_frame,
    text="Generate Password",
    command=generate_new_password
)

generate_button.grid(
    row=4,
    column=1,
    padx=5,
    pady=5,
    sticky="w"
)


button_frame = tk.Frame(window)
button_frame.pack(pady=5)


tk.Button(
    button_frame,
    text="Create",
    width=12,
    command=create_entry
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="Update",
    width=12,
    command=update_entry
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="Delete",
    width=12,
    command=delete_entry
).grid(row=0, column=2, padx=5)


tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields
).grid(row=0, column=3, padx=5)


search_frame = tk.Frame(window)
search_frame.pack(pady=10)


search_entry = tk.Entry(search_frame, width=35)
search_entry.grid(row=0, column=0, padx=5)


tk.Button(
    search_frame,
    text="Search",
    command=search_entries
).grid(row=0, column=1, padx=5)


tk.Button(
    search_frame,
    text="Show All",
    command=show_entries
).grid(row=0, column=2, padx=5)


entry_table = ttk.Treeview(
    window,
    columns=("title", "username", "password"),
    show="headings",
    height=12
)

entry_table.heading("title", text="Title")
entry_table.heading("username", text="Username")
entry_table.heading("password", text="Password")

entry_table.column("title", width=160)
entry_table.column("username", width=220)
entry_table.column("password", width=220)

entry_table.pack(padx=10, pady=10, fill="both", expand=True)

entry_table.bind("<<TreeviewSelect>>", select_entry)


show_entries()
window.mainloop()