# Write a program to take input of angles of triangle and check it is valid triangle or not

a1 = int(input("Enter the angle1 :"))
a2 = int(input("Enter the angle2 :"))
a3 = int(input("Enter the angle3 :"))

if a1 + a2 + a3 == 180:   #sum of angle of triangle is 180
    print(" The triangle is valid : ")
    
else:
    print(" The triangle is invalid :")    