#Sorteia números e voce tem que acertar
#IA que ajuda a decidir se o número deve ser maior ou menor 
# do que vc chutou.

import random

def jogo_adivinhacao():
    # Sorteia um número aleatório entre 1 e 100
    numero_sorteado = random.randint(1, 100)
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando (entre 1 e 100).")
    
    tentativas = 0
    acertou = False
    
    # Loop até o usuário acertar
    while not acertou:
        # Recebe a tentativa do usuário
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1
        
        # Verifica se o número está correto
        if palpite == numero_sorteado:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_sorteado:
            print("O número é maior do que você digitou. Tente novamente.")
        else:
            print("O número é menor do que você digitou. Tente novamente.")

# Chama a função para iniciar o jogo
jogo_adivinhacao()