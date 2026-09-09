from dados import estant, disponi
status_livros = [disponi[0]] * len(estant)


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


print("Livros disponíveis:", consultar_livros_disponiveis())
print("Livros emprestados:", consultar_livros_emprestados())