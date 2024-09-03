import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = task_entry.get()
    if title:
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "title": title, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task title cannot be empty.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f"{task['id']}. {task['title']} - {status}")

def mark_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = True
        update_task_list()

def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        task = tasks[task_index]
        title = task_entry.get()
        if title:
            task["title"] = title
            save_tasks(tasks)
            update_task_list()

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        del tasks[task_index]
        save_tasks(tasks)
        update_task_list()

def on_closing():
    save_tasks(tasks)
    root.destroy()

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

# Entry for new tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)
task_entry.insert(0, "Task Title")

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=80, height=15)
task_listbox.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
update_task_list()
root.mainloop()
