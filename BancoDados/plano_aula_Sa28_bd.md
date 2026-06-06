# UC: Fundamentos de Banco de Dados
## SA 28 — 3º Trimestre

---

## Tema

SQL DQL — Funções de Agregação

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o conceito de função de agregação e quando aplicá-la em uma consulta SQL
- Utilizar as cinco funções de agregação principais: `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`
- Agrupar registros com a cláusula `GROUP BY` e interpretar o resultado gerado
- Filtrar grupos com a cláusula `HAVING` e diferenciar seu uso do `WHERE`
- Construir consultas analíticas completas sobre o banco da locadora combinando agregação e agrupamento

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 27: estrutura do SELECT, WHERE, ORDER BY e DISTINCT
- O que são funções de agregação — definição e papel nas consultas analíticas
- As cinco funções principais:
  - `COUNT(coluna)` — conta o número de registros · `COUNT(*)` conta todas as linhas incluindo nulas
  - `SUM(coluna)` — soma os valores de uma coluna numérica
  - `AVG(coluna)` — calcula a média dos valores de uma coluna numérica
  - `MIN(coluna)` — retorna o menor valor de uma coluna
  - `MAX(coluna)` — retorna o maior valor de uma coluna
- Como usar funções de agregação sem `GROUP BY` — resultado único para toda a tabela
- Cláusula `GROUP BY` — agrupar registros por uma ou mais colunas antes de agregar:
  ```sql
  SELECT coluna, COUNT(*)
  FROM tabela
  GROUP BY coluna;
  ```
- Regra do `GROUP BY`: toda coluna no `SELECT` que não seja uma função de agregação deve estar no `GROUP BY`
- Cláusula `HAVING` — filtrar grupos após a agregação:
  ```sql
  SELECT genero, COUNT(*) AS total
  FROM filme
  GROUP BY genero
  HAVING COUNT(*) > 5;
  ```
- Diferença fundamental entre `WHERE` e `HAVING`:
  - `WHERE` filtra **linhas** antes da agregação
  - `HAVING` filtra **grupos** depois da agregação
- Alias com `AS` — nomear colunas calculadas no resultado
- Ordem de execução das cláusulas: `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`
- Exemplos práticos sobre o banco da locadora: total de locações por cliente, média de ano dos filmes por gênero, gêneros com mais de 3 filmes

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 27 — pergunta oral: *"Qual a diferença entre o operador BETWEEN e o operador IN?"* |
| Retomada | Professor projeta a pergunta: *"Quantas locações cada cliente fez? Qual o filme mais antigo do catálogo?"* — alunos tentam responder com o SELECT que conhecem e percebem a limitação · introdução natural às funções de agregação |
| Explicação | Slides — o que são funções de agregação, as cinco funções com exemplos, GROUP BY, HAVING, diferença WHERE x HAVING, ordem de execução |
| Dinâmica | "Qual Função Usar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: WHERE filtra linhas · GROUP BY agrupa · HAVING filtra grupos · Próxima aula: JOINs Parte 1 |

---

## Dinâmica — "Qual Função Usar?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar as funções de agregação e o uso do GROUP BY e HAVING por meio da escrita de consultas analíticas a partir de enunciados em português — consolidando a habilidade de identificar a função correta para cada necessidade de negócio.

**Materiais:** slide com o esquema do banco da locadora · folha A4 por grupo para escrever as consultas.

**Banco de referência — Locadora:**
```sql
CLIENTE (cpf PK, nome, email, cidade_cliente)
FILME   (id_filme PK, titulo, genero, ano)
LOCACAO (id_locacao PK, cpf_cliente FK, id_filme FK, data_locacao)
```

**Passo a passo:**

1. **Leitura do enunciado** *(1 min por rodada)*
O professor lê o enunciado em voz alta e projeta no slide.

2. **Escrita em grupo** *(2 min)*
O grupo escreve o comando SELECT com a função de agregação correta.

3. **Apresentação e correção** *(1 min)*
Um grupo apresenta a consulta. O professor compara com o gabarito e discute as decisões tomadas.

**Enunciados sugeridos (4 rodadas):**

| Rodada | Enunciado | Gabarito esperado |
|--------|-----------|-------------------|
| 1 | Mostre quantos filmes existem no catálogo no total | `SELECT COUNT(*) AS total_filmes FROM filme;` |
| 2 | Mostre o ano do filme mais recente e o ano do filme mais antigo cadastrados | `SELECT MAX(ano) AS mais_recente, MIN(ano) AS mais_antigo FROM filme;` |
| 3 | Mostre quantos filmes existem em cada gênero, ordenados do gênero com mais filmes para o com menos | `SELECT genero, COUNT(*) AS total FROM filme GROUP BY genero ORDER BY total DESC;` |
| 4 | Mostre apenas os gêneros que têm mais de 3 filmes cadastrados | `SELECT genero, COUNT(*) AS total FROM filme GROUP BY genero HAVING COUNT(*) > 3;` |

> **Nota:** na rodada 4, reforçar por que não é possível usar WHERE no lugar de HAVING — o COUNT ainda não existe no momento em que o WHERE é executado. Usar a ordem de execução das cláusulas para explicar visualmente.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 27 — 09/09/2026 · SQL DQL — SELECT Básico |
| Próxima aula → | SA 29 — 23/09/2026 · SQL DQL — JOINs Parte 1 |

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
