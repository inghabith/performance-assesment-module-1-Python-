def update_student_info(student_list): 
    
#while loop that maintains the user in, until they dont want to update anymore information
    keep_updating = "yes"
    while keep_updating == "yes":

# this iterates the list and return the len, Nothing to show if the list is empty
        if len(student_list) == 0: # If the list is empty, launch an error message and cut the code function saying that the list is empty
            print("The list is empty, please add student information.")
            return

        search_student = input("Please enter the student name: ").strip().lower()
        print()

        # iterates the list, Find the student, validate the information and update its values 
        found = False
        for iterant in student_list:
            if iterant["name"] == search_student:

                #new name validation values
                update_name = ""
                while update_name == "":
                    update_name = (input("Enter the new name: ")).strip().lower()
                    if update_name == "":
                        print(f"{'❌ Error: This field must be filled. ❌':^65}")

                #new age validation values
                update_age = 0
                while update_age <= 0:
                    try:
                        update_age = int(input("Enter the new age: "))
                        
                        if update_age <= 0:
                            print()
                            print(f"{'❌ Error: please enter an integer positive value. ❌':^65}")
                    except ValueError:
                            print()
                            print(f"{'❌ Error: please, enter an integer numeric positive value ❌':^65}")


                #new program validation values
                update_program = ""
                while update_program == "":
                    update_program = (input("Enter the new program: ")).strip().lower()
                    if update_program == "":
                        print(f"{'❌ Error: This field must be filled. ❌':^65}")

                #New state validation values
                update_state = ""
                while update_state == "":
                    update_state = (input("Enter the new state active/inactive: ")).strip().lower()
                    if update_state == "":
                        print(f"{'❌ Error: This field must be filled. ❌':^65}")

                #The iterant update the associated information
                iterant["name"] = update_name
                iterant["age"] = update_age
                iterant["program"] = update_program
                iterant["state"] = update_state

                found = True

        if found == False:  #if the itinerant does not match any of the students on the list, show an error on terminal and ask for a new update 
            print("The student doesn't exist")
        if found == True: #if the iterant match with any of the students on the list, show a succesfully message
            print()
            print("The update is successfully done!")
            print()

        keep_updating = input("Do you want to update another student information? yes/no: ")  #Ask the user if they want to update another student information