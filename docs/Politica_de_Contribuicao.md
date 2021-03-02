# Políticas do Repositório
## Histórico de versão

| Data | Versão | Modificação | Autor |
| :- | :- | :- | :- |
| 02/03/2021 | 1.0 | Criação da primeira versão do documento | Victor Lima e Vitor Lamego |

## 1. Introdução

Documento destinado a organizar e padronizar as políticas de contribuição para o projeto.

Aqui se encontram:

- Política de Branch
- Política de Commits


## 2. Políticas de Branch

<p align = "justify"> &emsp;&emsp; As branches do projeto serão dividas de acordo com a sua finalidade principal para manter uma organização no padrão do projeto. A seguir estão as regras de classificação das branches: </p>


### 2.1 Branch Main

<p align = "justify"> &emsp;&emsp; A branch <b>main</b> representa uma versão estável do produto, contendo código já testado e versionado, pronto para ser entregue ao usuário final ou cliente. Essa branch parte das branches <b>feature</b> através de pull requests aprovados. </p>

Regras:

1. Existe apenas uma branch **main**.
2. **Não** são permitidos commits feitos diretamente na **main**.


### 2.2 Branches Feature

<p align = "justify"> &emsp;&emsp; As branches <b>feature</b> representam as funcionalidades do sistema a serem desenvolvidas, elas devem ter a branch <b>main</b> como sua origem e fim. </p>

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Antes da abertura de pull request a branch deve ser mesclada à branch **main**.

Regras de nomenclatura:

`feature/issueID-titulo-da-issue`


### 2.3 Branches Release
<p align = "justify"> &emsp;&emsp; A branch <b>release</b> representa o conjunto de funcionalidades provenientes de um ponto específico da branch <b>main</b>. Essa branch contém funcionalidades prontas que, provavelmente, estarão presentes na próxima versão estável do produto. Apenas issues de <b>bug fixes</b> são permitidos nessa branch. </p>

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Essa branch sempre é mesclada à branch **main**.
3. Essa branch aceita apenas mesclagens de branches do tipo **bugfix**.

Regras de nomenclatura:

`release/vNúmero-da-versão`


### 2.4 Branches Bugfix

<p align = "justify"> &emsp;&emsp; As branches do tipo <b>bugfix</b> são utilizadas para implementar soluções para bugs, encontrados através de testes realizados em releases específicas, na branch <b>release</b>. Isso significa que a branch <b>bugfix</b> deve ter a branch <b>release</b> como sua origem e fim. </p>

Regras:

1. Essa branch sempre é criada a partir da branch **release**.
2. Essa branch sempre é mesclada na branch **release**.

Regras de nomenclatura:

`bugfix/issueID-titulo-da-issue`


### 2.5 Branches Hotfix

<p align = "justify"> &emsp;&emsp; A branch <b>hotfix</b> é utilizada para implementar soluções para problemas urgentes encontrados no ambiente de produção. Isso significa que essa branch deve ter a branch <b>main</b> como sua origem e fim. </p>

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Essa branch sempre é mesclada à branch **main**.

Regras de nomenclatura:

`hotfix/issueID-titulo-da-issue`


### 2.6 Branches Docs

<p align = "justify"> &emsp;&emsp; As branches <b>docs</b> representam a geração ou alteração dos documentos do projeto, elas devem ter a branch <b>main</b> como sua origem e fim. </p>

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Antes da abertura de pull request a branch deve ser mesclada à branch **main**. 

Regras de nomenclatura:

`docs/issueID-documento`


## 3. Políticas de Commits
<p align = "justify"> &emsp;&emsp; Commits devem ser escritos de forma clara e breve, em português, descrevendo as alterações feitas.

Regras para escrita das mensagens nos commits: </p>

``` 
#issueID Mensagem breve descrevendo alterações

Exemplo: #23 Definindo arquitetura do banco de dados
```

<p align = "justify"> &emsp;&emsp; O caractere "#", por padrão, representa uma linha de comentário no arquivo de mensagem do commit. Para evitar problemas, é necessário alterar o caractere com o seguinte comando: </p>

`git config --local core.commentChar auto`

<p align = "justify"> &emsp;&emsp; Caso deseje utilizar um outro caractere específico para definir uma linha de comentário, basta substituir a palavra "auto" pelo caractere desejado. </p>

<p align = "justify"> &emsp;&emsp; A mensagem principal do commit deve ser escrita no gerundio. Aqui estão alguns exemplos:</p>

<b>Maus exemplos:</b>

`Criada variável de acompanhamento`

`Documentos de visão editados`

<b>Bons exemplos:</b>

`Criando variável de acompanhamento`

`Editando os documentos de visão`

</p>
<b>Observação:</b> Para indicar quem te auxiliou em determinado commit, basta acrescentar à mensagem

`Co-Authored-by: nomeDaPessoa <emailDoGitHub>` 


## Referências
> Policies. Disponível em: < [https://fga-eps-mds.github.io/2019.2-Acacia/#/policies](https://fga-eps-mds.github.io/2019.2-Acacia/#/policies) > Acesso em: 2 de março de 2021

> Trunk Based Development. Disponível em: < [https://trunkbaseddevelopment.com/](https://trunkbaseddevelopment.com/) > Acesso em: 2 de março de 2021