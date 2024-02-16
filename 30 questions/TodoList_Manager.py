'''To-Do List Manager: Implement a simple to-do list
manager where users can add, remove, and mark tasks as
completed. Utilize loops to repeatedly present the menu and
handle user interactions until they choose to exit.'''
class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Task '{task}' removed from the to-do list.")
                return
        print(f"Task '{task}' not found in the to-do list.")

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Task '{task}' marked as completed.")
                return
        print(f"Task '{task}' not found in the to-do list.")

    def view_todo_list(self):
        print("\nCurrent To-Do List:")
        for idx, t in enumerate(self.tasks, start=1):
            status = "Completed" if t["completed"] else "Not Completed"
            print(f"{idx}. {t['task']} - {status}")
        print()

# Create an instance of ToDoListManager
todo_list_manager = ToDoListManager()

# Main loop
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View To-Do List")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list_manager.add_task(task)

    elif choice == "2":
        task = input("Enter the task to remove: ")
        todo_list_manager.remove_task(task)

    elif choice == "3":
        task = input("Enter the task to mark as completed: ")
        todo_list_manager.mark_as_completed(task)

    elif choice == "4":
        todo_list_manager.view_todo_list()

    elif choice == "5":
        print("Exiting the to-do list manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
print(todo_list_manager.tasks)