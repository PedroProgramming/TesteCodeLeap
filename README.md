# Teste - CodeLeap

## Requisitos
Antes de rodar o projeto, você precisa ter algumas dependências instaladas:

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)
- Banco de dados PostgreSQL, MySQL ou outro, dependendo da configuração. Caso não haja um banco de dados especificado, o Django fornece, por padrão, o SQLite.


Se for necessário um ambiente virtual, você pode utilizar o venv:

Linux:
```bash
    python3 -m venv venv
    source venv/bin/activate 
```

Windows
```bash
    python -m venv venv
    venv/scripts/activate 
```

## Instalação
Siga as etapas abaixo para instalar e configurar o projeto localmente.

1. Clone o repositório:
```bash
    git clone https://github.com/PedroProgramming/boilerplate.git
    cd boilerplate
```

2. Instale as dependências do projeto:
```bash
    pip install -r requirements.txt
```

3. Configure as variáveis de ambiente. Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
- As variáveis de ambientes usadas, se encontram em contrib/env-base. Copie e cole no arquivo.env criado na raiz do seu projeto


## Configuração
Certifique-se de configurar o banco de dados e outras dependências antes de rodar o projeto.

1. Crie o banco de dados:
```bash
    python manage.py migrate
```

2. (Opcional) Crie um superusuário para acessar o painel administrativo:
```bash
    python manage.py createsuperuser
```

## Como Rodar o Projeto
1. Inicie o servidor de desenvolvimento:
```bash
    python manage.py runserver
```

Agora o projeto estará rodando em http://127.0.0.1:8000/ (ou outro endereço configurado).
