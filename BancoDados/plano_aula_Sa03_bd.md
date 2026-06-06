# UC: Fundamentos de Banco de Dados
## SA 03 — 1º Trimestre

---

## Tema

Normalização — Parte 1 · Lançamento do Trabalho em Grupo

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o conceito de normalização e por que ela é aplicada em bancos de dados relacionais
- Identificar os problemas causados por tabelas não normalizadas: redundância e anomalias de dados
- Aplicar a Primeira Forma Normal (1FN): atomicidade dos atributos e eliminação de grupos repetitivos
- Reconhecer violações da 1FN em tabelas reais e propor a correção adequada
- Compreender o escopo, os critérios e as expectativas do Trabalho em Grupo do 1º trimestre

**Habilidade da matriz:** H04 — Identificar métodos de normalização

---

## Conteúdo

- O que é normalização — definição, objetivo e contexto de aplicação
- Problemas de um banco não normalizado:
  - **Redundância** — a mesma informação repetida em múltiplos lugares
  - **Anomalia de inserção** — não é possível inserir um dado sem que outro exista
  - **Anomalia de atualização** — alterar um dado exige atualizar múltiplas linhas
  - **Anomalia de exclusão** — excluir um registro apaga informações de outro contexto
- O conceito de chave primária como base da normalização
- **Primeira Forma Normal (1FN):**
  - Regra 1: todos os atributos devem ser atômicos — sem valores compostos ou múltiplos em uma célula
  - Regra 2: sem grupos repetitivos — sem colunas como `telefone1`, `telefone2`, `telefone3`
  - Regra 3: a tabela deve ter uma chave primária definida
  - Como corrigir uma tabela que viola a 1FN: separar atributos compostos, transformar multivalorados em tabela própria
- Exemplos práticos de violação e correção da 1FN em tabelas de sistemas reais
- **Lançamento do Trabalho em Grupo:**
  - Apresentação do enunciado, temas por grupo, critérios de avaliação e data de entrega
  - Orientações sobre o que se espera da pesquisa e da apresentação oral

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 02 — pergunta oral: *"Qual a diferença entre banco de dados relacional e NoSQL?"* |
| Retomada | Professor exibe uma tabela com dados repetidos e inconsistentes e pergunta: *"O que há de errado nessa tabela? O que acontece se o nome de uma cidade mudar?"* — alunos identificam os problemas livremente |
| Explicação | Slides — o que é normalização, os problemas de tabelas não normalizadas, a 1FN com exemplos de violação e correção |
| Lançamento do Trabalho | Professor apresenta o enunciado do Trabalho em Grupo: temas, critérios, formato e data de entrega · Espaço para perguntas |
| Dinâmica | "Está na 1FN?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: 1FN resolve atomicidade e grupos repetitivos · Próxima aula: Normalização — Parte 2 (2FN e 3FN) |

---

## Dinâmica — "Está na 1FN?"

**Duração:** 15 minutos · **Agrupamento:** turma inteira — votação individual

**Objetivo:** fixar as regras da 1FN por meio da análise rápida de tabelas reais, treinando o aluno a identificar violações e propor correções de forma objetiva.

**Materiais:** slides com as tabelas · quadro branco para registrar os votos.

**Passo a passo:**

1. **Exibição da tabela** *(1 min por rodada)*
O professor projeta uma tabela e pergunta: *"Esta tabela está na 1FN? SIM ou NÃO?"*

2. **Votação** *(1 min)*
Cada aluno vota. O professor registra os votos no quadro.

3. **Justificativa e correção** *(2 min)*
O professor escolhe um aluno de cada lado para justificar. Em seguida revela a resposta correta e mostra como corrigir caso haja violação.

**Tabelas sugeridas (5 rodadas):**

| Rodada | Situação | Violação | Resposta |
|--------|----------|----------|----------|
| 1 | Tabela CLIENTE com colunas `telefone1`, `telefone2`, `telefone3` | Grupo repetitivo | ❌ Não está na 1FN |
| 2 | Tabela PRODUTO com `id_produto PK`, `nome`, `preco`, `categoria` — uma categoria por produto | Nenhuma | ✅ Está na 1FN |
| 3 | Tabela PEDIDO com coluna `produtos` contendo: "Teclado, Mouse, Monitor" em uma célula | Atributo não atômico | ❌ Não está na 1FN |
| 4 | Tabela FUNCIONARIO com `cpf PK`, `nome`, `cargo`, `salario` | Nenhuma | ✅ Está na 1FN |
| 5 | Tabela ALUNO com coluna `endereço` contendo: "Rua XV, 100, Centro, Curitiba" em uma célula | Atributo composto não atômico | ❌ Não está na 1FN |

> **Nota:** nas rodadas com violação, após revelar a resposta o professor deve mostrar rapidamente como ficaria a versão corrigida — criando a tabela auxiliar ou separando os atributos compostos — reforçando o raciocínio de correção e não apenas o de identificação.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 02 — 25/02/2026 · Tipos e Arquitetura de BD |
| Próxima aula → | SA 04 — 11/03/2026 · Normalização — Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Enunciado do Trabalho em Grupo impresso — uma cópia por aluno
- Quadro branco e marcador

---

## Observações do Professor
