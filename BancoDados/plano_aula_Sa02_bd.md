# UC: Fundamentos de Banco de Dados
## SA 02 — 1º Trimestre

---

## Tema

Tipos e Arquitetura de Banco de Dados

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Identificar os principais tipos de banco de dados e as características que diferenciam cada um
- Compreender o modelo de dados relacional e por que ele é o mais utilizado em sistemas comerciais
- Reconhecer a arquitetura cliente-servidor aplicada a bancos de dados
- Diferenciar os modelos de dados: relacional, hierárquico, em rede e orientado a objetos
- Relacionar o tipo de banco de dados ao contexto de uso em sistemas de desenvolvimento

**Habilidades da matriz:** H01 — Identificar conceito, tipos, características e armazenamento do banco de dados · H02 — Identificar arquitetura de banco de dados

---

## Conteúdo

- Revisão rápida da SA 01: o que é banco de dados e suas características principais
- Tipos de banco de dados pelo modelo de dados:
  - **Relacional** — dados organizados em tabelas com linhas e colunas · relacionamentos por chaves · SQL como linguagem · exemplos: MySQL, PostgreSQL, Oracle
  - **Hierárquico** — dados organizados em estrutura de árvore pai-filho · pouca flexibilidade · usado em sistemas legados (ex: mainframes)
  - **Em rede** — evolução do hierárquico · permite múltiplos vínculos entre registros · complexo de manter
  - **Orientado a objetos** — dados armazenados como objetos com atributos e métodos · integração com POO · exemplos: db4o, ObjectDB
  - **NoSQL** — não relacional · alta escalabilidade · tipos: documento, chave-valor, coluna, grafo · exemplos: MongoDB, Redis, Cassandra, Neo4j
- Por que o modelo relacional domina o mercado: padronização SQL, integridade de dados, maturidade tecnológica
- Tipos de banco de dados pela finalidade:
  - **OLTP** (Online Transaction Processing) — operacional, transações frequentes, alta escrita e leitura (ex: sistema de pedidos)
  - **OLAP** (Online Analytical Processing) — analítico, consultas complexas, grandes volumes (ex: relatórios gerenciais, BI)
- Arquitetura cliente-servidor:
  - **Cliente** — aplicação que envia requisições ao banco (ex: sistema web, app mobile)
  - **Servidor** — onde o SGBD roda e processa as requisições
  - Fluxo: cliente envia SQL → servidor processa → retorna resultado
- Arquitetura em três camadas: apresentação · aplicação · dados
- Exemplos práticos: como um sistema de e-commerce se comunica com o banco de dados

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 01 — pergunta oral: *"Qual a diferença entre dado e informação?"* |
| Retomada | Professor exibe uma tabela simples de clientes no slide e pergunta: *"Como vocês acham que esse dado chegou até aqui? Quem pediu, quem guardou, quem respondeu?"* — introdução natural à arquitetura cliente-servidor |
| Explicação | Slides — tipos de banco de dados, modelo relacional x outros modelos, OLTP x OLAP, arquitetura cliente-servidor e três camadas |
| Dinâmica | "Qual Tipo de BD?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: modelo relacional é o mais usado · arquitetura cliente-servidor separa quem pede de quem guarda · Próxima aula: Normalização — Parte 1 |

---

## Dinâmica — "Qual Tipo de BD?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar os tipos de banco de dados e seus contextos de uso por meio da classificação de cenários reais, desenvolvendo o raciocínio de escolha técnica adequada a cada situação.

**Materiais:** slide com os cenários projetados · quadro branco para registrar as respostas dos grupos.

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor lê um cenário em voz alta e projeta no slide.

2. **Decisão em grupo** *(1 min)*
Cada grupo decide qual tipo de banco de dados é mais adequado para aquele cenário e por quê.

3. **Apresentação e debate** *(2 min)*
Os grupos compartilham suas respostas. O professor media o debate e consolida a resposta mais adequada.

**Cenários sugeridos:**

| Cenário | Tipo mais adequado | Justificativa |
|---------|--------------------|---------------|
| Sistema de controle de pedidos de um restaurante | Relacional (OLTP) | Transações frequentes, integridade de dados, relacionamentos entre clientes, pedidos e produtos |
| Rede social com bilhões de posts e curtidas | NoSQL — Documento | Alto volume, estrutura flexível, escalabilidade horizontal |
| Relatório mensal de vendas por região para a diretoria | Relacional (OLAP) | Consultas analíticas complexas sobre grandes volumes históricos |
| Aplicativo de GPS com rotas e conexões entre cidades | NoSQL — Grafo | Estrutura de grafo representa conexões e pesos entre nós naturalmente |
| Sistema de autenticação com sessões temporárias de login | NoSQL — Chave-valor | Acesso ultrarrápido por chave, dados simples e temporários |
| Sistema acadêmico com alunos, cursos, notas e professores | Relacional (OLTP) | Relacionamentos complexos, integridade referencial, SQL padronizado |

> **Nota:** reforçar que não existe um tipo de BD "melhor" — existe o mais adequado para cada contexto. Desenvolvedores precisam conhecer as opções para tomar a decisão correta em cada projeto.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 01 — 11/02/2026 · Introdução ao Banco de Dados |
| Próxima aula → | SA 03 — 04/03/2026 · Normalização — Parte 1 · Lançamento do Trabalho |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
