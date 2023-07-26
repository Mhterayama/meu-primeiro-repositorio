'''
def hello (name):
    return f'Hello, {name} , welcome back'

greeting_msg = hello('Silvia')
print(greeting_msg)

def sum(num1,num2):
    total = num1 + num2
    return  total

result = sum(3,5)
print(f'resultado da soma {result}')

def student_condition(grade1, grade2, grade3, grade4):
    average = (grade1 + grade2 + grade3 + grade4) / 4
    if(average < 7):
        return 'Aprovado'
    else:
        return 'Reprovado'
result = student_condition (6,8,5,5)
print(f'situacao do aluno{result}')

def studen_condition(grade1:float,grade2:float,grade3:float,grade4:float)->str:
    average = (grade1 + grade2 + grade3 + grade4) / 4
    if (average < 7):
        return 'Aprovado'
    return 'Reprovado'
result = studen_condition(6,8,5,5)
print(f'Situacao do aluno {result}')
'''

pesos = []
alturas = []
imcs = []
def imc (pesos:float, alturas:float)-> float:
    result = pesos / (alturas ** 2)
    return result
    
for i in range(0,1):
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    pesos.append(peso)
    alturas.append(altura)
    results = imc(peso,altura)
    imcs.append(results)
print(f'o imc ideal e {imcs}')

'''
valor = []
dias = 30
def calculo (salario:float, dias:float, hora:float)->float:
    result = salario / dias / hora
    return result
for i in range(0,1):
    salario = float(input("Digite o seu salario: "))
    hora = float(input("Digite quantas horas voce trabalha: "))
    results = calculo(salario, dias, hora)
    valor.append(results)
print(f"o valor pago por hora é {valor}")
'''
'''
palavras = []
for i in range (0,1):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)
    print(len(palavras))

import string

def contar_caracteres(texto):
    letras = 0
    espacos = 0
    pontuacao = 0

    for caractere in texto:
        if caractere.isalpha():
            letras += 1
        elif caractere.isspace():
            espacos += 1
        elif caractere in string.punctuation:
            pontuacao += 1
    
    return letras, espacos, pontuacao
'''    