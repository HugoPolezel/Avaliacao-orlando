from estruturas import Fila


class Comanda:
    def __init__(self, número, nome_cliente, data_abertura, hora_abertura):
        self.número = número
        self.nome_cliente = nome_cliente
        self.data_abertura = data_abertura
        self.hora_abertura = hora_abertura
        self.refeições = Fila()
        self.bebidas = Fila()

    def pedir_refeição(self, refeição):
        self.refeições.pedir(refeição)

    def cancelar_refeição(self, refeição):
        return self.refeições.cancelar(refeição)

    def pedir_bebida(self, bebida):
        self.bebidas.pedir(bebida)

    def cancelar_bebida(self, bebida):
        return self.bebidas.cancelar(bebida)

    def mostrar_itens(self):
        return self.refeições.mostrar() + self.bebidas.mostrar()
