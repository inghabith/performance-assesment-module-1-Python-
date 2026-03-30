# 📖 Description
A modular, command-line application developed in Python that automates the management of student records. The system allows users to register, search, update, and delete student information.

## ⚙️ System Architecture

The application follows a modular architecture where each feature lives in its own independent file. The main.py file acts as the entry point and orchestrator: it imports all feature functions, maintains the shared inventory state (a list of dictionaries), and routes user input from the main menu to the correct module.

## 🔁 Flow Diagram

diagrama.png

## 🚀 How to Run the Program
1. Clone or download the repository so all .py files are in the same folder.
2. Open a terminal in that folder and run python main.py.
3. Follow the on-screen menu to manage your register system.


## 💡 Data Structure and Module Descriptions

1. Register a student - feature_register_student - The user is prompted to enter the student's information: name, age, major, and whether they are currently enrolled or inactive. The system validates that the values ​​are not negative or incorrect. The new student is then stored as a dictionary entry and added to the student list.

2. Check student list - feature_check_student_list - Displays all available students on the list, indicating their name and ID. If the list is empty, displays a clear message.

3. Search student - feature_search_specific_student -: The user enters the student's name, and the system searches for it in the list. If it finds the student, it displays their details. If not, it informs the user without the system crashing.

4. Update student - feature_update_student : The user selects a student by name and can modify their information. Fields left blank are not modified. The system validates that the new values ​​are not negative and/or are valid before applying any updates.


5. Remove student - feature_remove_student -: The user enters the name of the student they wish to delete. The system checks if the student exists before removing them from the inventory. If the student is not found, a message is displayed and the system returns to the menu.


6. Exit: - Ends the program.
