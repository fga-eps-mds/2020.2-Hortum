<!-- Logo -->

<!-- (TODO) Badges -->

<!-- Nome do Projeto -->

<h1 align="center"> Hortum </h1>

<!-- Descrição sobre o Projeto -->
## Sobre o Projeto

<p align="justify">&emsp; &emsp; O projeto Hortum é um aplicativo para celulares Android, que busca <strong> facilitar </strong> e <strong> promover </strong> a venda e distribuição das mercadorias de pequenos produtores. Com uma plataforma <strong> simples </strong> e <strong> eficaz </strong>,os produtores podem desfrutar de diversas facilidades para a promoção de seus produtos, assim também facilitando para os compradores a comunicação, localização e possíveis aquisições de produtos dos vendedores. </p>

<!-- Ideias e Incentivos -->
## Ideias e Incentivos

<p align="justify">&emsp; &emsp; A ideia do projeto surgiu relacionada ao site <a href="https://dfrural.emater.df.gov.br/poenacesta/"> PõeNaCesta </a> da EMATER-DF, que tem como princípio promover o contato direto entre produtor e consumidor sem a necessidade de intervenções e intermediações de mercados. Dessa forma, a plataforma Hortum incentivada pelo PõeNaCesta busca seguir com os mesmo princípios em um aplicativo de fácil utilização para todos os seus usuários. </p>

<!-- Funcionalidades Principais -->
## Principais Funcionalidades

### Criação de anúncios de produtos
### Listagem dos anúncios para consumidores
### Visualização detalhada sobre os Produtos e Produtores

<!-- (TODO) Releases -->

<!-- Instalação -->
## Instalação

<!-- Pré-Requisitos -->
### Pré-Requisitos

> [Git](https://git-scm.com/)
>
> [Docker](https://www.docker.com/get-docker)
>
> [docker-compose](https://docs.docker.com/compose/install/#install-compose)
>
> [Windows Subsystem for Linux (para sistemas windows)](https://docs.microsoft.com/pt-br/windows/wsl/install-win10)
> > [docker-compose para WSL](https://docs.docker.com/docker-for-windows/wsl/)

<!-- Backend -->
### Baixando e rodando o Backend

```bash
# Clone o Backend
$ git clone https://github.com/fga-eps-mds/2020.2-Hortum.git

# Entre na pasta do projeto
$ cd 2020.2-Hortum

# Build do docker
$ docker-compose build

# Rodando o docker
$ docker-compose up
```
Ao rodar o código a porta 8000 estará aperta para o uso da API.

<!-- Frontend -->
### Baixando e rodando o Frontend
Para rodar o frontend acesse o repositório [mobile](https://github.com/fga-eps-mds/2020.2-Hortum-Mobile) e siga o passo a passo da instalação.

<!-- Usando o Sistema -->
## Utilizando o sistema

<!-- Backend -->
### Backend
Alguns comandos que podem ser úteis utilizando o backend.
```bash
# Acessando o container de maneira interativa
$ docker exec -it [hash do container] bash

# Rodar o docker do backend sem exibir os logs
$ docker-compose run -d

# Acessando o log caso a flag -d tenha sido utilizada
$ docker log [hash do container]
```

<!-- Frontend -->
<!-- (TODO) Gifs mostrando a utilização do frontend -->

<!-- Scripts de limpeza -->
### Script de Limpeza de migrations
```bash
# Entre na pasta do projeto
$ cd 2020.2-Hortum

# Rode o script de limpeza
$ ./src/scripts/clear_migrations.sh
```

<!-- Contributing -->
## Desenvolvedores
||**Membros**|**GitHub**|
|-|-|-|
||Brenno Oliveira Silva|[brenno-silva](https://github.com/brenno-silva)
||Carlos Eduardo de Sousa Fiuza|[CarlosFiuza](https://github.com/CarlosFiuza)
||João Pedro Moura Oliveira|[Joao-Moura](https://github.com/Joao-Moura)
||Lucas Braum Vieira Xavier|[LucasBraunX](https://github.com/LucasBraunX)
||Matheus Calixto Vaz Pinheiro|[matheuscvp](https://github.com/matheuscvp)
||Victor Souza Dantas Martins Lima|[vital14](https://github.com/vital14)
||Vitor Magalhães Lamego|[VitorLamego](https://github.com/VitorLamego)

<!-- License -->
## License
Hortum é distribuido sob a licença GPL-3.0. Para demais informações acesse nosso [LICENSE](./LICENSE)
