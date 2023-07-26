
# for fruit in fruits:
#   print(fruit)
    
# ADICIONAR ITEM NO FINAL DA LISTA VARIAVEL.APPEND \\ ESCOLHE ONDE QUE ADICIONAR O INTEM VARIVAEL.INSERT
# REMOVE O ULTIMO ITEM VARIVAEL.POP \\ PRA REMOVER UM EXPECIFICO VARIVAVEL.POP(NUMERO)
# REMOVE PELO NOME DO ITEAM VAVRIAVEL.REMOVE(NOME DO PRODUTO) \\ CONTA QUANTOS ITENS TEM NA LISTA VARIVAVEL.COUNT(LISTA)
# names = []

# numbers = [10, 5, 7, 9, 1]

# products = ["notebook", "mouse", "teclado", "headset"]

# # print(products[2])
# # print("Ao todo temos", len(products), "Produtos")

# products.append("celular")
# products.append("tablet")

# products.insert(2, "Monitor LED")

# products.pop(3)

# if "headset" in products:
#     products.remove("headset")
# else:
#     print("Não existe o produto")
    
# for product in products:
#     print(product)
'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
series = ["Breaking bad ", "Game of thrones ", "The walking dead", "Wandinha",
           "Friends", "Stranger Things", "Black Mirror", "La casa de papel",
           "Prision break", "Os Aneis do Poder", "You", "Panico"]

print("-" * 20)
print("Minha Lista de Series")
print("-" * 20)
print(f"As 5 primeiras são {series[0:5]}\nAs ultimas 4 series são {series[-4:]}")
print(f"Series em ordem Alfabetica{sorted(series)}")
print(f"Stranger things está na posição, {series.index('Stranger Things')+1}")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numbers = [2, 3, 4, 9, 8, 7, 15, 20, 12, 18]
soma = 0
maior = 0
menor = 1000
for i in numbers:
    soma = soma + i
    
    if i > maior:
        maior = i
    if i < menor:
        menor = i
        
print(f"A soma dos numeros é {soma}, e o numero maior é {maior}, e o numero menor é {menor}")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
even = []
odds = []
for number in range(0,10):
    num = int(input("Digite um numero "))
    if num % 2 == 0:
        even.append(num)
    else:
        odds.append(num)

print(f"Numeros pares: {even}\n Numeros Inpares: {odds}")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
num = [[], []]
valor = 0
for i in range(1, 11):
    valor = int(input(f'Digite um numero :'))    
    
    if valor % 2 == 0:
        num [0].append(valor)
        
    else:        num[1].append(valor)
    
print ('-='* 30)
num[0].sort()
num[1].sort()
print (f'Os valores pares foram {num[0]}\nOs valores impares são {num[1]}')
'''        
    
