
salariomaior = 0
salariototal = 0
for i in range (0,5):
    num = int(input("Digite o valor do seu salario :"))
    filhos = int(input("Digite quantos filhos você tem :"))

    if num <= 1500 :
        salariomaior += 1

    if filhos >= 3 :
        salariototal = salariototal + num
print(f"A quantidade de cidadãos que recebe até de R$1500 é {salariomaior}")
print(f"A soma do salario dos cidadãos que tem mais de 3 filhos é {salariototal}")