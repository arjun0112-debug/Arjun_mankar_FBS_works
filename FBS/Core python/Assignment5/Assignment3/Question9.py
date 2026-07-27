# Input 5 subject marks from user and display grade(eg. first class. Second class..)

sub1 = int(input("Enter the marks :"))
sub2 = int(input("Enter the marks :"))
sub3 = int(input("Enter the marks :"))
sub4 = int(input("Enter the marks :"))
sub5 = int(input("Enter the marks :"))

total = (sub1 + sub2 + sub3 + sub4 + sub5)

percentage = total / 500 * 100
# print("percentage")

if percentage >= 90:
    print(f"Grade : First class \npercentage is {percentage} \nMarks = {total}/500")
    
elif percentage >= 70:
    print(f"Grade : Second class \npercentage is {percentage} \nMarks = {total}/500")    
        
elif percentage >= 60: 
    print(f"Grade : Third class \npercentage is {percentage} \nMarks = {total}/500")       
    
elif percentage >= 35: 
    print(f"Grade : Pass \npercentage is {percentage} \nMarks = {total}/500")
        
else:
    print(f"Grade : Fail \npercentage is {percentage} \nMarks = {total}/500")        