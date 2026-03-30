#These are imports of the features that exists in diffrents files
from feature_resgister_student import register_student
from feature_check_student_list import check_student_list
from feature_search_especific_student import search_specific_student
from feature_update_student_info import update_student_info
from feature_remove_student import remove_student

student_list = []
#A interactive menu that allow the user use interact with all features of the program
print(f"""
    ╔═══════════════════════════════════════════════════════════╗
                    * Student register system *
            * Welcome to the Student Management System! *
    ╚═══════════════════════════════════════════════════════════╝""")

Menu = "yes"

while Menu == "yes":

    try:
        Option = int(input(f"""{"-"*24} MAIN MENU {"-"*25} 
1) 🥦  Register student 
2) 🔍  Check students list
3) 🧾  Check student
4) 🔄  Update student information
5) 📋  Remove student
6) 🚪  Exit                                                    
{"="*60}
~ Please select an option:
➤  """))

        if Option < 1 or Option > 6:
            print(f"\n{'❌ ERROR: Please enter a valid number ❌':^60}\n")
            continue

    except ValueError:
        print(f"\n{'❌ ERROR: Please enter a valid integer ❌':^60}\n")
        continue

    print()

    # Route to the correct feature based on user input
    if Option == 1:
        register_student(student_list)
    if Option == 2:
        check_student_list(student_list)
    if Option == 3:
        search_specific_student(student_list)
    if Option == 4:
        update_student_info(student_list)
    if Option == 5:
        remove_student(student_list)
    if Option == 6:
        print ("See you later")
        break
    print()
    Menu = input("Do you want to return to the main menu? yes/no: ")


    if Menu == "no":
        print("See you later") #farewell message and the end of the program
