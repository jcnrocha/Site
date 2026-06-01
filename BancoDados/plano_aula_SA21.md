# UC: Fundamentos de Banco de Dados
## Aula 08 — 2º Trimestre

---

## Tema

Normalização — 1FN e 2FN

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o objetivo da normalização e por que ela é aplicada após o mapeamento das dependências funcionais
- Aplicar a Primeira Forma Normal (1FN) eliminando grupos repetitivos e garantindo atomicidade dos atributos
- Aplicar a Segunda Forma Normal (2FN) eliminando dependências parciais da chave primária
- Converter uma tabela desnormalizada para 1FN e em seguida para 2FN passo a passo
- Verificar se uma tabela está ou não em conformidade com a 1FN e a 2FN e justificar a resposta

**Habilidade da matriz:** H04 — Identificar métodos de normalização

---

## Conteúdo

- Revisão rápida: o que é dependência funcional e por que ela importa para a normalização
- O que é normalização — objetivo, benefícios e contexto de aplicação
- **Primeira Forma Normal (1FN):**
  - Regra 1: todos os atributos devem ser atômicos — sem valores compostos ou múltiplos em uma célula
  - Regra 2: sem grupos repetitivos — sem colunas como `telefone1`, `telefone2`, `telefone3`
  - Regra 3: cada linha deve ser unicamente identificável — a tabela precisa de uma chave primária definida
  - Como aplicar a 1FN: separar atributos compostos, transformar multivalorados em tabela própria
- **Segunda Forma Normal (2FN):**
  - Pré-requisito: a tabela já deve estar em 1FN
  - Regra: todos os atributos não-chave devem depender da chave primária **inteira** — sem dependências parciais
  - Aplicável apenas quando a chave primária é composta
  - Como aplicar a 2FN: identificar dependências parciais, mover os atributos parciais para uma nova tabela com a parte da chave da qual dependem
- Processo completo: tabela original → 1FN → 2FN com exemplo passo a passo
- Resultado esperado após a 2FN: cada tabela tem um tema único e bem definido

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 07 — pergunta oral: *"Qual a diferença entre dependência parcial e dependência transitiva?"* |
| Retomada | Professor reapresenta a tabela `PEDIDO_ITEM` da aula anterior e recapitula as dependências mapeadas pelos grupos — conectando diretamente ao que será resolvido hoje |
| Explicação | Slides — o que é normalização, 1FN com exemplos de violação e correção, 2FN com o processo de separação de tabelas por dependência parcial |
| Dinâmica | "Normaliza Passo a Passo" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: 1FN resolve atomicidade e grupos repetitivos · 2FN resolve dependências parciais · Próxima aula: Normalização — 3FN |

---

## Dinâmica — "Normaliza Passo a Passo"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar o processo de normalização até a 2FN por meio da conversão guiada de uma tabela desnormalizada, tomando decisões reais de separação de atributos e criação de novas tabelas.

**Materiais:** slide ou folha com a tabela desnormalizada · folha A4 por grupo para escrever as tabelas resultantes.

**Passo a passo:**

1. **Apresentação da tabela** *(2 min)*
O professor projeta a tabela abaixo — diferente da usada na Aula 07 — e explica que ela representa um sistema de matrícula de uma escola técnica.

**Tabela MATRICULA (desnormalizada):**

| id_matricula | id_aluno | nome_aluno | telefones_aluno | id_curso | nome_curso | carga_horaria | nota |
|---|---|---|---|---|---|---|---|
| 1 | 101 | Fernanda | 99999-0001, 98888-0002 | 5 | Desenvolvimento de Sistemas | 1200h | 8,5 |
| 2 | 102 | Ricardo | 97777-0003 | 5 | Desenvolvimento de Sistemas | 1200h | 7,0 |
| 3 | 101 | Fernanda | 99999-0001, 98888-0002 | 6 | Redes de Computadores | 800h | 9,0 |

2. **Aplicação da 1FN** *(4 min)*
Cada grupo converte a tabela para 1FN eliminando a violação de atomicidade (`telefones_aluno` com múltiplos valores) e define uma chave primária adequada.

3. **Aplicação da 2FN** *(4 min)*
Com a tabela em 1FN, o grupo identifica as dependências parciais e separa as tabelas resultantes, garantindo que cada uma tenha um tema único.

4. **Apresentação e correção** *(5 min)*
Um grupo apresenta o resultado final. O professor compara com o gabarito e discute as decisões tomadas.

**Gabarito esperado:**

*Após 1FN — eliminar multivalorado e garantir chave:*
```
MATRICULA (id_matricula PK, id_aluno, nome_aluno, id_curso,
           nome_curso, carga_horaria, nota)

TELEFONE_ALUNO (id_aluno FK → ALUNO, telefone)
```

*Após 2FN — chave composta seria (id_aluno + id_curso); eliminar dependências parciais:*
```
ALUNO (id_aluno PK, nome_aluno)

CURSO (id_curso PK, nome_curso, carga_horaria)

MATRICULA (id_matricula PK, id_aluno FK → ALUNO,
           id_curso FK → CURSO, nota)

TELEFONE_ALUNO (id_aluno FK → ALUNO, telefone)
```

> **Nota:** reforçar com a turma que após a 2FN cada tabela tem responsabilidade única — ALUNO cuida dos dados do aluno, CURSO cuida dos dados do curso, e MATRICULA guarda apenas o vínculo e a nota. Isso elimina as anomalias de atualização identificadas na aula anterior.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 07 — 01/07/2026 · Dependência Funcional |
| Próxima aula → | Aula 09 — 29/07/2026 · Normalização — 3FN |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever as tabelas normalizadas na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
