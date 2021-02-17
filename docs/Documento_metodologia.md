# Documento de Metodologia e Processos

## Histórico
|Data|Versão|Modificação| Autor(es)
|--|--|--|--|
|17/02/2021|1.0|Abertura do Documento|Vitor Lamego e Victor Lima|  
|17/02/2021|1.1|Descrição das metodologias|Vitor Lamego|

## 1. Introdução
Este documento possui a finalidade de descrever e explicar quais serão as metodologias utilizadas no projeto. Será feito uma breve introdução das metodologias que serão utilizadas, assim como uma apresentação de quais artefatos e rituais/cerimônias serão realizadas pela equipe.

## 2. Metodologias de Base
A equipe não irá utilizar somente uma metodologia dentro do projeto, sendo então adotada uma metodologia híbrida, com base no SCRUM, Kanban e XP. A ideia é reunir alguns artefatos e rituais dessas diferentes metodologias e colocá-las em prática no andamento do prjeto.

Acreditamos que a utilização de uma metodologia híbrida possa ajudar na oferta de uma maior experiência e contato com diferentes processos já consolidados no mercado, além disso o objetivo da equipe não é estar preso a um processo irreversível, e sim estar apto a conhecer coisas novas e estar disposto a aplicar mudanças dentro do processo de acordo com o que a equipe sentir necessidade. "Respostas às mudanças do que seguir um contrato", como diz um dos valores das Metodologias Ágeis.

### 2.1 Scrum
O SCRUM é uma metodologia ágil muito conhecida e que já até se expandiu para diversas outras áreas além da Engenharia de Software. Focada no planejamento e gestão de projetos, ocorre de maneira iterativa, onde a iteração é mais conhecida por **Sprint**, que consiste no período que pode variar de 1 a 4 semanas. Dentro do período da Sprint os membros da equipe devem exercer as tarefas que assim foram demandadas naquele período de tempo.

O SCRUM possui alguns artefatos e rituais que colaboram de maneira significativa para o projeto. Durante a Sprint são realizadas reuniões diariamente conhecidas por Daily Meeting, que servem para alinhar toda a equipe do que vem acontecendo dentro do projeto, são reuniões rápidas e com o sentimento de urgência para que não seja extensa. Outros artefatos muito utilizados e falado no SCRUM são o **Product Backlog** que consiste em uma lista com todas as funcionalidades desejadas para o produto, e também o **Sprint Backlog** que se destina a todas as issues que a equipe se compromete a fazer naquela Sprint.

Além disso, o SCRUM define três papéis dentro da equipe, sendo eles:
* **Scrum Master**: Responsável por garantir que os valores e práticas do SCRUM estão sendo aplicados pela equipe. Também é responsável por assegurar que a equipe não se comprometa excessivamente durante uma Sprint.
* **Product Owner**: Responsável por maximizar o valor de produto em desenvolvimento e por priorizar as funcionalidades existentes no Product Backlog.
* **Development Team**: Responsável por realizar as tarefas que foram lhe designadas para determinada Sprint.

Em relação aos rituais, o SCRUM aplica os seguintes:
* **Sprint Planning**: Reunião que acontece ao início de toda Sprint com o objetivo de selecionar as funcionalidades presentes no Product Backlog que passarão para o Sprint Backlog. Vale ressaltar que o Product Owner possui importância fundamental nesta reunião para assegurar que o valor do produto esteja sendo maximizado.
* **Sprint Review**: Ocorre ao final da Sprint. É um momento onde a equipe se atualiza de tudo o que foi produzido na Sprint e de como está o projeto atualmente.
* **Sprint Retrospective**: É um momento de discussão para a equipe entender o que aconteceu na Sprint que pode ser melhorado para as próximas, e também reforçar aquilo que está funcionando bem, para manter para as próximas também.

