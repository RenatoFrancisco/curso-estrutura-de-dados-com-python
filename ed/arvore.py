from ed.lista_duplamente_ligada import ListaDuplamenteLigada

class ListaDeNodos(ListaDuplamenteLigada):
    def __init__(self):
        super().__init__()

class Nodo:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def imprimir(self):
        print(self.conteudo)

class Arvore:
    def __init__(self, conteudo):
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()


    
