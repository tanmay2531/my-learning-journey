def create_study_plan():
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
def track_study_hours():
    print("Opening Study Tracker...")
    time = int(input("How many hours did you study today?:"))
    if time >= 8:
        print("Outstanding Effort!")
    elif time >= 5:
            print("Great Consistency!")
    elif time >= 3:
            print("Good, but try to study a bit more tomorrow.")
    else:
            print("Let's improve tomorrow!")
def resource_tools():
    print("Opening Resource Tools...")
    print("Feature under development...")
while True:
    print("=" * 40)
    print("PROJECT ASTRA")
    print("=" * 40)
    print("1. Create Study Plan")
    print("2. Track Study Hours")
    print("3. Authenticate Resources / Find Resources")
    print("4. Exit")
    print("=" * 40)
    
        
    choice = input("Enter your choice: ")

    if choice == "1":
        create_study_plan()

    elif choice == "2":
        track_study_hours()

    elif choice == "3":
        resource_tools()

    elif choice == "4":
        print("Thank You for using ASTRA!")
        break

    else:
        print("Invalid choice.")