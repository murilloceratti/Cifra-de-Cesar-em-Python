# Cifra de César - Criptografia
# Murillo Ceratti Madalozzo

import os
from colorama import Fore, Back, Style, init
init()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
chave = 3


def codificar():
    mensagem_cript = ''
    os.system('cls') # Caso você esteja utlizando linux, substitua o comando.
    mensagem_codificar = input('Mensagem: ').lower()


    for letra in mensagem_codificar: 
                
        if letra in alfabeto:

            posicao = alfabeto.index(letra)
            nova_posicao = (posicao + chave) % 26
            mensagem_cript += alfabeto[nova_posicao]

        else:
            mensagem_cript += letra
    os.system('cls')
    print('Mensagem Criptografada:',mensagem_cript)
    input('Pressione ENTER para continuar...')
    os.system('cls')

def descodificar():
    mensagem_descript = ''
    os.system('cls')
    mensagem_descodificar = input('Mensagem: ').lower()

    for letra in mensagem_descodificar:

            if letra in alfabeto:

                posicao = alfabeto.index(letra)
                nova_posicao = (posicao - chave) % 26
                mensagem_descript += alfabeto[nova_posicao]
            
            else:
                mensagem_descript += letra
    os.system('cls')
    print('Mensagem Descriptografada:',mensagem_descript)
    input('Pressione ENTER para continuar...')
    os.system('cls')
    

while True:

    try:
        largura = 50

        borda_superior = "╔" + "═" * (largura - 2) + "╗"
        borda_inferior = "╚" + "═" * (largura - 2) + "╝"
        divisor        = "╟" + "─" * (largura - 2) + "╢"

        print(borda_superior)
        print(f"║{Fore.YELLOW + 'CIFRA DE CÉSAR'.center(largura - 2)+ Style.RESET_ALL}║")
        print(divisor)
        print(f"║ {'[1] Codificar Mensagem'.ljust(largura - 3)}║")
        print(f"║ {'[2] Decodificar Mensagem'.ljust(largura - 3)}║")
        print(f"║ {'[3] Sair'.ljust(largura - 3)}║")
        print(borda_inferior)

        op = int(input('Escolha uma opção para prosseguir: '))

        if op == 1:
            codificar()
        elif op == 2:
            descodificar()
        elif op == 3:
            break
    except ValueError:
        print('Insira um valor válido.')

