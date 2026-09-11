# funções para retornar livros e consultar livros de determinada categoria ou autor.
# zip é muito massssssssa, satisfatorio d+
from dados import cat, aut, estant

# livros + categoria 
def catliv():
    for categoria, livro in zip(cat, estant):
        print(f"#{categoria}:  {livro}")
        
def catliv_sombra():
    bibli = {}
    for categoria, livro in zip(cat, estant):
        bibli[categoria] = livro 
    return bibli

# livros + autor
def autliv():
    for autor, livro in zip(aut, estant):
        print(f"#{autor}:  {livro}")

# livros + autores + categoria e fds
def catauli():
    for cate, autor, livro in zip(cat, aut, estant):
        print(f'''#{cate}\n---{autor}: {livro}''')