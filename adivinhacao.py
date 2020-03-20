import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = random.randrange(100)
number_of_attempts = 5
attempt = 0

while attempt < number_of_attempts:

    print (f"\nTentativa {attempt + 1} de {number_of_attempts}: ")
    user_input = input("Digite seu chute:")

    if user_input.isnumeric():
        number_user_input = int(user_input)
        if number_user_input == secret_number:
            print(">>> --------------------- <<<")
            print(">>> VOCÊ ACERTOU O NUMERO <<<")
            print(">>> --------------------- <<<")
            exit()
        else:
            print("--- VOCÊ ERROU O NUMERO ---")
            if number_user_input > secret_number:
                print("Seu chute está acima do numero secreto")
            elif number_user_input < secret_number:
                print("Seu chute está abaixo do numero secreto")
    elif user_input.isalpha():
        if user_input is "q":
            exit()
    attempt += 1

if attempt >= number_of_attempts:
    print("Seu numero de tentativas se esgotou!")


