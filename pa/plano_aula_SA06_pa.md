# UC: Programação de Aplicativos
## SA 06 — 1º Trimestre

---

## Tema

Linguagem de Programação Estruturada — Parte 2

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Aplicar estruturas de repetição `for`, `while` e `do-while` para automatizar tarefas repetitivas em um programa
- Diferenciar cada estrutura de repetição e identificar a mais adequada para cada situação
- Declarar e manipular vetores (arrays) para armazenar múltiplos valores de um mesmo tipo
- Combinar estruturas de repetição com vetores para percorrer e processar listas de dados
- Escrever e executar programas com laços e vetores na IDE, aplicando boas práticas de código

**Capacidades da matriz:** 3. Linguagem de programação estruturada · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE) · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada rápida da SA 05: *"Na SA passada escrevemos programas com variáveis, operadores e if/else — hoje o programa aprende a repetir ações e a trabalhar com listas de dados"*

- **Por que precisamos de repetição:**
  - Sem repetição: para exibir 100 nomes seria necessário escrever 100 linhas de código
  - Com repetição: uma estrutura de laço resolve em 3 a 5 linhas — independente de quantos itens existam
  - Repetição é um dos pilares da programação estruturada: sequência · decisão · **repetição**

- **Estrutura `for` — quando se sabe quantas vezes repetir:**
  - Usada quando o número de repetições é conhecido antes de entrar no laço
  - Estrutura: inicialização · condição · incremento — tudo na mesma linha
  - Fluxo: inicializa a variável de controle → verifica a condição → executa o bloco → incrementa → verifica novamente

  ```
  for (int i = 0; i < 5; i++) {
      exibir("Repetição número: " + i);
  }
  ```
  > Executa 5 vezes: i assume os valores 0, 1, 2, 3, 4

- **Estrutura `while` — quando não se sabe quantas vezes repetir:**
  - Usada quando a repetição depende de uma condição que pode mudar durante a execução
  - Verifica a condição **antes** de executar o bloco — se já entrar falsa, não executa nenhuma vez
  - Risco: se a condição nunca se tornar falsa, o laço nunca termina (loop infinito)

  ```
  int tentativas = 0;
  while (tentativas < 3) {
      exibir("Tentativa: " + tentativas);
      tentativas++;
  }
  ```

- **Estrutura `do-while` — executa pelo menos uma vez:**
  - Semelhante ao `while`, mas verifica a condição **depois** de executar o bloco
  - Garante que o bloco seja executado ao menos uma vez, mesmo que a condição já seja falsa
  - Uso típico: menus de sistema onde o usuário precisa ver a opção antes de decidir

  ```
  do {
      exibir("Digite um número positivo:");
      numero = lerEntrada();
  } while (numero <= 0);
  ```

- **Comparativo das estruturas de repetição:**

  | Estrutura | Quando usar | Condição verificada | Execução mínima |
  |-----------|-------------|---------------------|-----------------|
  | `for` | Número de repetições conhecido | Antes do bloco | 0 vezes (se condição falsa) |
  | `while` | Número de repetições desconhecido | Antes do bloco | 0 vezes (se condição falsa) |
  | `do-while` | Precisa executar ao menos uma vez | Depois do bloco | 1 vez garantida |

- **Vetores (Arrays) — armazenando múltiplos valores:**
  - Variável que armazena uma coleção de valores do mesmo tipo em posições numeradas
  - Cada posição é chamada de **índice** — começa sempre em **0** (não em 1)
  - Tamanho fixo: definido na criação e não pode ser alterado
  - Declaração e inicialização:

  ```
  int[] notas = {8, 7, 9, 6, 10};   // vetor com 5 posições
  String[] nomes = new String[3];    // vetor vazio com 3 posições
  ```

  - Acesso por índice:

  ```
  exibir(notas[0]);   // exibe 8 — primeira posição
  exibir(notas[4]);   // exibe 10 — quinta posição
  notas[2] = 5;       // substitui o valor da posição 2
  ```

  - **Erro comum:** acessar um índice que não existe gera `ArrayIndexOutOfBoundsException`
    - Vetor com 5 posições: índices válidos são 0, 1, 2, 3 e 4 · índice 5 causa erro

