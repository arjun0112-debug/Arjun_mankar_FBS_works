# Convert distant given in feet and inches into meter and centimeter.
# d = int(input("Enter the distant in feet : "))
# a = int(input("Enter the distant in inches : "))

# q = d*0.3048  #converting feet into meter 
# r = d*30.48  #converting feet into centimeter

# s = a*0.0254 #converting inches into meter
# p = a*2.54  #converting inches into centimeter

# print(f'{q}is the conversion feet {d} into m , \n {r} is the conversion of feet {d} into cm')
# print(f'{s}is the conversion inches {a} into m, \n {p} is the conversion of inches {a} into cm')


feet = int(input("Enter the feet : "))
inches = int(input("Enter the inches : "))

a = feet * 12 + inches  # feet * 12 + inches = total inches
b = inches * 2.54  # inches * 2.54 = centimeter value
c = b/100  # centimeter/100 = meter value 

print(f'meter = {c} : ,\n  centimeter = {b} : ')