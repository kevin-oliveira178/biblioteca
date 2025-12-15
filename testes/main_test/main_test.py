from unittest.mock import patch
from src.UI.main import main

def test_menu_cadastrar_usuario():
    entradas = [
        "1",        # cadastrar usuário
        "Carlos",   # nome
        "3",        # limite
        "0"         # sair
    ]

    with patch("builtins.input", side_effect=entradas):
        main()
