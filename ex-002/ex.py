
rodando = True

while rodando == True:1
    
    print("V1 calculadora")
    print("Escolha a operação desejada:")
    print("1 - soma (+)")
    print("2 - subtracao (-)")
    print("3 - multiplicacao (*)")
    print("4 - divisao (/)")
    print("5 - sair do programa (5)")

    op = input("Digite a operação desejada: ")

    if op == "5":
        print("valeu por utilizar a calculadora")
        rodando = False
    elif op in ["1", "2", "3", "4"]:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if op == "1":
            print("Resultado: ", n1+n2)
        elif op == "2":
            print("Resultado: ", n1-n2)
        elif op == "3":
            print("Resultado: ", n1*n2)
        elif op == "4":
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print("Resultado: ", n1/n2)
    else:
        print("Opção inválida. Tente novamente.")
