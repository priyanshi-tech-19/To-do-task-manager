from tkinter import *
import tkinter as tk
from tkinter import ttk
# from tkinter import Entry


tasks = []

try:
    with open("tasks_UI.txt",'r') as fh:
        tasks = [line.strip() for line in fh.readlines() if line.strip()]

except FileNotFoundError:
    tasks = []

root = tk.Tk()
root.title("To-Do Application")
root.geometry('500x300')

task_label = ttk.Label(root,text="Enter new task:")
task_label.pack()

entry = ttk.Entry(root)
entry.pack(pady=5)

number_label = ttk.Label(root,text="Enter task number:")
number_label.pack()

number_task = ttk.Entry(root)
number_task.pack()

msg_label = ttk.Label(root,text="")
msg_label.pack()


def add_task():
    task = entry.get().strip()
    task_with_status = task + " || Pending"

    if task == "":
        msg_label.config(text="Please enter a task")
        return
    tasks.append(task_with_status)
    try:
        with open("tasks_UI.txt",'a') as fh:
            fh.write(task_with_status + "\n")
        
        msg_label.config(text="Task added!")
    except Exception as err:
        msg_label.config(text="Error while adding task")
    
    entry.delete(0, END)
    number_task.delete(0, END)

def view_task():
    if not tasks:
        msg_label.config(text="No Tasks Available")
    else:
        all_tasks = "Your tasks :\n\n"

        for i,task in enumerate(tasks):
            all_tasks += f"{i+1}. {task}\n"

        msg_label.config(text=all_tasks)

    entry.delete(0, END)
    number_task.delete(0, END) 

def update_task():

    if not tasks:
        msg_label.config(text="No Tasks Available")
        return
     
    all_tasks = "Your tasks :\n\n"

    for i, task in enumerate(tasks):
        all_tasks += f"{i+1}. {task}\n"

    all_tasks += "\nEnter task number and new task"

    msg_label.config(text=all_tasks)

    if number_task.get() == "":
        return

    if entry.get() == "":
        return

    task_num = int(number_task.get())

    if task_num > len(tasks) or task_num <= 0:
        msg_label.config(text="Invalid task number")
        return

    tasks[task_num - 1] = entry.get() + " || Pending"

    try:
        with open("tasks_UI.txt",'w') as fh:

            for task in tasks:
                fh.write(task + "\n")

        msg_label.config(text="Task Updated!")

    except Exception:
        msg_label.config(text="Error While Updating tasks")
    
    entry.delete(0, END)
    number_task.delete(0, END)


def mark_task():
     
    if not tasks:
        msg_label.config(text="No Tasks Available")
        return
    
    all_tasks = "Your tasks :\n\n"

    for i, task in enumerate(tasks):
       all_tasks += f"{i+1}. {task}\n"

    all_tasks += "\nEnter task number to Mark"

    msg_label.config(text=all_tasks)
    
    if number_task.get() == "":
        return
    
    try:  
      task_num = int(number_task.get())  
    except ValueError:
        msg_label.config(text="Invalid task number")
        return
    
    if task_num < 1 or task_num > len(tasks):
        msg_label.config(text="Invalid task number")
        return
         
    selected_task = tasks[task_num -1]

    if "||" in selected_task:
        task_name,status = selected_task.split("||")
        task_name = task_name.strip()
        status = status.strip()
    else:
        task_name = selected_task
        status = "Pending"    
               
    if status == "Done":
        msg_label.config(text="Task already marked as done")
        return
    
        
    tasks[task_num - 1] = f"{task_name} || Done"
            
    try:
        with open("tasks_UI.txt",'w') as fh:
            for task in tasks:
                fh.write(task + "\n")

        msg_label.config(text="Task Marked as Done successfully!")

    except Exception:
        msg_label.config(text="Error While Updating tasks")

    entry.delete(0, END)
    number_task.delete(0, END)

def delete_task():
    
    if not tasks:
        msg_label.config(text="No Tasks Available")
        return
    
    all_tasks = "Your tasks :\n\n"

    for i, task in enumerate(tasks):
       all_tasks += f"{i+1}. {task}\n"

    all_tasks += "\nEnter task number to delete"

    msg_label.config(text=all_tasks)
    
    if number_task.get() == "":
        return

    task_num = int(number_task.get())

    if task_num > len(tasks) or task_num <= 0:
        msg_label.config(text="Invalid task number")
        return

    tasks.pop(task_num - 1)

    try:
        with open("tasks_UI.txt",'w') as fh:

            for task in tasks:
                fh.write(task + "\n")
        msg_label.config(text="Task Deleted!")

    except Exception:
        msg_label.config(text="Error occurred while deleting task!")
    
    entry.delete(0, END)
    number_task.delete(0, END)


btn_add = ttk.Button(root,text="Add Task",width=15,command=add_task)
btn_add.pack()

btn_view = ttk.Button(root,text="View Task",width=15,command=view_task)
btn_view.pack()

btn_update = ttk.Button(root,text="Update Task",width=15,command=update_task)
btn_update.pack()

btn_mark = ttk.Button(root,text="Task done!",width=15,command=mark_task)
btn_mark.pack()

btn_delete = ttk.Button(root,text="Delete Task",width=15,command=delete_task)
btn_delete.pack()


root.mainloop()


