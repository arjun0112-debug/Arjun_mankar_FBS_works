# Write a program to reverse three-digit number

digit = int(input("Enter the three digit number : "))

num1 = digit // 100

num2 = digit // 10 % 10

num3 = digit % 10

reverse = num3 * 100 + num2 * 10 + num1

print(f'The reverse digit is : {reverse}')