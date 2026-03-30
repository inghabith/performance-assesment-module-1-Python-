def remove_student(products_list):
    keep_removing = "yes"
    while keep_removing == "yes":


# this iterates the list and return the len, Nothing to show if the list is empty
        if len(products_list) == 0:
            print("The list is empty, please add students information.")
            return

        search_product = input("Please enter the student name: ")

        # Search and remove the student if it exists
        found = False
        for iterant in products_list:
            if iterant["name"] == search_product:
                products_list.remove(iterant)
                found = True

        if found == False:    #if the iterant doesn't match, show an error 
            print("The student doesn't exist")
        if found == True:
            print("The student was removed successfully!")

        keep_removing = input("Do you want to remove another student? yes/no: ") #ask the user if they want to remove another student