# Write a program to convert days into years, weeks and days.10

 
                       
days = int(input("Enter the num1 : "))
# years = int(input("Enter the num3 : "))
# weeks = int(input("Enter the num3 : "))

# days = 1000
years = days // 365 #floor give us perfect answer without decimal point
#print(years)

day = days % 365 # modulus give reminder
#print(days)

weeks = days // 7 
#print(weeks)

days = days % 7
print(f'Years :{years}, Weeks :{weeks}, Days :{days}. ')