# 📚 Sistema de Biblioteca — BIBLIOTECA_FUP

## 📌 Visão Geral

Este projeto implementa um **Sistema de Biblioteca** utilizando **Python** e princípios de **Domain-Driven Design (DDD)**.  
O sistema permite:

- Cadastro de usuários
- Cadastro de livros
- Empréstimo de livros
- Devolução de livros
- Listagem de usuários, livros e empréstimos

O foco principal do projeto é **organização arquitetural**, **separação de responsabilidades** e **clareza do domínio**, e não persistência em banco de dados (os dados são mantidos em memória).

Este projeto foi desenvolvido com fins **acadêmicos**, atendendo aos requisitos de organização, arquitetura e documentação.

---

## 🧠 Arquitetura Utilizada

O projeto segue uma **arquitetura em camadas**, inspirada em **DDD**, organizada da seguinte forma:

```text
src/
├── app/            → Camada de aplicação (orquestração)
│   ├── use_cases/
│   │   ├── conteiner.py
│   │   └── fachada.py
│
├── dominio/        → Coração do sistema (regras de negócio)
│   ├── entidades.py
│   ├── servicos.py
│   ├── regras.py
│   └── abstract_repo.py
│
├── infra/          → Infraestrutura (implementações técnicas)
│   └── repositorios.py
│
├── UI/             → Interface com o usuário (CLI)
│   └── main.py
│
└── testes/         → Testes automatizados

🧭 Por onde começar a ler o código?

Para compreender o projeto de forma correta, recomenda-se a seguinte ordem de leitura:

    dominio/entidades.py
    Modela os principais conceitos do negócio: Usuário, Livro e Empréstimo.

    dominio/regras.py
    Contém regras auxiliares do domínio, como prazo de devolução e cálculo de multa.

    dominio/abstract_repo.py
    Define os contratos (interfaces) dos repositórios utilizados pelo domínio.

    dominio/servicos.py
    Implementa os serviços de domínio, onde estão as regras de negócio principais.

    infra/repositorios.py
    Implementa os repositórios em memória, respeitando os contratos do domínio.

    app/use_cases/conteiner.py
    Responsável pela injeção de dependências e configuração do sistema.

    app/use_cases/fachada.py
    Fornece uma interface simplificada para interação com o sistema.

    UI/main.py
    Implementa a interface de linha de comando (CLI).

🧩 Camada de Domínio

A camada de domínio representa o núcleo do sistema, onde estão as regras de negócio.
📦 Entidades (dominio/entidades.py)
🔹 Usuario

Representa um usuário da biblioteca.

Principais regras:

    O usuário pode estar ativo ou inativo

    Existe um limite máximo de empréstimos simultâneos

    O usuário controla a quantidade de empréstimos ativos

🔹 Livro

Representa um livro do acervo da biblioteca.

Principais regras:

    Controla a quantidade total de exemplares

    Controla a quantidade disponível

    Não permite empréstimo caso não haja disponibilidade

🔹 Emprestimo

Representa um empréstimo de livro.

Principais regras:

    Possui status (ativo ou devolvido)

    Registra datas de empréstimo e devolução

    Permite verificação de atraso

📏 Regras de Negócio (dominio/regras.py)

    📆 Prazo padrão de devolução: 7 dias

    💰 Multa calculada por dia de atraso

Essas regras são utilizadas pelos serviços de domínio.
⚙️ Serviços de Domínio (dominio/servicos.py)

Os serviços de domínio representam os casos de uso do sistema, incluindo:

    Cadastro de usuários

    Cadastro de livros

    Empréstimo de livros

    Devolução de livros

Esses serviços garantem:

    Validação das entidades

    Aplicação correta das regras de negócio

    Atualização do estado do sistema

🗄️ Camada de Infraestrutura
📁 Repositórios (infra/repositorios.py)

Contém as implementações em memória dos repositórios definidos no domínio:

    UsuarioRepositoryMemoria

    LivroRepositoryMemoria

    EmprestimoRepositoryMemoria

Essas classes são responsáveis apenas por armazenar e recuperar dados, sem conter regras de negócio.
🧱 Camada de Aplicação
🔌 Container (app/use_cases/conteiner.py)

O container é responsável por:

    Criar instâncias dos repositórios

    Criar instâncias dos serviços

    Injetar dependências

    Montar a fachada do sistema

Ele centraliza toda a configuração da aplicação.
🪟 Fachada (app/use_cases/fachada.py)

A fachada fornece uma interface simplificada para uso do sistema, expondo métodos como:

    cadastrar_usuario

    cadastrar_livro

    emprestar_livro

    devolver_livro

A interface do usuário não acessa diretamente os serviços, apenas a fachada.
🖥️ Interface do Usuário (CLI)
📄 UI/main.py

Implementa uma interface de linha de comando (CLI), responsável por:

    Exibir menus

    Ler entradas do usuário

    Acionar a fachada

    Exibir os resultados

Não contém regras de negócio.
▶️ Como executar o projeto
1️⃣ Criar o ambiente virtual

python3 -m venv .venv
source .venv/bin/activate

2️⃣ Instalar as dependências

pip install -r requirements.txt

3️⃣ Executar o sistema

python src/UI/main.py

🧪 Testes

Os testes estão localizados em:

src/testes/

Eles validam:

    Serviços de domínio

    Fachada

    Regras de negócio

📜 Histórico do Projeto

O histórico detalhado de mudanças do projeto pode ser encontrado no arquivo:

📄 HISTORY.md