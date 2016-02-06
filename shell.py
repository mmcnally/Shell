# wooo shellllllss
import sys
import os
import subprocess

curr_dir = os.getcwd()
print(curr_dir)

def print_prompt():
    return '> '
#    print('> ', end="", flush=True)

def run_shell():
    while True:
        line = input(print_prompt())
        lst = line.split(' ')
        length = len(lst)
        # print(length, flush=True)
        if length > 0:
            code = subprocess.call(line, shell=True)
            print(code)
            

run_shell()
    
