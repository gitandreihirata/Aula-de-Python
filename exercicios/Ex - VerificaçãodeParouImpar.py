#Enunciado: Escreva um programa que 
# peça ao usuário para inserir um 
# número inteiro. O programa deve 
# verificar se o número é par ou ímpar
#  e exibir uma mensagem apropriada.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

