# Write a program to prompt user to enter userid and password. After verifying userid and password display



start = int(input("Enter the starting number: "))
n = int(input("Enter the ending number: "))

for i in range(start, n + 1):
    if i % 2 != 0:
        print(i)