import sys

def no_print(s):
    s = str(s)
    sys.stdout.write(s)
    sys.stdout.flush()

def backspace(s):
    s = str(s)
    for i in s:
        no_print('\b')
