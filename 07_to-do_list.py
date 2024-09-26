def to_do_list():
    todo={}
    while True:
        choice=int(input("Enter 1 for additing a task to your to do list \n Enetr 2 for editing any task of your to do list \n Enter 3 for removing any task fro your to do list \n Enter 4 for changing status of your task \n Enter 5 for vieing your to do list \n Enter 6 for exiting this program \n Enter your choice:\t"))

        if choice==1:
            task=input("Enter the  task that you wa nted to add in your your to do:\t")
            deadline=input("Enetr the deadline if the task")
            todo.update=({task:deadline})
            print(todo.get[task])



        elif choice==2:
            for index, (key, value) in enumerate(todo.items(), start=1):
                print(f"{index}. {key}: {value}")
            
            edit=input("Enter the no. of task that you want to edit")
            lenght=len(todo)+1
            if 0<edit<=lenght:
                task=input("enter the new task that you wanted to enter ")
                deadline=input("Enter new deadline")
                key=list(todo.keys())[edit-1]
                value=list(todo.values())[edit-1]
                todo.update=({task:deadline})
                todo.pop(key)
                print(f"the old task was was{key} that has been changed to {task}\n the old deadline was {value} that has been changed to {deadline}|therefore the new to do list is as follows: \n {todo} ")
            else:
                print("the task you selected to be edited is not in the todo")



        elif choice==3:
            remove=input("Enter the no. of task that you want to remove:\t")
            lenght=len(todo)+1
            if 0<remove<=lenght:
                key=list(todo.keys())[remove-1]
                todo.pop(key)
                print(f"the todo list after removing the given task is as follows :\n{todo}")
            else:
                print("enter valid no. of task")



        elif choice==4:
            status=int(input("Enter the no. of element that you wants to mark complete :"))
            lenght=len(todo)+1
            if 0<status<=lenght:
                key=list(todo.keys())[status-1]
                todo.update({key:"completed"})
                print(f"updated to do list is as follows:\n{todo}")
            else:
                print("Enter valid task number")



        elif choice==5:
            print(f"the to do list currently looks as {todo}")


        elif choice==6:
            print("exiting the program ")
            break


        else:
            print("invalid choice enetr a valid choice")
to_do_list()




