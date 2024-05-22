def PalavraProxima(palavraCorreta, palavraDigitada):
    resultado = {}

    for i in range(len(palavraCorreta)):
        resultado[i] = {}
        for j in range(len(palavraDigitada)):
            if palavraCorreta[i] == palavraDigitada[j]:
                if i > 0 and j > 0:
                    resultado[i][j] = resultado[i-1][j-1] + 1
                else:
                    resultado[i][j] = 1
            else:
                resultado[i][j] = 0
              
    return resultado

print(PalavraProxima('fish', 'vista'))
