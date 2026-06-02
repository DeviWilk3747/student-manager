import os
class Student:
    def __init__(self, name, major, graduation_year):
        self.name = name
        self.major = major
        self.graduation_year = graduation_year


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):

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
        new_student = Student(
                                name,
                                major,
                                graduation_year
                                )
    
        # Add student dictionary to list
        self.students.append(new_student)

        # Saves student data to file
        self.save_student()

        print(type(self.students[0]))
        print("Student added successfully!\n")

    # Displays all the students that are currently stored
    def view_student(self):

        # Checks if student list is empty
        if not self.students:
            print("No students available")
            return
    
        # Loop through and display each student
        for index, student in enumerate(self.students, start=1):
            print(f"{index + 1}. {student.name}")
            print("Major: ", student.major)
            print("Graduation Year: ", student.graduation_year)
            print()

    # Searches for the students by name
    def search_student(self):

        search_name = input("What is the name of the student you are looking for? ")

        # Tracks whether a student was found
        found = False

        # Loop through students to find  match
        for student in self.students:

            # Compare student name with search input
            if student.name.lower() == search_name.lower():

                # Display matching studenyt information
                print("Name: ", student.name)
                print("Major: ", student.major)
                print("Graduation Year: ", student.graduation_year)
                print()

                found = True

        # Display message if no matching student exists
        if not found:
            print(f"The student {search_name} could not be found \n")


    # Deletes a student from the system
    def delete_student(self):

        delete_student = input("What is the name of the student you want to delete? ")

        # Tracks whether a student was found
        found = False

        # Searches for a matching student
        for student in self.students:

            # Removes matching student
            if student.name.lower() == delete_student.lower():
                self.students.remove(student)
                self.save_student()
                print("Student removed successfully")
                found = True

                # Exit loop after deletion
                break

        # Display message if student was not found
        if not found:
            print(f"The student {delete_student} could not be found. \n")

    # Function updates the student's major if they want to change
    def update_student(self):
        found = False

        update_name = input("What is the name of the student whose major you want to update? ")

        for student in self.students:
            if student.name.lower() == update_name.lower():
                new_major = input("What is the student's new major? ")
                student.major = new_major
                print("Student updated successfully \n")

                found = True
                self.save_student()

                break
        if not found:
            print(f"The student {update_name} could not be found. \n")

    # Rewrites the student file using the current students list
    def save_student(self):

        file_path = os.path.join(
            os.path.dirname(__file__),
            "student_manager.txt"
        )
        with open(file_path, "w") as file:

            for student in self.students:
                file.write(f"{student.name}, {student.major}, {student.graduation_year}\n")
    

    # Loads students that may already exist
    def load_student(self):
        self.students.clear()
        file_path = os.path.join(
            os.path.dirname(__file__),
            "student_manager.txt"
        )
        try:
            with open(file_path, "r") as file:

                # Loops through lines in the file
                for line in file:
                    parts = line.strip().split(",")
    
                    name = parts[0].strip()
                    major = parts[1].strip()
                    graduation_year = int(parts[2].strip())

                    student = Student(
                        name,
                        major,
                        graduation_year
                    )
    
                    self.students.append(student)

            return
        
        except FileNotFoundError:
            print("The file does not exist.")


    def run(self):
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
                self.add_student()

            elif choice == "2":
                self.view_student()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.delete_student()
    
            elif choice == "5":
                self.update_student()

            # Exit application
            elif choice == "6":
                break

            # Handle invalid menu input
            else:
                print("Invalid Option")



student = StudentManager()
student.load_student()
student.run()