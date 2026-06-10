# UC: Programação de Aplicativos
## SA 05 — 1º Trimestre

---

## Tema

Linguagem de Programação Estruturada — Parte 1

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o paradigma de programação estruturada e suas características principais
- Declarar variáveis utilizando os tipos de dados primitivos corretos para cada situação
- Aplicar operadores aritméticos, relacionais e lógicos em expressões simples
- Construir estruturas condicionais com if/else para controlar o fluxo de execução de um programa
- Escrever e executar programas simples na IDE, respeitando boas práticas de nomenclatura

**Capacidades da matriz:** 3. Linguagem de programação estruturada · Reconhecer especificações técnicas e paradigmas de linguagem de programação · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE)

---

## Conteúdo

- Retomada rápida da SA 04: *"Na SA passada configuramos o ambiente — hoje ele entra em uso: vamos escrever os primeiros programas de verdade"*

- **Paradigma de programação estruturada:**
  - Forma de programar baseada em três estruturas fundamentais: sequência, decisão e repetição
  - O programa é executado de cima para baixo, linha por linha, em ordem lógica
  - Foco em clareza, legibilidade e organização do código em blocos bem definidos
  - Base de todos os outros paradigmas — quem entende programação estruturada aprende qualquer linguagem com mais facilidade
  - Linguagens estruturadas: C, Pascal, Python, Java (também suporta OO), Portugol

- **Variáveis e tipos de dados:**
  - **Variável:** espaço nomeado na memória do computador para armazenar um valor durante a execução do programa
  - Toda variável tem: nome (identificador) · tipo (qual dado armazena) · valor (o dado em si)
  - **Boas práticas de nomenclatura:**
    - Nomes descritivos: `idadeAluno` em vez de `x` ou `a`
    - camelCase para variáveis: `nomeCompleto`, `totalItens`, `valorFinal`
    - Sem espaços, acentos ou caracteres especiais
    - Começar sempre com letra minúscula

  - **Tipos de dados primitivos:**

  | Tipo | O que armazena | Exemplo de valor | Exemplo de declaração |
  |------|---------------|-----------------|----------------------|
  | `int` | Números inteiros | 18, -5, 0, 1000 | `int idade = 18;` |
  | `double` / `float` | Números decimais | 3.14, -0.5, 99.9 | `double preco = 29.90;` |
  | `String` | Texto (cadeia de caracteres) | "João", "Olá!" | `String nome = "João";` |
  | `boolean` | Verdadeiro ou falso | true, false | `boolean ativo = true;` |
  | `char` | Um único caractere | 'A', '7', '@' | `char letra = 'A';` |

- **Operadores:**
  - **Aritméticos** — realizam cálculos matemáticos:

  | Operador | Operação | Exemplo | Resultado |
  |----------|----------|---------|-----------|
  | `+` | Adição | `10 + 3` | `13` |
  | `-` | Subtração | `10 - 3` | `7` |
  | `*` | Multiplicação | `10 * 3` | `30` |
  | `/` | Divisão | `10 / 3` | `3` (inteiro) ou `3.33` (decimal) |
  | `%` | Resto da divisão | `10 % 3` | `1` |

  - **Relacionais** — comparam dois valores e retornam verdadeiro ou falso:

  | Operador | Significado | Exemplo | Resultado |
  |----------|-------------|---------|-----------|
  | `==` | Igual a | `5 == 5` | `true` |
  | `!=` | Diferente de | `5 != 3` | `true` |
  | `>` | Maior que | `7 > 3` | `true` |
  | `<` | Menor que | `3 < 7` | `true` |
  | `>=` | Maior ou igual | `5 >= 5` | `true` |
  | `<=` | Menor ou igual | `4 <= 3` | `false` |

  - **Lógicos** — combinam condições:

  | Operador | Significado | Exemplo | Resultado |
  |----------|-------------|---------|-----------|
  | `&&` | E (ambos verdadeiros) | `idade >= 18 && temCNH` | `true` se os dois forem verdadeiros |
  | `\|\|` | OU (pelo menos um verdadeiro) | `ehAdmin \|\| ehGerente` | `true` se ao menos um for verdadeiro |
  | `!` | NÃO (inverte o valor) | `!ativo` | `true` se ativo for false |

