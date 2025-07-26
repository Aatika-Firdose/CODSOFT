# Task 1 - To-Do List Application
# Created by Aatika Firdose for CodSoft Internship

todo_list = []

def show_menu():
    print("\n To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        for i, t in enumerate(todo_list):
            status = "" if t["done"] else ""
            print(f"{i+1}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed = todo_list.pop(task_num)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting... Good luck, Aatika!")
        break
    else:
        print("Invalid choice. Please try again.")
