# UC: Fundamentos de Banco de Dados
## SA 26 — 2º Trimestre

---

## Tema

Conexão com o 3º trimestre — Introdução ao SELECT

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender como o modelo físico construído no 2º trimestre serve de base para as consultas SQL do 3º trimestre
- Reconhecer o comando SELECT como o principal instrumento de recuperação de dados em um banco relacional
- Identificar a estrutura básica do SELECT e as cláusulas fundamentais: FROM, WHERE, ORDER BY e DISTINCT
- Diferenciar os comandos já conhecidos (DDL e DML) do novo bloco DQL — a linguagem de consulta
- Antecipar o que será desenvolvido ao longo do 3º trimestre e como os conteúdos se encadeiam

**Habilidade da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais

---

## Conteúdo

- Encerramento formal do 2º trimestre: síntese do percurso — do modelo conceitual ao modelo físico
- Revisão da posição do DQL dentro das categorias SQL: DDL · DML · **DQL** · DCL
- O que é o DQL — Data Query Language: a linguagem de consulta
- O comando SELECT — estrutura e papel dentro do SQL
- Cláusulas fundamentais do SELECT:
  - `SELECT` — quais colunas retornar
  - `FROM` — de qual tabela
  - `WHERE` — condição de filtro
  - `ORDER BY` — ordenação do resultado (ASC e DESC)
  - `DISTINCT` — eliminar linhas duplicadas no resultado
- Operadores de comparação usados no WHERE: `=`, `<>`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `AND`, `OR`, `NOT`
- Como o SELECT se conecta ao modelo físico: só é possível consultar bem um banco que foi bem modelado
- Mapa do 3º trimestre: SELECT → Funções de Agregação → JOINs → Subqueries → Views → UPDATE/DELETE → Documentação → Projeto Integrador

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Encerramento simbólico do 2º trimestre: professor resume em 3 frases o percurso das 13 aulas · Abertura do 3º trimestre |
| Retomada | Professor exibe o script SQL do modelo físico da locadora — produzido na SA 19 — e pergunta: *"Sabemos criar esse banco. Agora: como fazemos perguntas a ele?"* — alunos respondem livremente |
| Explicação | Slides — posição do DQL no SQL, estrutura do SELECT, cláusulas fundamentais com exemplos sobre o banco da locadora já conhecido da turma |
| Dinâmica | "Lê o SELECT" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Mapa do 3º trimestre projetado · Professor apresenta o encadeamento das próximas aulas · Encerramento do 2º trimestre |

---

## Dinâmica — "Lê o SELECT"

**Duração:** 15 minutos · **Agrupamento:** turma inteira — resposta oral individual

**Objetivo:** desenvolver a leitura e interpretação de comandos SELECT em linguagem natural, fixando o papel de cada cláusula por meio da tradução do código SQL para o português — habilidade fundamental para as aulas do 3º trimestre.

**Materiais:** slides com os comandos SELECT · quadro branco para anotações.

**Passo a passo:**

1. **Exibição do comando** *(1 min por rodada)*
O professor projeta um comando SELECT sobre o banco da locadora. A turma deve "traduzir" o que o comando faz em uma frase em português.

2. **Tradução oral** *(1 min)*
O professor escolhe um aluno para traduzir o comando. A turma complementa ou corrige.

3. **Consolidação** *(1 min)*
O professor confirma a tradução correta, destaca a cláusula trabalhada e mostra o resultado esperado da consulta.

**Comandos sugeridos (5 rodadas):**

| Rodada | Comando SQL | Tradução esperada |
|--------|-------------|-------------------|
| 1 | `SELECT titulo, ano FROM filme;` | "Mostre o título e o ano de todos os filmes cadastrados" |
| 2 | `SELECT * FROM cliente WHERE cidade_cliente = 'Curitiba';` | "Mostre todos os dados dos clientes que moram em Curitiba" |
| 3 | `SELECT titulo FROM filme ORDER BY ano DESC;` | "Mostre os títulos dos filmes ordenados do mais recente para o mais antigo" |
| 4 | `SELECT DISTINCT genero FROM filme;` | "Mostre cada gênero de filme uma única vez, sem repetição" |
| 5 | `SELECT titulo FROM filme WHERE ano >= 2020 AND genero = 'Ação';` | "Mostre o título dos filmes de ação lançados a partir de 2020" |

> **Nota:** usar o banco da locadora — já familiar da turma desde a SA 15 — elimina a necessidade de apresentar um novo contexto e permite que o foco fique 100% na leitura e interpretação do SELECT.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 25 — 26/08/2026 · Revisão e correção comentada das provas do 2º trimestre |
| Próxima aula → | SA 27 — 09/09/2026 · SQL DQL — SELECT Básico |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Script SQL do modelo físico da locadora (SA 19) para referência na retomada
- Quadro branco e marcador

---

## Observações do Professor
