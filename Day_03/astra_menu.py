print("=" * 40)
print("PROJECT ASTRA")
print("=" * 40)
print("1. Create Study Plan")
print("2. Track Study Hours")
print("3. Authenticate Resources / Find Resources")
print("4. Exit")
print("=" * 40)
while True:
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nOpening Study Planner...\n")

        exam = input("Enter the exam name: ")
        days = int(input("Days left for the exam: "))
        target = int(input("Target marks to be scored: "))

        print()
        print("=" * 40)
        print("Study Plan Created")
        print("=" * 40)
        print("Exam       :", exam)
        print("Days Left  :", days)
        print("Target     :", target)
        print("Good Luck!")
        print("=" * 40)

        hours = int(input("How many hours can you study daily? "))

        if hours >= 6:
            print("Excellent Dedication!")
        elif hours >= 4:
            print("Good Pace.")
        else:
            print("Increase your study time.")

    elif choice == "2":
        print("Opening Study Tracker...")

    elif choice == "3":
        print("Opening Resource Tools...")

    elif choice == "4":
        print("Thank You for using ASTRA!")
        break

    else:
        print("Invalid choice.")