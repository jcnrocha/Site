# UC: Fundamentos de Banco de Dados
## SA 04 — 1º Trimestre

---

## Tema

Normalização — Parte 2

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o conceito de dependência funcional como base para a aplicação da 2FN e da 3FN
- Aplicar a Segunda Forma Normal (2FN) eliminando dependências parciais da chave primária
- Aplicar a Terceira Forma Normal (3FN) eliminando dependências transitivas entre atributos
- Executar o processo completo de normalização — 1FN → 2FN → 3FN — sobre uma tabela desnormalizada
- Reconhecer as anomalias que cada forma normal resolve e justificar a necessidade de cada etapa

**Habilidade da matriz:** H04 — Identificar métodos de normalização

---

## Conteúdo

- Revisão rápida da SA 03: o que a 1FN resolve e o que ainda pode estar errado após ela
- Dependência funcional: o conceito que fundamenta a 2FN e a 3FN
  - *"A determina B"* (A → B): se soubermos o valor de A, sabemos o valor de B
- **Segunda Forma Normal (2FN):**
  - Pré-requisito: a tabela já deve estar em 1FN
  - Regra: todos os atributos não-chave devem depender da chave primária **inteira** — sem dependências parciais
  - Aplicável apenas quando a chave primária é composta
  - Como aplicar: identificar atributos que dependem de parte da chave e movê-los para uma nova tabela
- **Terceira Forma Normal (3FN):**
  - Pré-requisito: a tabela já deve estar em 2FN
  - Regra: nenhum atributo não-chave pode depender de outro atributo não-chave — sem dependências transitivas
  - Como aplicar: identificar atributos que descrevem outro atributo não-chave e movê-los para uma nova tabela
- Diferença entre 2FN e 3FN:
  - 2FN: elimina dependência em relação a **parte** da chave
  - 3FN: elimina dependência em relação a **atributos não-chave**
- Anomalias de inserção, atualização e exclusão — como cada forma normal as resolve
- Processo completo 1FN → 2FN → 3FN com exemplo de sistema de pedidos

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 03 — pergunta oral: *"O que a 1FN exige de uma tabela para que ela esteja normalizada?"* |
| Retomada | Professor reapresenta a tabela desnormalizada da SA 03 já corrigida para 1FN e pergunta: *"Está tudo certo agora? Ainda pode ter algum problema?"* — alunos analisam livremente |
| Explicação | Slides — dependência funcional, 2FN com exemplo de separação de tabelas, 3FN com eliminação de dependências transitivas, processo completo 1FN → 2FN → 3FN |
| Dinâmica | "Completa a Normalização" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: frase de ouro da 3FN — *"cada atributo não-chave deve depender da chave, de toda a chave, e de nada mais além da chave"* · Próxima aula: SGBD |

---

## Dinâmica — "Completa a Normalização"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar o processo completo de normalização — da 1FN à 3FN — por meio da conversão guiada de uma tabela desnormalizada, com cada grupo tomando decisões reais de separação e criação de tabelas.

**Materiais:** slide ou folha com a tabela desnormalizada · folha A4 por grupo para registrar as etapas.

**Passo a passo:**

1. **Apresentação da tabela** *(2 min)*
O professor projeta a tabela abaixo — sistema de controle de vendas de uma loja de informática.

**Tabela VENDA (desnormalizada):**

| id_venda | id_produto | nome_produto | id_categoria | nome_categoria | qtd | id_vendedor | nome_vendedor | cidade_vendedor |
|---|---|---|---|---|---|---|---|---|
| 1 | 10 | Teclado | 3 | Periféricos | 2 | 5 | Ana | Curitiba |
| 1 | 12 | Mouse | 3 | Periféricos | 1 | 5 | Ana | Curitiba |
| 2 | 10 | Teclado | 3 | Periféricos | 3 | 7 | Carlos | Londrina |

2. **Normalização em três etapas** *(10 min)*
Cada grupo registra as três etapas na folha A4:
- **1FN:** verificar atomicidade e definir chave primária
- **2FN:** chave composta é `id_venda + id_produto` — eliminar dependências parciais
- **3FN:** nas tabelas resultantes, eliminar dependências transitivas

3. **Apresentação e correção** *(3 min)*
Um grupo apresenta o esquema final. O professor consolida o gabarito correto.

**Gabarito esperado:**

```
PRODUTO (id_produto PK, nome_produto, id_categoria FK → CATEGORIA)

CATEGORIA (id_categoria PK, nome_categoria)

VENDEDOR (id_vendedor PK, nome_vendedor, cidade_vendedor)

VENDA_ITEM (id_venda, id_produto FK → PRODUTO,
            id_vendedor FK → VENDEDOR, qtd)
```

> **Nota:** reforçar que saímos de uma tabela com 9 colunas e chegamos a 4 tabelas com responsabilidade única — cada uma descrevendo apenas um conceito do negócio.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 03 — 04/03/2026 · Normalização — Parte 1 · Lançamento do Trabalho |
| Próxima aula → | SA 05 — 18/03/2026 · SGBD — Sistemas de Gerenciamento de Banco de Dados |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para registrar as etapas de normalização)
- Quadro branco e marcador

---

## Observações do Professor
