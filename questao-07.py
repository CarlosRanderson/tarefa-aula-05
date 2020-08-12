# 7.Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
# O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
# função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor
# de prestação e assim continuar até que seja informado um valor igual a zero para a prestação.
# Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total
# de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma.
# Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor_prestacao, n_dias):
    multa_por_atraso = 0.03
    multa_por_dia = 0.001
    parcela_com_multa = valor_prestacao + (valor_prestacao * multa_por_atraso) + (valor_prestacao * (n_dias * multa_por_dia))
    return parcela_com_multa

valor_prestacao = 1

while valor_prestacao != 0:
    valor_prestacao = int(input("Digite o valor da prestação: "))
    if valor_prestacao == 0:
        print("Interrompendo a execução da repetição.")
        break
    dias_atrazo = int(input("Digite os dias de atrazo: "))

    print("O valor do boleto é: ", valorPagamento(valor_prestacao, dias_atrazo))