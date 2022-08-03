# Central Topic

## Criar App

### digitar

- python manage.py startapp 

	- e o nome_app
	- criará um diretório

### Configurando APP

- Acesse o arquivo

	- settings.py

		- adicione o App

			- INSTALLED_APPS

- Configurando o Model

	- Acesse o arquivo

		- models.py

			- adicione os campos

		- admin.py

			- register modelo

### Serializador

- criar arquivo

	- serializers.py

## Desafio

### API

- "delivery-api"
- controlar
- endpoints 

	- pedidos

		- criação
		- atualização
		- exclusão
		- consulta

	- atualizar o estado atual

		- estados

			- RECEIVED

				- dado a todos os novos pedidos criados

			- CONFIRMED

				- não poderá retornar para um estado 

					- RECEIVED

				- poderá receber um novo estado 

					- DISPATCHED

			- DISPATCHED

				- não poderá retornar para nenhum

					- estados anteriores

				- receber um estado final 

					- DELIVERED

			- DELIVERED 

				- não poderá mudar para nenhum outro estado

			- CANCELED

				- poderá mudar CANCELED

					- se estiver

						- RECEIVED
						- CONFIRMED 
						- DISPATCHED

				- não poderá mudar para nenhum outro estado

- pedidos 

	- salvos

		- arquivo

			- pedidos.json

	- atributos

		- ID

			- int

				- gerado automaticamente 

					- não se repita

		- nomeCliente 

			- string

		- nomeProduto 

			- string

		- valorProduto 

			- float

		- estadoAtualPedido 

			- enumeration

		- horarioCriacaoPedido 

			- timestamp

- Conteinerização 

	- Imagem

		- Docker

- Criar um backlog 

	- ordenado 

		- ordem de execução 

			- tarefas

- Critérios de Aceitação

	- API 

		- padrão REST
		- Metodos

			- cadastre, 
			- liste, 
			- edite
			- atualize 

	- enviado 

		- Git 

			- README.md 

				- •	Deixe instruções 

					- rodar as aplicações

	- responder e-mail 

		- link do projeto 
		- mandar e-mail 

			- lab@cocobambu.com

				- assunto 

					- Estágio Dev - <%SEU_NOME%> 

			- link para o seu repositório

	- Documentação 

		- explicação 

			- arquitetura
			- design 
			- hipóteses assumidas

		- passo a passo 

			- executar a sua solução

				- não poderá 

					- depender

						- IDE

	- Avaliação

		- desenvolvimento do Coco Bambu

	- Execução

		- Build

			- contém instruções 

				- configurarmos o ambiente 
				- fazer o build

		- Execução

			- documentação enviada 

				- contém todas 

					- instruções 

						- executarmos sua solução

		- Performance

			- possui uma performance adequada

	- Código

		- •	Manutenibilidade e extensibilidade

			- escrito é de fácil leitura

				- fácil é criar novas funcionalidades 

		- •	Arquitetura e Design

			- Como está desenhada a arquitetura 
			- responsabilidades estão bem definidas
			- técnica para guiar o desenvolvimento?

		- •	Qualidade de Código e Testes

			- utilizada alguma ferramenta

				- estilo de código para a linguagem

			- possui testes unitários

				- É fácil alterar os testes 

## Criando um usuário

### administrador

- digitar

	- python manage.py createsuperuser

		- responder as perguntas

### Testar acesso

- abra um navegador

	- http://127.0.0.1:8000/admin

## Ambiente

### instalar 

- python

	- https://www.python.org/downloads/
	- Marcar a opcao

		- add python to path

	- testar a instacao

		- abrir o terminal

			- digitar

				- python --version
				- pip --version

	- install virtualenv

		- python -m venv env
		- source ./env/Scripts/activate

	- djangorestframework

		- pip install djangorestframework
		- markdown
		- django-filter

	- Arquivo de gerenciamento

		- pip freeze > requirements.txt

- git

	- https://git-scm.com/download/win

- IDE

	- vs code

		- https://code.visualstudio.com/download
		- instalar extensoes

			- python

	- pycharm

		- https://www.jetbrains.com/pycharm/download/#section=windows

- docker
- Django

	- abrir o terminal

		- digitar

			- pip --version
			- pip install django

## Criar o projeto com Django

### aplicacao

- digitar

	- django-admin startproject

		- e o nome_projeto

	- acessar a pasta do projeto

		- cd nome_projeto

### banco de dados

- digitar

	- python manage.py migrate

### testar o projeto

- digitar

	- python manage.py runserver

- Abrir no navegador

	- http://127.0.0.1:8000/

