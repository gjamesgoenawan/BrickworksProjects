a = int(input("Enter a number>"))

if a <= 0:
    print("Invalid Number")

for i in range(1,a+1,2):
    for j in range (0,int((a-i)/2)):
        print(" ", end = "")
    for j in range(i):
        print("*", end = "")
    for j in range (0,int((a-i)/2)):
        print(" ", end = "")
    print("")
