# Manhwa api

Api com tema de manhwa

* `main.py`: O código da API.
* `alembic`: Registra as migrações do banco de dados.
* `requirements.txt`: Uma lista dos pacotes Python necessários.
* `.env`: Um arquivo de configuração para a API.

### Instalação

Para instalar os pacotes Python necessários, execute os seguintes comandos:

1 - Criar o venv do Python
```bash
python3 -m venv venv
```

2 - Entrar no venv (ex: fish)
```bash
. venv/bin/activate.fish
```

3 - instalar os pacotes Python
```bash
pip install -r requirements.txt
```

### Execução

Para executar a API, execute o seguinte comando:

```bash
./run.sh
```

`http://localhost:8000`

### .env

O arquivo `.env` contém as seguintes configurações:

| Variável | Descrição |
|---|---|
| `api_title` | O título da API. |
| `api_version` | A versão da API. |
| `api_description` | A descrição da API. |
| `api_contact_name` | O nome do contato da API. |
| `api_contact_email` | O e-mail do contato da API. |

### Exemplo

Um exemplo de `.env` é o seguinte:

```.env
api_title="Manhwa api docs"
api_version="1.0.0"
api_description="Api para criação de manhwa"
api_contact_name="KayoRonald"
api_contact_email="teste@gmail.com"
```

### Documentação

A documentação da API pode ser acessada em `http://localhost:8000/docs``
