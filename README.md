# Sistema de Gestão de Despesas Pessoais

## Descrição
Este sistema tem como objetivo auxiliar os usuários no gerenciamento de suas despesas pessoais, permitindo que cadastrem gastos mensais e emitam relatórios detalhados. Com uma interface baseada em terminal, a aplicação permite que os usuários realizem diversas operações para organizar suas finanças de forma prática e eficiente.

## Funcionalidades
O sistema possibilita a realização das seguintes ações:

- **Cadastrar Usuário**: O usuário pode criar uma conta fornecendo seu nome, nome de usuário e senha. Essas informações são armazenadas de forma segura no banco de dados.
- **Login**: Para acessar o sistema, o usuário deve inserir seu nome de usuário e senha previamente cadastrados.
- **Cadastrar Categoria**: O usuário pode criar categorias personalizadas para classificar suas despesas, facilitando a organização e análise dos gastos.
- **Registrar Despesa**: Cada despesa pode ser cadastrada associando-a a uma categoria, informando o valor gasto e a data em que ocorreu.
- **Definir Meta Mensal**: O sistema permite ao usuário estabelecer um limite de gastos mensais, ajudando a manter o controle financeiro.
- **Gerar Relatório**: O sistema gera um resumo das despesas do mês, permitindo ao usuário visualizar o total gasto em cada categoria e compará-lo com a meta estabelecida.
- **Logout**: O usuário pode encerrar sua sessão, garantindo a privacidade de suas informações.

## Estrutura do Projeto
O código está estruturado em módulos para garantir organização e facilidade de manutenção:

- **main.py**: Ponto de entrada da aplicação.


- **user.py**: Gerenciamento de usuários.


- **category.py**: Gerenciamento de categorias de despesas.


- **expense.py**: Registro de despesas.


- **report.py**: Geração de relatórios financeiros.


- **database.py**: Conexão e operações no SQLite.


- **README.md**: Documentação do projeto.

## Tecnologias Utilizadas
A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- **Linguagem**: Python 3.7+
- **Banco de Dados**: SQLite
- **Ferramentas de Desenvolvimento**: Visual Studio Code, DB Designer Online, GitHub

Este sistema oferece uma solução completa para o gerenciamento de despesas, permitindo que os usuários tenham um controle mais eficaz sobre seus gastos mensais.
