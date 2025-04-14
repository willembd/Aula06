n1 = int(input("Digite o primeiro valor: "))
n2 =int(input("Digite o segundo valor: "))

while n2 == 0:
    print("Segundo Valor Não pode ser 0")
    n2 = int(input("Digite o segundo valor: "))

media = (n1+n2)/2
print(media)