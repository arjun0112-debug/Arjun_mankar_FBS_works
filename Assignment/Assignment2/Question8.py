#Write a program to swap two numbers using third variable.

a = int(input("Enter the num1 : "))
b = int(input("Enter the num2 : "))

c = a
a = b
b = c

print(a)
print(b)