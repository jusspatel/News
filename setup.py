try:
    import pyfiglet
    import subprocess
    from subprocess import Popen
    import os
    import re
    import sys
    from colorama import * 
    import platform
    from tkinter import*
    from tkinter.ttk import*


except ImportError:
    os.system("pip3 install pyfiglet", shell=True)
    os.system("pip3 install coloroma", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("WEATHER APP SETUP")
print(ascii_banner)
init()
print(Fore.CYAN + " [+] ©Instant Devs Corp. 2020")
print(' ')
print(Fore.CYAN + " [+] Setting up WEATHER APP")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : 1.1.0")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.CYAN + "Developer : Juss Patel from Cyberites")

input('\n [=] Press Enter to download modules')
print("Please wait")
os.system('pip install requests')
os.system('pip install datetime')
os.system('pip install Pillow')

print(Fore.CYAN + " [+] OPENING APP ")

Popen('Gnews Pro.py', shell=True)



