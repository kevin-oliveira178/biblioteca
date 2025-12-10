from datetime import datetime, timedelta
from src.dominio.entidades import Livro, Usuario, Emprestimo
from src.infra.repositorios import (
    LivroRepository,
    UsuarioRepository,
    EmprestimoRepository
)


# ========================================
#   SERVIÇO: Cadastrar Usuário
# ========================================
class CadastrarUsuarioService:

    def __init__(self, usuarios: UsuarioRepository):
        self.usuarios = usuarios

    def executar(self, nome: str, email: str, matricula: str) -> Usuario:
        if self.usuarios.buscar_por_email(email):
            raise ValueError("Já existe um usuário cadastrado com esse e-mail.")

        usuario = Usuario(nome=nome, email=email, matricula=matricula)
        self.usuarios.salvar(usuario)

        return usuario


# ========================================
#   SERVIÇO: Cadastrar Livro
# ========================================
class CadastrarLivroService:

    def __init__(self, livros: LivroRepository):
        self.livros = livros

    def executar(self, titulo: str, autor: str, isbn: str,
                 ano: int, quantidade: int) -> Livro:

        livro = Livro(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            ano_publicacao=ano,
            quantidade_total=quantidade,
            quantidade_disponivel=quantidade
        )

        self.livros.salvar(livro)

        return livro


# ========================================
#   SERVIÇO: Emprestar Livro
# ========================================
class EmprestarLivroService:

    def __init__(self, livros: LivroRepository,
                 usuarios: UsuarioRepository,
                 emprestimos: EmprestimoRepository):
        self.livros = livros
        self.usuarios = usuarios
        self.emprestimos = emprestimos

    def executar(self, id_usuario: str, id_livro: str) -> Emprestimo:

        usuario = self.usuarios.buscar_por_id(id_usuario)
        if usuario is None:
            raise ValueError("Usuário não encontrado.")

        livro = self.livros.buscar_por_id(id_livro)
        if livro is None:
            raise ValueError("Livro não encontrado.")

        # Regra: só empresta se há exemplares disponíveis
        livro.emprestar()

        # Cria empréstimo (prevendo devolução em 7 dias)
        emprestimo = Emprestimo(
            id_usuario=id_usuario,
            id_livro=id_livro,
            data_prevista_devolucao=datetime.now() + timedelta(days=7)
        )

        # Persistência
        self.livros.salvar(livro)
        self.emprestimos.salvar(emprestimo)

        return emprestimo


# ========================================
#   SERVIÇO: Devolver Livro
# ========================================
class DevolverLivroService:

    def __init__(self, livros: LivroRepository,
                 emprestimos: EmprestimoRepository):
        self.livros = livros
        self.emprestimos = emprestimos

    def executar(self, id_emprestimo: str):

        emp = self.emprestimos.buscar_por_id(id_emprestimo)
        if emp is None:
            raise ValueError("Empréstimo não encontrado.")

        livro = self.livros.buscar_por_id(emp.id_livro)
        if livro is None:
            raise ValueError("Livro não encontrado para este empréstimo.")

        # Regras
        emp.marcar_devolvido()
        livro.devolver()

        # Persistência
        self.emprestimos.salvar(emp)
        self.livros.salvar(livro)

        return emp