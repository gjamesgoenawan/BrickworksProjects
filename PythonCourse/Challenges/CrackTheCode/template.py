import os
import sys
from subprocess import call
hashseed = os.getenv('PYTHONHASHSEED')

if not hashseed:
    call([sys.executable, sys.argv[0]], env={'PYTHONHASHSEED': '0'})
    exit()

// Write Your Code Below!
