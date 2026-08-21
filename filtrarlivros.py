livros = [
    {"titulo": "1984", "categoria": "Ficção"},
    {"titulo": "Clean Code", "categoria": "Programação"},
    {"titulo": "Python Fluente", "categoria": "Programação"},
    {"titulo": "O Hobbit", "categoria": "Fantasia"},
    {"titulo": "Harry Potter", "categoria": "Fantasia"}
]

categoria_desejada = "Programação"

livros_filtrados = [
    livro for livro in livros
    if livro["categoria"] == categoria_desejada
]

print(livros_filtrados)