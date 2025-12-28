from unittest.mock import patch
from src.UI.main import main

def test_menu_cadastrar_usuario():
    entradas = [
        "1",        # cadastrar usuário
        "Carlos", #nome
        "carlos.oliveira",#email
        "654321",#matricula

        "2",        # cadastrar livro
        "1984",     #titulo
        "George Orwell",  #autor
        "987sd4321",     #isbn
        "1949",         #ano
        "5",            #quantidade   
        
        "5",        # listar usuarios
        "6",        # listar livros

        "0"         # sair
    ]

    with patch("builtins.input", side_effect=entradas):
        main()
