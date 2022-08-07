import os, platform
from time import sleep
sys = os.system

def vefOs():
    so = platform.platform()
    if "ARCH" in so.upper() or "MANJARO" in so.upper():
        sys("python3 src/arch.py")
    elif "DEBIAN" in so.upper() or "UBUNTU" in so.upper():
        sys("python3 src/debian.py")
    else:
        sleep(1)
        print('''Não foi possível detectar seu OS!
        Se você tiver certeza do que está fazendo,
        digite o nome do seu OS abaixo: ''')
        secondSO = input("Insira seu OS: ")
        try:
            sys(f"python3 src/{secondSO.lower()}.py")
        except:
            print("Não foi possível encontrar os arquivos de instalação para este OS!")

varstart="\033[1;32m"
negrito="\033[1m"
varend="\033[m"
banner = open("src/banner.txt", "r").read()

print("{}{}{}{}".format(varstart, banner, negrito, varend))
print("{}A caceta desse programa tem como intuito fazer a configuraçção inicial do seu linux, leia a readme para melhor uso{}\n\n".format(negrito, varend))
print("\033[1;31mBy: Azz4\033[m")
q = input("Tecle S para prsseguir: ")
if q == 'S' or 's':
    vefOs()

        
