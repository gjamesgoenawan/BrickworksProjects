def fibo(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
            


a = int(input("Enter a Number>"))

if a<0:
    print("Invalid Input")
    exit()

print(fibo(a))


