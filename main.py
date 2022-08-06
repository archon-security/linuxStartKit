import os, platform
from time import sleep

def vefOs():
    os = platform.platform()
    if 'ARCH' or 'MANJARO' in os.upper():
        exec(open("arch.py").read())
    elif 'DEBIAN' or 'UBUNTU' in os.upper():
        exec(open("debian.py").read())

varstart="\033[1;32m"
negrito="\033[1m"
varend="\033[m"
banner = open("banner.txt", "r").read()

print("{}{}{}{}".format(varstart, banner, negrito, varend))
print("{}A caceta desse programa tem como intuito fazer a configuraçção inicial do seu linux, leia a readme para melhor uso{}\n\n".format(negrito, varend))
print("\033[1;31mBy: Azz4\033[m")
q = input("Tecle S para prsseguir: ")
if q == 'S' or 's':
    vefOs()

        
