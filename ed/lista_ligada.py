class Celula:
    def __init__(self, conteudo):
        self.conteudo
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade