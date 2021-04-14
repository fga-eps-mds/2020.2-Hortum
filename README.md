<div align="center">
	<img width=40% src="https://raw.githubusercontent.com/fga-eps-mds/2020.2-Hortum/main/docs/img/logo.png" alt="Vamos Cuidar" class="lg">
</div>

<!-- Nome do Projeto -->
<h1 align="center"> Hortum </h1>

<!-- Badges -->
<!-- (TODO) Adicionar as Badges de DevOps -->
<p align="center">
      	<a href="https://codecov.io/gh/fga-eps-mds/2020.2-Hortum">
        	<img src="https://codecov.io/gh/fga-eps-mds/2020.2-Hortum/branch/main/graph/badge.svg?token=R7MI4CF8JV"/>
      		</a>
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum/actions/workflows/deploy.yml">
		<img alt="Deploy status" src="https://github.com/fga-eps-mds/2020.2-Hortum/actions/workflows/deploy.yml/badge.svg?style=flat">
		</a>
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum/issues?q=is%3Aissue+is%3Aclosed">
        	 <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed-raw/fga-eps-mds/2020.2-Hortum?style=flat">
		</a>
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum/pulls?q=is%3Apr+is%3Aclosed">
		<img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed-raw/fga-eps-mds/2020.2-Hortum?style=flat">
        </a>
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum/blob/main/LICENSE">
		<img alt="GitHub" src="https://img.shields.io/github/license/fga-eps-mds/2020.2-Hortum?style=flat">
	</a>
</p>

<!-- Repositórios/wiki -->
<p align="center">
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum"><strong>Acesse a API do Hortum</strong></a>
</p>
<p align="center">
	<a href="https://github.com/fga-eps-mds/2020.2-Hortum-Mobile"><strong>Acesse o Frontend do Hortum</strong></a>
</p>
<p align="center">
	<a href="https://fga-eps-mds.github.io/2020.2-Hortum"><strong>Acesse a nossa Wiki</strong></a>
</p>

<!-- Descrição sobre o Projeto -->
## Sobre o Projeto

<p align="justify">&emsp; &emsp; O projeto Hortum é um aplicativo para celulares Android, que busca <strong> facilitar </strong> e <strong> promover </strong> a venda e distribuição das mercadorias de pequenos produtores. Com uma plataforma <strong> simples </strong> e <strong> eficaz </strong>,os produtores podem desfrutar de diversas facilidades para a promoção de seus produtos, assim também facilitando para os compradores a comunicação, localização e possíveis aquisições de produtos dos vendedores. </p>

<!-- Ideias e Incentivos -->
## Ideias e Incentivos

<p align="justify">&emsp; &emsp; A ideia do projeto surgiu relacionada ao site <a href="https://dfrural.emater.df.gov.br/poenacesta/"> PõeNaCesta </a> da EMATER-DF, que tem como princípio promover o contato direto entre produtor e consumidor sem a necessidade de intervenções e intermediações de mercados. Dessa forma, a plataforma Hortum incentivada pelo PõeNaCesta busca seguir com os mesmos princípios em um aplicativo de fácil utilização para todos os seus usuários. </p>

<!-- Funcionalidades Principais -->
## Principais Funcionalidades

1. #### Criação de anúncios de produtos
1. #### Listagem dos anúncios para consumidores
1. #### Visualização detalhada sobre os Produtos e Produtores

<!-- Releases -->
## Releases
### Release 1 (30/03)
#### [Slides](https://docs.google.com/presentation/d/1LPcu3EU9AnJIsrmF4KuUFmTl85_jbg21nd3B3bkKDvI/edit?usp=sharing)
#### [Apresentação](https://drive.google.com/file/d/1pTRLDNsnZ4VCxlIdEfnUGkJpgglq8PEH/view?usp=sharing)
<!-- TODO adicionar R2 -->

<!-- Instalação -->
## Instalação

