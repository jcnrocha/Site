# UC: Fundamentos de Banco de Dados
## Aula 01 — 2º Trimestre

---

## Tema

Retomada SQL — CREATE TABLE e INSERT INTO

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Relembrar as categorias da linguagem SQL: DDL, DML, DQL e DCL
- Reconhecer a sintaxe do `CREATE TABLE`, os principais tipos de dados e as restrições disponíveis
- Reconhecer a sintaxe do `INSERT INTO` com e sem lista de colunas, e com múltiplos registros
- Identificar erros comuns em comandos SQL e justificar por que estão incorretos
- Conectar os conceitos do 1º Trimestre com o que será desenvolvido no 2º Trimestre

**Habilidades da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Categorias da linguagem SQL: DDL, DML, DQL, DCL — definição e exemplos de comandos
- `CREATE TABLE` — sintaxe completa
- Tipos de dados: `INT`, `VARCHAR`, `DECIMAL`, `DATE`, `BOOLEAN`, `TEXT`
- Restrições: `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `FOREIGN KEY`
- `INSERT INTO` — sintaxe com e sem lista de colunas
- `INSERT INTO` — múltiplos registros em um único comando
- Erros comuns no `INSERT INTO`: tipo incompatível, coluna omitida, valor nulo em campo NOT NULL
- Conexão: o que foi visto no 1º Tri × o que vem no 2º Tri (Modelagem e Normalização)

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada, boas-vindas ao 2º Trimestre e apresentação do tema da aula |
| Retomada | Perguntas orais rápidas: "O que é DDL?", "Qual a diferença entre PRIMARY KEY e NOT NULL?" — alunos respondem sem consulta |
| Explicação | Slides — revisão das categorias SQL, sintaxe de CREATE TABLE e INSERT INTO com exemplos de sistemas reais |
| Dinâmica | "Certo ou Errado?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo oral: o que revisamos hoje e o que vem na próxima aula (Modelagem de Dados) |

---

## Dinâmica — "Certo ou Errado?"

**Duração:** 15 minutos · **Agrupamento:** turma inteira

**Objetivo:** revisar a sintaxe dos comandos SQL por meio de análise crítica de código, trabalhando identificação de erros de forma ativa e colaborativa.

**Materiais:** quadro branco ou slides com os blocos de código.

**Passo a passo:**

1. **Apresentação do bloco de código** *(2 min por rodada)*
O professor exibe um bloco SQL no quadro ou nos slides — código limpo, sem marcações de erro.

**Exemplo de bloco:**
```sql
CREATE TABLE produto (
    id_produto INT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(8,2),
    data_cadastro DATE DEFAULT
);
```

2. **Votação da turma** *(1 min)*
A turma decide: **CERTO ✅ ou ERRADO ❌**. O professor conta os votos sem revelar a resposta.

3. **Justificativa obrigatória** *(2 min)*
Quem votou ❌ deve apontar exatamente a linha com problema e explicar o erro.
Sem justificativa, o ponto não conta.

4. **Reveal e consolidação** *(0,5 min)*
O professor exibe o slide de reveal com a linha errada destacada e a versão corrigida.

**Blocos sugeridos (3 rodadas):**

| Rodada | Comando | Problema |
|--------|---------|----------|
| 1 | `CREATE TABLE` com `DEFAULT` sem valor | Sintaxe incompleta |
| 2 | `INSERT INTO` sem listar colunas, mas com valores fora de ordem | Ordem de valores incorreta |
| 3 | `INSERT INTO` com valor de texto em campo `INT` | Tipo incompatível |

> **Nota:** os blocos devem aparecer como código limpo no slide de apresentação, sem nenhuma marcação visual do erro. O slide de reveal (exibido só após a votação) mostra a linha incorreta destacada em vermelho ao lado da versão corrigida.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Prova Escrita — 1º Trimestre (06/05) · SQL DDL, DML, DCL, SGBD, NoSQL, Normalização |
| Próxima aula → | Aula 02 — 27/05/2026 · Modelagem de Dados — Conceitos e Fases |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador (para a dinâmica)

---

## Observações do Professor
