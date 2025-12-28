from src.dominio.entidades import Usuario

def test_usuario_pode_emprestar():
    u = Usuario(nome="Kevin", limite_emprestimos=2)
    assert u.pode_emprestar() is True

def test_usuario_nao_pode_emprestar():
    u = Usuario(nome="Kevin", limite_emprestimos=1)
    u.emprestimos_ativos = 1

    assert u.pode_emprestar() is False
