i = 1
soma = 0
n = int(input("Digte a quantidade de Alunos: "))

while i <= n:
    nota = int(input(f"Digite a Nota do Aluno: "))
    soma = soma + nota
    i+=1
media = soma / n
print(f"A Média das notas é: {media}")