entrada = input()
passos = []
total_passos = 0
while entrada != 'FIM':
    passos.append(entrada)
    entrada = input()
    total_passos += 1

print(f'Olá seguimores! O primeiro passo da dancinha é {passos[0]}')
print(f'Depois, a gente faz o {passos[1]} e {passos[2]}')
print(f'Temos ainda mais {total_passos - 3} passos pra aprender!')
print(f'Por último, vamos fazer o {passos[total_passos-1]}')
