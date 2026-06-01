# UC: Fundamentos de Banco de Dados
## Aula 09 — 2º Trimestre

---

## Tema

Normalização — 3FN

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o conceito da Terceira Forma Normal (3FN) e por que ela complementa a 2FN
- Identificar dependências transitivas em tabelas que já estão em 2FN
- Aplicar a 3FN eliminando dependências transitivas por meio da criação de novas tabelas
- Executar o processo completo de normalização — da tabela original até a 3FN — passo a passo
- Avaliar se um conjunto de tabelas está em conformidade com as três primeiras formas normais e justificar a análise

**Habilidade da matriz:** H04 — Identificar métodos de normalização

---

## Conteúdo

- Revisão rápida: 1FN e 2FN — o que cada uma resolve e o que ainda pode estar errado após a 2FN
- **Terceira Forma Normal (3FN):**
  - Pré-requisito: a tabela já deve estar em 2FN
  - Regra: nenhum atributo não-chave pode depender de outro atributo não-chave — sem dependências transitivas
  - Definição formal: se A → B e B → C, então C tem dependência transitiva de A por meio de B
  - Como identificar: procurar atributos que descrevem outro atributo não-chave, e não a entidade em si
  - Como aplicar: mover o atributo transitivo e seu determinante para uma nova tabela
- Diferença entre 2FN e 3FN:
  - 2FN elimina dependências em relação a **parte** da chave primária
  - 3FN elimina dependências em relação a **atributos não-chave**
- Processo completo 1FN → 2FN → 3FN aplicado a um sistema real passo a passo
- Resultado esperado após a 3FN: cada atributo não-chave descreve exclusivamente a chave primária da sua tabela — e nada mais
- Por que parar na 3FN: na prática, a maioria dos bancos de dados relacionais de uso comercial não exige formas normais superiores

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 08 — pergunta oral: *"Uma tabela com chave primária simples pode violar a 2FN? Por quê?"* |
| Retomada | Professor reapresenta o resultado final da dinâmica da Aula 08 — as quatro tabelas normalizadas até a 2FN — e pergunta: *"Será que ainda há algum problema nessas tabelas?"* — alunos analisam livremente |
| Explicação | Slides — revisão rápida de 1FN e 2FN, conceito de dependência transitiva, como a 3FN resolve, processo completo com exemplo de sistema de pedidos |
| Dinâmica | "Da Bagunça à 3FN" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: a frase de ouro da 3FN — *"cada atributo não-chave deve depender da chave, de toda a chave, e de nada mais além da chave"* · Encerramento da SA2 · Próxima aula: Revisão Geral do 2º Trimestre |

---

## Dinâmica — "Da Bagunça à 3FN"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** consolidar o processo completo de normalização — 1FN, 2FN e 3FN — por meio da conversão integral de uma tabela desnormalizada, exigindo que os grupos tomem todas as decisões de forma autônoma e registrem cada etapa separadamente.

**Materiais:** slide ou folha com a tabela desnormalizada · folha A4 por grupo para registrar as três etapas.

**Passo a passo:**

1. **Apresentação da tabela** *(2 min)*
O professor projeta a tabela abaixo — sistema de controle de projetos de uma empresa de desenvolvimento — e esclarece que ela precisa passar pelas três formas normais.

**Tabela PROJETO_EQUIPE (desnormalizada):**

| id_projeto | id_funcionario | nome_funcionario | cargo | salario_cargo | habilidades | nome_projeto | id_cliente | nome_cliente | cidade_cliente |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 201 | Lucas | Dev Backend | 6500,00 | Python, Django | Sistema ERP | 30 | Grupo Alfa | Curitiba |
| 10 | 202 | Mariana | UX Designer | 5800,00 | Figma, Sketch | Sistema ERP | 30 | Grupo Alfa | Curitiba |
| 11 | 201 | Lucas | Dev Backend | 6500,00 | Python, Django | App Mobile | 31 | Tech Soluções | São Paulo |
| 11 | 203 | Felipe | Dev Frontend | 6000,00 | React, TypeScript | App Mobile | 31 | Tech Soluções | São Paulo |

2. **Normalização em três etapas** *(10 min)*
Cada grupo executa e registra cada etapa na folha A4:
- **Etapa 1 — 1FN:** eliminar o atributo multivalorado `habilidades` e garantir que todos os atributos são atômicos
- **Etapa 2 — 2FN:** a chave composta é `id_projeto + id_funcionario` — identificar e eliminar as dependências parciais
- **Etapa 3 — 3FN:** nas tabelas resultantes, identificar e eliminar as dependências transitivas restantes

3. **Apresentação e correção** *(3 min)*
Um grupo apresenta o esquema final. O professor consolida o resultado correto.

**Gabarito esperado:**

*Após 1FN:*
```
PROJETO_EQUIPE (id_projeto, id_funcionario, nome_funcionario,
                cargo, salario_cargo, nome_projeto,
                id_cliente, nome_cliente, cidade_cliente)

HABILIDADE_FUNC (id_funcionario FK → FUNCIONARIO, habilidade)
```

*Após 2FN — eliminar dependências parciais da chave (id_projeto + id_funcionario):*
```
ALOCACAO (id_projeto FK → PROJETO, id_funcionario FK → FUNCIONARIO)

FUNCIONARIO (id_funcionario PK, nome_funcionario, cargo, salario_cargo)

PROJETO (id_projeto PK, nome_projeto, id_cliente,
         nome_cliente, cidade_cliente)

HABILIDADE_FUNC (id_funcionario FK → FUNCIONARIO, habilidade)
```

*Após 3FN — eliminar dependências transitivas:*
```
ALOCACAO (id_projeto FK → PROJETO,
          id_funcionario FK → FUNCIONARIO)

FUNCIONARIO (id_funcionario PK, nome_funcionario,
             id_cargo FK → CARGO)

CARGO (id_cargo PK, nome_cargo, salario_cargo)

PROJETO (id_projeto PK, nome_projeto,
         id_cliente FK → CLIENTE)

CLIENTE (id_cliente PK, nome_cliente, cidade_cliente)

HABILIDADE_FUNC (id_funcionario FK → FUNCIONARIO, habilidade)
```

> **Nota:** ao apresentar o gabarito final, o professor deve ressaltar que partimos de uma única tabela com 10 colunas e chegamos a 6 tabelas bem definidas — cada uma com responsabilidade única. Reforçar a frase de ouro: *"cada atributo não-chave deve depender da chave, de toda a chave, e de nada mais além da chave."*

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 08 — 08/07/2026 · Normalização — 1FN e 2FN |
| Próxima aula → | Aula 10 — 05/08/2026 · Revisão Geral — 2º Trimestre |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para registrar as três etapas de normalização)
- Quadro branco e marcador

---

## Observações do Professor
