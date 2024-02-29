class Biblioteca:
    def __init__(self, tamanho_tabela):
        self.tamanho_tabela = tamanho_tabela 
        self.tabela_hash = [None] * tamanho_tabela 
        self.espacos_ocupados = 0 

    def funcao_hash(self, id):
        return id % self.tamanho_tabela

    def adicionar_livro(self, id, titulo, autor):
    
        if self.espacos_ocupados >= self.tamanho_tabela:
            print("\nAviso: A tabela está cheia. Não é possível adicionar mais livros.")
            return

        indice = self.funcao_hash(id)

        while self.tabela_hash[indice] is not None:
            indice = (indice + 1) % self.tamanho_tabela

        self.tabela_hash[indice] = {'id': id, 'titulo': titulo, 'autor': autor}

        self.espacos_ocupados += 1

    def buscar_livro(self, id):
    
        indice = self.funcao_hash(id)
   
        while self.tabela_hash[indice] is not None:

            if self.tabela_hash[indice]['id'] == id:
                return self.tabela_hash[indice]
            
            indice = (indice + 1) % self.tamanho_tabela

        return None
    
    def imprimir_tabela_hash(self):
    
        print("Biblioteca:\n")
        for indice, elemento in enumerate(self.tabela_hash):
            if elemento is not None:
                print(f'Índice {indice}: {elemento}')
            else:
                print(f'Índice {indice}: Vazio')

biblioteca = Biblioteca(tamanho_tabela=10)

biblioteca.adicionar_livro(1, 'Livro 1', 'Autor 1')
biblioteca.adicionar_livro(2, 'Livro 2', 'Autor 2')
biblioteca.adicionar_livro(3, 'Livro 3', 'Autor 3')
biblioteca.adicionar_livro(4, 'Livro 4', 'Autor 4')

def menu_do_usuario():

    print("\nBem vindo a biblioteca")
    while True:
        print("\n1 - Buscar livro")
        print("2 - Inserir livro")
        print("3 - Mostrar lista de livros")
        print("0 - Sair")

        option = int(input())

        if option == 1:
            id = int(input("Digite o ID do livro: "))

            livro = biblioteca.buscar_livro(id)

            if livro:
                print(f'\nTítulo: {livro["titulo"]}, Autor: {livro["autor"]}')
            else:
                print('\nLivro não encontrado.')
        
        elif option == 2:
            id = int(input("Digite o ID do livro: "))
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")

            biblioteca.adicionar_livro(id=id, titulo=titulo, autor=autor)
            print("\nLivro inserido com sucesso!")
        
        elif option == 3:
            biblioteca.imprimir_tabela_hash()

        elif option == 0:
            break

        else:
            print("Digite uma opção válida")

menu_do_usuario()
