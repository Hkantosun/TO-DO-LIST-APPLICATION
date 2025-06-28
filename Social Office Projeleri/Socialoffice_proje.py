
def print_menu(): 
    print("-"*3 + " TO-DO LIST APPLICATION " + "-"*3)
    print("Missions loaded successfully.")
    print("Please enter the one of the options below:")
    print("1.List Tasks")
    print("2.Add Task")
    print("3.Edit Task")
    print("4.Delete Task")
    print("5.Exit")
    print("-"*60)

def print_menu2(): 
    print("-"*3 + " TO-DO LIST APPLICATION " + "-"*3)
    print("The task file could not be found or read. A new list has been created")
    print("Please enter the one of the options below:")
    print("1.List Tasks")
    print("2.Add Task")
    print("3.Edit Task")
    print("4.Delete Task")
    print("5.Exit")
    print("-"*60)    

def save_tasks_to_file(filename="tasks.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file(filename="tasks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# To-Do List Application
open("tasks.txt", "w", encoding="utf-8").close()

tasks = load_tasks_from_file() 
statu = True

if len(tasks) > 0:
    print_menu()
else:
    print_menu2()


while statu:
    option = input("Enter your choice(1-5): ")

    if option == "1":
        if not tasks:
            print("There are no missions yet.")
        else:
            print("Listing all tasks...")
            print("-"*5 +" TASK LİST " + "-"*5)
            for index, task in enumerate(tasks ,1):
                print(f"{index}: {task}")
            print("-"*60)    
            print_menu() if len(tasks) > 0  else print_menu2()
    elif option == "2":
        task = input("Enter the task to add: ")
        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            save_tasks_to_file()
            print(f"Task '{tasks[-1]}' added.")
            print("Mission added successfully.") 
            print_menu() if len(tasks) > 0  else print_menu2()
    elif option == "3":
        for index, task in enumerate(tasks ,1):
                print(f"{index}: {task}")
        task_index = int(input("Enter the number of the task to edit: "))
        try:
            if 1 <= task_index <= len(tasks):
                old_task = tasks[task_index - 1] 
                new_task = input("Enter the new task: ")
                if new_task.strip() == "":
                    print("Task cannot be empty.")
                else:
                    tasks[task_index - 1] = new_task
                    save_tasks_to_file()
                print(f"Task '{old_task}' updated to '{new_task}'.")
                print("Task updated successfully.")
                print_menu() if len(tasks) > 0  else print_menu2()
            else:
                print("Invalid task number.")
        except ValueError:
                print("Invalid input. Please enter a task number.")    
    elif option == "4":
        for index, task in enumerate(tasks ,1):
                print(f"{index}: {task}")
        task_index = int(input("Enter the number of the task to delete: "))
        try: 
            if 1 <= task_index < len(tasks) + 1:
                removed_task = tasks.pop(task_index - 1)
                save_tasks_to_file()
                print(f"Task '{removed_task}' deleted.")
                print("Task saved successfully.")
                print_menu() if len(tasks) > 0  else print_menu2()
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please enter a task number.")        
    elif option == "5":
        print("Exiting the program.")
        print("-"*60)
        print("Thank you for using the To-Do List Application!") 
        statu = False
    else:
        print("Invalid option. Please enter number between 1 and 5 again.")


