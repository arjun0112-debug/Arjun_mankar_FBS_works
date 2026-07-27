# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.


x = int(input("Enter the amount :"))
two_hundred = x // 200
rem = x % 200
print(f'to represent amount of {x} Rs into the 200 notes the user needs to {two_hundred} notes of 200 Rs. note and {rem} Rs.')

five_hundred = x // 500
rem = x % 500
print(f'to represent amount of {x} Rs into the 500 notes the user needs to {five_hundred} notes of 500 Rs. note and {rem} Rs.')

Hundred = x // 100
rem = x % 100
print(f'to represent amount of {x} Rs into the 100 notes the user needs to {Hundred} notes of 100 Rs. note and {rem} Rs.')

fifty = x // 50
rem = x % 50
print(f'to represent amount of {x} Rs into the 50 rs notes the user needs to {fifty} notes of 50 Rs. note and {rem} Rs.')

twenty = x // 20
rem = x % 20
print(f'to represent amount of {20} Rs into the 20 rs notes the user needs to {twenty} notes of 20 Rs. note and {rem} Rs.')

ten = x // 10
rem = x % 10
print(f' to represnt amoutn of {10} Rs into the 10 notes the user needs to {ten} notes of 10 Rs. note and {rem} Rs.')