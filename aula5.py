'''
from random import randint

random_number = randint(0,20)

qnt_digitada = 1
num = int(input("Digite um numero de 0 a 20 : "))
while num != random_number:
    qnt_digitada += 1   
    num = int(input("Digite um numero de 0 a 20 : "))
    if num > random_number:
        print("O numero deve ser menor")
    elif num < random_number:
        print('O numero deve ser maior')



   

print(f"A quantida de tentativas foram {qnt_digitada}, o numero digitado foi {num}")


for i in range(0,5):
    email = input("Digite Seu email ")   
    senha = input("Digite sua senha ")
    confirmacao = input("Confirme sua senha ")

    while senha != confirmacao:
        confirmacao = input("A confimacao esta Diferente da senha\n Confirme novamente : ")
'''
num = int(input("Digite um numero"))
for i in range(1,11):
    resultado = num * i
    print()