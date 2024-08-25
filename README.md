Guia de Uso da API de CNPJ
Este guia fornece instruções sobre como usar a API de CNPJ desenvolvida com Django e Django REST Framework. A API permite criar e salvar informações de empresas usando o CNPJ fornecido.

Introdução
Esta aplicação é uma API REST que permite consultar informações de uma empresa a partir do CNPJ e salvar essas informações no banco de dados. A URL base da API é http://127.0.0.1:8000/api/cnpj/.

Pré-requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados:

*Python (versão 3.6 ou superior)
*Django (versão 3.2 ou superior)
*Django REST Framework (versão 3.12 ou superior)
*requests (para fazer requisições HTTP)
*Instalação

1. Clone o Repositório

Clone o repositório do GitHub para o seu ambiente local:
 git clone https://github.com/brunnoraone/DesafioFabricaBackend

2. Crie um Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto:
python -m venv venv

Ative o ambiente virtual:
venv\Scripts\activate

3. Instale as Dependências
   Instale as dependências do projeto a partir do arquivo requirements.txt:
pip install -r requirements.txt

4. Configure o Banco de Dados
Certifique-se de que as configurações do banco de dados no arquivo settings.py estão corretas. Se necessário, configure o banco de dados conforme as suas necessidades.

5. Aplique as Migrações
Aplique as migrações para criar as tabelas no banco de dados:
python manage.py migrate

6. Inicie o Servidor de Desenvolvimento

Inicie o servidor Django para rodar a aplicação localmente:
python manage.py runserver
A API estará disponível em http://127.0.0.1:8000/api/cnpj/.

*Como Usar a API*
A API permite criar novos registros de empresa com base no CNPJ fornecido. Veja como fazer uma requisição para adicionar uma empresa:

*Endpoint
URL: http://127.0.0.1:8000/api/cnpj/

*Método: POST

Corpo da Requisição:

Envie uma requisição POST para o endpoint com o seguinte JSON no corpo da requisição:

{
    "cnpj": "12345678000195"
}

Exemplo de Requisição com cURL:
curl -X POST http://127.0.0.1:8000/api/cnpj/ -H "Content-Type: application/json" -d '{"cnpj": "12345678000195"}'

Se o CNPJ for válido e os dados forem salvos com sucesso, a resposta será algo como:

{
    "cnpj": "12345678000195",
    "nome": "Nome da Empresa",
    "nomeFantasia": "Nome Fantasia"
}

*Detalhes da Implementação*

*Modelo Empresa: Representa os dados principais da empresa.
*Modelo Endereco: Armazena informações de endereço associadas ao CNPJ.
*Serializers: Usados para validar e converter dados entre JSON e os modelos Django.
*ViewSet cnpjViewSet: Gerencia as operações de criação e validação do CNPJ, fazendo uma requisição externa para obter os dados da empresa.
