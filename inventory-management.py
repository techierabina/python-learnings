print("Welcome to Inventory management")
inventory=[]
while True:
    print("\nInventory Menu:")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Find Item")
    print("6. Exit")
    user_input=input("Enter your choice: ").lower()
    if user_input=='add':
        while True:
            item_input=input("Enter the item or 'exit' for exit: ")
            if item_input.lower()=='exit':
                break
            inventory.append(item_input)
            print("Item added successfully")
    elif user_input=='view':
        if not inventory:
            print("Empty Inventory")
        for i,x in enumerate(inventory,start=1):
            print(f"{i}. {x}")
    elif user_input=='update':
        if not inventory:
            print("Empty Inventory")
        for i,x in enumerate(inventory,start=1):
            print(f"{i}. {x}")
        update_input=input("Enter the number you want to update.")
        if update_input.isdigit():
            update_input=int(update_input)
            if 1<=update_input<=len(inventory):
                update=input("Enter the updated item: ")
                inventory[update_input-1]=update
                print("Update Successful !")
            else:
                print("Invalid number")
        else:
            print("Please enter a valid number")
    elif user_input=='delete':
        if not inventory:
            print("Empty List")
        for i,x in enumerate(inventory,start=1):
            print(f"{i}. {x}")
        delete_item=input("Enter the number you want to delete.")
        if delete_item.isdigit():
            delete_item=int(delete_item)
            if 1<= delete_item <=len(inventory):
                deleted=inventory.pop(delete_item-1)
                print(f"{deleted} deleted successfully!")
            else:
                print("Invalid number")
        else:
            print("Please enter a valid number")
    elif user_input=='find':
        if not inventory:
            print("Empty list.")
        item=input("Enter the item: ")
        if item in inventory:
            print("Item found")
        else:
            print("Not in the list.")
    elif user_input=='exit':
        print("Thank you for using this app.")
        break
    else:
        print("Invalid Input, Please Try Again.")
      