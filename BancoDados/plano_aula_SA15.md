# UC: Fundamentos de Banco de Dados
## Aula 02 — 2º Trimestre

---

## Tema

Modelagem de Dados — Conceitos e Fases

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é modelagem de dados e qual é o seu papel no desenvolvimento de um sistema
- Diferenciar modelo de dados de banco de dados — entendendo que o modelo é o projeto, e o banco é a implementação
- Identificar as três fases da modelagem: conceitual, lógica e física, e o que cada uma representa
- Reconhecer qual artefato corresponde a cada fase (diagrama DER, esquema de tabelas, comandos SQL)
- Relacionar a necessidade de modelar com problemas reais causados por bancos mal estruturados

**Habilidade da matriz:** H03 — Identificar características de modelagem de dados

---

## Conteúdo

- O que é modelagem de dados — definição e propósito
- Por que modelar antes de criar o banco: custo de retrabalho, inconsistências e escalabilidade
- Analogia com projetos de engenharia: planta × obra
- Diferença entre modelo e banco de dados
- As três fases da modelagem:
  - **Fase 1 — Conceitual:** representação de alto nível, independente de tecnologia, foco em entidades e relacionamentos (artefato: DER)
  - **Fase 2 — Lógica:** estrutura de tabelas, chaves primárias e estrangeiras, sem código SQL (artefato: esquema lógico)
  - **Fase 3 — Física:** implementação real no SGBD com SQL — `CREATE TABLE`, tipos de dados e restrições (artefato: script SQL)
- Relação entre modelagem e o ciclo de desenvolvimento de sistemas
- Ferramentas usadas em cada fase: BRModelo / Lucidchart (conceitual), notação textual (lógico), MySQL Workbench / pgAdmin (físico)

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 01 — uma pergunta oral: *"Qual a diferença entre DDL e DML?"* |
| Retomada | O professor apresenta o problema motivador: *"Imagine um sistema de biblioteca criado sem nenhum planejamento — o que pode dar errado?"* — alunos falam livremente |
| Explicação | Slides — conceito de modelagem, analogia com planta de obra, as três fases com exemplos do mesmo sistema em cada fase |
| Dinâmica | "Em qual fase estou?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: *modelagem = planejar antes de construir* · Próxima aula: Modelo Conceitual — Entidades e Atributos |

---

## Dinâmica — "Em Qual Fase Estou?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar a distinção entre as três fases da modelagem por meio de classificação de artefatos reais, desenvolvendo capacidade de leitura e interpretação de representações de banco de dados.

**Materiais:** slides com os artefatos exibidos um por vez, ou cartões impressos distribuídos aos grupos.

**Passo a passo:**

1. **Distribuição dos artefatos** *(2 min)*
O professor exibe (ou distribui) 6 artefatos — 2 de cada fase — relacionados a um mesmo sistema fictício: **sistema de locadora de filmes**.

2. **Classificação em grupo** *(7 min)*
Cada grupo classifica cada artefato em uma das três fases: Conceitual, Lógica ou Física.
O grupo deve também justificar em uma frase por que escolheu aquela fase.

3. **Apresentação e debate** *(5 min)*
Cada grupo apresenta sua classificação para um artefato sorteado. O professor media o debate e consolida as respostas corretas.

**Artefatos sugeridos:**

| Artefato | Fase correta |
|----------|--------------|
| Diagrama com retângulos "Filme" e "Cliente" ligados por losango "Aluga" | Conceitual |
| Diagrama com entidade "Filme" com atributos (título, gênero, ano) sem tipos SQL | Conceitual |
| Tabela escrita: `FILME (id_filme PK, titulo, genero, ano)` | Lógica |
| Tabela escrita: `LOCACAO (id_locacao PK, id_cliente FK, id_filme FK, data_locacao)` | Lógica |
| `CREATE TABLE filme (id_filme INT PRIMARY KEY, titulo VARCHAR(150) NOT NULL, ano INT)` | Física |
| `CREATE TABLE locacao (id_locacao INT PRIMARY KEY, id_cliente INT, id_filme INT, data_locacao DATE)` | Física |

> **Nota:** os artefatos devem ser apresentados embaralhados, sem indicação de fase. O objetivo é que os alunos identifiquem a fase pelo nível de abstração e pelo tipo de representação.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 01 — 20/05/2026 · Retomada SQL — CREATE TABLE e INSERT INTO |
| Próxima aula → | Aula 03 — 03/06/2026 · Modelo Conceitual — Entidades e Atributos |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões ou slides com os artefatos da dinâmica (6 artefatos)
- Quadro branco e marcador

---

## Observações do Professor
