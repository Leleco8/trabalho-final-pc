from consuliv import catliv_sombra

def elemen_desejo():
    categoria_desejada = str(input("Qual a categoria desejada: "))
    livros = catliv_sombra()
    livros_filtrados = [
        livro for categoria, livro in livros.items()
        if categoria == categoria_desejada
    ]

    print(livros_filtrados)




            


