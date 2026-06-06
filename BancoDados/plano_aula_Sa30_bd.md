# UC: Fundamentos de Banco de Dados
## SA 30 — 3º Trimestre

---

## Tema

SQL DQL — JOINs Parte 2

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender a diferença entre INNER JOIN, LEFT JOIN e RIGHT JOIN e quando aplicar cada um
- Identificar situações em que registros sem correspondência precisam aparecer no resultado — e escolher o JOIN adequado
- Escrever consultas com `LEFT JOIN` e `RIGHT JOIN` utilizando a sintaxe correta
- Construir consultas com junção de três ou mais tabelas combinando diferentes tipos de JOIN
- Analisar o resultado de uma consulta e identificar qual tipo de JOIN foi utilizado com base nas linhas retornadas

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 29: o que é INNER JOIN e por que registros sem correspondência ficam de fora
- O problema do INNER JOIN: clientes que nunca fizeram locação não aparecem no resultado — e às vezes precisamos deles
- `LEFT JOIN` — retorna todos os registros da tabela da esquerda, com ou sem correspondência na direita:
  ```sql
  SELECT c.nome, l.data_locacao
  FROM cliente c
  LEFT JOIN locacao l ON c.cpf = l.cpf_cliente;
  ```
  - Registros sem correspondência aparecem com `NULL` nas colunas da tabela da direita
- `RIGHT JOIN` — retorna todos os registros da tabela da direita, com ou sem correspondência na esquerda:
  ```sql
  SELECT c.nome, l.data_locacao
  FROM locacao l
  RIGHT JOIN cliente c ON l.cpf_cliente = c.cpf;
  ```
  - Na prática, um RIGHT JOIN pode sempre ser reescrito como LEFT JOIN invertendo as tabelas
- Comparação visual dos três tipos de JOIN:
  - `INNER JOIN` → apenas a interseção das duas tabelas
  - `LEFT JOIN` → tudo da esquerda + interseção
  - `RIGHT JOIN` → tudo da direita + interseção
- Como identificar registros sem correspondência usando `IS NULL` após um LEFT JOIN:
  ```sql
  SELECT c.nome
  FROM cliente c
  LEFT JOIN locacao l ON c.cpf = l.cpf_cliente
  WHERE l.id_locacao IS NULL;
  ```
- Junção de três ou mais tabelas — ordem importa para legibilidade:
  ```sql
  SELECT c.nome, f.titulo, l.data_locacao
  FROM cliente c
  LEFT JOIN locacao l  ON c.cpf = l.cpf_cliente
  LEFT JOIN filme f    ON l.id_filme = f.id_filme;
  ```
- Dinâmica "Qual JOIN Usar?" — análise de cenários reais para escolha do tipo de JOIN
- Exemplos práticos sobre o banco da locadora: clientes sem locação, filmes nunca locados, relatório completo de clientes com ou sem histórico

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 29 — pergunta oral: *"O que acontece com um cliente que nunca fez locação se usarmos um INNER JOIN entre CLIENTE e LOCACAO?"* |
| Retomada | Professor projeta o resultado de um INNER JOIN entre CLIENTE e LOCACAO e aponta: *"Perceberam que o cliente Ana não aparece? Ela existe no banco mas nunca alugou nada. Como incluímos ela no resultado?"* — introdução natural ao LEFT JOIN |
| Explicação | Slides — LEFT JOIN, RIGHT JOIN, comparação visual dos três tipos, IS NULL para encontrar sem correspondência, junção de três tabelas |
| Dinâmica | "Qual JOIN Usar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: INNER = só correspondência · LEFT = todos da esquerda · RIGHT = todos da direita · IS NULL para encontrar ausências · Próxima aula: Subqueries |

---

## Dinâmica — "Qual JOIN Usar?"

**Duração:** 15 minutos · **Agrupamento:** turma inteira — votação individual

**Objetivo:** fixar a diferença entre os três tipos de JOIN por meio da análise de cenários de negócio reais, desenvolvendo o raciocínio de escolha técnica adequada antes de escrever o código.

**Materiais:** slides com os cenários · quadro branco para registrar os votos.

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor lê o cenário e projeta no slide. A turma deve identificar qual tipo de JOIN é o mais adequado.

2. **Votação** *(1 min)*
Cada aluno vota: **INNER JOIN**, **LEFT JOIN** ou **RIGHT JOIN**. O professor registra os votos no quadro.

3. **Justificativa e consolidação** *(2 min)*
O professor escolhe um aluno de cada opção para justificar. Em seguida apresenta o JOIN correto com a consulta correspondente.

**Cenários sugeridos (4 rodadas):**

| Cenário | JOIN correto | Justificativa |
|---------|-------------|---------------|
| Relatório de todas as locações realizadas — apenas locações que têm cliente e filme cadastrados | INNER JOIN | Só interessam registros com correspondência nas duas tabelas |
| Lista de todos os clientes, mostrando a data da última locação — inclusive os que nunca alugaram nada | LEFT JOIN | Precisamos de todos os clientes, mesmo sem locação — NULL aparece para quem nunca alugou |
| Relatório de todos os filmes do catálogo, mostrando quantas vezes cada um foi locado — inclusive os nunca locados | LEFT JOIN | Precisamos de todos os filmes, mesmo sem locação registrada |
| Lista de clientes que nunca realizaram nenhuma locação | LEFT JOIN + IS NULL | LEFT JOIN entre CLIENTE e LOCACAO filtrando WHERE id_locacao IS NULL |

> **Nota:** reforçar que o RIGHT JOIN pode sempre ser substituído por um LEFT JOIN invertendo a ordem das tabelas — na prática, a maioria dos desenvolvedores usa quase exclusivamente o LEFT JOIN por convenção de legibilidade. O importante é entender o conceito de qual lado deve trazer todos os registros.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 29 — 23/09/2026 · SQL DQL — JOINs Parte 1 |
| Próxima aula → | SA 31 — 07/10/2026 · SQL DQL — Subqueries |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
