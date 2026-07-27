# Multiple condition with dependenies

#Next condition is depend on true or false or some privious condition according to the secnorios
# branching inside branding 
# branching in branching


gender = (input("Enter the age : "))
age = int(input("Enter the age : "))

if(gender == "f"):
    if (age >= 18):
        print('Girl is eligible to marriage.')
    else:
        print('Pehele padhai kar lo .')
 
else:
    if(age >= 21):
        print('Boy is eligible for marriage')
    else:
        print('Pehele kam kar lo ')                
    
    
    
