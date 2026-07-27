# Write a program to check whether the triangle  is equilateral isosceles or scalene triangle.

a1 = int(input("Enter the angle1 :"))
a2 = int(input("Enter the angle2 :"))
a3 = int(input("Enter the angle3 :"))


if(a1 + a2 + a3 < 180):
    
    if(a1 == a2 == a3):
        print("Their is equilateral triangle.")
   
    elif(a1 == a2 != a3):
        print("Their is isoscele triangle.")
    
    elif(a1 != a2 != a3):
        print("Their is a scalene.")    
        
else:
    print("This is not triangle ")        