task=[]
print("Welcome to Todo App")
while True:
    print("\nChoose one of the following options:")
    print("1. 'add' for Adding")
    print("2. 'edit' for Editing")
    print("3. 'view' for Viewing")
    print("4. 'delete' for Deleting")
    print("5. 'exit' for Exiting")
    user_input = input("Enter your option: ").lower()
    if user_input=='add':
        while True:
            added_task=input("\nEnter your task or 'exit' for exiting: ")
            if added_task.lower()=='exit':
                break
            task.append(added_task)
            print("Task added successfully !")
    elif user_input=='view':
        if not task:
            print("The list is empty")
        for x in task:
            print("-",x)
    elif user_input=='delete':
        if not task:
            print("The list is empty.")
            continue
        print("\n Your Tasks:")
        for i,x in enumerate(task,start=1):
            print(f"{i}.{x}")
        delete_input=input("Enter the above number you want to delete.")
        if delete_input.isdigit():
            delete_input=int(delete_input)
            if 1<=delete_input<=len(task):
                removed_task=task.pop(delete_input-1)
                print(f"Task '{removed_task}' deleted successfully !")
            else:
                print("Enter a valid number")
        else:
            print("Please enter a valid number ")
    elif user_input=='edit':
        if not task:
            print("The list is empty.")
            continue
        print("\n Your Tasks:")
        for i,x in enumerate(task,start=1):
            print(f"{i}.{x}")
        edit_input=input("Enter the above number want to edit:")
        if edit_input.isdigit():
            edit_input=int(edit_input)
            if 1<=edit_input<=len(task):
                updated_task=input("Enter the task to update: ")
                task[edit_input-1]=updated_task
                print("Task updated successfully !")
            else:
                print("Invalid task number")
        else:
            print("Please enter a valid number")
    elif user_input=='exit':
        print("Thank you for using this app.")
        break
    else:
        print("Invalid Option. Please try again")