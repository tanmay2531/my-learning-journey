Num = int(input("Enter the number:"))
i = int(input("Enter the value till which table is to be printed:"))
print("=" * 30)
print("Multiplication Table of ",Num)
print("=" * 30)
for i in range(1,(i+1)):
    print(Num ,"x" ,i, "=" ,Num*i)
    