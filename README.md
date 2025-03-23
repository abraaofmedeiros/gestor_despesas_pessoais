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

## Estrutura do Banco de Dados
![Modelo Banco de Dados desenvolvido no DBDesigner Online.](imagens_readme/5%20-%20modelo%20banco%20de%20dados.png)


## Estrutura do Projeto
O código está estruturado em módulos para garantir organização e facilidade de manutenção:

- **main.py**: Ponto de entrada da aplicação.


- **user.py**: Gerenciamento de usuários.


- **category.py**: Gerenciamento de categorias de despesas.


- **expense.py**: Registro de despesas.


- **report.py**: Geração de relatórios financeiros.


- **database.py**: Conexão e operações no SQLite.


- **README.md**: Documentação do projeto.

## Como Executar o Projeto
1. Certifique-se de ter o Python 3.7 ou superior instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-despesas.git
3. Acesse o diretório do projeto:
    ```bash
    cd sistema-despesas
4. Execute o arquivo principal:
    ```bash
    python main.py

## Como Interagir com a aplicação

1. Ao iniciar o sistema, você pode cadastrar um novo usuário ou fazer login.
![Menu para usuário não logado](imagens_readme/0%20-%20menu%20nao%20logado.png)

2. Após o login, o menu exibirá opções como cadastrar categoria, registrar
despesa e definir meta mensal.
![Cadastro de categoria](imagens_readme/1%20-%20menu%20logado.png)

3. Escolha uma opção digitando o número correspondente.
![Cadastro de categoria](imagens_readme/2%20-%20cadastro%20categoria.png)

4. Para gerar um relatório, selecione a opção e visualize um resumo das suas
despesas.
![Gerando relatório com sistema](imagens_readme/4%20-%20relatorio.png)

5. Para sair da conta, selecione a opção de logout.

## Tecnologias Utilizadas
A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- **Linguagem**: Python 3.7+
- **Banco de Dados**: SQLite
- **Ferramentas de Desenvolvimento**: Visual Studio Code, DB Designer Online, GitHub

Este sistema oferece uma solução completa para o gerenciamento de despesas, permitindo que os usuários tenham um controle mais eficaz sobre seus gastos mensais.
