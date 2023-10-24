from time import sleep
import time
import os
import sys


def typing_print(text, sec=0.02):
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(sec)

def typing_print_emoji(text, sec=0.02):
    print("""\n♡/) /)\n( •֊•)♡:""")
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(sec)
    print("\n")

def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clear_screen():
    os.system("clear")
