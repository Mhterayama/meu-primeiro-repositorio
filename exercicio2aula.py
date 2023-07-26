maior = 0
numeromaior = 0
numeromenor = 0
numeroigual = 0
for i in range(0,3):
    num = int(input(f"Digite o {i+1} numero :"))

    if num > maior :
        maior = maior + num
    
    if num < maior or num < numeromenor:
        numeromenor = numeromenor + num

    else:
        num == maior and num == num

print(f"Os numero sao iguais {num}")



print(f"O numero maior e {maior} é o numero menor é {numeromenor}")


