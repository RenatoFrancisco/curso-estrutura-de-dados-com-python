from ed.lista_duplamente_ligada import ListaDuplamenteLigada, Celula

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return '{} - {}'.format(self.nome, self.endereco)

def main():
    loja1 = Loja('Minimercado', 'Rua das Flores, 12')
    loja2 = Loja('Hortifruti', 'Av das Borboletas. 23')
    loja3 = Loja('Padaria Pão Quente', 'Praça da Árvore')

    lista = ListaDuplamenteLigada()
    print('Quantidade: {}'.format(lista.quantidade))

    lista.inserir_no_inicio(loja1)
    print('Quantidade: {}'.format(lista.quantidade))
    print(lista.item(0))

    lista.inserir_no_inicio(loja2)
    print('Quantidade: {}'.format(lista.quantidade))
    print(lista.item(0))
    print(lista.item(1))

    lista.inserir_no_inicio(loja3)
    print('Quantidade: {}'.format(lista.quantidade))
    lista.imprimir()


main()