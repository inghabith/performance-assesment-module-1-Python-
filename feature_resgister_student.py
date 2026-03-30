def register_student(student_list):

    keep_registering = "yes"  # Variable that controls if the user wants to keep registering students

    # This loop keeps running as long as the user wants to add more customers
    while keep_registering == "yes":

        print("STUDENT REGISTRATION".center(50, "="))

# ── CUSTOMER ID VALIDATION ─────────────────────────────
        student_id = 0

        # Keep asking until the user enters a valid positive number
        while student_id <= 0:
            try:
                # Ask the user to type a number and convert it to integer
                student_id = int(input("Enter an ID: "))

                # If the number is zero or negative, show an error
                if student_id <= 0:
                    print()
                    print(
                        f"{'❌ Error: please enter integer positive value. ❌':^65}")

            except ValueError:
                # This runs if the user types letters instead of numbers
                print()
                print(
                    f"{'❌ Error: please, enter a integer numeric positive value. ❌':^65}")


# ── STUDENT NAME VALIDATION ─────────────────────────────────────────────────────────
        name = ""

        # Keep asking until the user types something
        while name == "":
            name = input("Enter the student name: ").strip()

            if name == "":
                print(f"{'❌ Error: This field must be filled. ❌':^65}")


# ── CUSTOMER AGE VALIDATION ──────────────────────────────────────────────────────
        age = 0

        # Keep asking until the user enters a valid positive number and diffrent to zero
        while age <= 0:
            try:
                # Ask the user to type a number and convert it to integer
                age = int(input("Enter the student age: "))

                # If the number is zero or negative, show an error
                if age <= 0:
                    print()
                    print(f"{'❌ Error: please enter an integer positive value. ❌':^65}")

            except ValueError:
                # This runs if the user types letters instead of numbers
                print()
                print(
                    f"{'❌ Error: please, enter an integer numeric positive value ❌':^65}")


# ── STUDENT EDUCATIVE PROGRAM VALIDATION ─────────────────────────────────────────────────────────
        program = ""

        # Keep asking until the user types something
        while program == "":
            program = input("Enter the student program: ").strip()

            if program == "":
                print(f"{'❌ Error: This field must be filled. ❌':^65}")


# ── STUDENT STATE VALIDATION ─────────────────────────────────────────────────────────
        state = ""

        # Keep asking until the user types something
        while state == "":
            state = input(
                "Enter the student state (active/inactive): ").strip().lower()

            if state == "":
                print(f"{'❌ Error: This field must be filled. ❌':^65}")


# ── SAVE THE NEW CUSTOMER ──────────────────────────────────────────────────────────
        # Pack all collected data into a dictionary
        students_dic = {
            "id":  student_id,
            "name":    name,
            "age": age,
            "program": program,
            "state": state
        }

        # Add the new customer to the list
        student_list.append(students_dic)

        # Show a success message to the user
        print()
        print("-" * 50)
        print("STUDENT SUCCESFULLY REGISTERED✅".center(50, "="))
        print("-" * 50)
        print()

        keep_registering = input(
            "Do you want to register another student? yes/no: ").strip().lower()
        print()

    # Send back the updated list with all registered customers
    return student_list
