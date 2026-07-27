# Write a program to swap two numbers witout using third variable

a = int(input("Enter the num1 : "))
b = int(input("Enter the num2 : "))

b , a = a , b

print(f'swap value of a {a}, and swap value of b {b}')