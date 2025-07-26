def add_student(students, name, marks):
    if name in students:
        print(f"{name} is already in the record.")
    else:
        students[name] = marks
        print(f"Added {name} with marks {marks}.")

def update_marks(students, name, marks):
    if name in students:
        students[name] = marks
        print(f"Marks updated for {name} to {marks}.")
    else:
        print(f"{name} is not found in the record.")

def display_records(students):
    if not students:
        print("No records found.")
    else:
        print("Student Records:")
        for name, marks in students.items():
            print(f"{name}: {marks}")

def calculate_stats(students):
    if not students:
        print("No records found.")
        return

    marks_list = list(students.values())
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)
    average_marks = sum(marks_list) / len(marks_list)

    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Average Marks: {average_marks}")

def main():
    students = {}

    while True:
        print("\nStudent Marks Management System")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Display All Records")
        print("4. Calculate Statistics")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            marks = float(input("Enter marks: "))
            add_student(students, name, marks)
        elif choice == '2':
            name = input("Enter student name to update marks: ")
            marks = float(input("Enter new marks: "))
            update_marks(students, name, marks)
        elif choice == '3':
            display_records(students)
        elif choice == '4':
            calculate_stats(students)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
