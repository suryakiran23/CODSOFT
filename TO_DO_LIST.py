tasks = []

def add_task(task_description):
    tasks.append({"description": task_description, "completed": False})
    print(f"Task '{task_description}' added.")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['description']} - {status}")

def mark_task_completed(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task['description']}' deleted.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Completed Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        task_description = input("Enter task description: ").strip()
        add_task(task_description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        try:
            task_number = int(input("Enter task number to mark as completed: ").strip())
            mark_task_completed(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '4':
        try:
            task_number = int(input("Enter task number to delete: ").strip())
            delete_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
