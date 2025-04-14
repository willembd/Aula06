i=1
nome = input("Digite seu nome: ")
senha = int(input("Cadastre a sua senha Númerica: "))

versenha = int(input("Digite a sua senha: "))

while senha != versenha:
    versenha = int(input("Senha Incorreta!! Digite novamente: "))

    if i == 3 and senha != versenha:
        print("Tentativas Excedidas ")
        break
    i += 1
print(i)
if i != 3:
    print(f"Login Efetuado com Sucesso {nome}!!")