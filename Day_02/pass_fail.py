Name = input("Enter the name of the student:")
Marks = int(input("ENter the marks:"))
if Marks >= 90:
    print(Name,"got A grade in exams.")
elif Marks >= 75 and Marks < 90:
    print(Name,"got B grade in exams.")
elif Marks >= 60 and Marks < 75:
    print(Name,"got C grade in exams.")
elif Marks >= 40 and Marks < 60:
    print(Name,"got D grade in exams.")
else:
    print(Name,"Failed in the exams.")