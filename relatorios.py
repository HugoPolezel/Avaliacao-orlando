def relatório_de_vendas(registro_pagamentos):
    linhas = []
    total = 0
    atual = registro_pagamentos.primeiro
    while atual != None:
        linhas.append(str(atual.número_comanda) + " - " + atual.nome_pagador + " - " + atual.forma_pagamento + " - " + str(atual.valor_pago))
        total = total + atual.valor_pago
        atual = atual.próximo
    linhas.append("Total vendido: " + str(total))
    return linhas


def relatório_de_consumo(comandas):
    linhas = []
    for comanda in comandas:
        itens = comanda.mostrar_itens()
        linhas.append(str(comanda.número) + " - " + comanda.nome_cliente + " - " + str(itens))
    return linhas
