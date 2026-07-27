# for i in range(1,5):
#     for j in range(1,5):
#         print(4*i , end = ' ')
#     print()



no = int(input("Enter the number :"))
row = int(input("Enter the Row :"))
col = int(input("Enter the column :"))

for i in range(1,row+1):
    for j in range(1,col+1):
        print(j*no , end = ' ')
    print()