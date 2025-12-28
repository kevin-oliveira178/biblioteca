from abc import ABC, abstractmethod
from src.dominio.entidades import Usuario, Livro, Emprestimo
from typing import Dict, List, Optional



# ============================================
#   REPOSITÓRIOS ABSTRATOS (DDD)
# ============================================

class UsuarioRepository(ABC):

    @abstractmethod
    def salvar(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id_usuario: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def listar(self) -> List[Usuario]:
        pass


class LivroRepository(ABC):

    @abstractmethod
    def salvar(self, livro: Livro) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id_livro: str) -> Optional[Livro]:
        pass

    @abstractmethod
    def listar(self) -> List[Livro]:
        pass


class EmprestimoRepository(ABC):

    @abstractmethod
    def salvar(self, emprestimo: Emprestimo) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, id_emprestimo: str) -> Optional[Emprestimo]:
        pass

    @abstractmethod
    def listar(self) -> List[Emprestimo]:
        pass

    @abstractmethod
    def listar_por_usuario(self, id_usuario: str) -> List[Emprestimo]:
        pass

