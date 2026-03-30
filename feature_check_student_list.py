def check_student_list(student_list): #def of the feature

    # this iterates the list and return the len, Nothing to show if the list is empty
    if len(student_list) == 0: # If the list is empty, launch an error message and cut the code function saying that the list is empty
        print("Error, the list is empty, please, enter new student information")
        return

    print("="*60)
    print("STUDENT LIST".center(60))

    # Print each product with its details
    for iterant in student_list:
        print("ID:".ljust(50), iterant["id"])
        print("name:".ljust(50), iterant["name"])
        

        print("-"*60)
        print()
