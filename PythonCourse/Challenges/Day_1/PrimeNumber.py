a = int(input("Enter a number>"))

if a <= 0:
    print("Invalid Number")

counter = 0

for i in range (1,a):
    if a%i == 0:
        counter += 1 
if counter == 1:
    print("Prime Number")
else:
    print("Non-Prime Number")
