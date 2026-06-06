# UC: Fundamentos de Banco de Dados
## SA 06 — 1º Trimestre

---

## Tema

SQL e NoSQL

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é SQL e qual é o seu papel como linguagem padrão dos bancos de dados relacionais
- Identificar as quatro categorias da linguagem SQL: DDL, DML, DQL e DCL — e reconhecer os comandos de cada uma
- Compreender o conceito de NoSQL e por que ele surgiu como alternativa ao modelo relacional
- Identificar os quatro tipos de banco de dados NoSQL: documento, chave-valor, coluna e grafo
- Diferenciar SQL e NoSQL — quando usar cada abordagem em um projeto de desenvolvimento

**Habilidade da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais

---

## Conteúdo

- O que é SQL — Structured Query Language: linguagem padrão para bancos de dados relacionais
- História do SQL: origem na IBM nos anos 1970, padronização ANSI/ISO, versões atuais
- As quatro categorias da linguagem SQL:
  - **DDL — Data Definition Language:** define a estrutura do banco · comandos: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
  - **DML — Data Manipulation Language:** manipula os dados · comandos: `INSERT`, `UPDATE`, `DELETE`
  - **DQL — Data Query Language:** consulta os dados · comando principal: `SELECT`
  - **DCL — Data Control Language:** controla o acesso · comandos: `GRANT`, `REVOKE`
- Exemplos simples de cada categoria para contextualizar os comandos
- O que é NoSQL — Not Only SQL: bancos de dados não relacionais projetados para escalabilidade e flexibilidade
- Por que o NoSQL surgiu: limitações do modelo relacional em cenários de Big Data, alta disponibilidade e esquemas dinâmicos
- Os quatro tipos de banco de dados NoSQL:
  - **Documento** — dados em formato JSON/BSON · flexibilidade de esquema · ex: MongoDB, CouchDB
  - **Chave-valor** — estrutura simples de par chave → valor · altíssima velocidade · ex: Redis, DynamoDB
  - **Coluna** — dados organizados por colunas em vez de linhas · ideal para analytics · ex: Cassandra, HBase
  - **Grafo** — entidades como nós e relacionamentos como arestas · ideal para redes e conexões · ex: Neo4j
- SQL × NoSQL: comparação direta — estrutura, escalabilidade, consistência, flexibilidade e casos de uso
- Quando usar SQL: dados estruturados, relacionamentos complexos, necessidade de transações ACID
- Quando usar NoSQL: alto volume, esquema variável, escalabilidade horizontal, dados não estruturados

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 05 — pergunta oral: *"Qual a diferença entre banco de dados e SGBD?"* |
| Retomada | Professor exibe dois blocos lado a lado: um comando SQL simples e um documento JSON do MongoDB · Pergunta: *"O que esses dois têm em comum? O que os diferencia?"* — alunos respondem livremente |
| Explicação | Slides — o que é SQL, as quatro categorias com exemplos de comandos, o que é NoSQL, os quatro tipos com exemplos de SGBDs, SQL × NoSQL comparativo |
| Dinâmica | "SQL ou NoSQL?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: SQL = linguagem padrão do relacional · NoSQL = família de abordagens para cenários não relacionais · a escolha depende do projeto · Próxima aula: Ferramentas de Banco de Dados |

---

## Dinâmica — "SQL ou NoSQL?"

**Duração:** 15 minutos · **Agrupamento:** turma inteira — votação individual

**Objetivo:** fixar a diferença entre SQL e NoSQL e desenvolver o raciocínio de escolha técnica adequada ao contexto, analisando cenários reais de sistemas de desenvolvimento.

**Materiais:** slides com os cenários · quadro branco para registrar os votos.

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor projeta um cenário de sistema e pergunta: *"Para este projeto você usaria SQL ou NoSQL? Por quê?"*

2. **Votação** *(1 min)*
Cada aluno vota: **SQL** ou **NoSQL**. O professor registra os votos no quadro.

3. **Justificativa e consolidação** *(2 min)*
O professor escolhe alunos de cada lado para justificar. Em seguida apresenta a resposta mais adequada com a justificativa técnica.

**Cenários sugeridos (5 rodadas):**

| Cenário | Resposta mais adequada | Justificativa |
|---------|----------------------|---------------|
| Sistema de controle financeiro de um banco — transações, contas, saldos e extratos | SQL | Transações ACID obrigatórias, relacionamentos complexos, integridade de dados crítica |
| Plataforma de streaming que recomenda filmes com base no histórico de cada usuário | NoSQL — Grafo | Modelagem de conexões entre usuários, filmes e preferências é naturalmente um grafo |
| Sistema de cadastro de clientes, produtos e pedidos de uma loja virtual de médio porte | SQL | Relacionamentos bem definidos, estrutura estável, volume gerenciável |
| Aplicativo de chat com milhões de mensagens simultâneas e histórico por conversa | NoSQL — Documento | Alto volume, esquema flexível (texto, imagem, vídeo), escalabilidade horizontal |
| Sistema acadêmico com alunos, professores, disciplinas, notas e frequências | SQL | Relacionamentos múltiplos, integridade referencial, consultas complexas com JOINs |

> **Nota:** reforçar que a resposta correta depende sempre do contexto — volume de dados, tipo de relacionamento, necessidade de transações e flexibilidade de esquema. Não existe escolha universalmente correta.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 05 — 18/03/2026 · SGBD — Sistemas de Gerenciamento de Banco de Dados |
| Próxima aula → | SA 07 — 01/04/2026 · Ferramentas de Banco de Dados |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
