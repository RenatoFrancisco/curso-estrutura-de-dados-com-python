from ed.lista_ligada import ListaLigada, Celula

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self.nome, self.endereco)

def main():
    print('main')
    loja1 = Loja("Mercadinho", "Rua das Laranjeira, 12")
    loja2 = Loja("Hortifruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")

    lista = ListaLigada()
    print(lista.quantidade)


    lista.inserir_no_inicio(loja1)
    print(lista.quantidade)
    lista.imprimir()

    lista.inserir_no_inicio(loja2)
    print(lista.quantidade)
    lista.imprimir()


    lista.inserir_no_inicio(loja3)
    print(lista.quantidade)
    lista.imprimir()

main()