#### 2.1.1 Recursos utilizados do SCRUM
* Scrum Master
* Product Owner
* Development Team
* Sprint Planning
* Sprint Review
* Sprint Retrospective
* Daily Meeting
* Product Backlog
* Sprint Backlog

### 2.2 Kanban
Kanban é outra metodologia ágil, foi cirada pela Toyota e ainda hoje é bastante utilizada por diversas empresas e áreas diferentes da de Software por trazer uma organização visual extrema pra dentro de projetos e por ser completamente tranquila de aplicar. Consiste basicamente em um quadro dividos em três principais etapas: **To Do**, **Doing** e **Done**. Desta maneira, as atividades e funcionalidades de um projeto são colocadas na parte de "To Do", assim que começam a ser implementadas passam para o "Doing" e quando finalizadas são colocadas no "Done".

Como se pode perceber é uma metodologia muito simples e que colabora com o alinhamento de toda a equipe do que está ocorrendo dentro do projeto como um todo. Os principais pontos desta metodologia são:
1. Evitar procastinação e tempo ocioso;
2. Economizar tempo;
3. Prático e fácil implementação;
4. Hierarquização de tarefas;
5. Reduz custo e desperdícios;
6. Ajuda a mensurar a produtividade;
7. Facilita comunicação.

Desta maneira a equipe irá utilizar um quadro virtual que possuirá estas diferentes etapas e também uma ligação ao Product Backlog e Sprint Backlog do SCRUM.


#### 2.2.1 Recursos utilizados do Kanban
* To Do
* Doing
* Done

### 2.3 XP
A XP (Extreme Programming) é uma metodologia ágil bastante conhecida também e fortemente ligada a respostas às mudanças de maneira rápida. Se assemelha bastante com os valores do SCRUM e muitas vezes essas duas metodologias são vistas como complementares, onde o SCRUM acaba sendo uma metodologia mais voltada para a área de gerência e a XP para a área de práticas da Engenharia de Software.

O principal objetivo desta metodologia é levar ao extremo algumas boas práticas da Engenharia de Software, sendo principalmente fundada na ideia de que a equipe deve estar apta a mudanças, trabalhando para que o erro dentro do projeto não seja nenhum grande empecilho, mas algo de baixo custo se assim forem seguidas as suas práticas e valores.

E quais são esses valores do Extreme Programming então ? A metodologia possui cinco principais valores, sendo eles: **Simplicidade**, **Feedback**, **Coragem**, **Respeito** e 
**Comunicação**. E seus princípios básicos são: feedback rápido, presumir simplicidade, mudanças incrementais, abraçar mudanças e trabalho de qualidade.

Para isso, algumas práticas como o **Pareamento**, onde dois desenvolvedores trabalham em uma mesma máquina, sendo um escrevendo o código e o outro observando para evitar e remover qualquer tipo de erro, a **Refatoração** com o objetivo de sempre deixar o código mais simples, mantendo sempre as funcionalidades já desenvolvidas, a prática de **Testes** onde todo código escrito deve passar por uma bateria de testes para ser validado ou não de acordo com os requisitos para entrar no código principal do projeto, a ideia de **Integração Contínua** também é altamente utilizada dento do XP.

Como visto, são várias as diferentes práticas exercidas pela XP, e nem todas foram citadas acima. Então a ideia é conseguir reunir, junto da alpicação do SCRUM algumas dessas boas práticas dentro dos rituais e das reuniões para que a equipe tenha um contato com esta metodologia também.

#### 2.3.1 Recursos utilizados do XP
* Pareamento
* Refatoração

## 3. Papéis da Equipe

## 4. Referências

>[SCRUM](https://www.desenvolvimentoagil.com.br/scrum/)
>[XP](https://www.devmedia.com.br/introducao-ao-extreme-programming-xp/29249)
>[Kanban](https://www.digitalhouse.com/br/blog/como-usar-metodologia-kanban)
>[Documento de Processo](https://fga-eps-mds.github.io/2019.2-Acacia/#/project_methodology)
