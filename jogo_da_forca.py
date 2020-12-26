import random

possíveis_palavras = ['Arroz', 'Cachorro', 'Amizade', 'Martelo', 'São Paulo']


def exibir():
    print(f'{30 * "-":>60}')
    print(f'{"BEM VINDO(A) AO JOGO DA FORCA":>60}')
    print(f'{30 * "-":>60}')

    print(f'{"JOGADORES: VOCÊ X COMPUTADOR":>59}')
    print()

    jogar()


def jogar():
    computador = random.choice(possíveis_palavras)
    chutes_usuario = list(range(len(computador)))
    chances = 10
    contador = 1

    for i in range(len(computador)):
        if computador[i].isalpha():
            chutes_usuario[i] = '-'
        else:
            chutes_usuario[i] = ' '

    while contador <= len(computador):
        print(95 * '*')
        print(f'{"Número de Tentativas: ":>50} {chances}', end=' ')

        # ------------percorre a lista "chutes do usuário" e exibe na tela---------------------------------
        print()
        print(f'{"":>28}', end=' ')
        for i in chutes_usuario:
            print(f'{i:>3}', end=' ')
        # -------------------------------------------------------------------------------------------------
        print()

        # -----Pede que o usuário chute uma letra, verifica se está na frase e, se sim, adiciona na lista
        # chutes_usuario---------------------------------------------------------------------------------

        escolha = str(input(f'{"Chute uma letra: ":>48}')).lower()

        if escolha in computador.lower():
            for i in range(len(computador)):
                if computador[i].lower() == escolha:
                    chutes_usuario[i] = computador[i]

        chances -= 1
        # -------------------------------------------------------------------------------------------

        # ---------------Veirifica se o ususário ganhou ou perdeu------------------------------------
        if chutes_usuario == list(computador):
            print(95 * '-')
            print(f'{"PARABÉNS, VOCÊ ACERTOU A PALAVRA! :)":>63}')
            break
        elif chances == 0:
            print(95 * '-')
            print(f'{"SUAS CHANCES ACABARAM :(":>53}')
            break
        # --------------------------------------------------------------------------------------------
    print()
    print(f'{"Palavra:":>40} {computador}')


print(95 * '*')

exibir()
