# Find the sum of three digit number

digit = int(input("Enter the three digit number : "))


num1 = digit // 100

num2 = digit // 10 % 10

num3 = digit % 10

sum = num1 + num2+ num3

print(sum)
