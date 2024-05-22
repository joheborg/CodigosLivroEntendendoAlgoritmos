def mochila(capacidade, pesos, valores, n):
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                tabela[i][w] = 0
            elif pesos[i - 1] <= w:
                tabela[i][w] = max(valores[i - 1] + tabela[i - 1][w - pesos[i - 1]], tabela[i - 1][w])
            else:
                tabela[i][w] = tabela[i - 1][w]

    resultado = tabela[n][capacidade]
    return resultado

#Exemplo de uso
capacidade_mochila = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]
numero_itens = len(valores)

max_valor= mochila(capacidade_mochila, pesos, valores, numero_itens)
print("Valor máximo que pode ser carregado na mochila:", max_valor)


