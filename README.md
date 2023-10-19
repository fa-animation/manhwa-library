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
> Antes de qualquer coisa, configure os arquivos `.env` acessando o diretório `/server` e `/www`.

## **Configuração e Subindo o projeto**

Para este projeto, vai ser necessário:

<blockquote>

- É necessário possuir o **[Node.js](https://nodejs.org/en/)** instalado no computador (recomendado a versão LTS).

- Também, é preciso ter um gerenciador de pacotes o npm e npx já vem por padrão ao instalar o node.j ou **[Yarn](https://www.npmjs.com/package/yarn)**.

- Instale o **[Python](https://www.python.org/)** e o pip.

- Certifique-se de ter o [Docker](https://www.docker.com/get-started) instalado na sua máquina.
  
</blockquote>

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
