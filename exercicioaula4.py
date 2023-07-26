# Escreva um programa que leia um número inteiro positivo do usuário
# e imprima todos os números pares entre 0 e o número digitado.

"""
numero = int(input("Digite um número inteiro positivo: "))

print("Números pares entre 0 e", numero, ":")

for i in range(0, numero + 1, 2):
    print(i)

"""
    
#Escreva um programa que leia um número inteiro positivo do usuário
#  e imprima a soma de todos os números ímpares entre 1 e o número digitado.
"""
numero = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, numero + 1, 2):
    soma += i

print("A soma dos números ímpares entre 1 e", numero, "é:", soma)

"""
'''
while True:
    print("Menu de Opções:")
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Subtrair")
    print("5 - Sair do programa")

    opcao = int(input("Escolha uma opção do menu: "))

    if opcao == 5:
        print("Programa encerrado.")
        break

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    if opcao == 1:
        resultado = valor1 + valor2
        print("Resultado da soma:", resultado)
    elif opcao == 2:
        resultado = valor1 * valor2
        print("Resultado da multiplicação:", resultado)
    elif opcao == 3:
        if valor2 != 0:
            resultado = valor1 / valor2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro: divisão por zero.")
    elif opcao == 4:
        resultado = valor1 - valor2
        print("Resultado da subtração:", resultado)
    else:
        print("Opção inválida. Tente novamente.")

'''
