# UC: Programação de Aplicativos
## SA 07 — 1º Trimestre

---

## Tema

Linguagem de Programação Estruturada — Parte 3

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de modularização e por que dividir o programa em funções melhora a qualidade do código
- Criar funções com e sem retorno, definindo corretamente parâmetros e tipos
- Aplicar passagem de parâmetros por valor em funções, compreendendo o que é transmitido e o que é preservado
- Compreender o conceito de recursividade e identificar situações onde ela é aplicável
- Utilizar o depurador da IDE para rastrear o fluxo de execução de um programa com funções

**Capacidades da matriz:** 3. Linguagem de programação estruturada · 6.6 Rastreabilidade · Utilizar o ambiente de desenvolvimento (IDE) para rastreabilidade do código · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada rápida da SA 06: *"Na SA passada o programa aprendeu a repetir com `for`, `while` e `do-while` e a trabalhar com vetores — hoje ele aprende a se organizar em blocos reutilizáveis chamados funções"*

- **Por que modularizar — o problema do código sem funções:**
  - Programa sem funções: tudo em um bloco único · longo · difícil de ler · difícil de corrigir · impossível de reutilizar
  - Com funções: cada tarefa tem seu próprio bloco nomeado · o programa principal fica limpo e legível · o mesmo bloco pode ser chamado quantas vezes for necessário
  - Analogia: uma cozinha industrial tem estações separadas — corte, preparo, fritura, finalização. Cada estação faz bem uma coisa. O prato final é a combinação. Funções funcionam da mesma forma.

- **O que é uma função:**
  - Bloco de código nomeado que realiza uma tarefa específica
  - Pode receber dados de entrada (parâmetros) e pode retornar um resultado (retorno)
  - Definida uma vez — chamada quantas vezes for necessário
  - Quatro elementos de uma função: **nome** · **parâmetros** · **corpo** · **retorno**

- **Funções sem retorno (void):**
  - Realizam uma ação mas não devolvem nenhum valor ao chamador
  - Usadas para exibir dados, registrar logs, atualizar estado

  ```
  void exibirBoasVindas(String nome) {
      exibir("Bem-vindo, " + nome + "!");
  }

  // Chamada:
  exibirBoasVindas("Ana");   // exibe: Bem-vindo, Ana!
  ```

- **Funções com retorno:**
  - Realizam uma operação e devolvem um resultado ao chamador
  - O tipo do retorno deve ser declarado no lugar de `void`
  - O resultado pode ser armazenado em uma variável ou usado diretamente

  ```
  double calcularMedia(double nota1, double nota2) {
      return (nota1 + nota2) / 2;
  }

  // Chamada:
  double media = calcularMedia(8.0, 6.0);   // media = 7.0
  exibir("Média: " + media);
  ```

- **Passagem de parâmetros por valor:**
  - Quando uma variável é passada para uma função, o que é enviado é uma **cópia** do valor
  - A variável original não é alterada dentro da função
  - Isso protege os dados originais de modificações acidentais

  ```
  void dobrar(int numero) {
      numero = numero * 2;
      exibir("Dentro da função: " + numero);   // exibe 20
  }

  int valor = 10;
  dobrar(valor);
  exibir("Fora da função: " + valor);   // ainda exibe 10 — original preservado
  ```

- **Boas práticas na criação de funções:**
  - **Uma função, uma responsabilidade** — função que faz muitas coisas deve ser dividida
  - **Nome descritivo com verbo** — `calcularMedia`, `exibirRelatorio`, `verificarIdade`
  - **Parâmetros claros** — nomes que descrevem o dado esperado: `nota1` em vez de `n`
  - **Tamanho ideal** — função que não cabe na tela merece ser dividida
  - **Evitar efeitos colaterais** — função deve fazer o que o nome promete, sem alterar dados externos inesperadamente

- **Recursividade — função que chama a si mesma:**
  - Uma função é recursiva quando, dentro do seu corpo, ela chama a si mesma
  - Toda função recursiva precisa de uma **condição de parada** — sem ela, o programa entra em loop infinito e trava
  - Usada em problemas que se dividem naturalmente em subproblemas menores do mesmo tipo
  - Exemplo clássico — fatorial:

  ```
  int fatorial(int n) {
      if (n == 0) return 1;           // condição de parada
      return n * fatorial(n - 1);     // chamada recursiva
  }

  // fatorial(4) = 4 * fatorial(3)
  //             = 4 * 3 * fatorial(2)
  //             = 4 * 3 * 2 * fatorial(1)
  //             = 4 * 3 * 2 * 1 * fatorial(0)
  //             = 4 * 3 * 2 * 1 * 1 = 24
  ```

