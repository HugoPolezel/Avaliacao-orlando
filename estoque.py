class Produto:
    def __init__(self, nome, preço_compra, preço_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preço_compra = preço_compra
        self.preço_venda = preço_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade
        self.próximo = None


class Estoque:
    def __init__(self):
        self.primeiro = None
        self.último = None

    def adicionar_produto(self, produto):
        if self.primeiro == None:
            self.primeiro = produto
            self.último = produto
            return

        anterior = None
        atual = self.primeiro
        while atual != None and atual.data_vencimento <= produto.data_vencimento:
            anterior = atual
            atual = atual.próximo

        if anterior == None:
            produto.próximo = self.primeiro
            self.primeiro = produto
        else:
            produto.próximo = atual
            anterior.próximo = produto
            if atual == None:
                self.último = produto

    def editar_quantidade(self, nome, nova_quantidade):
        atual = self.primeiro
        while atual != None:
            if atual.nome == nome:
                atual.quantidade = nova_quantidade
                return True
            atual = atual.próximo
        return False

    def mostrar(self):
        lista = []
        atual = self.primeiro
        while atual != None:
            lista.append(atual.nome)
            atual = atual.próximo
        return lista
