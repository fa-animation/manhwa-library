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


> [!IMPORTANT]  
> Antes de qualquer coisa, configure os arquivos `.env` acessando o diretório `/server` e `/www`.

## **Configuração e Subindo o projeto**

1 - Caso queria, mexer no projeto, é necessário baixar os seguintes dependencias:

Entre, nos diretórios `www` e `server`, e sigas as do README.

2 - Se você quiser apenas subir o projeto, o seu unico requesito é o seguinte:

Docker: Certifique-se de ter o [Docker](https://www.docker.com/get-started) caso ainda não o tenha. instalado na sua máquina.

### Rodando projeto com docker-compose

Para gerar o build do projeto, rode o seguinte comando:
```bash
make build
```

Para executar o projeto, rode o seguinte comando:
```bash
make up
```

Para parar o projeto, rode o seguinte comando:
```bash
make down
```

Para ver os logs do projeto, rode o seguinte comando:
```bash
make logs
```

## **Autores**

- [@IgorBrenno](https://www.github.com/IgorBrenno)
- [@kayoRonald](https://www.github.com/kayoRonald)

## **Licença**

O projeto é licenciado sob a licença MIT.
