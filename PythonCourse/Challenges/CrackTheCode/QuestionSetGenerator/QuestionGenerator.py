import os
import sys
from subprocess import call
hashseed = os.getenv('PYTHONHASHSEED')

if not hashseed:
    call([sys.executable, sys.argv[0]], env={'PYTHONHASHSEED': '0'})
    exit()

a = input(">")
result = []
for i in a:
    result.append(str(hash(i)) +"\n")
f = open("password.txt", "a")
f.writelines(result) 
f.close()