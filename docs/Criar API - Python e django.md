[]([http://www.exemplodeurl.com](https://cocobambu.com/wp-content/uploads/2022/06/coco-bambu_logo-header.png))

# Criar API - Python - Desafio Coco Bambu 

## Baclog

- [x] Ambiente
- [x] Configuração do Projeto
	- [x] Arquitetura
	- [x] Design	
- [x] Modelagem
- [x] Serializer
- [x] ViewSets
- [x] Routers
- [ ] Conteinerização
- [ ] Qualidade de Código e Testes

## Ambiente

### instalar 

- python

	- https://www.python.org/downloads/
	- Marcar a opcao

		- add python to path

	- testar a instacao

		- abrir o terminal

			- python --version
			- pip --version

	- install virtualenv

		- python -m venv env
		- source ./env/Scripts/activate

	- Arquivo de gerenciamento

		- pip freeze > requirements.txt

- Django

	- abrir o terminal

		- digitar

			- pip --version
			- pip install django

- git

	- https://git-scm.com/download/win

- IDE

	- vs code

		- https://code.visualstudio.com/download
		- instalar extensoes

			- python

- docker

	- https://www.docker.com/products/docker-desktop/

## Criar o projeto com Django

### aplicacao

- django-admin startproject

### criar banco de dados

- python manage.py migrate

### testar o projeto

- python manage.py runserver
- Abrir no navegador

	- http://127.0.0.1:8000/


## Criar App Pedido

### 1 python manager.py startapp pedidos

### 2 acessar a pasta config

- settings.py 

	- Na opcao -> APP_INSTALLER

		-  adiciona nome do APP 

### 3 acessa pasta pedidos

- o arquivo -> models.py

	- criar os atributos

### 4 acessar o arquivo admin.py

- registrar o Model

### 5 criar as migrations 

- python manager.py makemigrations

### 6 atualiza o banco

- python manager.py migrate

### 7 testar a aplicação

- python manager.py runserver
- http://localhost:8000/admin

## gerando APIs

### 1 Instalar o djangorestframework

-  pip install djangorestframework

### 2 criar a pasta api dentro da pasta pedidos

- criar as subpastas

### 3 criar o arquivo de serializacao 

- pedidosSerializer

### 4 criar o arquivo de visualizacao

- pedidosViewSet

### 5 configurar a rota no arquivo

- urls.py dentro da pasta config

### 6 testar a aplicação

- python manager.py runserver
- http://localhost:8000/api/v1/pedidos

## Criando um usuário

### administrador

- python manage.py createsuperuser

### abra um navegador

- http://127.0.0.1:8000/admin

## Sobre o Desafio

### Construir - API

- "delivery-api"

	- atributos

		- ID
		- nomeCliente 
		- nomeProduto 
		- valorProduto 
		- estadoAtualPedido 
		- horarioCriacaoPedido 

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

		- Maquina de estados

			-     RECEIVED

				-  ["Confirmado", "Despachado", "Entregue","Cancelado"]

			-     CONFIRMED

				- ["Despachado", "Cancelado"]

			-     DISPATCHED

				- ["Entregue","Cancelado"]

			-     DELIVERED

				- []

			-     CANCELED

				- []

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


