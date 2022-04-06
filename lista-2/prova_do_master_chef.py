acidez = 20
agua = 15
tempero = 10

while acidez != agua and acidez != tempero:
    quantidade = int(input())
    acao = input()

    if acao == 'reduzir agua':
        agua -= quantidade
        tempero += quantidade - 1
    elif acao == 'adicionar agua':
        agua += quantidade
        tempero -= quantidade + 2
    elif acao == 'reduzir acidez':
        acidez -= quantidade
    elif acao == 'aumentar acidez':
        acidez += quantidade
    else:
        tempero += quantidade

    
    if min(acidez, agua, tempero) == agua:

        print('Muit seca! melhorre a combinaçon')

    elif  min(acidez, agua, tempero) == tempero:

        print('Falta tomperro! non agradou meu paladar')

    elif  min(acidez, agua, tempero) == acidez:

        print('Falta acidez! non pode subir o mezanin')

print('Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin')
