print('''CAÇAS PALAVRAS
Dica é um animal\n''')

advinhacao = ['g','a','t','o']
acertos = []

while True:
    jogo = input('Escolha uma leta: ')
    for i in advinhacao:
        if jogo == i:
            print('Ebaa! Acetou.')
            acertos+=jogo
            print(acertos)

    if acertos == advinhacao:
        print('Parabens! Você ganhou.')
        break