aluno={'nome':'daniel', 'nota': 5.1, 'nota1': 10, 'nota2': 5}
media = (aluno['nota'] + aluno['nota1'] + aluno['nota2']) / 3
if media >= 6:
    print(f'o aluno daniel esta aprovado')
else:
    print(f'o aluno daniel nao esta reprovado')
print (type (aluno['nota']))