import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import pytz

#Customize the default_timezone to your timezone.
default_timezone = pytz.timezone('America/New_York')


# Function to save the journal entry
def save_entry():
    date_time = date_entry.get()
    title = title_entry.get()
    entry_text = text_editor.get("1.0", tk.END)

    entry_id = str(date_time)
    entry = {
        "Date/Time": date_time,
        "Title": title,
        "Entry": entry_text
    }

    # Check if entry_id already exists and delete the existing entry if found
    if entry_id in entries:
        del entries[entry_id]

    entries[entry_id] = entry

    with open("journal_entries.txt", "w") as file:
        for id, entry in entries.items():
            file.write(f"Entry ID: {id}\n")
            file.write(f"Date/Time: {entry['Date/Time']}\n")
            file.write(f"Title: {entry['Title']}\n")
            file.write(f"Entry:\n{entry['Entry']}\n\n")

    messagebox.showinfo("Success", "Journal entry saved successfully.")

# Function to create a new journal entry
def new_entry():
    title_entry.delete(0, tk.END)
    text_editor.delete("1.0", tk.END)
    date_entry.delete(0, tk.END)
    date_entry.insert(tk.END, datetime.now(default_timezone).strftime("%Y-%m-%d %H:%M:%S"))

# Function to view past journal entries
def view_entries():
    entries.clear()

    with open("journal_entries.txt", "r") as file:
        lines = file.readlines()
        entry_id = None
        for line in lines:
            if line.startswith("Entry ID:"):
                entry_id = line.split(": ")[1].strip()
                entries[entry_id] = {}
            elif line.startswith("Date/Time:"):
                entries[entry_id]["Date/Time"] = line.split(": ")[1].strip()
            elif line.startswith("Title:"):
                entries[entry_id]["Title"] = line.split(": ")[1].strip()
            elif line.startswith("Entry:"):
                entries[entry_id]["Entry"] = ""
            elif entry_id:
                entries[entry_id]["Entry"] += line

    view_window = tk.Toplevel(window)
    view_window.title("View Past Entries")

    entry_listbox = tk.Listbox(view_window, width=60, height=20)
    entry_listbox.pack(fill=tk.BOTH, expand=True)

    for id, entry in entries.items():
        entry_listbox.insert(tk.END, f"Entry ID: {id} - {entry['Date/Time']} - {entry['Title']}")

    def open_entry(event):
        selected_index = entry_listbox.curselection()
        if selected_index:
            selected_id = str(entry_listbox.get(selected_index).split(" - ")[0].split(": ")[1])
            selected_entry = entries[selected_id]
            edit_entry(selected_entry)

    entry_listbox.bind("<Double-Button-1>", open_entry)

# Function to delete selected journal entry
def delete_entry():
    entry_id = simpledialog.askstring("Delete Entry", "Enter the ID of the entry to delete:")
    if entry_id in entries:
        del entries[entry_id]
        with open("journal_entries.txt", "w") as file:
            for id, entry in entries.items():
                file.write(f"Entry ID: {id}\n")
                file.write(f"Date/Time: {entry['Date/Time']}\n")
                file.write(f"Title: {entry['Title']}\n")
                file.write(f"Entry:\n{entry['Entry']}\n\n")
        messagebox.showinfo("Success", "Journal entry deleted successfully.")
    else:
        messagebox.showerror("Error", "Entry ID not found.")

# Function to edit an existing entry
def edit_entry(selected_entry):
    title_entry.delete(0, tk.END)
    title_entry.insert(tk.END, selected_entry['Title'])
    text_editor.delete("1.0", tk.END)
    text_editor.insert(tk.END, selected_entry['Entry'])
    date_entry.delete(0, tk.END)
    date_entry.insert(tk.END, selected_entry['Date/Time'])

window = tk.Tk()
window.title("Journal App")

entries = {}

date_label = tk.Label(window, text="Date/Time:")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(window)
date_entry.grid(row=0, column=1, padx=5, pady=5)
date_entry.insert(tk.END, datetime.now(default_timezone).strftime("%Y-%m-%d %H:%M:%S"))

title_label = tk.Label(window, text="Title:")
title_label.grid(row=1, column=0, padx=5, pady=5)
title_entry = tk.Entry(window)
title_entry.grid(row=1, column=1, padx=5, pady=5)

text_editor = ScrolledText(window, width=60, height=10)
text_editor.grid(row=2, columnspan=2, padx=5, pady=5)

save_button = tk.Button(window, text="Save Entry", command=save_entry)
save_button.grid(row=3, column=0, padx=5, pady=5)

new_button = tk.Button(window, text="New Entry", command=new_entry)
new_button.grid(row=3, column=1, padx=5, pady=5)

view_button = tk.Button(window, text="View Entries", command=view_entries)
view_button.grid(row=4, column=0, padx=5, pady=5)

delete_button = tk.Button(window, text="Delete Entry", command=delete_entry)
delete_button.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
