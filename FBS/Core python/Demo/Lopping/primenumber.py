# num = int(input("Enter the number"))
# if(num > 1):
    
#     for i in range(2,num):
#         print(i)
#         if (num % i == 0):
#             print(f'{num} is not a prime number.')
#             break
    
#     else:
#         print(f'{num} is a prime number.')
# else:
#     print(f'{num} is a prime number.')
    
    
# #num = int(input ("Enter number ="))
# if(num>1):
#     for i in range(2, num // 2 + 1):
#         print(i)
#         if(num % i == 0):
#             print(f"{num} is not prime number...")
#             break
#     else:
#         print(f"{num} is a prime number...")

# else:
#     print(f"{num} is not prime number")        

start = int(input("Enter the starting number = "))
endvr = int(input("Enter the ending number = "))

print(f"The prime number from {start} to {endvr}.")
for num in range(start,endvr):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
    else:
        print("The number is not prime num composite")            