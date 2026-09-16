class No:
    def __init__(self, produto):
        self.produto = produto
        self.próximo = None


class Sequência:
    def __init__(self):
        self.primeiro = None
        self.último = None

    def adicionar(self, produto):
        novo = No(produto)
        if self.primeiro == None:
            self.primeiro = novo
            self.último = novo
        else:
            self.último.próximo = novo
            self.último = novo

    def remover_produto(self, produto):
        atual = self.primeiro
        anterior = None
        while atual != None:
            if atual.produto == produto:
                if anterior == None:
                    self.primeiro = atual.próximo
                else:
                    anterior.próximo = atual.próximo
                if atual == self.último:
                    self.último = anterior
                return True
            anterior = atual
            atual = atual.próximo
        return False

    def mostrar(self):
        lista = []
        atual = self.primeiro
        while atual != None:
            lista.append(atual.produto)
            atual = atual.próximo
        return lista


class Fila:
    def __init__(self):
        self.pedidos = Sequência()

    def pedir(self, produto):
        self.pedidos.adicionar(produto)

    def cancelar(self, produto):
        return self.pedidos.remover_produto(produto)

    def mostrar(self):
        return self.pedidos.mostrar()