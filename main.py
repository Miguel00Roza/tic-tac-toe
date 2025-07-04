matrizJogo = [
    [".",".","."],
    [".",".","."],
    [".",".","."]
]

x = 0
linha = 0
coluna = 0
while True:

    #Printando A situação atual da matriz
    print("    0   1   2")
    print(f"    {matrizJogo[0][0]} | {matrizJogo[0][1]} | {matrizJogo[0][2]}   0")
    print("   --- --- ---")
    print(f"    {matrizJogo[1][0]} | {matrizJogo[1][1]} | {matrizJogo[1][2]}   1")
    print("   --- --- ---")
    print(f"    {matrizJogo[2][0]} | {matrizJogo[2][1]} | {matrizJogo[2][2]}   2")

    #Atribuição de posição alternando entre X e O
    if x == 0:
        print("Vez de X")
        print("Escolha a posição que desenha inserir")
        linha = int(input("Insira a linha que deseja inserir\n"))
        coluna = int(input("Insira a coluna que deseja inserir\n"))
        if matrizJogo[linha][coluna] != ".":
            print("Posição já ocupada!")
            continue
        else:
            matrizJogo[linha][coluna] = "X"
        x += 1
    else:
        print("Vez de O")
        print("Escolha a posição que desenha inserir")
        linha = int(input("Insira a linha que deseja inserir\n"))
        coluna = int(input("Insira a coluna que deseja inserir\n"))
        if matrizJogo[linha][coluna] != ".":
            print("Posição já ocupada!")
            continue
        else:
            matrizJogo[linha][coluna] = "O"
        x = 0

    
    #Verificação se há vencedor
    #linhas horizontais
    if matrizJogo[0][0] == matrizJogo[0][1] == matrizJogo[0][2] != ".":
        print(f"Vencedor: {matrizJogo[0][0]}")
        break
    if matrizJogo[1][0] == matrizJogo[1][1] == matrizJogo[1][2] != ".":
        print(f"Vencedor: {matrizJogo[1][0]}")
        break
    if matrizJogo[2][0] == matrizJogo[2][1] == matrizJogo[2][2] != ".":
        print(f"Vencedor: {matrizJogo[2][0]}")
        break
    
    #linhas verticais
    if matrizJogo[0][0] == matrizJogo[1][0] == matrizJogo[2][0] != ".":
        print(f"Vencedor: {matrizJogo[0][0]}")
        break
    if matrizJogo[0][1] == matrizJogo[1][1] == matrizJogo[2][1] != ".":
        print(f"Vencedor: {matrizJogo[0][1]}")
        break
    if matrizJogo[0][2] == matrizJogo[1][2] == matrizJogo[2][2] != ".":
        print(f"Vencedor: {matrizJogo[0][2]}")
        break
    
    #linhas cruzadas
    if matrizJogo[0][0] == matrizJogo[1][1] == matrizJogo[2][2] != ".":
        print(f"Vencedor: {matrizJogo[0][0]}")
        break
    if matrizJogo[0][2] == matrizJogo[1][1] == matrizJogo[2][0] != ".":
        print(f"Vencedor: {matrizJogo[0][2]}")
        break

print("    0   1   2")
print(f"    {matrizJogo[0][0]} | {matrizJogo[0][1]} | {matrizJogo[0][2]}   0")
print("   --- --- ---")
print(f"    {matrizJogo[1][0]} | {matrizJogo[1][1]} | {matrizJogo[1][2]}   1")
print("   --- --- ---")
print(f"    {matrizJogo[2][0]} | {matrizJogo[2][1]} | {matrizJogo[2][2]}   2")

print("Bom jogo!")