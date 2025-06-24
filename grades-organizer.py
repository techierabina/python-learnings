print("Welcome to the grade organizer !")
grades=[]
while True:
    print("Menu of Grade Organizer:")
    print("1. 'add' for adding the grades")
    print("2. 'view'for viewing the grades")
    print("3. 'average' for average grade")
    print("4. 'highest' for highest grade ")
    print("5. 'lowest' for lowest grade")
    print("6. 'exit' for exiting this program")
    user_input=input("Enter your opiton from above: ").lower()
    if user_input=='add':
       while True:
           add_input=input("Enter the grade or 'exit' for exiting: ")
           if add_input.lower()=='exit':
               break
           elif add_input.replace('.', '', 1).isdigit():
               grades.append(float(add_input))
               print("Grade added successfully")
           else:
              print("Invalid input. Please enter a number.")
          
    elif user_input=='view':
      if not grades:
        print("The list is empty.")
      else:
        for i,x in enumerate(grades,start=1):
            print(f"{i}.{x}")
    elif user_input=='average':
        average_grade=sum(grades)/len(grades)
        print(f"The average grade is {average_grade}.")
    elif user_input=='highest':
        if grades:
           print(f"The highest grade is {max(grades)}")
        else:
           print("No grades for calucaltion")
    elif user_input=='lowest':
        if grades:
           print(f"The lowest grade is {min(grades)}")
        else:
           print("No grades for calucaltion")
    elif user_input=='exit':
        print("Thank you for using this app")
        break
    else:
       print("Invalid input. Please try again.")