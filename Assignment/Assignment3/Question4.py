# Write a program to input all the sides of a triangle and check whether triangle is valid or not.

a1 = int(input("Enter the side1 : "))
a2 = int(input("Enter the side2 : "))
a3 = int(input("Enter the side3 : "))

if (a1 + a2 > a3) and (a2 + a3 > a1) and (a3 + a1 > a2):
    print("It is valid")
    
else:
    print("It is invalid")    
    