# interface sistema
import os   
import subprocess
from dados import salvar_dados, usua
from cadastros import cadastrar_liv, cadastrar_leitor
from consuliv import catliv, autliv, catauli
from emprestimos import emprestar_livro, devolver_livro, consultar_livros_disponiveis, consultar_livros_emprestados

def limpar_tela():
    subprocess.run(["cls" if os.name == "nt" else "clear"], shell=True)
    
def invalido():
    limpar_tela()
    print("Comando inválido. Tente novamente.")
    input("\nPressione Enter para voltar ao menu...")
    limpar_tela()

def interface():
    
    while True:
        print("|" + "=" * 75 + "|")
        print("|" + " " * 24 + "BIBLIOTECA ESCOLAR - SYSTEM 3.1" + " " * 20 + "|")
        print("|" + "=" * 75 + "|")
        print("|" + "1. Gestao de Acervo (Cadastrar / Consultar Livros)" + " " * 25 + "|")
        print("|" + "2. Cadastrar / Listar Leitores" + " " * 45 + "|")
        print("|" + "3. Registrar Emprestimo de Obra" + " " * 44 + "|")
        print("|" + "4. Registrar Devolucao e Calcular Multas" + " " *35 + "|")
        print("|" + "5. Exportar / Importar Base de Dados (biblioteca.csv)" + " " * 22 + "|")
        print("|" + "0. Encerrar" + " " * 64 + "|")
        print("|" + "=" * 75 + "|")

        comandoxxx = str(input("Escolha o comando desejado: "))
        
        if comandoxxx == "0":
            salvar_dados()
            print("Dados salvos. Encerrando o sistema...")
            break
        
        elif comandoxxx == "1":
            limpar_tela()
            print("GESTÃO DE ACERVO:\n #1: Cadastrar Livros\n #2: Consultar Livros\n #3: Voltar para o inicio")
            comandoxxx = str(input("Escolha o comando desejado: "))
            if comandoxxx == "1":
                limpar_tela()
                print("Você escolheu... 1\n Escolheu CADASTRAR!")
                cadastrar_liv()
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()
            elif comandoxxx == "2":
                limpar_tela()
                print("Você escolheu... 2\n Escolheu CONSULTAR!")
                print("CONSULTAR LIVRO POR...:\n #1: Categoria\n #2: Autor\n #3: Categoria e Autor\n #4: Livros Disponiveis\n #5: Livros Emprestados\n #6: Voltar para o inicio")
                comandoxxx = str(input("Escolha o comando desejado: "))
                if comandoxxx == "1":
                    limpar_tela()
                    print("Consultar livro por CATEGORIA!")
                    catliv()
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                elif comandoxxx == "2":
                    limpar_tela()
                    print("Consultar livro por AUTOR!")
                    autliv()
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                elif comandoxxx == "3":
                    limpar_tela()
                    print("Consultar livro por CATEGORIA & AUTOR!")
                    catauli()
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                elif comandoxxx == "4":
                    limpar_tela()
                    print("Consultar livros DISPONIVEIS!")
                    disponiveis = consultar_livros_disponiveis()
                    print(disponiveis)
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                elif comandoxxx == "5":
                    limpar_tela()
                    print("Consultar livros EMPRESTADOS!")
                    emprestados = consultar_livros_emprestados()
                    print(emprestados)
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                elif comandoxxx == "6":
                    limpar_tela()
                    print("Você escolheu 6\n==> VOLTAR PARA O INICIO!")
                    input("\nPressione Enter para voltar ao menu...")
                    limpar_tela()
                else:
                    invalido()
                        
            elif comandoxxx == "3":
                limpar_tela()
                print("Você escolheu 3\n==> VOLTAR PARA O INICIO!")
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()
        
        elif comandoxxx == "2":
            limpar_tela()
            print("LEITORES:\n #1: Cadastrar Leitores\n #2: Listar Leitores\n #3: Voltar para o inicio")
            comandoxxx = str(input("Escolha o comando desejado: "))
            if comandoxxx == "1":
                limpar_tela()
                print("CADASTRAR LEITORES!")
                cadastrar_leitor()
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()
            elif comandoxxx == "2":
                print("LISTAR LEITORES!")
                print(usua)
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()
            elif comandoxxx == "3":
                print("Você escolheu... 3\n==> VOLTAR PARA O INICIO!")
                input("\nPressione Enter para voltar ao menu...")
                limpar_tela()
            else:
                if comandoxxx != "0":
                    invalido()
        
        elif comandoxxx == "3":
            limpar_tela()
            print("REGISTRAR EMPRESTIMO DE OBRA")
            emprestar_livro()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        
        elif comandoxxx == "4":
            limpar_tela()
            print("REGISTRAR DEVOLUÇÃO E CALCULAR MULTAS")
            devolver_livro()
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
        
        elif comandoxxx == "5":
            limpar_tela()
            print("Essa funcionalidade ainda está em fase de desenvolvimento, pedimos desculpas pela insatisfação!")
            input("\nPressione Enter para voltar ao menu...")
            limpar_tela()
            
        else:
            if comandoxxx != "0":
                invalido()