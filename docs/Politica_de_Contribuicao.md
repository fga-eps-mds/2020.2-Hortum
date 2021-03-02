# Políticas do Repositório
## Histórico de versão

| Data | Versão | Modificação | Autor |
| :- | :- | :- | :- |
| 02/03/2021 | 1.0 | Criação da primeira versão do documento | Victor Lima, Vitor Lamego |

## Introdução

Documento destinado a organizar e padronizar as políticas de contribuição para o projeto.

Aqui se encontram:

- Política de Branch
- Política de Commits

## Políticas de Branch

Branches devem seguir as seguintes regras explicadas neste tópico:

Breve explicação sobre o fluxo de trabalho:

- A branch **main** representa uma versão estável do produto, contendo código já testado e versionado, pronto para ser entregue ao usuário final ou cliente. Essa branch parte das branches **feature** através de pull requests aprovados.

Regras:

1. Existe apenas uma branch **main**.
2. **Não** são permitidos commits feitos diretamente na **main**.

- As branches **feature** representam as funcionalidades do sistema a serem desenvolvidas, elas devem ter a branch **main** como sua origem e fim.

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Antes da abertura de pull request a branch deve ser mesclada à branch **main**.

Regras de nomenclatura:

`feature/issueID-titulo-da-issue`

- A branch **release** representa o conjunto de funcionalidades provenientes de um ponto específico da branch **main**. Essa branch contém funcionalidades prontas que, provavelmente, estarão presentes na próxima versão estável do produto. Apenas issues de **bug fixes** são permitidos nessa branch.

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Essa branch sempre é mesclada à branch **main**.
3. Essa branch aceita apenas mesclagens de branches do tipo **bugfix**.

Regras de nomenclatura:

`release/vNúmero-da-versão`



- As branches do tipo **bugfix** são utilizadas para implementar soluções para bugs, encontrados através de testes realizados em releases específicas, na branch **release**. Isso significa que a branch **bugfix** deve ter a branch **release** como sua origem e fim.

Regras:

1. Essa branch sempre é criada a partir da branch **release**.
2. Essa branch sempre é mesclada na branch **release**.

Regras de nomenclatura:

`bugfix/issueID-titulo-da-issue`


A branch **hotfix** é utilizada para implementar soluções para problemas urgentes encontrados no ambiente de produção. Isso significa que essa branch deve ter a branch **main** como sua orgigem e fim.

- Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Essa branch sempre é mesclada à branch **main**.

Regras de nomenclatura:

`hotfix/issueID-titulo-da-issue`

- As branches **docs** representam a geração ou alteração dos documentos do projeto, elas devem ter a branch **main** como sua origem e fim.

Regras:

1. Essa branch sempre é criada a partir da branch **main**.
2. Antes da abertura de pull request a branch deve ser mesclada à branch **main**.

Regras de nomenclatura:

`docs/issueID-documento`


## Políticas de Commits
Commits devem ser escritos de forma clara e breve, em Português, descrevendo as alterações feitas.

Regras para escrita das mensagens nos commits:

``` 
#issueID Mensagem breve descrevendo alterações
Mensagem mais detalhada sobre o que foi feito neste commit. (Opcional)
```
Observação: é possível indicar quem auxiliou no commit utilizando: "Co-Authored-by: nomeDaPessoa <emailDoGitHub>" na mensagem do commit.

O caractere "#", por padrão, representa uma linha de comentário no arquivo de mensagem do commit. Para evitar problemas, é necessário alterar o caractere com o seguinte comando:

`git config --local core.commentChar auto`

Caso deseje utilizar um outro caractere específico para definir uma linha de comentário, basta substituir a palavra "auto" pelo caractere desejado.

A mensagem principal do commit deve ser escrita no gerundio. Aqui estão alguns exemplos:

Maus exemplos:

`Criada variável de acompanhamento`

`Documentos de visão editados`

Bons exemplos:

`Criando variável de acompanhamento`

`Editando os documentos de visão`

# Política de migrações

As migrações criadas automaticamente pelo Django devem ser adicionadas nos commits dos desenvolvedores, exceto quando possuirem "_auto_" ou "_merge_" em seu nome.

## Referências
> Policies. Disponível em: < [https://fga-eps-mds.github.io/2019.2-Acacia/#/policies](https://fga-eps-mds.github.io/2019.2-Acacia/#/policies) > Acesso em: 2 de março de 2021
> Trunk Based Development. Disponível em: < [https://trunkbaseddevelopment.com/](https://trunkbaseddevelopment.com/) > Acesso em: 2 de março de 2021