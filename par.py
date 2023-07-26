num = [[], []]
valor = 0
for c in range(1, 6):
    valor = int(input(f'Digite um numero :'))
    if valor % 2 == 0:
        num [0].append(valor)
    else:
        num[1].append(valor)

print ('-='* 30)
num[0].sort()

print (f'Os valores pares foram {num[0]}')
