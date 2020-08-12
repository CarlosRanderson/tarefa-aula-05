def imprimir(numero):
    parada_i = numero + 1
    resposta = ''
    for i in range(1, parada_i):
        parada_j = i + 1
        for j in range(1, parada_j):
            resposta += str(j) + ' '
        resposta += '\n'
    return resposta

# Início do algoritmo

print (imprimir(5))