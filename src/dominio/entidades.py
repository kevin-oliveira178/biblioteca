from dataclasses import dataclass, field
import uuid
from datetime import datetime

# classe de livros

@dataclass
class Livro:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    titulo: str = ""
    autor: str = ""
    isbn: str = ""
    ano_publicacao: int = 0
    quantidade_total: int = 0
    quantidade_disponivel: int = 0

    def emprestar(self):
        if self.quantidade_disponivel <= 0:
            raise ValueError("Não há exemplares disponíveis para empréstimo.")
        self.quantidade_disponivel -= 1

    def devolver(self):
        if self.quantidade_disponivel >= self.quantidade_total:
            raise ValueError("Todos os exemplares já foram devolvidos.")
        self.quantidade_disponivel += 1


#classe de usuários
@dataclass
class Usuario:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nome: str = ""
    email: str = ""
    matricula: str = ""
    ativo: bool = True


#classe de emprestimo 

@dataclass
class Emprestimo:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    id_usuario: str = ""
    id_livro: str = ""
    data_emprestimo: datetime = field(default_factory=datetime.now)
    data_prevista_devolucao: datetime = None
    data_devolucao: datetime = None
    status: str = "ativo"  # ativo, devolvido, atrasado

    def marcar_devolvido(self):
        self.status = "devolvido"
        self.data_devolucao = datetime.now()

    def esta_atrasado(self) -> bool:
        if self.data_prevista_devolucao is None:
            return False
        if self.data_devolucao is None:
            return datetime.now() > self.data_prevista_devolucao
        return self.data_devolucao > self.data_prevista_devolucao
