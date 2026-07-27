# Convert the time entered int hh,min and sec into seconds

hh = int(input("Enter the value hh : "))
min = int(input("Enter the value min : "))
sec = int(input("Enter the value sec : "))

total = (hh * 3600)+(min * 60)+sec
print(total)