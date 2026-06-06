# UC: Fundamentos de Banco de Dados
## SA 09 — 1º Trimestre

---

## Tema

SQL DML — INSERT INTO

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o papel do DML dentro das categorias SQL e o que o comando `INSERT INTO` realiza
- Escrever a sintaxe correta do `INSERT INTO` com e sem lista de colunas
- Inserir múltiplos registros em um único comando `INSERT INTO`
- Identificar os erros mais comuns na escrita do `INSERT INTO` e propor a correção adequada
- Relacionar o `INSERT INTO` com as restrições definidas no `CREATE TABLE` — entendendo como uma depende da outra

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida: o que é DML e qual é o seu papel dentro das categorias SQL
- O comando `INSERT INTO` — o que faz e quando usar
- Sintaxe com lista de colunas explícita:
  ```sql
  INSERT INTO nome_tabela (coluna1, coluna2, coluna3)
  VALUES (valor1, valor2, valor3);
  ```
- Sintaxe sem lista de colunas — quando usar e por que é arriscada:
  ```sql
  INSERT INTO nome_tabela
  VALUES (valor1, valor2, valor3);
  ```
- Inserção de múltiplos registros em um único comando:
  ```sql
  INSERT INTO nome_tabela (coluna1, coluna2)
  VALUES (valor1a, valor2a),
         (valor1b, valor2b),
         (valor1c, valor2c);
  ```
- Tipos de valores por tipo de dado:
  - Numéricos: sem aspas — `42`, `150.00`
  - Texto: entre aspas simples — `'João Silva'`
  - Data: entre aspas simples no formato `'AAAA-MM-DD'`
  - Booleano: `TRUE` ou `FALSE`
  - Valor nulo: `NULL`
- Como as restrições do `CREATE TABLE` impactam o `INSERT INTO`:
  - `NOT NULL` — impede inserção sem o valor da coluna
  - `UNIQUE` — impede inserção de valor duplicado
  - `PRIMARY KEY` — impede inserção de chave repetida ou nula
  - `DEFAULT` — assume o valor padrão quando a coluna é omitida
  - `AUTO_INCREMENT` — o valor é gerado automaticamente — não deve ser informado
- Erros comuns no `INSERT INTO`:
  - Tipo incompatível: inserir texto em coluna numérica
  - Coluna obrigatória omitida: esquecer uma coluna `NOT NULL` sem `DEFAULT`
  - Valor duplicado em coluna `UNIQUE` ou `PRIMARY KEY`
  - Ordem de valores incorreta quando se usa sintaxe sem lista de colunas
  - Aspas faltando em valores de texto ou data

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 08 — pergunta oral: *"Qual a diferença entre NOT NULL e UNIQUE?"* |
| Retomada | Professor exibe o `CREATE TABLE` de uma tabela de clientes criado na SA 08 e pergunta: *"A estrutura está pronta. Como populamos essa tabela com dados reais?"* — alunos tentam escrever o INSERT livremente no quadro |
| Explicação | Slides — sintaxe do INSERT INTO com e sem colunas, múltiplos registros, tipos de valores, relação com as restrições do CREATE TABLE, erros comuns |
| Dinâmica | "Certo ou Errado? — Round INSERT INTO" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: INSERT com colunas explícitas é mais seguro · as restrições do CREATE TABLE são a primeira linha de defesa contra dados inválidos · Próxima aula: SQL DCL + Revisão Geral |

---

## Dinâmica — "Certo ou Errado? — Round INSERT INTO"

**Duração:** 15 minutos · **Agrupamento:** turma inteira

**Objetivo:** fixar a sintaxe correta do `INSERT INTO` e a relação com as restrições da tabela por meio da análise crítica de comandos com erros intencionais, desenvolvendo leitura e identificação de problemas em código SQL.

**Materiais:** slides com os blocos de código · quadro branco para registrar os votos.

**Contexto da dinâmica:** todos os comandos INSERT são baseados na seguinte tabela, projetada antes das rodadas:

```sql
CREATE TABLE produto (
    id_produto   INT          PRIMARY KEY AUTO_INCREMENT,
    nome         VARCHAR(100) NOT NULL,
    preco        DECIMAL(8,2) NOT NULL,
    estoque      INT          DEFAULT 0,
    ativo        BOOLEAN      DEFAULT TRUE
);
```

**Passo a passo:**

1. **Apresentação do comando** *(1 min por rodada)*
O professor exibe um `INSERT INTO` no slide — código limpo, sem marcação de erro.

2. **Votação** *(1 min)*
A turma decide: **CERTO ✅ ou ERRADO ❌**. O professor registra os votos.

3. **Justificativa obrigatória** *(2 min)*
Quem votou ❌ aponta exatamente o problema e explica o erro. Sem justificativa o ponto não conta.

4. **Reveal e consolidação** *(1 min)*
O professor exibe a versão corrigida e reforça a regra técnica envolvida.

**Blocos sugeridos (4 rodadas):**

| Rodada | Comando | Problema |
|--------|---------|----------|
| 1 | `INSERT INTO produto (nome, preco) VALUES ('Teclado', 150.00);` | Correto ✅ — colunas com DEFAULT e AUTO_INCREMENT podem ser omitidas |
| 2 | `INSERT INTO produto VALUES ('Mouse', 80.00, 10, TRUE);` | Coluna `id_produto` omitida na sintaxe sem lista de colunas — o número de valores não corresponde ao número de colunas |
| 3 | `INSERT INTO produto (nome, preco, estoque) VALUES ('Monitor', '1200,00', 5);` | Valor de `preco` com vírgula entre aspas — tipo incompatível; deveria ser `1200.00` sem aspas |
| 4 | `INSERT INTO produto (nome, preco) VALUES ('Headset', 250.00), ('Webcam', 199.90), ('Hub USB', 89.50);` | Correto ✅ — inserção de múltiplos registros com sintaxe válida |

> **Nota:** as rodadas 1 e 4 são intencionalmente corretas. O objetivo é equilibrar identificação de erro com reconhecimento de código correto — evitando que os alunos desenvolvam o hábito de votar ❌ por precaução sem analisar o código com atenção.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 08 — 08/04/2026 · SQL DDL — CREATE TABLE |
| Próxima aula → | SA 10 — 22/04/2026 · SQL DCL + Revisão Geral · Apresentação dos Trabalhos |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador

---

## Observações do Professor
