resposta = "s"
while resposta == "s":
    n1 = int(input("Digite a primeria nota: "))
    while n1 < 0 or n1 > 10 :
        print("Primeira Nota Invalida!")
        n1 = int(input("Digite a primeria nota: "))

    n2 = int(input("Digite a segunda nota: "))
    while n2 < 0 or n2 > 10 :
        print("Segunda nota Invalida!!")
        n2 = int(input("Digite a segunda nota: "))

    media = (n1+n2)/2

    print(f"A Média é: {media}")

    resposta = input("Deseja realizar novo cálculo? s = sim, n = não: ")