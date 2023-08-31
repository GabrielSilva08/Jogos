def desenheForca(v):
    """
    -----
    |   |
    |   O
    |  /|\
    |  / \
    -
    """
    if v == 7:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", " ", " "], ["|", " ", " ", " ", " ", " "], ["|", " ", " ", " ", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 6:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", " ", " ", " "], ["|", " ", " ", " ", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 5:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 4:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", "/", "|", " "], ["|", " ", " ", " ", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 3:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", "/", "|", "\\"], ["|", " ", " ", " ", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 2:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", "/", "|", "\\"], ["|", " ", " ", "/", " ", " "], ["-", " ", " ", " ", " ", " "]]
    elif v == 1:
        forca = [["-", "-", "-", "-", "-", " "], ["|", " ", " ", " ", "|", " "], ["|", " ", " ", " ", "O", " "], ["|", " ", " ", "/", "|", "\\"], ["|", " ", " ", "/", " ", "\\"], ["-", " ", " ", " ", " ", " "]]
    for i in range(6):
        for j in range(6):
            print(forca[i][j], end="")
        print()
def main():
    """    
    Programa: Jogo da forca;
    Versão: 1.0;
    Data: 29/08/2023.
    """
    frase_mascarada = [] #lista com as letras da frase ocultada
    letras_tentadas = [] #lista de letras já tentadas pelo jogador
    vidas = 7 #Vidas
    frase = input("Digite a frase queira adivinhar: ")
    frase = frase.lower()
    for letra in frase: #Mascaramento da frase para frase_mascarada
        if letra != " ":
            frase_mascarada.append("#")
        else:
            frase_mascarada.append(" ")
    while vidas > 0:
        if "".join(frase_mascarada) == frase: #Verifica se o jogador já advinhou todas as letras
            print(f"{frase}\nParabéns!")
            break
        print("\n")
        desenheForca(vidas)
        print("".join(frase_mascarada))
        letra = input("Digite uma letra: ")
        if letra in letras_tentadas: #Verifica se o jogador já tentou a letra digitada
            print("Letra já tentada!\n")
        if letra in frase: #Se a letra estiver presente na frase, frase_mascarada é atualizada
            for i, l in enumerate(frase):
                if l == letra:
                    frase_mascarada[i] = letra
            letras_tentadas += letra
        else: #Se a letra não estiver presente na frase, o número de vidas é atualizado
            vidas -= 1
            print("Letra não presente!\n")
            letras_tentadas += letra
if __name__ == "__main__":
    main()
