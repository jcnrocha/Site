# UC: Fundamentos de Banco de Dados
## SA 05 — 1º Trimestre

---

## Tema

SGBD — Sistemas de Gerenciamento de Banco de Dados

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um SGBD e qual é o seu papel entre a aplicação e o banco de dados
- Identificar as principais funções de um SGBD: definição, manipulação, controle de acesso, recuperação e concorrência
- Diferenciar banco de dados de SGBD — entendendo que são coisas distintas
- Reconhecer os principais SGBDs do mercado e suas características
- Relacionar o uso do SGBD ao contexto do desenvolvimento de sistemas

**Habilidade da matriz:** H05 — Identificar sistemas de gerenciamento de banco de dados

---

## Conteúdo

- O que é um SGBD — definição e papel no ecossistema de um sistema de informação
- SGBD × banco de dados: o banco é onde os dados ficam, o SGBD é o software que gerencia o acesso
- Funções principais de um SGBD:
  - **Definição de dados** — permite criar e modificar a estrutura do banco (DDL)
  - **Manipulação de dados** — permite inserir, atualizar, excluir e consultar dados (DML, DQL)
  - **Controle de acesso** — define quem pode fazer o quê no banco (DCL)
  - **Recuperação** — restaura o banco a um estado consistente após falhas (backup e recovery)
  - **Controle de concorrência** — gerencia múltiplos acessos simultâneos sem conflito
  - **Integridade** — garante que os dados respeitam as regras definidas (restrições e constraints)
- Tipos de SGBD:
  - **Relacionais (RDBMS):** MySQL, PostgreSQL, Oracle, SQL Server, MariaDB
  - **NoSQL:** MongoDB (documento), Redis (chave-valor), Cassandra (coluna), Neo4j (grafo)
  - **NewSQL:** combinam escalabilidade do NoSQL com transações do relacional (ex: CockroachDB)
- Principais SGBDs relacionais do mercado — características, uso típico e quem mantém:
  - **MySQL** — código aberto, muito usado em aplicações web, mantido pela Oracle
  - **PostgreSQL** — robusto, extensível, forte em conformidade com padrões SQL
  - **Oracle Database** — corporativo, alto desempenho, pago
  - **SQL Server** — Microsoft, integrado ao ecossistema Windows e Azure
  - **SQLite** — leve, embutido em aplicações mobile e desktop, sem servidor
- Como o SGBD se posiciona na arquitetura cliente-servidor
- Por que o desenvolvedor de sistemas precisa conhecer o SGBD que está usando

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 04 — pergunta oral: *"Qual a diferença entre dependência parcial e dependência transitiva?"* |
| Retomada | Professor pergunta: *"Quando vocês abrem um app no celular e ele mostra seus dados, quem está no meio do caminho entre o app e o banco?"* — alunos respondem livremente · introdução natural ao papel do SGBD |
| Explicação | Slides — o que é SGBD, diferença entre BD e SGBD, funções principais, tipos de SGBD, principais SGBDs do mercado |
| Dinâmica | "Quem Sou Eu? — Round SGBD" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: SGBD é o intermediário entre a aplicação e os dados · cada SGBD tem seu contexto de uso ideal · Próxima aula: SQL e NoSQL |

---

## Dinâmica — "Quem Sou Eu? — Round SGBD"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar as características dos principais SGBDs do mercado por meio de um jogo de identificação baseado em pistas, desenvolvendo a associação entre características técnicas e os sistemas correspondentes.

**Materiais:** cartões com as pistas — um conjunto por grupo · ou slide com as pistas projetadas uma de cada vez.

**Passo a passo:**

1. **Leitura das pistas** *(1 min por rodada)*
O professor lê as pistas de um SGBD em ordem crescente de especificidade — da mais genérica para a mais reveladora. Os grupos tentam identificar o SGBD após cada pista.

2. **Resposta em grupo** *(1 min)*
O grupo que identificar primeiro levanta a mão e responde. Acertou na primeira pista: 3 pontos · na segunda: 2 pontos · na terceira: 1 ponto.

3. **Consolidação** *(1 min)*
O professor confirma a resposta e reforça as características do SGBD identificado.

**SGBDs sugeridos (5 rodadas):**

| Rodada | Pista 1 | Pista 2 | Pista 3 | Resposta |
|--------|---------|---------|---------|----------|
| 1 | Sou relacional e código aberto | Sou muito usado em aplicações web com PHP e WordPress | Sou mantido pela Oracle e meu nome tem a ver com o nome de uma filha do meu criador | MySQL |
| 2 | Sou relacional e conhecido pela minha robustez | Sou forte em conformidade com padrões SQL e extensibilidade | Meu nome significa "elefante" e meu logo é um elefante azul | PostgreSQL |
| 3 | Sou um banco de dados que não precisa de servidor | Sou embutido direto na aplicação e muito usado em apps mobile | Estou presente em todos os iPhones e aparelhos Android sem que o usuário saiba | SQLite |
| 4 | Sou NoSQL e guardo dados no formato de documentos JSON | Sou muito usado em aplicações que precisam de alta escalabilidade | Meu nome vem da palavra francesa que significa "canhão" | MongoDB |
| 5 | Sou NoSQL e especializado em guardar pares de chave e valor | Sou extremamente rápido porque guardo os dados em memória | Sou muito usado para cache de sessões e filas de mensagens | Redis |

> **Nota:** ao final da dinâmica, o professor deve projetar uma tabela comparativa rápida com os 5 SGBDs trabalhados, reforçando o contexto de uso de cada um — preparando o terreno para a próxima aula sobre SQL e NoSQL.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 04 — 11/03/2026 · Normalização — Parte 2 |
| Próxima aula → | SA 06 — 25/03/2026 · SQL e NoSQL |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com as pistas da dinâmica impressos (1 conjunto por grupo) ou slide com as pistas
- Quadro branco e marcador (para registrar pontuação dos grupos)

---

## Observações do Professor
