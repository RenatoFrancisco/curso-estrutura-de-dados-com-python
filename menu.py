from ed.arvore import Arvore

def main():
    livraria = Arvore('Livros')
    livraria.imprimir()
    livraria.raiz.inserir_filho('Gastronomia')
    livraria.raiz.inserir_filho('Informática')
    livraria.imprimir()

main()
