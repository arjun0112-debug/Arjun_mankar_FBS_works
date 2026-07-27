# # multiple conditon 
 

#check month in digit

# num = int(input("Enter the num :"))

# if (num == 1):
#     print("January : ")

# elif(num == 2):
#     print("February : ")
    
# elif(num == 3):
#     print("March : ")
   
# elif(num == 4):
#     print("April : ")
    
# elif(num == 5):
#     print("May : ")                
    
# elif(num == 6):
#     print("June : ")
    
# elif(num == 7):
#     print("July : ")
    
# elif(num == 8):
#     print("August : ")
    
# elif(num == 9):
#     print("September : ")
    
# elif(num == 10):
#     print("Octomber : ")
    
# elif(num == 11):
#     print("November : ")
    
# elif(num == 12):
#     print("December : ")
    
# else:
#     print("Invalid : ")                    
            
            

num = int(input("Enter the num :"))

if(num > 0):
        
    if (num < 50):
        print("The number is between 0 to 50 : ")
    elif(num < 100):
        print("The number is between 50 to 100 : ")        
        
    elif(num < 150):
        print("The number is between 100 to 150 : ") 
       
    elif(num < 250):
        print("The number is between 150 to 250")       
        
    else:
        print("The number is less than 0 : ")    