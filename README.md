# sprint-relampago-django

Sistema web em Django para gerenciar projetos e as tarefas de cada projeto, desenvolvido como atividade prática da disciplina de Desenvolvimento de Sistemas Web.

## Funcionalidades
- CRUD de Projetos (cadastrar, listar, editar e excluir)
- CRUD de Tarefas vinculadas a um projeto
- Menu de navegação comum a todas as páginas

## Entidades
- *Projeto:* nome, descricao, data_inicio
- *Tarefa:* titulo, descricao, status, (pendente, em andamento ou concluida), prazo, criada_em, projeto(ForeignKey para Projeto)

## Tecnologias
- Python 3
- Django
- SQLite

## Como executar
1. Clone o repositório e entre na pasta:

        git clone https://github.com/provatrack-dev/sprint-relampago-django.git
        cd sprint-relampago-django

2. Crie e ative o ambiente virtual (Windows):

        python -m venv venv
        venv\Scripts\activate

3. Instale as dependências:

        pip install -r requirements.txt

4. Crie o banco de dados:

        python manage.py migrate

5. Crie um superusuário para o admin (opcional):

        python manage.py createsuperuser

6. Rode o servidor e acesse http://127.0.0.1:8000:

        python manage.py runserver

## Fluxo de trabalho
- Cada issue é desenvolvida em uma branch separada (ex.: feature/crud-projetos)
- É proibido commitar direto na main
- Todo código entra por Pull Request, revisado pelo colega da dupla
- Mensagens de commit seguem o padrão tipo: descrição (#número da issue)

## Equipe
- Samuel
- Vitor
