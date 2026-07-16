name = input("Enter the name of the student:")
p = int(input("Enter the marks obtained in physics:"))
c = int(input("Enter the marks obtained in chemistry:"))
m = int(input("Enter the marks obtained in maths:"))
total_marks = p + c + m 
average = (total_marks)/3
print("======RESULT======")
print("Name:", name)
print("Physics:", p)
print("Chemistry:", c)
print("Maths:", m)
print("Total Marks Obtained:", total_marks)
print("Average of all three subjects:", average)
print("="* 35)