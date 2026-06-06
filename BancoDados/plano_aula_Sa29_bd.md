# UC: Fundamentos de Banco de Dados
## SA 29 — 3º Trimestre

---

## Tema

SQL DQL — JOINs Parte 1

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um JOIN e por que ele é necessário para consultar dados distribuídos em múltiplas tabelas
- Identificar a relação entre chave estrangeira e JOIN — entendendo como o modelo lógico sustenta as consultas
- Escrever consultas com `INNER JOIN` entre duas tabelas utilizando a sintaxe correta
- Interpretar o resultado de um INNER JOIN e compreender por que registros sem correspondência são excluídos
- Construir consultas com INNER JOIN sobre o banco da locadora combinando filtros e ordenação

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 28: funções de agregação, GROUP BY e HAVING
- O problema que o JOIN resolve: dados distribuídos em tabelas separadas precisam ser combinados para gerar informação completa
- O que é um JOIN — definição e relação com as chaves estrangeiras do modelo lógico
- Como o JOIN funciona: o banco compara os valores de duas colunas — uma de cada tabela — e retorna as linhas que têm correspondência
- Tipos de JOIN — visão geral (aprofundamento na SA 30):
  - `INNER JOIN` — retorna apenas os registros que têm correspondência nas duas tabelas
  - `LEFT JOIN` — retorna todos da esquerda, com ou sem correspondência
  - `RIGHT JOIN` — retorna todos da direita, com ou sem correspondência
- Sintaxe do `INNER JOIN`:
  ```sql
  SELECT tabela1.coluna, tabela2.coluna
  FROM tabela1
  INNER JOIN tabela2 ON tabela1.chave = tabela2.chave;
  ```
- Uso de alias de tabela para simplificar a escrita:
  ```sql
  SELECT c.nome, f.titulo
  FROM cliente c
  INNER JOIN locacao l ON c.cpf = l.cpf_cliente
  INNER JOIN filme f   ON l.id_filme = f.id_filme;
  ```
- Quando usar `tabela.coluna` — necessário quando o mesmo nome de coluna existe em mais de uma tabela
- INNER JOIN com `WHERE`, `ORDER BY` e funções de agregação
- Por que registros sem correspondência ficam de fora do INNER JOIN — e quando isso é um problema
- Exemplos práticos sobre o banco da locadora: nome do cliente + título do filme nas locações, total de locações por cliente

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 28 — pergunta oral: *"Qual a diferença entre WHERE e HAVING?"* |
| Retomada | Professor projeta duas tabelas separadas — CLIENTE e LOCACAO — e pergunta: *"Quero ver o nome do cliente junto com a data da locação. Consigo fazer isso com o SELECT que conhecemos?"* — alunos percebem a limitação e o JOIN é introduzido naturalmente |
| Explicação | Slides — o que é JOIN, relação com FK, como o INNER JOIN funciona, sintaxe com e sem alias, combinação com WHERE e ORDER BY, exemplos sobre a locadora |
| Dinâmica | "Junta as Tabelas" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: INNER JOIN retorna só o que tem correspondência nas duas tabelas · o JOIN une o que a FK conectou no modelo lógico · Próxima aula: JOINs Parte 2 — LEFT e RIGHT JOIN |

---

## Dinâmica — "Junta as Tabelas"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar a sintaxe e a lógica do INNER JOIN por meio da escrita de consultas que combinam duas ou três tabelas, partindo de enunciados em português e traduzindo para SQL — consolidando a conexão entre o modelo lógico e as consultas.

**Materiais:** slide com o esquema do banco da locadora · folha A4 por grupo para escrever as consultas.

**Banco de referência — Locadora:**
```sql
CLIENTE (cpf PK, nome, email, cidade_cliente)
FILME   (id_filme PK, titulo, genero, ano)
ATOR    (id_ator PK, nome, nacionalidade)
ELENCO  (id_filme FK → FILME, id_ator FK → ATOR)
LOCACAO (id_locacao PK, cpf_cliente FK → CLIENTE,
         id_filme FK → FILME, data_locacao)
```

**Passo a passo:**

1. **Leitura do enunciado** *(1 min por rodada)*
O professor lê o enunciado e projeta no slide. O grupo identifica quais tabelas precisam ser unidas.

2. **Escrita em grupo** *(2 min)*
O grupo escreve o INNER JOIN correspondente na folha A4.

3. **Apresentação e correção** *(1 min)*
Um grupo apresenta a consulta. O professor compara com o gabarito e discute as decisões.

**Enunciados sugeridos (4 rodadas):**

| Rodada | Enunciado | Gabarito esperado |
|--------|-----------|-------------------|
| 1 | Mostre o nome do cliente e a data de cada locação realizada | `SELECT c.nome, l.data_locacao FROM cliente c INNER JOIN locacao l ON c.cpf = l.cpf_cliente;` |
| 2 | Mostre o nome do cliente e o título do filme de cada locação | `SELECT c.nome, f.titulo FROM cliente c INNER JOIN locacao l ON c.cpf = l.cpf_cliente INNER JOIN filme f ON l.id_filme = f.id_filme;` |
| 3 | Mostre o título do filme e o nome dos atores que participaram de cada filme | `SELECT f.titulo, a.nome FROM filme f INNER JOIN elenco e ON f.id_filme = e.id_filme INNER JOIN ator a ON e.id_ator = a.id_ator;` |
| 4 | Mostre quantas locações cada cliente realizou, exibindo o nome do cliente e o total — ordenado do maior para o menor | `SELECT c.nome, COUNT(*) AS total FROM cliente c INNER JOIN locacao l ON c.cpf = l.cpf_cliente GROUP BY c.nome ORDER BY total DESC;` |

> **Nota:** a rodada 4 combina INNER JOIN com COUNT e GROUP BY — reforçando que as cláusulas aprendidas nas aulas anteriores continuam funcionando normalmente junto ao JOIN. Reforçar que o alias de tabela (`c`, `l`, `f`) é uma boa prática que torna o código mais legível.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 28 — 16/09/2026 · SQL DQL — Funções de Agregação |
| Próxima aula → | SA 30 — 30/09/2026 · SQL DQL — JOINs Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever as consultas na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
