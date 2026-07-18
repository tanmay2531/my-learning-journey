print("=" * 40)
print("PROJECT ASTRA")
print("=" * 40)
print("1. Create Study Plan.")
print("2. Track Study Hours.")
print("3. 4Authenticize Resources/Find Resources")
print("4. Exit.")
print("=" * 40)

choice = input("Enter your choice:")
if choice == "1":
    print("Opening Study Planner...")
    exam = input("Enter the exam name:")
    print("\n",exam)
    days = int(input("Days left for the exam?"))
    print("\n",days)
    target = int(input("Target marks to be scored?"))
    print("\n",target)
    print("\n""\n")
    print("=" * 20)
    print("Study Plan Created.")
    print("Exam:",exam)
    print("Days Left:",days)
    print("Target:",target)
    print("Good Luck!")
elif choice == "2":
    print("Opening Study Tracker:")
elif choice =="3":
    print("Opening Resource Tools...")
elif choice == "4":
    print("Thank You for using ASTRA!")
else:
    print("Invalid choice.")
