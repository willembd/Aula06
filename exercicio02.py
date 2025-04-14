i = 0
n = 4
soma = 0
while i <=n:
    num =int(input("Digite uma nota:"))
    soma = soma + num
    i+=1
media = soma / 5

print(f"A média das notas é: {media}")
