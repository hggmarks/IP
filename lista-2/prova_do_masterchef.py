acidez = 20
agua = 15
tempero = 10

while acidez != agua or acidez != tempero or agua != tempero:
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
    elif acao == 'aumentar tempero':
        tempero += quantidade

    
    if (agua < acidez and agua < tempero):

        print('Muit seca! melhorre a combinaçon')
        
    elif (tempero < agua and tempero < acidez):

        print('Falta tomperro! non agradou meu paladar')

    elif (acidez < agua and acidez < tempero):

        print('Falta acidez! non pode subir o mezanin')
    
    elif agua == tempero and agua != acidez:
      
        print('Muit seca! melhorre a combinaçon')
        print('Falta tomperro! non agradou meu paladar')
        
    elif agua == acidez and agua != tempero:
      
        print('Muit seca! melhorre a combinaçon')
        print('Falta acidez! non pode subir o mezanin')
        
    elif tempero == acidez and tempero != agua:
        print('Falta tomperro! non agradou meu paladar')
        print('Falta acidez! non pode subir o mezanin')

        
print('Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin')
