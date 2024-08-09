import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Welcome to the To-Do List Application!")
    print("Please choose an option:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def update_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_task = input("Enter the new task: ")
        old_task = tasks[task_number]
        tasks[task_number] = new_task
        print(f"Task '{old_task}' has been updated to '{new_task}' successfully!")
    else:
        print("Invalid task number!")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task}' deleted successfully!")
    else:
        print("Invalid task number!")

def main():
    tasks = []
    while True:
        clear_console()
        display_menu()
        choice = input("Enter your choice (1-5): ")
        clear_console()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank You !")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
