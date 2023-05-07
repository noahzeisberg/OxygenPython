import os

import psutil
from colorama import init, Back, Fore

init(convert=True)
color = Fore.LIGHTMAGENTA_EX
bg_color = Back.LIGHTMAGENTA_EX
idle_color = Fore.LIGHTBLACK_EX
bg_idle_color = Back.LIGHTBLACK_EX


def get_percentage(n: float, v: float):
    return round(n / v * 100)


def bars(percentage: int):
    bar_string = ""
    for i in range(round(percentage / 2)):
        bar_string += bg_color + " " + Back.RESET
    for i in range(50 - round(percentage / 2)):
        bar_string += bg_idle_color + " " + Back.RESET
    return bar_string


def get_memory_usage():
    max_memory = round(psutil.virtual_memory().total / 1024 / 1024)
    used_memory = round(psutil.virtual_memory().used / 1024 / 1024)
    print("Memory usage: " + color + str(used_memory) + "GB" + Fore.RESET + " of " + color + str(max_memory) + "GB")
    print(bars(get_percentage(used_memory, max_memory)))


def get_cpu_usage():
    processor_usage = psutil.cpu_percent()
    print("Processor usage: " + color + str(processor_usage) + "%")
    print(bars(round(processor_usage)))


print(color +
      """_______                                         
__  __ \____  _______  _________ ______ _______ 
_  / / /__  |/_/__  / / /__  __ `/_  _ \__  __ \\
/ /_/ / __>  <  _  /_/ / _  /_/ / /  __/_  / / /
\____/  /_/|_|  _\__, /  _\__, /  \___/ /_/ /_/ 
                /____/   /____/                 
""" + Fore.RESET)
get_memory_usage()
print(Fore.RESET)
get_cpu_usage()
print(Fore.RESET)
os.system("pause")
