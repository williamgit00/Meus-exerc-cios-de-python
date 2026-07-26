import random

print ("Bem vindo aos numeros aleatorios!")

numero_aleatorio = input("digite um numero teto para o jogo:")
if numero_aleatorio.isdigit():
    numero_aleatorio = int(numero_aleatorio)

else:
    print("digite um numero valido")
    quit()

aleatorio = random.randint(0, numero_aleatorio)

tentativas = 0

while True:
   chute = input("adivinhe o numero:")

   if chute.isdigit():
    chute = int (chute)

   else:
         print ("Digite um numero valido")
         continue

   tentativas = tentativas + 1

   if chute == aleatorio:
        print("Parabens voce acertou!")
        break 

   elif chute < aleatorio:
        print("O numero e maior que isso")

   else:
        print("O numero e menor que isso")

print("Numero de tentativas: " + str(tentativas))