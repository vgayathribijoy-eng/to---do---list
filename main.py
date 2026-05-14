from tkinter import *
from tkinter import messagebox
from time import strftime

root = Tk()
root.title("Advanced To-Do List")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# ---------- FUNCTIONS ----------

def update_time():
    current = strftime('%H:%M:%S')
    clock_label.config(text=current)
    clock_label.after(1000, update_time)

def update_task_count():
    count_label.config(text=f"Total Tasks: {listbox.size()}")

def add_task():
    task = task_entry.get()

    if task != "":
        listbox.insert(END, task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        task_entry.delete(0, END)

        update_task_count()

def delete_task():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected)

        save_tasks()

        update_task_count()

def complete_task():
    selected = listbox.curselection()

    if selected:
        task = listbox.get(selected)

        listbox.delete(selected)

        listbox.insert(END, "✔ " + task)

        save_tasks()

def clear_all():
    answer = messagebox.askyesno("Clear All", "Delete all tasks?")

    if answer:
        listbox.delete(0, END)

        save_tasks()

        update_task_count()

def save_tasks():
    tasks = listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ---------- LOAD TASKS ----------

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            listbox.insert(END, line.strip())
except:
    pass

# ---------- GUI ----------

title = Label(
    root,
    text="Advanced To-Do List",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=10)

clock_label = Label(
    root,
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="cyan"
)
clock_label.pack()

update_time()

task_entry = Entry(
    root,
    width=30,
    font=("Arial", 14)
)
task_entry.pack(pady=15)

add_btn = Button(
    root,
    text="Add Task",
    width=15,
    command=add_task
)
add_btn.pack(pady=5)

delete_btn = Button(
    root,
    text="Delete Task",
    width=15,
    command=delete_task
)
delete_btn.pack(pady=5)

complete_btn = Button(
    root,
    text="Mark Complete",
    width=15,
    command=complete_task
)
complete_btn.pack(pady=5)

clear_btn = Button(
    root,
    text="Clear All",
    width=15,
    command=clear_all
)
clear_btn.pack(pady=5)

listbox = Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    selectbackground="green"
)
listbox.pack(pady=20)

count_label = Label(
    root,
    text=f"Total Tasks: {listbox.size()}",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)
count_label.pack()

update_task_count()

root.mainloop()
