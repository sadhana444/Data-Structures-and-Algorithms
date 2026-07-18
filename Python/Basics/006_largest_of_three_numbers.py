num1=int(input("Enter a 1st number:"))
num2=int(input("Enter a 2nd number:"))
num3=int(input("Enter a 3rd number:"))
if num1>num2 and num1>num3:
    print(num1,"is greatest number")
elif num2>num1 and num2>num3:
    print(num2, "is greatest number")
elif num3>num2 and num3>num1:
    print(num3, "is greatest number")    
else:
    print("All numbers are equal")
