# Documento de Arquitetura de Software

## Histórico de Revisão

Data|Versão|Descrição|Autor
-|-|-|-
13/02/2021|1.0|Abertura do Documento|João Pedro
15/02/2021|1.0.1|Padronização de Documento|João Pedro
17/02/2020|1.0.2|Adição do tópico Representação Arquitetural|Victor Lima
19/02/2021|1.0.3|Padronização de Wiki|Carlos Eduardo e João Pedro

## 1. Introdução

### 1.1 Finalidade

<p align = "justify"> &emsp;&emsp; O Seguinte documento tem como finalidade mostrar e esclarecer de uma forma geral a arquitetura utilizada no projeto, tornando o seu processo de entendimento o mais simples possível. Além disso, esse documento também tem como objetivo demonstrar as decisões arquiteturais tomadas pelo grupo em relação ao projeto.</p>

### 1.2 Escopo

<p align = "justify"> &emsp;&emsp; Esse documento visa permitir ao leitor se informar sobre a arquitura utilizada no projeto, incentivando um entendimento mais simples e eficaz a cerca do produto.</p>

### 1.3 Definições, Acrônimos e Abreviações

Abreviação|Significado
-|-
**MDS**| Métodos de Desenvolvimento de Software
**UNB**| Universidade de Brasília

### 1.4 Visão Geral

<p align="justify"> &emsp;&emsp; Esse documento de arquitetura se encontra dividido em 1 tópico, que descrevem os detalhes do software desenvolvido. Se organiza da sequinte forma: </p>

- Introdução: Fornece uma visão geral e introdutória sobre o documento;
- Representação Arquitetural: Fornece informações sobre as tecnologias e os motivos pelos quais elas foram escolhidas;

## 2. Representação Arquitetural

### 2.1 Django REST Framework
<p align = "justify"> &emsp;&emsp; O Django Rest é uma biblioteca para o framework Django que torna simples e ágil a implementação de APi's REST.</p>
<p align = "justify"> &emsp;&emsp; REST(Representational State Transfer) é um conjunto de princípios e definições necessários para a criação de um projeto com interfaces bem definidas.</p>

### 2.2 Django
<p align = "justify"> &emsp;&emsp; Django é um framework web baseado em python de alto nível. O framework dispõe de bastante segurança através do ORM que realiza queries sem utilizar do código SQL para acesso ao banco de dados, o ORM é uiitilizado como ponte de comunicação. Além da segurança é um framework com curva de aprendizagem pequena e por ser baseado em python, a maior parte do grupo têm um pequeno conhecimento para trabalhar com a linguagem no projeto.</p>

### 2.3 Flutter
<p align = "justify"> &emsp;&emsp;O Flutter é um framework desenvolvido na liguagem Dart e permite que sejam criadas aplicações nativas para os aparelhos IOS e android. Por ter essa facilidade de desenvolvimento para dois sistemas diferentes, a linguagem têm crescido bastante e tornado cada vez maior a quantidade de informação para aprendizado, além disso, alguns dos integrantes do grupo já têm conhecimento prévio relacionados a linguagem e por isso, ela foi selecionada.</p>

### Referências

> Como documentar a arquitetura de software. Disponível em: < [http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx](http://www.linhadecodigo.com.br/artigo/3343/como-documentar-a-arquitetura-de-software.aspx) > Acesso em: 13 de Fevereiro de 2021

> Documento de arquitetura Acácia. Disponível em: < [https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document](https://fga-eps-mds.github.io/2019.2-Acacia/#/architecture_document) > Acesso em: 13 de Fevereiro de 2021

> Documento de arquitetura VCU. Disponível em: < [https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Documento_de_Arquitetura](https://fga-eps-mds.github.io/2020.1-VC_Usuario/#/docs/Documento_de_Arquitetura) > Acesso em: 13 de Fevereiro de 2021

> TEMPLATE Documento de Arquitetura de Software. Disponível em: < [https://github.com/DroidFoundry/DroidMetronome/wiki/TEMPLATE-Documento-de-Arquitetura-de-Software](https://github.com/DroidFoundry/DroidMetronome/wiki/TEMPLATE-Documento-de-Arquitetura-de-Software) > Acesso em: 13 de Fevereiro de 2021