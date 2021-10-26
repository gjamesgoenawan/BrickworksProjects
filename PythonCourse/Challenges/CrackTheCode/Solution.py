import os
import sys
from subprocess import call
hashseed = os.getenv('PYTHONHASHSEED')

if not hashseed:
    call([sys.executable, sys.argv[0]], env={'PYTHONHASHSEED': '0'})
    exit()

f = open("password.txt", "r")
hashes = f.readlines() 
result = []
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
f.close()
for i in hashes:
    i = i.strip()
    for j in possible_characters:
        if i == str(hash(j)):
            result.append(j)

print("\nCracked Password:")
for i in result:
    print(i, end="")
print("")