- **Estruturas condicionais — if / else:**
  - Permitem que o programa tome decisões com base em uma condição
  - Se a condição for verdadeira → executa o bloco do `if`
  - Se a condição for falsa → executa o bloco do `else`

  ```
  if (idade >= 18) {
      exibir("Maior de idade — acesso permitido");
  } else {
      exibir("Menor de idade — acesso negado");
  }
  ```

  - **if / else if / else** — para múltiplas condições encadeadas:

  ```
  if (nota >= 7.0) {
      exibir("Aprovado");
  } else if (nota >= 5.0) {
      exibir("Recuperação");
  } else {
      exibir("Reprovado");
  }
  ```

  - **Boas práticas:**
    - Sempre usar chaves `{}` mesmo quando o bloco tem apenas uma linha
    - Indentar corretamente o bloco interno — o Prettier faz isso automaticamente ao salvar
    - Condições claras e objetivas — evitar condições desnecessariamente complexas

- **Primeiro programa completo na IDE:**
  - Criar projeto novo no VS Code
  - Declarar variáveis com nome, tipo e valor
  - Usar operadores para calcular ou comparar valores
  - Usar if/else para exibir uma mensagem diferente conforme o resultado
  - Executar no terminal integrado e verificar a saída

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 04: *"Ambiente configurado e funcionando — hoje escrevemos os primeiros programas reais"* |
| Retomada | Professor pergunta: *"Quando você vai ao caixa eletrônico e digita sua senha, o que o sistema faz com esse dado? Como ele decide se libera ou bloqueia o acesso?"* — alunos respondem livremente · professor conecta com variáveis, comparação e estrutura condicional |
| Explicação | Slides — paradigma estruturado, variáveis e tipos, operadores aritméticos/relacionais/lógicos, if/else com exemplos práticos · demonstração ao vivo na IDE |
| Dinâmica | "Verdadeiro, Falso ou Erro?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: variável é memória com nome · tipo define o que pode ser guardado · if/else é o programa tomando decisão · Próxima SA: estruturas de repetição e vetores |

---

## Dinâmica — "Verdadeiro, Falso ou Erro?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar variáveis, operadores e estruturas condicionais por meio da análise de trechos de código — desenvolvendo a leitura crítica de código e a capacidade de identificar erros lógicos e de tipo antes mesmo de executar o programa.

**Materiais:** slide com os trechos de código projetados · ou cartões impressos com os trechos (1 conjunto por grupo).

**Passo a passo:**

1. **Apresentação do trecho** *(1 min por rodada)*
O professor projeta um trecho de código. Cada grupo deve classificar: o código está correto e a saída é verdadeira · o código está correto mas a saída é falsa · o código tem um erro.

2. **Decisão em grupo** *(1 min)*
Os grupos discutem e registram: classificação (correto/falso/erro) + justificativa de uma frase.

3. **Apresentação e correção** *(2 min)*
Os grupos compartilham a classificação. O professor revela a resposta e explica o raciocínio.

**Trechos sugeridos:**

| Trecho de código | Classificação | Explicação |
|-----------------|---------------|------------|
| `int idade = 17;` `if (idade >= 18) { exibir("maior"); }` → exibe "maior" | Falso | 17 não é >= 18 · o bloco if não é executado |
| `double preco = 10;` `double desconto = preco * 0.1;` `exibir(desconto);` → exibe 1.0 | Correto | 10 * 0.1 = 1.0 |
| `String nome = João;` | Erro | String precisa estar entre aspas duplas: `"João"` |
| `int a = 10; int b = 3;` `exibir(a % b);` → exibe 1 | Correto | Resto da divisão de 10 por 3 é 1 |
| `boolean ativo = true;` `if (!ativo) { exibir("inativo"); }` → exibe "inativo" | Falso | !true = false · o bloco if não executa |
| `int x = 5;` `if (x = 5) { exibir("igual"); }` | Erro | `=` é atribuição · para comparar usa-se `==` |
| `int nota = 6;` `if (nota >= 7) { exibir("aprovado"); } else { exibir("recuperação"); }` → exibe "recuperação" | Correto | 6 não é >= 7 · cai no else |

> **Nota:** o objetivo é que os alunos desenvolvam o hábito de ler o código antes de executar — uma das habilidades mais valorizadas no mercado. Reforçar que erros de lógica (como usar `=` em vez de `==`) não geram mensagem de erro na compilação em algumas linguagens, tornando-os difíceis de detectar sem leitura cuidadosa.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 04 — 11/03/2026 · Instalação e Configuração do Ambiente |
| Próxima SA → | SA 06 — 25/03/2026 · Linguagem de Programação Estruturada — Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (para demonstração ao vivo e prática)
- Cartões com os trechos de código da dinâmica impressos (1 conjunto por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