- **Percorrendo vetores com `for`:**
  - Combinação clássica da programação: laço `for` + vetor
  - A variável de controle do `for` funciona como o índice do vetor

  ```
  int[] notas = {8, 7, 9, 6, 10};
  for (int i = 0; i < notas.length; i++) {
      exibir("Nota " + i + ": " + notas[i]);
  }
  ```

  - `notas.length` retorna o tamanho do vetor automaticamente — evita erro de índice e permite que o código funcione independente do tamanho do vetor

- **Boas práticas com laços e vetores:**
  - Usar `length` em vez de número fixo para percorrer vetores — código mais robusto
  - Evitar laços infinitos: garantir que a condição de saída seja sempre alcançável
  - Nomear a variável de controle do `for` com `i`, `j`, `k` — convenção universalmente aceita
  - Comentar laços com lógica complexa para facilitar a manutenção futura

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 05: *"Sabemos declarar variáveis e tomar decisões com if/else — hoje o programa aprende a repetir ações e trabalhar com coleções de dados"* |
| Retomada | Professor pergunta: *"Se eu pedir para vocês escreverem no caderno 'Eu não vou usar o celular em aula' 50 vezes, quanto tempo demora? E se eu programar um computador para fazer isso — quantas linhas de código precisaria?"* — alunos respondem · professor revela que com um laço `for` são apenas 3 linhas |
| Explicação | Slides — por que repetição existe, `for` com exemplo, `while` com exemplo, `do-while` com exemplo, comparativo dos três, vetores com índice, percorrendo vetores com `for` · demonstração ao vivo na IDE |
| Dinâmica | "Monte o Laço" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: `for` quando sabe quantas vezes · `while` quando depende de condição · `do-while` quando precisa executar ao menos uma vez · vetor começa no índice 0 · `for` + vetor é uma combinação clássica · Próxima SA: funções e modularização |

---

## Dinâmica — "Monte o Laço"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar as estruturas de repetição e o uso de vetores por meio da montagem e análise de laços a partir de situações-problema — desenvolvendo a capacidade de escolher a estrutura correta e prever o comportamento do programa antes de executá-lo.

**Materiais:** cartões com os fragmentos de código embaralhados (1 conjunto por grupo) · ou slide com as situações projetadas.

**Passo a passo:**

1. **Apresentação da situação-problema** *(1 min por rodada)*
O professor projeta ou lê uma situação. O grupo precisa: escolher a estrutura de repetição correta · montar o laço com os fragmentos fornecidos · e prever qual será a saída do programa.

2. **Montagem em grupo** *(7 min)*
Os grupos organizam os fragmentos na ordem correta e registram a saída esperada.

3. **Apresentação e debate** *(7 min)*
Os grupos apresentam suas soluções. O professor compara as respostas e discute: *"Por que escolheram `for` e não `while`? Qual seria o problema se usassem `do-while` aqui?"*

**Situações sugeridas:**

| Situação-problema | Estrutura ideal | Saída esperada |
|------------------|----------------|----------------|
| Exibir os números de 1 a 10 | `for` | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| Pedir senha ao usuário até que ele acerte (máximo 3 tentativas) | `while` | Repete enquanto senha errada e tentativas < 3 |
| Exibir um menu e perguntar se o usuário quer continuar | `do-while` | Menu aparece ao menos 1 vez antes da pergunta |
| Percorrer um vetor de 5 notas e exibir cada uma | `for` com vetor | Exibe notas[0] até notas[4] |
| Somar todos os valores de um vetor de preços | `for` com vetor e acumulador | Exibe a soma total dos preços |
| Contar quantos alunos tiraram nota acima de 7 em um vetor de notas | `for` com vetor e contador | Exibe a quantidade de aprovados |

> **Nota:** reforçar que a escolha da estrutura de repetição não é arbitrária — ela comunica a intenção do código para quem vai ler depois. Um `for` diz: *"sei quantas vezes vou repetir"* · um `while` diz: *"vou repetir enquanto essa condição for verdadeira"*. Código que comunica intenção é código de qualidade.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 05 — 18/03/2026 · Linguagem de Programação Estruturada — Parte 1 |
| Próxima SA → | SA 07 — 01/04/2026 · Linguagem de Programação Estruturada — Parte 3 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (para demonstração ao vivo e prática)
- Cartões com os fragmentos de código da dinâmica impressos (1 conjunto por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
