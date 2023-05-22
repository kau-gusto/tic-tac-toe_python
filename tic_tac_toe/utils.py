import os
import sys


def clear():
    command = "clear"
    if sys.platform.startswith("win"):
        command = "cls" 
    os.system(command)
