# UC: Fundamentos de Tecnologias da Informação
## SA 33 — 3º Trimestre

---

## Tema

Python — Funções e Projeto · Organização do código e mini-projeto prático

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de função em Python e sua importância para organização e reutilização de código
- Criar funções com e sem parâmetros e com e sem retorno de valor
- Chamar funções e utilizar seus retornos em diferentes partes do programa
- Aplicar os conceitos de variáveis, tipos de dados, estruturas de controle e funções em um mini-projeto prático
- Desenvolver autonomia na resolução de problemas usando Python

---

## Conteúdo

- O que é uma função — conceito, finalidade e vantagens (organização, reutilização e legibilidade)
- Definindo funções — sintaxe com def, nome, parâmetros e indentação
- Funções sem parâmetros e sem retorno — exibir mensagens e blocos de código reutilizáveis
- Funções com parâmetros — passar valores para a função
- Funções com retorno — usar return para devolver um resultado
- Escopo de variáveis — variáveis locais e globais
- Mini-projeto prático — calculadora de médias com funções, menu interativo e estruturas de controle

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Conexão com a SA 32 — estruturas de controle · Pergunta motivadora: "Se você precisasse calcular a média de 30 alunos, repetiria o mesmo código 30 vezes?" |
| Retomada | Revisão oral rápida — if/elif/else, while e for da SA 32 |
| Explicação | Slides — conceito de função, sintaxe, parâmetros e retorno. Demonstração ao vivo: criar funções progressivamente no IDLE projetado |
| Prática | Alunos criam no computador: função sem parâmetro (saudação) · função com parâmetro (verificar aprovação) · função com retorno (calcular média) |
| Dinâmica | "Conserta a Função" — ver seção abaixo |
| Mini-Projeto | Alunos desenvolvem a calculadora de médias com menu interativo usando tudo que aprenderam nas SA 31, 32 e 33 |
| Fechamento | Resumo oral — o que é uma função e quando usar · Antecipação da SA 34 — Cloud Computing e Armazenamento |

---

## Dinâmica — Conserta a Função

**Nome:** Conserta a Função  
**Duração:** 10 a 15 minutos  
**Agrupamento:** 5 grupos de 4 alunos

**Descrição:** O professor projeta funções Python com erros propositais — indentação errada, parâmetro faltando, return ausente ou nome incorreto. Cada grupo identifica o erro e escreve a versão corrigida.

**Passo a passo:**

1. **Apresentação** — Professor projeta a função com erro
2. **Análise em grupo** — Cada grupo identifica o erro e corrige
3. **Compartilhamento** — Um representante apresenta a correção
4. **Correção** — Professor executa a versão corrigida ao vivo e valida

**Funções com erros sugeridos:**

| # | Código com erro | Erro | Correção esperada |
|---|---|---|---|
| 1 | `def saudacao():` `print("Olá!")` (sem indentação) | Indentação incorreta | Indentar o print com 4 espaços |
| 2 | `def somar(a, b):` `return a` (falta somar b) | Retorno incompleto | `return a + b` |
| 3 | `def verificar(nota)` `:` (falta parêntese de fechamento) | Erro de sintaxe | `def verificar(nota):` |
| 4 | `def media(a, b, c):` `resultado = (a+b+c)/3` (sem return) | Sem retorno | Adicionar `return resultado` |
| 5 | `calcular_media(7, 8)` sendo que a função foi definida como `def calcularMedia(a, b):` | Nome incorreto na chamada | Usar o nome exato: `calcularMedia(7, 8)` |

---

## Avaliação

- Questões Objetivas
- Questões Discursivas

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior (SA 32) | Python — Estruturas de Controle · if/elif/else, while e for · 20/10/2026 |
| Próxima aula (SA 34) → | Cloud Computing e Armazenamento · Google Drive, OneDrive, Dropbox e uso profissional · 03/11/2026 |

---

## Recursos Necessários

- Laboratório de informática — 1 computador por aluno com Python e IDLE instalados
- Projetor / TV
- Slides — Python: Funções (PPTX)
- Questionário impresso ou digital
- Quadro branco / Marcador

---

## Observações do Professor

> 📌 O mini-projeto da calculadora de médias pode ser usado como atividade avaliativa de participação ou como base para o trabalho do 3º Trimestre.
