# UC: Fundamentos de Banco de Dados
## Aula 06 — 2º Trimestre

---

## Tema

Modelo Físico — Restrições, Chaves e Design

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é o modelo físico e como ele se diferencia do modelo lógico
- Traduzir um esquema lógico em comandos SQL utilizando `CREATE TABLE` com tipos de dados e restrições
- Aplicar corretamente as restrições de integridade: `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT` e `CHECK`
- Escolher o tipo de dado adequado para cada coluna com base na natureza da informação
- Identificar a relação direta entre cada decisão do modelo lógico e o código SQL gerado no modelo físico

**Habilidade da matriz:** H03 — Identificar características de modelagem de dados · H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Revisão rápida: o que o modelo físico representa e onde ele está no processo de modelagem
- Da notação lógica ao SQL: como cada elemento do esquema lógico vira código
- Tipos de dados em MySQL — escolha e justificativa:
  - Numéricos: `INT`, `SMALLINT`, `DECIMAL(p,s)`, `FLOAT`
  - Texto: `VARCHAR(n)`, `CHAR(n)`, `TEXT`
  - Data e hora: `DATE`, `DATETIME`, `TIMESTAMP`
  - Lógico: `BOOLEAN`
- Restrições de integridade:
  - `PRIMARY KEY` — identifica unicamente cada linha
  - `FOREIGN KEY ... REFERENCES` — garante integridade referencial entre tabelas
  - `NOT NULL` — impede valor vazio em uma coluna obrigatória
  - `UNIQUE` — garante que não há valores duplicados em uma coluna
  - `DEFAULT` — define valor padrão quando nenhum é fornecido
  - `CHECK` — valida uma condição antes de inserir ou atualizar
  - `AUTO_INCREMENT` — geração automática de identificadores numéricos
- Ordem de criação das tabelas: tabelas sem FK devem ser criadas antes das que dependem delas
- Conversão completa do esquema lógico da locadora para script SQL
- Boas práticas: nomenclatura de tabelas e colunas, consistência de tipos, documentação mínima

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 05 — pergunta oral: *"Por que o relacionamento N:N precisa de uma tabela associativa?"* |
| Retomada | Professor exibe o esquema lógico da locadora produzido na aula anterior e pergunta: *"O que ainda falta para criarmos esse banco de verdade no MySQL?"* — alunos identificam: tipos de dados e restrições |
| Explicação | Slides — tipos de dados, restrições de integridade, ordem de criação das tabelas, conversão do esquema lógico para SQL |
| Dinâmica | "Certo ou Errado? — Round Físico" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: as três perguntas do modelo físico (qual tipo? qual restrição? qual ordem?) · Próxima aula: Dependência Funcional |

---

## Dinâmica — "Certo ou Errado? — Round Físico"

**Duração:** 15 minutos · **Agrupamento:** turma inteira

**Objetivo:** fixar as restrições de integridade e a escolha de tipos de dados por meio da análise crítica de blocos de código SQL com erros intencionais — reativando a dinâmica já conhecida da Aula 01, agora voltada ao modelo físico.

**Materiais:** slides com os blocos de código SQL · quadro branco para registrar votos.

**Passo a passo:**

1. **Apresentação do bloco** *(1 min por rodada)*
O professor exibe um `CREATE TABLE` no slide — código limpo, sem marcação de erro.

2. **Votação** *(1 min)*
A turma decide: **CERTO ✅ ou ERRADO ❌**. O professor registra os votos.

3. **Justificativa obrigatória** *(2 min)*
Quem votou ❌ aponta a linha com problema e explica o erro. Sem justificativa, o ponto não conta.

4. **Reveal e consolidação** *(1 min)*
O professor exibe a versão corrigida e reforça a regra técnica envolvida.

**Blocos sugeridos (4 rodadas):**

| Rodada | Bloco | Problema |
|--------|-------|----------|
| 1 | `CREATE TABLE cliente (cpf VARCHAR(11), nome VARCHAR(150) NOT NULL, email VARCHAR(100));` | Ausência de `PRIMARY KEY` — nenhuma coluna identifica unicamente o registro |
| 2 | `CREATE TABLE locacao (id INT PRIMARY KEY AUTO_INCREMENT, id_cliente VARCHAR(11), data_locacao DATE DEFAULT);` | `DEFAULT` sem valor definido — sintaxe incompleta |
| 3 | `CREATE TABLE elenco (id_filme INT NOT NULL, id_ator INT NOT NULL, FOREIGN KEY (id_filme) REFERENCES filmes(id_filme));` | Nome da tabela referenciada errado — `filmes` deveria ser `filme` |
| 4 | `CREATE TABLE produto (id INT PRIMARY KEY, preco CHAR(10), estoque INT DEFAULT 0 NOT NULL);` | Tipo inadequado — `preco` como `CHAR(10)` não permite operações numéricas; deveria ser `DECIMAL` |

> **Nota:** o bloco da rodada 4 está sintaticamente correto, mas semanticamente errado — o objetivo é que os alunos percebam que erros de design não geram mensagem de erro no SGBD, mas causam problemas sérios de integridade e desempenho.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 05 — 17/06/2026 · Modelo Lógico — Conceitos e Conversão do DER |
| Próxima aula → | Aula 07 — 01/07/2026 · Dependência Funcional |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador (para registrar votos da dinâmica)

---

## Observações do Professor
