# src/app/use_cases/conteiner.py

from src.infra.repositorios import (
    UsuarioRepositoryMemoria,
    LivroRepositoryMemoria,
    EmprestimoRepositoryMemoria
)

from src.dominio.servicos import (
    CadastrarUsuarioService,
    CadastrarLivroService,
    EmprestarLivroService,
    DevolverLivroService
)


class Container:
    def __init__(self):
        # =======================================================
        # REPOSITÓRIOS (injeção de dependências)
        # =======================================================
        self.usuario_repo = UsuarioRepositoryMemoria()
        self.livro_repo = LivroRepositoryMemoria()
        self.emprestimo_repo = EmprestimoRepositoryMemoria()

        # =======================================================
        # SERVIÇOS DE DOMÍNIO
        # =======================================================
        self.usuario_service = CadastrarUsuarioService(self.usuario_repo)
        self.livro_service = CadastrarLivroService(self.livro_repo)

        # atenção: nomes alinhados!
        self.emprestar_service = EmprestarLivroService(
            self.livro_repo,
            self.usuario_repo,
            self.emprestimo_repo
        )

        self.devolver_service = DevolverLivroService(
            self.livro_repo,
            self.usuario_repo,
            self.emprestimo_repo
        )

        # =======================================================
        # FACHADA
        # =======================================================
        from src.app.fachada import Fachada


        self.fachada = Fachada(
            usuario_service=self.usuario_service,
            livro_service=self.livro_service,
            emprestimo_service=self.emprestar_service,   # <-- nome certo
            devolver_service=self.devolver_service        # <-- nome certo
        )
