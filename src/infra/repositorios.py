# infra/repositorios.py

from dominio.entidades import Usuario, Livro


class UsuarioRepositorioMemoria:
    def __init__(self):
        self.usuarios = {}
        self._carregar_dados_iniciais()

    def _carregar_dados_iniciais(self):
        # Dados fake para teste
        u1 = Usuario(id=1, nome="Kevin", ativo=True, limite_emprestimos=3)
        u2 = Usuario(id=2, nome="Maria", ativo=True, limite_emprestimos=2)
        u3 = Usuario(id=3, nome="João", ativo=False, limite_emprestimos=1)

        self.usuarios[u1.id] = u1
        self.usuarios[u2.id] = u2
        self.usuarios[u3.id] = u3

    def obter_por_id(self, usuario_id):
        return self.usuarios.get(usuario_id)

    def atualizar(self, usuario):
        self.usuarios[usuario.id] = usuario


class LivroRepositorioMemoria:
    def __init__(self):
        self.livros = {}
        self._carregar_dados_iniciais()

    def _carregar_dados_iniciais(self):
        l1 = Livro(id=1, titulo="Python para Iniciantes", disponivel=True)
        l2 = Livro(id=2, titulo="Estatística Aplicada", disponivel=True)
        l3 = Livro(id=3, titulo="Senhor dos Anéis", disponivel=False)

        self.livros[l1.id] = l1
        self.livros[l2.id] = l2
        self.livros[l3.id] = l3

    def obter_por_id(self, livro_id):
        return self.livros.get(livro_id)

    def atualizar(self, livro):
        self.livros[livro.id] = livro


class EmprestimoRepositorioMemoria:
    def __init__(self):
        self.emprestimos = []

    def salvar(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar(self):
        return self.emprestimos
