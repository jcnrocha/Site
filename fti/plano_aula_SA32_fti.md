# UC: Fundamentos de Tecnologias da Informação
## SA 32 — 3º Trimestre

---

## Tema

Python — Estruturas de Controle · if/elif/else, while e for

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Utilizar a estrutura de decisão if/elif/else para controlar o fluxo de um programa Python
- Aplicar operadores relacionais e lógicos em condições de decisão
- Utilizar a estrutura de repetição while para executar um bloco de código enquanto uma condição for verdadeira
- Utilizar a estrutura de repetição for para percorrer sequências e intervalos com range()
- Resolver problemas práticos combinando variáveis, entrada/saída e estruturas de controle

---

## Conteúdo

- Revisão rápida — variáveis, tipos de dados e operadores da SA 31
- Estrutura de decisão — if, elif e else: sintaxe, indentação e exemplos
- Operadores relacionais — == != > < >= <=
- Operadores lógicos — and, or, not
- Estrutura de repetição while — sintaxe, condição de parada e cuidado com loop infinito
- Estrutura de repetição for — sintaxe e uso com range(início, fim, passo)
- break e continue — controle do fluxo dentro de loops
- Exercícios práticos — calculadora com menu, verificador de nota e tabuada

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada do gap de 2 semanas · Conexão com a SA 31 — variáveis, tipos e operadores |
| Retomada | Revisão oral rápida — print(), input(), tipos de dados e operadores aritméticos |
| Explicação | Slides — if/elif/else, while e for com exemplos progressivos. Demonstração ao vivo: escrever e executar cada estrutura no IDLE projetado |
| Prática | Alunos escrevem no computador: verificador de aprovação com if/elif/else · contador com while · tabuada com for e range() |
| Dinâmica | "O Que Este Código Faz?" — ver seção abaixo |
| Fechamento | Resumo oral — diferença entre if, while e for · quando usar cada estrutura · Antecipação da SA 33 — Python: Funções e Projeto |

---

## Dinâmica — O Que Este Código Faz?

**Nome:** O Que Este Código Faz?  
**Duração:** 10 a 15 minutos  
**Agrupamento:** 5 grupos de 4 alunos

**Descrição:** O professor projeta trechos de código Python com estruturas de controle. Cada grupo analisa o código, determina o que ele faz e qual será a saída exibida. Professor valida e explica o raciocínio.

**Passo a passo:**

1. **Apresentação** — Professor projeta o trecho de código
2. **Análise em grupo** — Cada grupo determina a saída ou comportamento do código
3. **Compartilhamento** — Um representante apresenta a resposta
4. **Correção** — Professor executa o código ao vivo e valida

**Trechos de código sugeridos:**

| # | Código | Saída esperada |
|---|---|---|
| 1 | `nota = 7` `if nota >= 6:` `    print("Aprovado")` `else:` `    print("Reprovado")` | Aprovado |
| 2 | `i = 0` `while i < 3:` `    print(i)` `    i += 1` | 0, 1, 2 |
| 3 | `for n in range(1, 6):` `    print(n)` | 1, 2, 3, 4, 5 |
| 4 | `x = 10` `if x > 5 and x < 20:` `    print("Dentro do intervalo")` | Dentro do intervalo |
| 5 | `for n in range(2, 11, 2):` `    print(n)` | 2, 4, 6, 8, 10 |

---

## Avaliação

- Questões Objetivas
- Questões Discursivas

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior (SA 31) | Introdução ao Python · Variáveis, tipos de dados, entrada e saída · 06/10/2026 |
| Próxima aula (SA 33) → | Python — Funções e Projeto · Organização do código e mini-projeto prático · 27/10/2026 |

---

## Recursos Necessários

- Laboratório de informática — 1 computador por aluno com Python e IDLE instalados
- Projetor / TV
- Slides — Python: Estruturas de Controle (PPTX)
- Questionário impresso ou digital
- Quadro branco / Marcador

---

## Observações do Professor

> ⚠️ Esta SA ocorre após gap de 2 semanas (sem aula em 13/10/2026). Retomar os conceitos da SA 31 antes de avançar.
