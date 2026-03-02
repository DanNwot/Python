tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
jogador1= 'X'
jogador2= 'O'
vencedor= False
for i in range(9):
    if i == 9:
        print("Deu velha")
    linha= int (input ('digite a linha que deseja jogar:\n'))
    coluna= int (input ('digite a coluna que deseja jogar:\n'))
    if coluna > 2 or linha > 2 or linha < 0 or coluna < 0:
        print("entrada invalida por favor tente novamente:\n")
        i-=1
    elif tabuleiro[linha][coluna]!= ' ':
        print("A posição ja esta ocupada \n")
    else:
        tabuleiro[linha][coluna] = jogador1
        print(tabuleiro)
        if jogador1 == 'X': jogador1 ='O'
        else:
            jogador1 = 'X'
        if jogador2 == 'O': jogador2 ='X'
        else:
            jogador2 = 'O'

        for j in range (3):
            if tabuleiro[j][0]== tabuleiro[j][1]== tabuleiro[j][2]==jogador2:
                print(f'o {jogador2} venceu')
                vencedor = True
                break
        for j in range (3):
            if tabuleiro[0][j]== tabuleiro[1][j]== tabuleiro[2][j] == jogador2:
                print(f'o {jogador2} venceu')
                vencedor = True
                break
        if tabuleiro[0][0]== tabuleiro[1][1]== tabuleiro[2][2] == jogador2:
            print(f'o {jogador2} venceu')
            vencedor = True
            break
        if tabuleiro[0][2]== tabuleiro[1][1]== tabuleiro[2][0] == jogador2:
            print(f'o {jogador2} venceu')
            vencedor = True
            break

    if vencedor: 
        break
