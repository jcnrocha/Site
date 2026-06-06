# UC: Fundamentos de Banco de Dados
## SA 27 — 3º Trimestre

---

## Tema

SQL DQL — SELECT Básico

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o papel do DQL dentro das categorias SQL e o que o comando `SELECT` realiza
- Escrever consultas básicas utilizando `SELECT`, `FROM`, `WHERE`, `ORDER BY` e `DISTINCT`
- Aplicar operadores de comparação e operadores lógicos para filtrar registros com precisão
- Diferenciar a ordem de escrita das cláusulas da ordem de execução do `SELECT`
- Construir consultas progressivamente mais complexas sobre o banco da locadora já conhecido da turma

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 26 — como o modelo físico construído no 2º trimestre é a base das consultas
- O que é DQL — Data Query Language: a linguagem de consulta de dados
- O comando `SELECT` — estrutura, papel e posição no ciclo de uso do banco de dados
- Estrutura básica do SELECT:
  ```sql
  SELECT coluna1, coluna2
  FROM tabela
  WHERE condição
  ORDER BY coluna ASC|DESC;
  ```
- Selecionar todas as colunas com `*` — quando usar e quando evitar
- Cláusula `WHERE` — filtragem de registros por condição
- Operadores de comparação: `=`, `<>`, `>`, `<`, `>=`, `<=`
- Operadores lógicos: `AND`, `OR`, `NOT`
- Operador `BETWEEN` — intervalo de valores: `WHERE preco BETWEEN 100 AND 500`
- Operador `LIKE` — busca por padrão em texto: `WHERE nome LIKE 'A%'`
- Operador `IN` — lista de valores: `WHERE cidade IN ('Curitiba', 'São Paulo')`
- Cláusula `ORDER BY` — ordenação por coluna · `ASC` (padrão) e `DESC`
- Cláusula `DISTINCT` — eliminar linhas duplicadas no resultado
- Diferença entre a ordem de escrita e a ordem de execução das cláusulas
- Exemplos práticos sobre o banco da locadora: consultas sobre filmes, clientes e locações

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Abertura formal do 3º trimestre · Conexão com a SA 26: *"Na aula anterior aprendemos a ler um SELECT. Hoje vamos aprender a escrever."* |
| Retomada | Professor exibe o script SQL completo do banco da locadora e pergunta: *"Sabemos criar e popular esse banco. Agora: como fazemos perguntas específicas a ele?"* |
| Explicação | Slides — estrutura do SELECT, cláusulas fundamentais, operadores de comparação e lógicos, ORDER BY, DISTINCT — com exemplos sobre o banco da locadora |
| Dinâmica | "Escreve o SELECT" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: SELECT + FROM + WHERE + ORDER BY + DISTINCT · Próxima aula: Funções de Agregação |

---

## Dinâmica — "Escreve o SELECT"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar a sintaxe e as cláusulas do SELECT por meio da escrita de consultas a partir de enunciados em português — desenvolvendo a habilidade de traduzir uma necessidade de negócio em código SQL.

**Materiais:** slide com o esquema do banco da locadora · folha A4 por grupo para escrever os SELECTs.

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
O grupo escreve o comando SELECT correspondente na folha A4.

3. **Apresentação e correção** *(1 min)*
Um grupo apresenta o SELECT escrito. O professor compara com o gabarito e discute diferenças.

**Enunciados sugeridos (4 rodadas):**

| Rodada | Enunciado | Gabarito esperado |
|--------|-----------|-------------------|
| 1 | Mostre o título e o ano de todos os filmes cadastrados, ordenados do mais recente para o mais antigo | `SELECT titulo, ano FROM filme ORDER BY ano DESC;` |
| 2 | Mostre o nome e o e-mail dos clientes que moram em Curitiba | `SELECT nome, email FROM cliente WHERE cidade_cliente = 'Curitiba';` |
| 3 | Mostre os gêneros de filmes disponíveis no catálogo, sem repetição | `SELECT DISTINCT genero FROM filme;` |
| 4 | Mostre o título dos filmes de ação lançados entre 2015 e 2023 | `SELECT titulo FROM filme WHERE genero = 'Ação' AND ano BETWEEN 2015 AND 2023;` |

> **Nota:** reforçar que existem formas ligeiramente diferentes de escrever o mesmo resultado — o professor deve valorizar a lógica correta mesmo que a sintaxe varie em detalhes não essenciais, como maiúsculas ou espaçamento.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 26 — 02/09/2026 · Conexão com o 3º trimestre — Introdução ao SELECT |
| Próxima aula → | SA 28 — 16/09/2026 · SQL DQL — Funções de Agregação |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever os SELECTs na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
