# wooo shellllllss
import sys
import os
import subprocess

def print_prompt():
    split = os.getcwd().split('/')
    return split[len(split) - 1] + '> '

def run_shell():
    prev_dir = os.getcwd()
    curr_dir = os.getcwd()
    print(curr_dir)

    while True:
        line = input(print_prompt())
        lst = line.split(' ')
        length = len(lst)
        if length > 0:
            code = subprocess.call(line, shell=True)
            line = line.strip()
            split_line = line.split(' ')
            if code == 0 and "cd" in line:
                if line == "cd":
                    prev_dir = curr_dir
                    os.chdir("~/")
                    curr_dir = os.getcwd()
                elif line == "cd .":
                    prev_dir = curr_dir
                elif line == "cd ..":
                    prev_dir = curr_dir
                    os.chdir("..")
                    curr_dir = os.getcwd()
                elif len(split_line) == 2:
                    prev_dir = curr_dir
                    os.chdir(split_line[1])
                    curr_dir = os.getcwd()
            print(code)

run_shell()