- **Rastreabilidade com o depurador da IDE:**
  - O depurador permite acompanhar o fluxo de execução linha por linha
  - **Breakpoint:** ponto de parada inserido em uma linha · a execução pausa naquele ponto
  - **Step Over:** executa a linha atual e para na próxima — sem entrar dentro das funções chamadas
  - **Step Into:** entra dentro da função chamada na linha atual — rastreia a execução interna
  - **Step Out:** sai da função atual e volta para onde ela foi chamada
  - **Watch / Variables:** painel que exibe o valor atual de cada variável em tempo real
  - Usar o depurador em um programa com funções permite ver exatamente: qual função foi chamada · com quais valores · e o que foi retornado

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 06: *"Dominamos laços e vetores — hoje o código ganha estrutura com funções e aprendemos a rastrear o que acontece dentro do programa"* |
| Retomada | Professor projeta um programa longo sem funções que calcula a média de uma turma · pergunta: *"Se eu precisar corrigir um erro neste código, onde começo a procurar?"* — alunos identificam o problema · professor reescreve o mesmo programa com funções e mostra a diferença de legibilidade |
| Explicação | Slides — por que modularizar, funções void e com retorno, passagem por valor, boas práticas, recursividade com fatorial, uso do depurador (breakpoint, step into, watch) · demonstração ao vivo na IDE com depurador |
| Dinâmica | "Rastreio na Mão" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: função é um bloco com nome que faz uma coisa bem feita · void não retorna · tipo retorna · passagem por valor preserva o original · recursividade precisa de condição de parada · depurador mostra o que acontece por dentro · Próxima SA: orientação a objetos — classes e objetos |

---

## Dinâmica — "Rastreio na Mão"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a capacidade de rastrear manualmente o fluxo de execução de um programa com funções — simulando o que o depurador faz automaticamente na IDE, e consolidando a compreensão de parâmetros, retorno e passagem por valor.

**Materiais:** slide com o código projetado · ficha de rastreio impressa (1 por grupo) ou quadro branco.

**Passo a passo:**

1. **Apresentação do código** *(2 min)*
O professor projeta um programa com 2 a 3 funções. Os grupos recebem a ficha de rastreio em branco.

2. **Rastreio em grupo** *(8 min)*
Os grupos executam o programa mentalmente, preenchendo a ficha linha por linha: qual função está ativa · quais são os valores dos parâmetros · o que é retornado · qual é a saída final.

3. **Confronto e debate** *(5 min)*
Os grupos compartilham seus rastreios. O professor executa o programa ao vivo na IDE com o depurador, mostrando o painel de variáveis em tempo real e comparando com o que os grupos previram.

**Código para rastrear:**

```
int somar(int a, int b) {
    return a + b;
}

boolean ehPositivo(int numero) {
    return numero > 0;
}

void analisarResultado(int x, int y) {
    int resultado = somar(x, y);
    if (ehPositivo(resultado)) {
        exibir("Resultado positivo: " + resultado);
    } else {
        exibir("Resultado não positivo: " + resultado);
    }
}

// Programa principal:
analisarResultado(8, -3);
analisarResultado(-5, -2);
```

**Ficha de rastreio:**

| Chamada | Função ativa | Parâmetros | Retorno | Saída exibida |
|---------|-------------|------------|---------|---------------|
| `analisarResultado(8, -3)` | `somar(8, -3)` | a=8, b=-3 | 5 | — |
| | `ehPositivo(5)` | numero=5 | true | — |
| | `analisarResultado` | resultado=5 | — | "Resultado positivo: 5" |
| `analisarResultado(-5, -2)` | `somar(-5, -2)` | a=-5, b=-2 | -7 | — |
| | `ehPositivo(-7)` | numero=-7 | false | — |
| | `analisarResultado` | resultado=-7 | — | "Resultado não positivo: -7" |

> **Nota:** o objetivo é que os alunos internalizem que o depurador não é uma ferramenta para quando o código quebra — é uma ferramenta de compreensão que todo desenvolvedor profissional usa para entender o comportamento do programa antes e depois de um problema. Rastrear na mão primeiro torna o uso do depurador muito mais intuitivo.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 06 — 25/03/2026 · Linguagem de Programação Estruturada — Parte 2 |
| Próxima SA → | SA 08 — 08/04/2026 · Linguagem de Programação Orientada a Objetos — Introdução |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (essencial para demonstração do depurador ao vivo)
- Ficha de rastreio impressa (1 por grupo) ou quadro branco
- Quadro branco e marcador

---

## Observações do Professor
