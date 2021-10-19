def compute(text):
    current = 0
    temp = 0
    current_sign = "+"
    for i in text:
        if i in "+-*/=":
            if current_sign == "+":
                current = current + temp
            if current_sign == "-":
                current = current - temp
            if current_sign == "*":
                current = current * temp
            if current_sign == "/":
                current = current / temp    
            temp = 0
            if i == "=":
                return current
            else:
                current_sign = i

        else:
            temp = temp * 10 + int(i)
            


a = input("Enter an equation>")

for i in a:
    if i.isalpha():
        print("No Alphabet should be present")
        exit()

if a.find(".")!=-1:
    print("All numbers must be integer(s)")
    exit()

if a[len(a)-1] != "=":
    a = a + "="

print(compute(a))


