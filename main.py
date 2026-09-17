import random
import pickle
from faker import Faker

from comanda import Comanda
from estoque import Produto, Estoque
from pagamento import Pagamento, RegistroDePagamentos
from relatorios import relatório_de_vendas, relatório_de_consumo

fake = Faker("pt_BR")


def criar_estoque_inicial():
    estoque = Estoque()
    estoque.adicionar_produto(Produto("Feijoada", 10, 25, "01/01/2026", "01/01/2027", 50))
    estoque.adicionar_produto(Produto("Salada", 5, 15, "01/01/2026", "01/01/2027", 50))
    estoque.adicionar_produto(Produto("Coca Cola", 3, 6, "01/01/2026", "01/12/2026", 100))
    estoque.adicionar_produto(Produto("Suco", 2, 5, "01/01/2026", "01/06/2026", 100))
    estoque.adicionar_produto(Produto("Água", 1, 3, "01/01/2026", "01/01/2027", 100))
    return estoque


def buscar_produto(estoque, nome):
    atual = estoque.primeiro
    while atual != None:
        if atual.nome == nome:
            return atual
        atual = atual.próximo
    return None


def simular_atendimento(número, estoque):
    nome_cliente = fake.name()
    comanda = Comanda(número, nome_cliente, "16/09/2026", "12:30")

    refeições_disponíveis = ["Feijoada", "Salada"]
    bebidas_disponíveis = ["Coca Cola", "Suco", "Água"]

    comanda.pedir_refeição(random.choice(refeições_disponíveis))
    comanda.pedir_bebida(random.choice(bebidas_disponíveis))

    return comanda


def fechar_comanda(comanda, estoque, registro_pagamentos):
    itens = comanda.mostrar_itens()
    valor_total = 0

    for item in itens:
        produto = buscar_produto(estoque, item)
        if produto != None and produto.quantidade > 0:
            produto.quantidade = produto.quantidade - 1
            valor_total = valor_total + produto.preço_venda

    forma_pagamento = random.choice(["PIX", "Cartão", "Dinheiro"])
    pagamento = Pagamento(comanda.nome_cliente, comanda.número, forma_pagamento, valor_total, "16/09/2026", "13:00")
    registro_pagamentos.adicionar_pagamento(pagamento)


def salvar_dados(estoque, comandas, registro_pagamentos):
    with open("dados.pkl", "wb") as arquivo:
        pickle.dump((estoque, comandas, registro_pagamentos), arquivo)


def carregar_dados():
    with open("dados.pkl", "rb") as arquivo:
        return pickle.load(arquivo)


def main():
    estoque = criar_estoque_inicial()
    registro_pagamentos = RegistroDePagamentos()
    comandas = []

    for número in range(1, 4):
        comanda = simular_atendimento(número, estoque)
        comandas.append(comanda)
        fechar_comanda(comanda, estoque, registro_pagamentos)

    salvar_dados(estoque, comandas, registro_pagamentos)

    print("Relatório de vendas:")
    for linha in relatório_de_vendas(registro_pagamentos):
        print(linha)

    print("Relatório de consumo:")
    for linha in relatório_de_consumo(comandas):
        print(linha)


if __name__ == "__main__":
    main()