<!-- Pré-Requisitos -->
### Pré-Requisitos
#### Obrigatórias
|Tecnologias|Descrição|
|-|-|
|[Git](https://git-scm.com/)|`git` é uma ferramenta de versionamento de código `gratuito` e `open source`, capaz de lidar com tudo desde pequenos até grandes projetos, com `velocidade` e `eficiência`.|
|[Docker](https://www.docker.com/get-docker)|o `docker` é uma plataforma `open source` de containerização, ou seja um software para criação de sistemas isolados. Os `containers` são extremamente leves e permitem que os softwares sejam `facilmente` executados e exportados para os diversos sistemas existentes atualmente.|
|[Docker compose](https://docs.docker.com/compose/install/#install-compose)|O `docker-compose` é uma tecnologia de `multi-dockerização` que permite, através de um único arquivo de configuração `.yml`, criar e rodar todos os serviços/dockers da sua aplição.|

#### Para sistemas Windows
|Tecnologias|Descrição|
|-|-|
|[Windows Subsystem for Linux](https://docs.microsoft.com/pt-br/windows/wsl/install-win10)|O Subsistema do Windows para Linux permite que os desenvolvedores executem um `ambiente GNU/Linux`, incluindo a maioria das ferramentas de linha de comando, utilitários e aplicativos, diretamente no Windows, sem modificações e sem a sobrecarga de uma `máquina virtual tradicional` ou instalação `dualboot`.|
|[Docker compose para WSL](https://docs.docker.com/docker-for-windows/wsl/)|O Windows Subsystem for Linux `WSL` apresenta uma mudança significativa na arquitetura, pois é um kernel Linux completo desenvolvido pela Microsoft, permitindo que os contêineres do Linux sejam executados `nativamente`, `sem emulação`. |

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
Ao rodar o código a *porta 8000* estará aberta para o uso da API.

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
<table>
	<tr>
		<td align="center"><a href="https://github.com/brenno-silva"><img src="https://avatars.githubusercontent.com/u/54643530?s=460&u=35993e065c3b56710145bc3bdb13b40d36b2d433&v=4" width="100px;" alt=""/><br /><sub><b>Brenno Oliveira Silva</b></sub></a><br /><a href="https://github.com/brenno-silva"></a></td>
		<td align="center"><a href="https://github.com/CarlosFiuza"><img src="https://avatars.githubusercontent.com/u/71738659?s=460&u=61e0cdb48aa16f91870a3c25e1c93e1bf2856072&v=4" width="100px;" alt=""/><br /><sub><b>Carlos Eduardo de Sousa Fiuza</b></sub></a><br /><a href="https://github.com/CarlosFiuza"></a></td>
		<td align="center"><a href="https://github.com/Joao-Moura"><img src="https://avatars.githubusercontent.com/u/46077033?s=460&u=f32654cf2f096598e9eca3e48b040641fcff3009&v=4" width="100px;" alt=""/><br /><sub><b>João Pedro Moura Oliveira</b></sub></a><br /><a href="https://github.com/Joao-Moura"></a></td>
		<td align="center"><a href="https://github.com/LucasBraunX"><img src="https://avatars.githubusercontent.com/u/78307547?s=460&u=4850fd4162bdaad78e15d7f133673cacfa61dfb6&v=4" width="100px;" alt=""/><br /><sub><b>Lucas Braun Vieira Xavier</b></sub></a><br /><a href="https://github.com/LucasBraunX"></a></td>
		<td align="center"><a href="https://github.com/matheuscvp"><img src="https://avatars.githubusercontent.com/u/54119660?s=460&u=c4c6a51b9894b9773ce04caae2a0dd4d16612b83&v=4" width="100px;" alt=""/><br /><sub><b>Matheus Calixto Vaz Pinheiro</b></sub></a><br /><a href="https://github.com/matheuscvp"></a></td>
		<td align="center"><a href="https://github.com/vital14"><img src="https://avatars.githubusercontent.com/u/54643459?s=460&u=d1761ee486cfc4cf7ac0a36adb98572d3db35e32&v=4" width="100px;" alt=""/><br /><sub><b>Victor Souza Dantas Martins Lima</b></sub></a><br /><a href="https://github.com/vital14"></a></td>
		<td align="center"><a href="https://github.com/VitorLamego"><img src="https://avatars.githubusercontent.com/u/54643464?s=460&u=43a46df920c57476dfe9abe953eba2b89f8f7ca0&v=4" width="100px;" alt=""/><br /><sub><b>Vitor Magalhães Lamego</b></sub></a><br /><a href="https://github.com/VitorLamego"></a></td>
	</tr>
</table>

<!-- License -->
## License
GPLv3 © Hortum. Para demais informações acesse nossa [LICENSE](./LICENSE).
