class Celula:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None

class ListaDuplamenteLigada:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim

    @property
    def quantidade(self):
        return self._quantidade

    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError('Posição inválida: {}'.format(posicao))

    def _celula(self, posicao):
        self._validar_posicao(posicao)

        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual

