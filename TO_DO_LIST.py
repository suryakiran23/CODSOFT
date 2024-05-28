class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

import pickle

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def save_tasks(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            self.tasks = []

def main():
    todo_list = ToDoList()
    todo_list.load_tasks('tasks.pkl')

    while True:
        print("\nOptions:")
        print("1. Add task") 
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Save and exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_tasks('tasks.pkl')
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
