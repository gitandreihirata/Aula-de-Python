
#Receba 3 numeros pelo usuário
#e mostre qual o maior numero e o menor número

# Recebendo três números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Encontrando o maior e o menor número
maior_numero = max(num1, num2, num3)
menor_numero = min(num1, num2, num3)

# Exibindo o maior e o menor número
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
