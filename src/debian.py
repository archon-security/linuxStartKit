import os
from time import sleep
varstart = '\033[1;32m'
negrito = '\033[1m'
varend = '\033[m'
os.system('clear')


def main():
    banner = open("banner.txt","r").read()
    print("{}{}{}{}".format(varstart, negrito,banner, varend))
    print("A caceta desse programa tem como intuito fazer a configuração inicial do seu Linux\n\n")
    print("     1 - Instalação completa de programas recomendados")
    sleep(0.5)
    print("     2 - Instalar lista de pacotes")
    sleep(0.5)
    print("     3 - Criar lista de pacotes instalados")
    sleep(0.5)
    op = int(input("Escolha uma opção: "))
    if op == 1:
        installCompl()
    elif op == 2:
        installPackages()
    elif op == 3:
        packagesList()
    
def installCompl():
    print("Nada pra ver aqui")
    
def installPackages():
    print("Nada pra ver aqui")
    
def packageList():
    print("Nada pra ver aqui")
    

main()