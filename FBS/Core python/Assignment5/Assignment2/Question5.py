# WAP to calculate selling price of book based on cost price and discount

cost = int(input("Enter the cost price : "))
discount = int(input("Enter the discount : "))

discount_price = cost * discount / 100

selling_price = cost - discount_price

print(f'discount is {discount_price} , \n  selling price is {selling_price}')