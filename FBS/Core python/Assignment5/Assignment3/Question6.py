# Write a program to calculate Profit or loss.


num1 = int(input("Enter the cost price :"))
num2 = int(input("Enter the selling price :"))

if num1 < num2:
    print("Profit")

elif num1 > num2:
    print("Loss")
        
else:
    print("Their is no profit not loss")    