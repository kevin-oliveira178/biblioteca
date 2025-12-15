from src.app.conteiner import Container


def menu():
    print("\n===== BEM VINDO AO SISTEMA DE BIBLIOTECA  =====")
    print("1 - Cadastrar Usuário")
    print("2 - Cadastrar Livro")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("5 - Listar Usuários")
    print("6 - Listar Livros")
    print("7 - Listar Empréstimos")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    container = Container()
    fachada = container.fachada

    while True:
        opc = menu()

        # ===============================
        # CADASTRAR USUÁRIO
        # ===============================
        if opc == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            matricula = input("Matrícula: ")

            usuario = fachada.cadastrar_usuario(nome, email, matricula)
            print("\nUsuário cadastrado com sucesso:")
            print(usuario)

        # ===============================
        # CADASTRAR LIVRO
        # ===============================
        elif opc == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            ano = int(input("Ano: "))
            quantidade = int(input("Quantidade: "))

            livro = fachada.cadastrar_livro(titulo, autor, isbn, ano, quantidade)
            print("\nLivro cadastrado com sucesso:")
            print(livro)

        # ===============================
        # EMPRESTAR LIVRO
        # ===============================
        elif opc == "3":
            id_usuario = input("ID do usuário: ")
            id_livro = input("ID do livro: ")

            emprestimo = fachada.emprestar_livro(id_usuario, id_livro)
            print("\nEmpréstimo realizado:")
            print(emprestimo)

        # ===============================
        # DEVOLVER LIVRO
        # ===============================
        elif opc == "4":
            id_emprestimo = input("ID do empréstimo: ")

            devolucao = fachada.devolver_livro(id_emprestimo)
            print("\nLivro devolvido:")
            print(devolucao)

        # ===============================
        # LISTAR USUÁRIOS
        # ===============================
        elif opc == "5":
            usuarios = container.usuario_repo.listar()
            print("\n--- Usuários cadastrados ---")
            for u in usuarios:
                print(u)

        # ===============================
        # LISTAR LIVROS
        # ===============================
        elif opc == "6":
            livros = container.livro_repo.listar()
            print("\n--- Livros cadastrados ---")
            for b in livros:
                print(b)

        # ===============================
        # LISTAR EMPRÉSTIMOS
        # ===============================
        elif opc == "7":
            emprestimos = container.emprestimo_repo.listar()
            print("\n--- Empréstimos ---")
            for e in emprestimos:
                print(e)

        elif opc == "0":
            print("Saindo... até mais!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
