from os import system as sys
from time import sleep

varstart="\033[1;32m"
negrito="\033[1m"
varend="\033[m"
sys("clear")

def main():
    banner = open("banner.txt", "r").read()
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
    sys("sudo pacman -Sy --needed - <rec_packages_arch.txt --noconfirm")
    
def installPackages():
    print("Instalando pacotes apartir da lista de backup")
    sys("sudo pacman -Sy --needed - <arch_packages.txt")
    
    
def packageList():
    print("Criando txt com lista de pacotes do sistema")
    sys("pacman -Q > arch_packages.txt")
    print("Lista de pacotes completo.")
    sys("tar -cjf pacman_database.tar.bz2 /var/lib/pacman/local")
    print("Backup da base de dados do pacman realizado.")
    print("Caso queira restaurar a base de dados, basta move o arquivo \033[0;31m pacman_database.tar.bz2\033[m para o diretorio \033[0;31m /\033[m  e depois dar o comando \033[0;31m tar -xjvf pacman_database.tar.bz2\033[m")
    

main()