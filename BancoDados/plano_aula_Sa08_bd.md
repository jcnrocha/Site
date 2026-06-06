# UC: Fundamentos de Banco de Dados
## SA 08 — 1º Trimestre

---

## Tema

SQL DDL — CREATE TABLE

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o papel do DDL dentro das categorias SQL e o que o comando `CREATE TABLE` realiza
- Escrever a sintaxe correta do `CREATE TABLE` com tipos de dados e restrições
- Escolher o tipo de dado adequado para cada coluna com base na natureza da informação
- Aplicar as principais restrições de integridade: `PRIMARY KEY`, `NOT NULL`, `UNIQUE` e `DEFAULT`
- Identificar erros comuns na escrita do `CREATE TABLE` e propor a correção adequada

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida: o que é DDL e qual é o seu papel dentro das categorias SQL
- O comando `CREATE TABLE` — o que faz, quando usar e sua posição no ciclo de desenvolvimento
- Sintaxe completa do `CREATE TABLE`:
  ```sql
  CREATE TABLE nome_tabela (
      nome_coluna TIPO_DADO RESTRICOES,
      ...
  );
  ```
- Tipos de dados em MySQL — definição e exemplos de uso:
  - **Numéricos:** `INT` (inteiro), `SMALLINT` (inteiro pequeno), `DECIMAL(p,s)` (valores monetários), `FLOAT` (ponto flutuante)
  - **Texto:** `VARCHAR(n)` (texto variável até n caracteres), `CHAR(n)` (texto fixo), `TEXT` (texto longo)
  - **Data e hora:** `DATE` (data), `DATETIME` (data e hora), `TIMESTAMP` (marca temporal)
  - **Lógico:** `BOOLEAN` (verdadeiro ou falso)
- Restrições de integridade:
  - `PRIMARY KEY` — identifica unicamente cada linha da tabela
  - `NOT NULL` — impede que a coluna receba valor vazio
  - `UNIQUE` — garante que não há valores duplicados em uma coluna
  - `DEFAULT valor` — define valor padrão quando nenhum é fornecido
  - `AUTO_INCREMENT` — gera valor numérico sequencial automaticamente
- Como combinar restrições em uma mesma coluna
- Boas práticas: nomenclatura de tabelas e colunas, uso de letras minúsculas e underline
- Erros comuns: `DEFAULT` sem valor, tipo inadequado para o dado, ausência de `PRIMARY KEY`
- Exemplos completos: `CREATE TABLE` para sistema de clientes, produtos e pedidos

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 07 — pergunta oral: *"Qual ferramenta usaríamos para gerenciar um banco MySQL? E um PostgreSQL?"* |
| Retomada | Professor exibe o esquema lógico de uma tabela simples e pergunta: *"Como transformamos isso em código SQL?"* — alunos tentam escrever a sintaxe livremente no quadro |
| Explicação | Slides — sintaxe do CREATE TABLE, tipos de dados com exemplos, restrições de integridade, boas práticas, erros comuns |
| Dinâmica | "Certo ou Errado? — Round CREATE TABLE" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: tipo certo + restrição certa + nome claro = CREATE TABLE bem feito · Próxima aula: SQL DML — INSERT INTO |

---

## Dinâmica — "Certo ou Errado? — Round CREATE TABLE"

**Duração:** 15 minutos · **Agrupamento:** turma inteira

**Objetivo:** fixar a sintaxe correta do `CREATE TABLE`, os tipos de dados e as restrições por meio da análise crítica de blocos de código com erros intencionais — desenvolvendo a capacidade de leitura e identificação de problemas em código SQL.

**Materiais:** slides com os blocos de código · quadro branco para registrar os votos.

**Passo a passo:**

1. **Apresentação do bloco** *(1 min por rodada)*
O professor exibe um `CREATE TABLE` no slide — código limpo, sem marcação de erro.

2. **Votação** *(1 min)*
A turma decide: **CERTO ✅ ou ERRADO ❌**. O professor registra os votos.

3. **Justificativa obrigatória** *(2 min)*
Quem votou ❌ aponta a linha com problema e explica o erro. Sem justificativa o ponto não conta.

4. **Reveal e consolidação** *(1 min)*
O professor exibe a versão corrigida e reforça a regra técnica envolvida.

**Blocos sugeridos (4 rodadas):**

| Rodada | Bloco | Problema |
|--------|-------|----------|
| 1 | `CREATE TABLE cliente (nome VARCHAR(150) NOT NULL, email VARCHAR(100) UNIQUE, cpf CHAR(11));` | Ausência de `PRIMARY KEY` — nenhuma coluna identifica unicamente o registro |
| 2 | `CREATE TABLE produto (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(100) NOT NULL, preco CHAR(10), estoque INT DEFAULT 0);` | Tipo inadequado — `preco` como `CHAR(10)` não permite operações numéricas; deveria ser `DECIMAL` |
| 3 | `CREATE TABLE pedido (id INT PRIMARY KEY AUTO_INCREMENT, data_pedido DATE NOT NULL DEFAULT (CURRENT_DATE), valor_total DECIMAL(10,2) NOT NULL);` | Correto ✅ — sintaxe, tipos e restrições estão adequados |
| 4 | `CREATE TABLE funcionario (id INT PRIMARY KEY, nome VARCHAR(150) NOT NULL, salario DECIMAL(8,2) DEFAULT, ativo BOOLEAN DEFAULT TRUE);` | `DEFAULT` sem valor definido — sintaxe incompleta na coluna `salario` |

> **Nota:** a rodada 3 é intencionalmente correta — o objetivo é que os alunos desenvolvam segurança para reconhecer um código bem escrito, e não apenas identificar erros. Reforçar que saber quando está certo é tão importante quanto saber quando está errado.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 07 — 01/04/2026 · Ferramentas de Banco de Dados |
| Próxima aula → | SA 09 — 15/04/2026 · SQL DML — INSERT INTO |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
