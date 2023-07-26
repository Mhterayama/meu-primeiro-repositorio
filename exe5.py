from random import randint
random_number = []
hit_count = 0
guesses = []
for i in range(0,6):
    random_number.append(randint(1,30))

for i in range(0,3):
    guess = int(input("Digite um palpite entre 1 e 30: "))
    guesses.append(guess)

for guess in guesses:
    if guess in random_number:
        hit_count += 1


print(f"A contagem de acertos é : {hit_count}, Os numeros da sorte eram {random_number}")
