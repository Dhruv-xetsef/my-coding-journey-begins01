'''Mistakes & Corrections according to chatgpt

    Incorrect use of update method:
        Problem: You used todo.update=({task:deadline}) instead of todo.update({task:deadline}). update is a method, not an attribute, so you should not use = when calling it.
        Fix:

        python

    todo.update({task: deadline})

Using get instead of [] brackets:

    Problem: print(todo.get[task]) should be print(todo.get(task)). The get method is called using parentheses () not square brackets [].
    Fix:

    python

    print(todo.get(task))

Incorrect handling of user input types (edit, remove, status):

    Problem: You're taking edit, remove, and status as strings but comparing them with integers in the range check 0 < edit <= length. Convert them to integers using int() before comparison.
    Fix:

    python

    edit = int(input("Enter the no. of task that you want to edit: "))
    remove = int(input("Enter the no. of task that you want to remove: "))
    status = int(input("Enter the no. of element that you want to mark complete: "))

Incorrect calculation of length:

    Problem: length = len(todo) + 1 is incorrect because you want to compare up to len(todo).
    Fix:

    python

    length = len(todo)

Populating and removing tasks in elif choice == 2:

    You are adding the new task using update before removing the old task, which may cause confusion if keys overlap. You should first remove the old key and then update the dictionary.
    Fix:

    python

key = list(todo.keys())[edit - 1]
todo.pop(key)
todo.update({task: deadline})'''


def to_do_list():
    todo = {}
    while True:
        choice = int(input("Enter 1 for adding a task to your to-do list \n Enter 2 for editing any task in your to-do list \n Enter 3 for removing any task from your to-do list \n Enter 4 for changing the status of your task \n Enter 5 for viewing your to-do list \n Enter 6 for exiting this program \n Enter your choice:\t"))

        if choice == 1:
            task = input("Enter the task that you want to add to your to-do list:\t")
            deadline = input("Enter the deadline for the task: ")
            todo.update({task: deadline})
            print(f"Task '{task}' with deadline '{deadline}' added to your to-do list.")

        elif choice == 2:
            for index, (key, value) in enumerate(todo.items(), start=1):
                print(f"{index}. {key}: {value}")
            
            edit = int(input("Enter the number of the task that you want to edit: "))
            length = len(todo)
            if 0 < edit <= length:
                task = input("Enter the new task description: ")
                deadline = input("Enter the new deadline: ")
                key = list(todo.keys())[edit - 1]
                todo.pop(key)
                todo.update({task: deadline})
                print(f"Task '{key}' has been updated to '{task}' with a new deadline '{deadline}'.\n Updated to-do list:\n {todo}")
            else:
                print("Invalid task number.")

        elif choice == 3:
            remove = int(input("Enter the number of the task that you want to remove: "))
            length = len(todo)
            if 0 < remove <= length:
                key = list(todo.keys())[remove - 1]
                todo.pop(key)
                print(f"Task '{key}' has been removed. The updated to-do list is:\n{todo}")
            else:
                print("Invalid task number.")

        elif choice == 4:
            status = int(input("Enter the number of the task that you want to mark as completed: "))
            length = len(todo)
            if 0 < status <= length:
                key = list(todo.keys())[status - 1]
                todo.update({key: "completed"})
                print(f"Task '{key}' marked as completed. The updated to-do list is:\n{todo}")
            else:
                print("Invalid task number.")

        elif choice == 5:
            if todo:
                print("Your current to-do list:")
                for task, status in todo.items():
                    print(f"Task: {task} | Status/Deadline: {status}")
            else:
                print("Your to-do list is currently empty.")

        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please enter a valid choice.")

to_do_list()




'''message for myself to never repeat my mistakes'''