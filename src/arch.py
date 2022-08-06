import os
from time import sleep

varstart="\033[1;32m"
negrito="\033[1m"
varend="\033[m"
os.system("clear")

def main():
    banner = open("../banner.txt", "r").read()
    print("{}{}{}{}".format(varstart, negrito, banner, varend))
    print("A caceta desse programa tem como intuito fazer a configuraçção inicial do seu linux\n\n")
    print("     1 - Instalação completa de programas recomendados")
    sleep(1.0)
    print("     2 - Instalar lista de pacotes")
    sleep(1.0)
    print("     3 - Listagem de pacotes instalado")
    sleep(1.0)
    op = int(input("Escolha uma opção: "))
    if op == 1:
        installCompl()
    elif op == 2:
        installPackages()
    elif op == 3:
        packageList()

def installCompl():
    print("Instalando programas")
    os.system("sudo pacman -Sy --needed - <recommended_packages.txt --noconfir")
    
def installPackages():
    print("Instalando pacotes apartir da lista de backup")
    os.system("sudo pacman -Sy --needed - <arch_packages.txt")
    
    
def packageList():
    print("Criando txt com lista de pacotes do sistema")
    os.system("pacman -Q > arch_packages.txt")
    

main()