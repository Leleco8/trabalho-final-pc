from dados import estant, disponi, status_livros, salvar_dados

def consultar_livros_disponiveis():
    disponiveis = []
    
    for i in range(len(estant)):
        if status_livros[i] == disponi[0]:  
            disponiveis.append(estant[i])  
            
    return disponiveis

def consultar_livros_emprestados():
    emprestados = []

    for i in range(len(estant)):
        if status_livros[i] == disponi[1]:
            emprestados.append(estant[i]) 
            
    return emprestados

def emprestar_livro():
    titulo = str(input("Digite o título do livro que deseja emprestar: "))

    if titulo not in estant:
        print("Livro não encontrado no acervo.")
        return

    idx = estant.index(titulo)

    if status_livros[idx] != disponi[0]:
        print(f"'{titulo}' já está emprestado.")
        return

    status_livros[idx] = disponi[1]
    salvar_dados()
    print(f"Empréstimo registrado com sucesso: '{titulo}'")

def devolver_livro():
    multa_dia = 1.5
    titulo = input("Digite o título do livro a devolver: ")

    if titulo not in estant:
        print("Livro não encontrado no acervo.")
        return

    idx = estant.index(titulo)

    if status_livros[idx] != disponi[1]:
        print(f"'{titulo}' não está emprestado no momento.")
        return

    prazo = int(input("Digite o prazo de empréstimo (em dias): "))
    dias_atraso = int(input("Digite quantos dias de atraso houve (0 se não houve atraso): "))
    
    status_livros[idx] = disponi[0]

    if dias_atraso > 0:
        multa = dias_atraso * multa_dia
        print(f"Livro devolvido com {dias_atraso} dia(s) de atraso (prazo era de {prazo} dias).\n Multa: R$ {multa}")
        print("Livro devolvido com sucesso!")
        print("Tente não atrasar mais!")
    else:
        print(f"Livro devolvido dentro do prazo de {prazo} dias.\n Sem multa.")
        print("Livro devolvido com sucesso!")
        
    salvar_dados()