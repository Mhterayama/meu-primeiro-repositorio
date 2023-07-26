num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

if num1 == num2 or num1 == num3 or num2 == num3:
    if num1 == num2 and num1 == num3:
        numeros_iguais = [num1]
    elif num1 == num2:
        numeros_iguais = [num1]
    else:
        numeros_iguais = [num2]
else:
    numeros_iguais = []

print("O maior número é:", maior)
print("O menor número é:", menor)
if numeros_iguais:
    print("Há números iguais:", ", ".join(str(num) for num in numeros_iguais))