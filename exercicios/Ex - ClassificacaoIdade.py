#Enunciado: Escreva um programa que 
# pergunte ao usuário sua idade e, 
# com base na resposta, classifique-o 
# em uma das seguintes categorias:
#  "Criança" (0-12 anos),
#  "Adolescente" (13-17 anos), 
# "Adulto" (18-64 anos), ou 
# "Idoso" (65 anos ou mais).



idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é classificado como: Criança.")
elif idade >= 13 and idade <= 17:
    print("Você é classificado como: Adolescente.")
elif idade >= 18 and idade <= 64:
    print("Você é classificado como: Adulto.")
elif idade >= 65:
    print("Você é classificado como: Idoso.")
else:
    print("Idade inválida! Por favor, digite um número positivo.")
