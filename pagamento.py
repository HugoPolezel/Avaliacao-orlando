class Pagamento:
    def __init__(self, nome_pagador, número_comanda, forma_pagamento, valor_pago, data_pagamento, hora_pagamento):
        self.nome_pagador = nome_pagador
        self.número_comanda = número_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_pago = valor_pago
        self.data_pagamento = data_pagamento
        self.hora_pagamento = hora_pagamento
        self.próximo = None


class RegistroDePagamentos:
    def __init__(self):
        self.primeiro = None
        self.último = None

    def adicionar_pagamento(self, pagamento):
        if self.primeiro == None:
            self.primeiro = pagamento
            self.último = pagamento
        else:
            self.último.próximo = pagamento
            self.último = pagamento

    def mostrar(self):
        lista = []
        atual = self.primeiro
        while atual != None:
            lista.append(atual.nome_pagador)
            atual = atual.próximo
        return lista
