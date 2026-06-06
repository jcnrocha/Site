# UC: Fundamentos de Banco de Dados
## SA 31 — 3º Trimestre

---

## Tema

SQL DQL — Subqueries

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é uma subquery e qual problema ela resolve em relação ao SELECT simples e ao JOIN
- Identificar os contextos de uso de uma subquery: no WHERE, no FROM e no SELECT
- Escrever subqueries escalares e subqueries com operadores `IN`, `EXISTS` e `NOT IN`
- Diferenciar subquery e JOIN — entendendo quando cada abordagem é mais adequada
- Construir consultas com subqueries sobre o banco da locadora para resolver necessidades analíticas reais

**Habilidade da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais

---

## Conteúdo

- Revisão rápida da SA 30: INNER JOIN, LEFT JOIN, RIGHT JOIN e IS NULL para encontrar ausências
- O que é uma subquery — uma consulta SQL dentro de outra consulta SQL
- Por que subqueries existem: algumas perguntas precisam de um resultado intermediário antes de responder a pergunta principal
- Tipos de subquery pelo resultado que retornam:
  - **Escalar** — retorna um único valor (uma linha, uma coluna) · usada com operadores de comparação
  - **De múltiplas linhas** — retorna várias linhas · usada com `IN`, `NOT IN`, `EXISTS`
  - **De múltiplas colunas** — retorna várias colunas · usada no FROM como tabela derivada
- Subquery no `WHERE` com operador de comparação:
  ```sql
  SELECT titulo FROM filme
  WHERE ano = (SELECT MAX(ano) FROM filme);
  ```
- Subquery no `WHERE` com operador `IN`:
  ```sql
  SELECT nome FROM cliente
  WHERE cpf IN (SELECT cpf_cliente FROM locacao);
  ```
- Subquery no `WHERE` com operador `NOT IN`:
  ```sql
  SELECT nome FROM cliente
  WHERE cpf NOT IN (SELECT cpf_cliente FROM locacao);
  ```
- Subquery no `FROM` — tabela derivada com alias obrigatório:
  ```sql
  SELECT genero, media_ano
  FROM (SELECT genero, AVG(ano) AS media_ano
        FROM filme GROUP BY genero) AS resumo
  WHERE media_ano > 2010;
  ```
- Subquery vs JOIN — quando usar cada abordagem:
  - Subquery: quando o resultado intermediário não precisa aparecer no SELECT final
  - JOIN: quando colunas de múltiplas tabelas precisam aparecer juntas no resultado
- Cuidados com subqueries: performance em grandes volumes, subqueries correlacionadas e legibilidade do código

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 30 — pergunta oral: *"Qual a diferença entre INNER JOIN e LEFT JOIN?"* |
| Retomada | Professor projeta a pergunta: *"Quero saber o título do filme mais recente do catálogo. Consigo fazer isso com o que já sei?"* — alunos tentam com MAX e percebem que precisam de uma etapa intermediária · introdução natural à subquery |
| Explicação | Slides — o que é subquery, tipos pelo resultado, subquery no WHERE com comparação e IN, NOT IN, subquery no FROM, subquery vs JOIN |
| Dinâmica | "Resolve com Subquery" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: subquery = consulta dentro de consulta · WHERE escalar para valor único · IN para lista de valores · NOT IN para ausência · Próxima aula: Views |

---

## Dinâmica — "Resolve com Subquery"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar o uso de subqueries no WHERE por meio da escrita de consultas que exigem um resultado intermediário — consolidando a distinção entre subquery escalar, com IN e com NOT IN em situações reais do banco da locadora.

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
O professor lê o enunciado e projeta no slide. O grupo identifica se precisa de subquery escalar, com IN ou com NOT IN.

2. **Escrita em grupo** *(2 min)*
O grupo escreve a consulta com subquery na folha A4.

3. **Apresentação e correção** *(1 min)*
Um grupo apresenta a consulta. O professor compara com o gabarito e discute as decisões.

**Enunciados sugeridos (4 rodadas):**

| Rodada | Enunciado | Gabarito esperado |
|--------|-----------|-------------------|
| 1 | Mostre o título do filme mais antigo do catálogo | `SELECT titulo FROM filme WHERE ano = (SELECT MIN(ano) FROM filme);` |
| 2 | Mostre o nome dos clientes que já realizaram pelo menos uma locação | `SELECT nome FROM cliente WHERE cpf IN (SELECT cpf_cliente FROM locacao);` |
| 3 | Mostre o nome dos clientes que nunca realizaram nenhuma locação | `SELECT nome FROM cliente WHERE cpf NOT IN (SELECT cpf_cliente FROM locacao);` |
| 4 | Mostre o título dos filmes que foram locados mais de uma vez | `SELECT titulo FROM filme WHERE id_filme IN (SELECT id_filme FROM locacao GROUP BY id_filme HAVING COUNT(*) > 1);` |

> **Nota:** a rodada 4 combina subquery com GROUP BY e HAVING — reforçando que subqueries podem conter qualquer estrutura SQL válida. Comparar a solução com a versão usando JOIN e GROUP BY para mostrar que ambas produzem o mesmo resultado, mas com lógicas diferentes.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 30 — 30/09/2026 · SQL DQL — JOINs Parte 2 |
| Próxima aula → | SA 32 — 14/10/2026 · Views — Criando Visões do Banco |

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
