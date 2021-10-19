a = int(input("Enter a number>"))

if a <= 0:
    print("Invalid Number")

for i in range (1,a+1):
    for j in range (0,i):
        print("*", end="")
    print("")
