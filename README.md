<h1 align="center">Manhwa Library</h1>

<p align="center">
A Manhwa Library é um projeto que busca disponibilizar uma biblioteca simples de manhwas online. O projeto está sendo desenvolvido utilizando as tecnologias Next.js, Python, FastAPI e SqlAlchemy.
</p>

## **Stack utilizada**

**Front-end:** TypeScript, Next.js, Chakra-ui, eslint, prettier.

**Back-end:** Python, FastAPI, SqlAlchemy.

## **Estrutura de diretórios**

O projeto está estruturado da seguinte maneira:

* `www`: diretório do front-end
* `server`: diretório do back-end
* `docker-compose.yml`: arquivo de configuração do docker-compose
* `makefile`: arquivo de configuração do makefile
* `dockerfile`: arquivo de configuração do dockerfile

<hr/>
<br/>

> [!IMPORTANT]  
> Para que o projeto funcione corretamente, é necessário configurar os arquivos `.env`. Esses arquivos estão localizados nos diretórios `/server` e `/www`. Abra-os em um editor de texto e insira as informações necessárias. As informações específicas necessárias estão documentadas nos arquivos `.env.example`.


<br/>
<hr/>

## **Configuração e Subindo o projeto**

Para este projeto, vai ser necessário:

<blockquote>

- É necessário possuir o **[Node.js](https://nodejs.org/en/)** instalado no computador (recomendado a versão LTS).

- Também, é preciso ter um gerenciador de pacotes o npm e npx já vem por padrão ao instalar o node.j ou **[Yarn](https://www.npmjs.com/package/yarn)**.

- Instale o **[Python](https://www.python.org/)** e o pip.

- Certifique-se de ter o [Docker](https://www.docker.com/get-started) instalado na sua máquina.
  
</blockquote>

### Rodando o projeto separado

Dentro da pasta `cd www` execute esses comandos:

1° Instala as dependências do projeto
```bash
yarn
```

2° Inicia o servidor de desenvolvimento
```bash
yarn dev

```

Abra um segundo terminal, entre dentro da pasta `cd server`, execute:

1° Cria e ativa um ambiente virtual
```bash
python3 -m venv venv
```

2° Ativa o ambiente virtual
```bash
source venv/bin/activate
```

3° Instala as dependências do projeto no ambiente virtual
```bash
pip install -r requirements.txt

```

4° Inicia o servidor
```bash
./run.sh

```

### Rodando projeto com docker-compose

Para gerar o build do projeto, execute o seguinte comando:
```bash
make build
```

Para executar o projeto, execute o seguinte comando (Por padrão, não vai mostrar os logs):
```bash
make up
```

Para interromper e remover os volumes, execute o seguinte comando:
```bash
make down
```

Para ver os logs do projeto, execute o seguinte comando:
```bash
make logs
```

## **Autores**

- [@IgorBrenno](https://www.github.com/IgorBrenno)
- [@kayoRonald](https://www.github.com/kayoRonald)

## **Licença**

O projeto é licenciado sob a licença MIT.
