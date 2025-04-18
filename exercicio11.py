op = 5
resul = 0
while op == 5:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    op = int(input("Selecione a Operação \n"
                   "1. Soma \n"
                   "2. Subtração \n"
                   "3. Multiplicação \n"
                   "4. Divisão \n"
                   "5. Digitar novo Número \n"
                   "6. Sair \n"
                   "Digite:"))

    match op:
        case 1:
            resul = n1 + n2
        case 2:
            resul = n1 - n2
        case 3:
            resul = n1 * n2
        case 4:
            resul = n1 / n2
        case 5:
            print("Digite Novamente!")
        case 6:
            print("Finalizando!!")
            break
    if op != 5 and op != 6:
        print(f"Resultado: {resul}")
