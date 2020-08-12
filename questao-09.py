# 9.Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    return str(n[::-1])

n = str(input('Digite um número: ')).strip()
print(f'Reverso: {reverso(n)}')