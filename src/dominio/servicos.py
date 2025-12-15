from datetime import datetime
from src.dominio.entidades import Livro, Usuario, Emprestimo
from src.dominio.regras import prazo_padrao
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

        usuario.registrar_emprestimo()
        livro.emprestar()

        emprestimo = Emprestimo(
            id_usuario=id_usuario,
            id_livro=id_livro,
            data_prevista_devolucao=datetime.now() + prazo_padrao()
        )

        # Persistência
        self.usuarios.salvar(usuario)
        self.livros.salvar(livro)
        self.emprestimos.salvar(emprestimo)

        return emprestimo


# ========================================
#   SERVIÇO: Devolver Livro
# ========================================
class DevolverLivroService:

    def __init__(self, livros: LivroRepository,
                 usuarios: UsuarioRepository,
                 emprestimos: EmprestimoRepository):
        self.livros = livros
        self.usuarios = usuarios
        self.emprestimos = emprestimos

    def executar(self, id_emprestimo: str):

        emp = self.emprestimos.buscar_por_id(id_emprestimo)
        if emp is None:
            raise ValueError("Empréstimo não encontrado.")

        livro = self.livros.buscar_por_id(emp.id_livro)
        if livro is None:
            raise ValueError("Livro não encontrado para este empréstimo.")

        usuario = self.usuarios.buscar_por_id(emp.id_usuario)
        if usuario is None:
            raise ValueError("Usuário não encontrado para este empréstimo.")

        emp.marcar_devolvido()
        livro.devolver()
        usuario.registrar_devolucao()

        self.emprestimos.salvar(emp)
        self.livros.salvar(livro)
        self.usuarios.salvar(usuario)

        return emp
