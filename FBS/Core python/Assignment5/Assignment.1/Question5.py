# write a program to enter P.T.R and calculate Compound Interest.

P = int(input("Enter the num1 : "))
T = int(input("Enter the num2 : "))
R = int(input("Enter the num3 : "))
N = int(input("Enter the num4 : "))

CI = P * (1 + R / (100 * N)) ** (N * T) - P

print("Compound intrest : ", CI)