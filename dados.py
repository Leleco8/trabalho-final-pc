import pickle
import os

arquivo = "biblioteca.pkl"

def _carregar():
    if os.path.exists(arquivo):
        with open(arquivo, "rb") as f:
            return pickle.load(f)
    return None

_salvos = _carregar()

if _salvos:
    aut = _salvos["aut"]
    cat = _salvos["cat"]
    estant = _salvos["estant"]
    usua = _salvos["usua"]
    disponi = _salvos["disponi"]
    status_livros = _salvos["status_livros"]
else:
    from autores import autores
    from cateedisp import categoria, disp
    from livros import estante
    from usuarios import alunos

    aut = autores
    cat = categoria
    estant = estante
    usua = alunos
    disponi = disp
    status_livros = [disponi[0]] * len(estant)

def salvar_dados():
    dados = {"aut": aut, "cat": cat, "estant": estant, "usua": usua, "disponi": disponi, "status_livros": status_livros}
    with open(arquivo, "wb") as f:
        pickle.dump(dados, f)