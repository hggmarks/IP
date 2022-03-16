contador  = 10
frases_original = []
frases_limpas = []
noise = True
num_ruidos = 0
while contador > 0:
    frases_original.append(input())
    contador -= 1




for frase in frases_original:
    if not (frase == 'tss' or frase == 'zzz'):
        noise = False
    
    if (frase[:3] == 'tss' or frase[:3] == 'zzz') and (frase[-3:] == 'tss' or frase[-3:] == 'zzz'):
        frases_limpas.append(frase[3:-3].strip())
        num_ruidos += 2
    elif frase[:3] == 'tss' or frase[:3] == 'zzz':
        frases_limpas.append(frase[3:].strip())
        num_ruidos += 1
    elif frase[-3:] == 'tss' or frase[-3:] == 'zzz':
        frases_limpas.append(frase[:-3].strip())
        num_ruidos += 1
    elif ('tss' not in frase) and ('zzz' not in frase):
        frases_limpas.append(frase.strip())

for item in frases_limpas.copy():
    if item == '':
        frases_limpas.remove('')

        
if noise:
    print('Eita, a legenda simplesmente inexiste! Tudo era ruido!')
else:
    print('Legenda final:\n')
    
    print(*frases_limpas, sep='\n')
    print()

    if (num_ruidos >= 1) and (num_ruidos <= 4) and (len(frases_limpas) >= 8):
        print('Todo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!')
    elif num_ruidos == 0:
        print('Nem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus')
    elif num_ruidos > 4 or len(frases_limpas) < 8:
        print('Ih, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar.')