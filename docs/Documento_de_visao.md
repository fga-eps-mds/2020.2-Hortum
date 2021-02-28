# Documento de Visão

## Histórico de Revisão

|Data|Versão|Descrição| Autor(es)
|--|--|--|--|
|15/02/2021|1.0|Abertura do Documento|Brenno Oliveira e Carlos Eduardo|  
|19/02/2021|1.0.1|Padronização da Wiki|Carlos Eduardo e João Pedro|

## 1. Introdução

### 1.1 Objetivo

<p align = "justify"> &emsp;&emsp; Este documento tem a finalidade de apresentar a ideia geral, as funcionalidades, exemplificar os problemas existentes a serem resolvidos e como o aplicativo é utilizado para resolver tais adversidades. </p>

### 1.2 Escopo

<p align = "justify"> &emsp;&emsp; O projeto em questão tem o objetivo de facilitar a comunicação entre produtores rurais e compradores. Essa mediação será feita por meio de um aplicativo de forma a auxiliar a localização e aquisição de horticulturas. </p>

### 1.3 Definições, Acrônimos e Abreviações

Abreviação|Significado
-|-
**UnB**|Universidade de Brasília
**MDS**|Métodos e Desenvolvimento de Software

### 1.4 Referências

> Documento de Visão - ArBC. Disponível em: < [https://jlucassr.github.io/ArBC-Pages/mds/Documento_de_visao/](https://jlucassr.github.io/ArBC-Pages/mds/Documento_de_visao/) > Acesso em: 14 de Fevereiro de 2021

> Documento de Visão - Lino, o Bot. Disponível em: < [https://botlino.github.io/docs/doc-visao](https://botlino.github.io/docs/doc-visao) > Acesso em: 14 de Fevereiro de 2021

> IBM Knowledge Center - Documento de Visão. Disponível em: < [https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_6.0.3/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html](https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_6.0.3/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html) > Acesso em: 14 de Fevereiro de 2021



### 3.4 Principais Necessidades da Parte Interessada ou do Usuário
Usuário|Necessidade|Solução Atual|Solução Proposta
-|-|-|-
Produtor|Plataforma para anunciar produtos|Negociação presencial e por redes sociais|Plataforma que integra produtor ao cliente, possibilitando cadastro de produtos
Comprador|Achar produtos mais facilmente|Ir a feiras|Plataforma que integra cliente ao produtor, possibilitando a busca de produtos 

### 3.5. Ambiente do Usuário
<p align = "justify">&emsp;&emsp; Aplicativo mobile para Android</p>

### 3.6. Alternativas e Concorrência
#### 3.6.1. PôeNaCesta 
<p align = "justify">&emsp;&emsp; Plataforma do Emater(Empresa de Assistência Técnica e Extensão Rural) para localização de produtores.</p>
&emsp;&emsp; Descrição do site: *“O produtor, diretamente de sua propriedade, oferece seus produtos para a população sem a necessidade de intermediação de mercados, é você e o produtor, basta procurar o que quer e falar diretamente com ele!”*.

## 4. Visão Geral do Produto

### 4.1. Perspectiva do Produto
<p align = "justify">&emsp;&emsp; O aplicativo Hortum busca facilitar a comunicação entre produtor e cliente, por meio de uma plataforma de anúncios, em que o produtor cadastra seus produtos e o cliente busca o que deseja, assim o cliente consegue contato direto com o pequeno produtor.</p>

### 4.2. Resumo das Capacidades
Benefício|Recursos de suporte
-|-
Ajudar pequenos produtores a anunciar sua mercadoria|Aplicativo com uma interface amigável onde poderão cadastrar toda a sua mercadoria
Auxiliar compradores a encontrar produtos|Interface fácil utilização para pesquisar produtos de horticultura 

### 4.3. Suposições e Dependências
- O usuário deverá possuir um celular Android com acesso a internet
- O aplicativo unirá produtores a compradores

## 5. Recursos do Produto
### 5.1. Recursos do Produtor
- Cadastrar na plataforma
- Anunciar produtos
- Registrar horários 
- Editar anúncios
- Compartilhar anúncio
- Denunciar outro usuário

### 5.2. Recursos do Comprador
- Cadastrar na plataforma
- Pesquisar produtos
- Pesquisar produtor
- Favoritar produtor
- Curtir anúncio
- Compartilhar anúncio
- Avaliar produtor
- Denunciar outro usuário

## 6. Restrições
### 6.1. Restrições de Design
<p align = "justify">&emsp;&emsp; O aplicativo busca proporcionar aos usuários uma utilização autoexplicativa e fácil, dispensando conhecimentos técnicos.</p>

### 6.2. Restrições de implementação
<p align = "justify">&emsp;&emsp; O sistema será implementado utilizando 2 principais frameworks, sendo eles o Django Rest para o back-end e o Flutter para o front-end mobile.</p>

### 6.3. Restrições de Uso
<p align = "justify">&emsp;&emsp; As restrições para utilização do produto se limitam ao usuário possuir um smartphone com acesso a internet.</p>

## 7. Requisitos Funcionais
Funcionalidades|Prioridade
-|-
Cadastro e login de usuário, logar e sair da conta e atualizar dados|Alta
Definição dos produtos (produtor)|Alta
Listagem de produtos|Alta
Listagem de localizações e horários|Média
Compartilhar anúncio|Baixa
Favoritar produtor|Média
Curtir anúncio|Média
Avaliação de usuário|Baixa
Chat entre produtor e comprador|Baixa
Denúncia de usuário|Média
