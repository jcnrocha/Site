# UC: Programação de Aplicativos
## SA 30 — 3º Trimestre

---

## Tema

Consolidação — Ambiente, Ferramentas e Programação Estruturada

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Revisar e consolidar os conteúdos de ambiente de desenvolvimento, ferramentas e repositórios (SAs 01 a 04)
- Aplicar os conceitos de programação estruturada em exercícios práticos com foco em qualidade de código
- Utilizar repositório e controle de versão na prática como parte do fluxo de desenvolvimento
- Identificar e corrigir problemas comuns de configuração de ambiente e uso de ferramentas
- Preparar-se para o Projeto Final integrando ambiente, ferramentas e programação estruturada em um contexto real

**Capacidades da matriz:** Bloco 2 e 3 da matriz · Reconhecer ferramentas para o desenvolvimento de atividades · Instalar ferramentas · Aplicar linguagem de programação por meio da IDE

---

## Conteúdo

- Contextualização da SA: *"Entramos na fase de consolidação — nas próximas SAs vamos revisar os grandes blocos da UC antes do Projeto Final. Hoje revisamos o começo: ambiente, ferramentas e programação estruturada"*

- **Revisão — Ambiente e Ferramentas (SAs 01 a 04):**

  | Tema | Pontos-chave para revisar |
  |------|--------------------------|
  | Ferramentas do ciclo | IDE · repositório · controle de versão · compilador · gerenciador de dependências |
  | Git e GitHub | `git init` · `git add` · `git commit` · `git push` · `git pull` · mensagem de commit |
  | IDE — VS Code | Terminal integrado · depurador · extensões · formatação automática · integração com Git |
  | Instalação e configuração | Requisitos mínimos · PATH · extensões essenciais · `formatOnSave` |

- **Revisão — Programação Estruturada (SAs 05 a 07):**

  | Tema | Pontos-chave para revisar |
  |------|--------------------------|
  | Variáveis e tipos | `int`, `double`, `String`, `boolean`, `char` · camelCase · nomes descritivos |
  | Operadores | Aritméticos · relacionais · lógicos (`&&`, `\|\|`, `!`) |
  | Condicionais | `if` · `else` · `else if` · condições compostas |
  | Repetição | `for` (quantidade conhecida) · `while` (condição) · `do-while` (mínimo 1 vez) |
  | Vetores | Declaração · índice começa em 0 · `.length` · percorrimento com `for` |
  | Funções | `void` vs retorno · parâmetros · passagem por valor · recursividade |
  | Depurador | Breakpoint · step over/into · painel de variáveis |

- **Qualidade de código em programação estruturada — revisão integrada:**
  - Aplicar formatação automática (Prettier) em todos os exercícios
  - Nomear variáveis e funções de forma descritiva — sem `x`, `n`, `temp` sem contexto
  - Comentar decisões não óbvias — não comentar o óbvio
  - Usar `break` para interromper laços quando a resposta já foi encontrada
  - Verificar índice de vetores com `.length` — nunca usar número fixo

- **Controle de versão na prática — fluxo completo:**
  - Criar pasta do projeto → `git init` → escrever código → `git add .` → `git commit -m "mensagem clara"` → `git push`
  - Importância da mensagem de commit: descrever o que foi feito, não o como
  - Boas mensagens: `"adiciona função de cálculo de média"` · `"corrige índice fora do limite no vetor de notas"`
  - Más mensagens: `"update"` · `"correção"` · `"ajustes finais"`

- **Exercícios práticos de consolidação:**

  ```
  Exercício 1 — Funções e vetores:
  Criar uma função que recebe um vetor de notas e retorna:
  - a maior nota
  - a menor nota
  - a média da turma
  - quantos alunos foram aprovados (nota >= 7.0)

  Exercício 2 — Estruturas de repetição e condicionais:
  Criar um programa que lê números inteiros até o usuário
  digitar 0 e exibe: a soma total, a quantidade de números
  positivos e a quantidade de números negativos.

  Exercício 3 — Repositório:
  Criar repositório no GitHub, commitar os dois exercícios
  anteriores com mensagens de commit descritivas e verificar
  o histórico de commits no repositório remoto.
  ```

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização da fase de consolidação: *"Estamos a 12 SAs do fim da UC — hoje revisamos o começo para chegar ao Projeto Final com tudo fresco"* |
| Retomada | Professor projeta uma pergunta rápida de cada bloco revisado e pede resposta oral da turma — diagnóstico rápido de quais tópicos precisam de mais atenção nesta SA |
| Revisão dirigida | Professor revisa os pontos com maior dúvida identificados no diagnóstico · exemplos práticos ao vivo na IDE · foco em qualidade de código integrado à revisão |
| Prática | Alunos resolvem os exercícios práticos na IDE · professor circula auxiliando · foco em aplicar boas práticas: nomes descritivos, formatação, commit com mensagem clara |
| Dinâmica | "Revisão em Dupla" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: ambiente configurado é pré-requisito · Git registra o histórico com mensagens claras · estruturado é a base de tudo · qualidade começa no nome da variável · Próxima SA: consolidação de POO e banco de dados |

---

## Dinâmica — "Revisão em Dupla"

**Duração:** 15 minutos · **Agrupamento:** duplas

**Objetivo:** consolidar os conteúdos de ambiente, ferramentas e programação estruturada por meio de revisão mútua — um aluno explica para o outro, alternando os papéis, desenvolvendo ao mesmo tempo a compreensão do conteúdo e a capacidade de comunicação técnica.

**Materiais:** ficha de revisão impressa (1 por dupla) com os tópicos e perguntas guia.

**Passo a passo:**

1. **Distribuição dos tópicos** *(1 min)*
Cada dupla recebe uma ficha com 4 tópicos. O Aluno A explica os 2 primeiros para o Aluno B · o Aluno B explica os 2 últimos para o Aluno A.

2. **Explicação mútua** *(10 min)*
Cada aluno explica seus tópicos com suas próprias palavras, usando exemplos práticos. O colega que ouve pode fazer perguntas e corriger se necessário.

3. **Consolidação coletiva** *(4 min)*
Professor escolhe 2 duplas para compartilhar uma explicação cada com a turma · complementa e corrige se necessário.

**Tópicos e perguntas guia para a ficha:**

| Tópico | Pergunta guia |
|--------|--------------|
| Diferença Git × GitHub | O que é o Git? O que é o GitHub? Por que precisamos dos dois? |
| Estruturas de repetição | Qual a diferença entre `for`, `while` e `do-while`? Quando usar cada um? |
| Funções com retorno | Qual a diferença entre uma função `void` e uma com retorno? Dê um exemplo de cada |
| Vetores e índice | O que é um vetor? Por que o índice começa em 0? O que acontece se acessar um índice inválido? |

> **Nota:** ensinar é a forma mais eficaz de aprender — quando o aluno precisa explicar um conceito com suas próprias palavras, ele identifica exatamente o que sabe e o que ainda não entendeu completamente. Esse método de revisão em dupla é uma técnica pedagógica chamada de ensino recíproco, amplamente validada em contextos de educação técnica.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 29 — 16/09/2026 · Modelagem de Negócios — Canvas Aplicado a Sistemas |
| Próxima SA → | SA 31 — 30/09/2026 · Consolidação — POO e Conexão com Banco de Dados |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores com VS Code configurado e acesso ao GitHub
- Ficha de revisão em dupla impressa (1 por dupla)
- Quadro branco e marcador

---

## Observações do Professor
