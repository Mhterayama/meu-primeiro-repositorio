''' 

# i = 4

# while i < 8:
#     print(i)
#     i += 1
    
# var2 = 1
# while var2 != 0:
#     var2 = int(input('digite um nuemro:'))
#     print(var2)
    
# #neste exemplo nos criamos uma estrutura de looping que
# # so saira do laço quando digitarmos 0.
    
    
name = input ('digite o nome:')
salary = float(input('digitte o salário:'))    

while salary < 1500:
    salary = float(input('salario invalido, digite um valor acima de 1500:'))

gender = input ("digite o sexo: ")

while gender != 'm' and gender != 'f' and gender != "M" and gender != "F":
    gender = input('sexo invalido.digite novamente ')
        
# criar uma situação que obrigue o usuario a cadastrar um
# salario sempre > 1500.
'''


qtd_digitado = 0
num = 0
numtotal = 0

while num != -1:
    qtd_digitado += 1
    numtotal = numtotal + num
    num = int(input('digite um numero: '))
    
print(f'numero de tentativas foram {qtd_digitado},e a soma dos numeros foi {numtotal}')
 
 # crie um programa em python que solicite ao usuario que digite numeros
 # inteiros. o programa so deve parar quando for digitado -1 ao final mostre:
 # quantos numeros foram digitados
 #qual a soma entre eles.





