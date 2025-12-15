from datetime import datetime, timedelta
from src.dominio.entidades import Emprestimo

def test_emprestimo_inicia_ativo():
    e = Emprestimo(id_usuario="u1", id_livro="l1")
    assert e.status == "ativo"
    assert e.data_emprestimo is not None

def test_marcar_devolvido():
    e = Emprestimo(id_usuario="u1", id_livro="l1")
    e.marcar_devolvido()

    assert e.status == "devolvido"
    assert e.data_devolucao is not None

def test_emprestimo_atrasado_sem_devolucao():
    e = Emprestimo(
        id_usuario="u1",
        id_livro="l1",
        data_prevista_devolucao=datetime.now() - timedelta(days=1)
    )

    assert e.esta_atrasado() is True
