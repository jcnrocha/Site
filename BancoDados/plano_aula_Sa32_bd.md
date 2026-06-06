# UC: Fundamentos de Banco de Dados
## SA 32 — 3º Trimestre

---

## Tema

Views — Criando Visões do Banco

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é uma View e qual problema ela resolve no contexto de consultas recorrentes e complexas
- Identificar as vantagens do uso de Views: reutilização, segurança, simplificação e manutenção
- Criar e remover Views utilizando os comandos `CREATE VIEW` e `DROP VIEW`
- Consultar uma View como se fosse uma tabela, combinando-a com SELECT, WHERE e JOIN
- Reconhecer as limitações das Views e os cenários em que seu uso é mais adequado

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida da SA 31: subqueries no WHERE, com IN e NOT IN
- O problema que as Views resolvem: consultas complexas repetidas em múltiplos lugares do sistema exigem manutenção duplicada
- O que é uma View — uma consulta SQL salva com um nome, que pode ser usada como se fosse uma tabela
- Como uma View funciona internamente: não armazena dados — executa a consulta toda vez que é acessada
- Vantagens das Views:
  - **Reutilização** — escreve-se a consulta uma vez e reutiliza em qualquer lugar
  - **Segurança** — permite que o usuário acesse apenas as colunas expostas pela View, sem ver a tabela inteira
  - **Simplificação** — transforma consultas complexas com JOINs em algo acessível como uma tabela simples
  - **Manutenção** — alterar a lógica da consulta em um único lugar reflete em todo o sistema
- Sintaxe do `CREATE VIEW`:
  ```sql
  CREATE VIEW vw_locacoes_completas AS
  SELECT c.nome AS cliente, f.titulo AS filme, l.data_locacao
  FROM cliente c
  INNER JOIN locacao l ON c.cpf = l.cpf_cliente
  INNER JOIN filme f   ON l.id_filme = f.id_filme;
  ```
- Consultando uma View como tabela:
  ```sql
  SELECT * FROM vw_locacoes_completas
  WHERE cliente = 'Ana Silva'
  ORDER BY data_locacao DESC;
  ```
- Substituindo ou atualizando uma View com `CREATE OR REPLACE VIEW`
- Removendo uma View com `DROP VIEW`:
  ```sql
  DROP VIEW IF EXISTS vw_locacoes_completas;
  ```
- Limitações das Views: não armazenam dados, podem ter performance inferior a tabelas em grandes volumes, Views complexas podem ser difíceis de depurar
- Boas práticas: prefixo `vw_` no nome da View, nomes descritivos, documentar o propósito com comentários SQL
- Exemplos práticos sobre o banco da locadora: View de locações completas, View de clientes ativos, View de filmes por gênero com contagem

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 31 — pergunta oral: *"Qual a diferença entre usar uma subquery com IN e usar um JOIN para o mesmo resultado?"* |
| Retomada | Professor projeta uma consulta longa com três JOINs e pergunta: *"Se precisarmos desta consulta em 10 lugares diferentes do sistema, o que acontece se mudarmos uma tabela?"* — alunos percebem o problema de manutenção · introdução natural às Views |
| Explicação | Slides — o que é uma View, como funciona internamente, vantagens, CREATE VIEW, consultar como tabela, CREATE OR REPLACE, DROP VIEW, limitações e boas práticas |
| Dinâmica | "Cria a View" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: View = consulta com nome · não armazena dados · simplifica, reutiliza e protege · Próxima aula: SQL DML Avançado — UPDATE e DELETE |

---

## Dinâmica — "Cria a View"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar a criação e o uso de Views por meio da escrita de consultas que serão encapsuladas em uma View e depois consultadas — consolidando a conexão entre CREATE VIEW e SELECT sobre a View criada.

**Materiais:** slide com o esquema do banco da locadora · folha A4 por grupo para escrever os comandos.

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
O professor lê o enunciado e projeta no slide. O grupo deve criar a View e em seguida escrever uma consulta que a utiliza.

2. **Escrita em grupo** *(3 min)*
O grupo escreve o `CREATE VIEW` e o `SELECT` sobre a View na folha A4.

3. **Apresentação e correção** *(1 min)*
Um grupo apresenta os dois comandos. O professor compara com o gabarito e discute as decisões.

**Enunciados sugeridos (3 rodadas):**

| Rodada | Enunciado | Gabarito esperado |
|--------|-----------|-------------------|
| 1 | Crie uma View chamada `vw_filmes_por_genero` que mostre o gênero e o total de filmes de cada gênero. Em seguida, consulte a View para mostrar apenas os gêneros com mais de 2 filmes | **CREATE VIEW:** `CREATE VIEW vw_filmes_por_genero AS SELECT genero, COUNT(*) AS total FROM filme GROUP BY genero;` · **SELECT:** `SELECT * FROM vw_filmes_por_genero WHERE total > 2;` |
| 2 | Crie uma View chamada `vw_historico_locacoes` que mostre o nome do cliente, o título do filme e a data de locação. Em seguida, consulte a View para mostrar apenas as locações de clientes de Curitiba | **CREATE VIEW:** `CREATE VIEW vw_historico_locacoes AS SELECT c.nome, f.titulo, l.data_locacao, c.cidade_cliente FROM cliente c INNER JOIN locacao l ON c.cpf = l.cpf_cliente INNER JOIN filme f ON l.id_filme = f.id_filme;` · **SELECT:** `SELECT nome, titulo, data_locacao FROM vw_historico_locacoes WHERE cidade_cliente = 'Curitiba';` |
| 3 | Remova a View `vw_filmes_por_genero` com segurança, sem gerar erro caso ela não exista | `DROP VIEW IF EXISTS vw_filmes_por_genero;` |

> **Nota:** reforçar na rodada 2 que a View expõe `cidade_cliente` apenas para filtro interno — em um cenário real de segurança, poderíamos criar uma View sem essa coluna para que o usuário não veja o endereço do cliente, mas ainda possa usar a View filtrada pelo administrador. Isso ilustra a vantagem de segurança das Views.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 31 — 07/10/2026 · SQL DQL — Subqueries |
| Próxima aula → | SA 33 — 21/10/2026 · SQL DML Avançado — UPDATE e DELETE |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever os comandos na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
