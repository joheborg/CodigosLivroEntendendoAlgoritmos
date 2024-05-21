def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        # menores = [i for i in array[1:] if i <= pivo] # modo de Compreensão de Lista
        menores = []
        for i in array[1:]:
            if i <= pivo:
                menores.append(i)

        # maiores = [i for i in array[1:] if i > pivo] # modo de Compreensão de Lista
        maiores = []
        for i in array[1:]:
            if i > pivo:
                maiores.append(i)
        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort([10, 5, 3, 7, 9, 2, 4, 6, 8]))
