tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]):  # Linhas
            return True
        if all([tabuleiro[j][i] == jogador for j in range(3)]):  # Colunas
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):  # Diagonais
        return True
    return False

jogador_atual = "X"
jogadas = 0

while jogadas < 9:
    imprimir_tabuleiro()
    print(f"Vez do jogador {jogador_atual}")
    
    try:
        linha = int(input("Digite a linha (0 a 2): "))
        coluna = int(input("Digite a coluna (0 a 2): "))
    except ValueError:
        print("Entrada inválida. Digite números de 0 a 2.")
        continue

    if 0 <= linha < 3 and 0 <= coluna < 3:
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1

            if verificar_vitoria(jogador_atual):
                imprimir_tabuleiro()
                print(f"Jogador {jogador_atual} venceu!")
                break

            # Troca de jogador
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição já ocupada. Escolha outra.")
    else:
        print("Linha ou coluna fora do intervalo. Digite de 0 a 2.")

else:
    imprimir_tabuleiro()
    print("Empate! Ninguém venceu.")