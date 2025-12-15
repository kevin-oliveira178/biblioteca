from src.infra.repositorios import UsuarioRepositoryMemoria
from src.dominio.entidades import Usuario

def test_salvar_e_buscar_usuario():
    repo = UsuarioRepositoryMemoria()
    u = Usuario(nome="Maria", limite_emprestimos=3)

    repo.salvar(u)
    usuario = repo.buscar_por_id(u.id)

    assert usuario is not None
    assert usuario.nome == "Maria"

def test_listar_usuarios():
    repo = UsuarioRepositoryMemoria()

    repo.salvar(Usuario(nome="A", limite_emprestimos=1))
    repo.salvar(Usuario(nome="B", limite_emprestimos=2))

    usuarios = repo.listar()
    assert len(usuarios) == 2
