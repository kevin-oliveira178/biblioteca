# src/infra/repositorios.py

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from src.dominio.entidades import Usuario, Livro, Emprestimo


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


# ============================================
#   IMPLEMENTAÇÕES EM MEMÓRIA
# ============================================

class UsuarioRepositoryMemoria(UsuarioRepository):

    def __init__(self):
        self.usuarios: Dict[str, Usuario] = {}

    def salvar(self, usuario: Usuario) -> None:
        self.usuarios[usuario.id] = usuario

    def buscar_por_id(self, id_usuario: str) -> Optional[Usuario]:
        return self.usuarios.get(id_usuario)

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        return next((u for u in self.usuarios.values() if u.email == email), None)

    def listar(self) -> List[Usuario]:
        return list(self.usuarios.values())


class LivroRepositoryMemoria(LivroRepository):

    def __init__(self):
        self.livros: Dict[str, Livro] = {}

    def salvar(self, livro: Livro) -> None:
        self.livros[livro.id] = livro

    def buscar_por_id(self, id_livro: str) -> Optional[Livro]:
        return self.livros.get(id_livro)

    def listar(self) -> List[Livro]:
        return list(self.livros.values())


class EmprestimoRepositoryMemoria(EmprestimoRepository):

    def __init__(self):
        self.emprestimos: Dict[str, Emprestimo] = {}

    def salvar(self, emprestimo: Emprestimo) -> None:
        self.emprestimos[emprestimo.id] = emprestimo

    def buscar_por_id(self, id_emprestimo: str) -> Optional[Emprestimo]:
        return self.emprestimos.get(id_emprestimo)

    def listar(self) -> List[Emprestimo]:
        return list(self.emprestimos.values())

    def listar_por_usuario(self, id_usuario: str) -> List[Emprestimo]:
        return [e for e in self.emprestimos.values() if e.id_usuario == id_usuario]
