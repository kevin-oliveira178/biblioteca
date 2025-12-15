from src.app.fachada import Fachada
from src.dominio.servicos import (
    CadastrarUsuarioService,
    CadastrarLivroService,
    EmprestarLivroService
)
from src.infra.repositorios import (
    UsuarioRepositoryMemoria,
    LivroRepositoryMemoria,
    EmprestimoRepositoryMemoria
)


def test_fluxo_completo_emprestimo():
    # Repositórios
    usuario_repo = UsuarioRepositoryMemoria()
    livro_repo = LivroRepositoryMemoria()
    emprestimo_repo = EmprestimoRepositoryMemoria()

    # Serviços
    usuario_service = CadastrarUsuarioService(usuario_repo)
    livro_service = CadastrarLivroService(livro_repo)
    emprestimo_service = EmprestarLivroService(
        usuario_repo,
        livro_repo,
        emprestimo_repo
    )

    # Fachada (como foi projetada)
    fachada = Fachada(
        usuario_service=usuario_service,
        livro_service=livro_service,
        emprestimo_service=emprestimo_service
    )

    # Fluxo
    usuario = fachada.cadastrar_usuario(
        nome="joão",
        email="jc@gmail.com",
        matricula="12345"
    )

    livro = fachada.cadastrar_livro(
        titulo="Livro X",
        autor="Autor X",
        isbn="123",
        ano=2021,
        quantidade=1
    )

    emprestimo = fachada.emprestar_livro(usuario.id, livro.id)

    assert emprestimo is not None
    assert livro.quantidade_disponivel == 0

