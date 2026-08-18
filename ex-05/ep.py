import random
import string

def gerador_de_senha(len_pass = 8):

    ascii_options = string.ascii_letters 
    numbers = string.digits
    punt_options = string.punctuation
    options = ascii_options + numbers + punt_options

    password = ""
    for digit in range (0, len_pass):
        digit = random.choice(options)
        password = password + digit

    return password   

choice = input("Qual o tamanho da senha")
if choice.isdigit():
    choice = int(choice)
else:
    print("Digite um número válido")    
    quit()
response = gerador_de_senha(len_pass = choice)    
print(f"Sua senha gerada é: {response}")
