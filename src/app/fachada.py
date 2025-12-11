# src/app/use_cases/fachada.py

from typing import List
from src.dominio.entidades import Usuario, Livro, Emprestimo

from src.dominio.servicos import (
    CadastrarUsuarioService,
    CadastrarLivroService,
    EmprestarLivroService,
    DevolverLivroService
)


class Fachada:

    def __init__(
        self,
        usuario_service: CadastrarUsuarioService,
        livro_service: CadastrarLivroService,
        emprestimo_service: EmprestarLivroService,
        devolver_service: DevolverLivroService = None
    ):
        """
        A fachada recebe as instâncias dos serviços já configurados
        pelo Container.
        """

        self.cadastrar_usuario_service = usuario_service
        self.cadastrar_livro_service = livro_service
        self.emprestar_livro_service = emprestimo_service
        self.devolver_livro_service = devolver_service

    # ==========================================
    #   USUÁRIOS
    # ==========================================
    def cadastrar_usuario(self, nome: str, email: str, matricula: str) -> Usuario:
        return self.cadastrar_usuario_service.executar(nome, email, matricula)

    # ==========================================
    #   LIVROS
    # ==========================================
    def cadastrar_livro(
        self,
        titulo: str,
        autor: str,
        isbn: str,
        ano: int,
        quantidade: int
    ) -> Livro:
        return self.cadastrar_livro_service.executar(
            titulo, autor, isbn, ano, quantidade
        )

    # ==========================================
    #   EMPRÉSTIMOS
    # ==========================================
    def emprestar_livro(self, id_usuario: str, id_livro: str) -> Emprestimo:
        return self.emprestar_livro_service.executar(id_usuario, id_livro)

    def devolver_livro(self, id_emprestimo: str) -> Emprestimo:
        if not self.devolver_livro_service:
            raise RuntimeError("Serviço de devolução não foi inicializado no Container.")
        return self.devolver_livro_service.executar(id_emprestimo)
