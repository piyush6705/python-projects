tasks= []

def add_task():
    task= input("enter a task:")
    tasks.append(task)
    print("task added ")

def view_tasks():
    if not tasks:
        print("theres is not task  to show right now")
    else:
        print("your tasks: ")
        for i , task in enumerate(tasks, start=1):
            print(f"{i}.{task}")

def remove_task():
    view_tasks()
    if not tasks:
        return
    
    task_num = input("Enter task number to delete: ")

    if task_num.isdigit():
        task_num = int(task_num)

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Task number out of range")
    else:
        print("Please enter a valid number")


while True:
    print("Todo list manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    print("5. clear all tasks")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbyee!")
        break
    elif choice =="5":
        tasks.clear()
        print("Your all tasks have been cleared ")
    else:
        print("Invalid option Please try again")

