from src.dominio.entidades import Livro

def test_livro_inicia_disponivel():
    b = Livro(
        titulo="Livro A",
        autor="Autor A",
        isbn="123",
        ano_publicacao=2020,
        quantidade_total=3
    )

    assert b.quantidade_disponivel == 3

def test_emprestar_livro_diminui_quantidade():
    b = Livro(
        titulo="Livro A",
        autor="Autor A",
        isbn="123",
        ano_publicacao=2020,
        quantidade_total=1
    )

    b.emprestar()
    assert b.quantidade_disponivel == 0
