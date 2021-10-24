arr = []
for i in range (5):
    a = input("Enter a Word>")
    arr.append(a)

cnt = None
max_length = None
for i in arr:
    if max_length == None or len(i)> max_length:
        cnt = i
        max_length = len(i)
print(cnt)