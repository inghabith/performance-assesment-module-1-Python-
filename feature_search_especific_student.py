def search_specific_student(products_list):

# this iterates the list and return the len, Nothing to show if the list is empty
    if len(products_list) == 0: # If the list is empty, launch an error message and cut the code function saying that the list is empty
            print("The list is empty, please add new student information.")
            return
    

    #while loop that maintains the user in until they dont want to search another
    keep_searching = "yes"  #variable that control the loop
    while keep_searching == "yes":

        search_student = input("Please enter the student name: ").strip().lower()
        print()
        print("-"*50)

        # Look for the student by name and show they information
        found = False
        for iterant in products_list:
            if iterant["name"] == search_student:
                print("ID:".ljust(50), iterant["id"])
                print("name:".ljust(50), iterant["name"])
                print("age:".ljust(50), iterant["age"])
                print("program:".ljust(50), iterant["program"])
                print("state:".ljust(50), iterant["state"])
                found = True
            print("-"*50)

        if found == False: #if the iterant doesn't match with the any of the students names register, display a error and ask if want to search another student
            print("The student doesn't exist")
            
        keep_searching = input("Do you want to search another student? yes/no: ")