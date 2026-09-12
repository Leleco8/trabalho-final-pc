from dados import estant, cat, aut, salvar_dados, usua, status_livros, disponi

def cadastrar_liv():
    titulo = input("Título: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")

    estant.append(titulo)
    aut.append(autor)
    cat.append(categoria)
    status_livros.append(disponi[0])
    
    salvar_dados()
    print("Livro cadastrado e salvo!")
    
def cadastrar_leitor():
    nome = str(input("Nome: "))
    sobrenome = str(input("Sobrenome: "))
    
    nome_completo = nome + " " + sobrenome
    
    usua.append(nome_completo)
    
    salvar_dados()
    print("Usuário cadastrado com sucesso!")
