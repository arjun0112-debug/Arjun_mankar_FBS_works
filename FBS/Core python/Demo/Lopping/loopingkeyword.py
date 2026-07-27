#1. pass : to neglate expected indentation error

# for i in range(1,10):
#     pass

# #2. break : to terminate the loop
# for i in range(1,11):
#     if (i == 3):
#         break 
#     print(i)
    
# #3. Continue: to stop current iteration only
# for i in range(1,11):
#     if(i == 3):
#         continue
#     print(i)    

#4. else: Will execute when loop executed successfully
for i in range(1,5):
    if(i == 3):
        continue
    print(i)
else:
    print("For loop executed successfully ")    
    