# Stores all student records
students = []

# Rewrites the student file using the current students list
def save_students():
    file = open("student_manager.txt", "w")

    for student in students:
        file.write(f"{student['Name']}, {student['Major']}, {student['Graduation Year']}\n")
    
    file.close()

# Loads students that may already exist
def load_students():

    # Resets memory
    students.clear()

    file = open("student_manager.txt", "r")

    # Loops through lines in the file
    for line in file:
        parts = line.strip().split(",")
    
        name = parts[0].strip()
        major = parts[1].strip()
        graduation_year = int(parts[2].strip())

        student = {
            "Name": name,
            "Major": major,
            "Graduation Year": graduation_year
        }
    
        students.append(student)

    file.close()
    
# Adds a new student to the system
def add_students():

    # Collect student informationi from user
    name = input("What is your name? ")
    major = input("What is you major? ")

    # Loop checks for a valid and releaistic graduation year
    while True:
        try:
            graduation_year = int(input("What is your anticipated graduation year? "))

            if not 2024 <= graduation_year <= 2035:
                print("Please enter a valid graduation year.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create dictionary contatining student data
    new_student = {"Name": name,
                    "Major": major,
                    "Graduation Year": graduation_year}
    
    # Add student dictionary to list
    students.append(new_student)

    # Saves student data to file
    save_students()


    print("Student added successfully!\n")

# Displays all the students that are currently stored
def view_students():

    # Checks if student list is empty
    if not students:
        print("No students available")
        return
    
    # Loop through and display each student
    for student in students:
            print("Name: ", student["Name"])
            print("Major: ", student["Major"])
            print("Graduation Year: ", student["Graduation Year"])
            print()

# Searches for the students by name
def search_students():

    search_name = input("What is the name of the student you are looking for? ")

    # Tracks whether a student was found
    found = False

    # Loop through students to find  match
    for student in students:

        # Compare student name with search input
        if student["Name"].lower() == search_name.lower():

            # Display matching studenyt information
            print("Name: ", student["Name"])
            print("Major: ", student["Major"])
            print("Graduation Year: ", student["Graduation Year"])
            print()

            found = True

    # Display message if no matching student exists
    if not found:
        print(f"The student {search_name} could not be found \n")

# Deletes a student from the system
def delete_students():

    delete_student = input("What is the name of the student you want to delete? ")

    # Tracks whether a student was found
    found = False

    # Searches for a matching student
    for student in students:

        # Removes matching student
        if student["Name"].lower() == delete_student.lower():
            students.remove(student)
            save_students()
            print("Student removed successfully")
            found = True

            # Exit loop after deletion
            break

    # Display message if student was not found
    if not found:
        print(f"The student {delete_student} could not be found. \n")

# Function updates the student's major if they want to change
def update_students():
    found = False

    update_name = input("What is the name of the student whose major you want to update? ")

    for student in students:
        if student["Name"].lower() == update_name.lower():
            new_major = input("What is the student's new major? ")
            student["Major"] = new_major
            print("Student updated successfully \n")

            found = True
            save_students()

            break
    if not found:
        print(f"The student {update_name} could not be found. \n")

print()


# Runs load_student function
load_students()

# Main application loop
while True:

    # Display menu options
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Delete Students")
    print("5. Update Students")
    print("6. Exit \n")

    # Get user menu selection
    choice = input("Choose an option: ")

    print()

    # Run selected menu features
    if choice == "1":
        add_students()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_students()

    elif choice == "4":
        delete_students()
    
    elif choice == "5":
        update_students()

    # Exit application
    elif choice == "6":
        break

    # Handle invalid menu input
    else:
        print("Invalid Option")
