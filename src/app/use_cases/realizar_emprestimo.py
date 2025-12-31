class RealizarEmprestimoService:
    def __init__(self, usuario_repo, livro_repo, emprestimo_repo, emprestimo_domain_service):
        self.usuario_repo = usuario_repo
        self.livro_repo = livro_repo
        self.emprestimo_repo = emprestimo_repo
        self.emprestimo_domain_service = emprestimo_domain_service

    def executar(self, usuario_id, livro_id):
        usuario = self.usuario_repo.obter_por_id(usuario_id)
        livro = self.livro_repo.obter_por_id(livro_id)

        # aplica regras de negócio do domínio
        self.emprestimo_domain_service.validar(usuario, livro)

        emprestimo = Emprestimo_serv(usuario_id, livro_id)
        self.emprestimo_repo.salvar(emprestimo)

        return emprestimo
