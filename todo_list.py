"""
To-Do List Project
Author : Thanusri Veera
Year : 2026
Description : Command-line application to create,update,and track tasks efficiently.
              Features like persistence,input validation,and status tracking.
"""


#Create an empty list to store the tasks and their status

tasks =[]

#Function to display a menu

def open_menu():
    print("===MAIN MENU===")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Remove a task")
    print("5. Exit")
    
def add_task():
    task=input("Enter new task:") 
    tasks.append({"task":task,"done":False})
    print(f"Task added:{task}")
    
def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("Your tasks:")
    for i,t in enumerate(tasks):
        status="*" if t["done"] else" "
        print(f"{i+1}.[{status}] {t['task']}")
        
def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_num=int(input("Enter task number to mark it as completed"))-1
        if 0<=task_num<len(tasks):
            tasks[task_num]["done"]=True
            print("Task marked as completed!")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a number") 
        
def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete:"))-1
        if 0 <= task_num < len(tasks):
            removed=tasks.pop(task_num)
            print(f"Deleted:{removed['task']}")     
        else:
            print("Invalid task number") 
    except ValueError:
        print("Please enter a number") 
        
#Main program loop
while True:
    open_menu()
    choice = input("choose option 1-5:")
    
    if choice=="1":
        add_task()

    elif choice=="2":
        view_tasks()
    
    elif choice=="3":
        mark_completed()
    
    elif choice=="4":
        remove_task()
    
    elif choice=="5":
       print("Bye!")
       break

    else:
       print("Invalid choice.Pick 1-5")   