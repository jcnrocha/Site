# UC: Programação de Aplicativos
## SA 08 — 1º Trimestre

---

## Tema

Linguagem de Programação Orientada a Objetos — Introdução

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o paradigma de programação orientada a objetos e sua diferença em relação ao paradigma estruturado
- Identificar os conceitos fundamentais de classe e objeto, reconhecendo a relação entre os dois
- Declarar uma classe com atributos e métodos, aplicando as convenções de nomenclatura da linguagem
- Instanciar objetos a partir de uma classe e acessar seus atributos e métodos
- Aplicar o princípio de encapsulamento utilizando modificadores de acesso e métodos getters e setters

**Capacidades da matriz:** 4. Linguagem de programação orientada a objetos · Reconhecer especificações técnicas e paradigmas de linguagem de programação · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE)

---

## Conteúdo

- Retomada rápida da SA 07: *"Na SA passada encerramos a programação estruturada com funções e recursividade — hoje começamos um novo paradigma: a orientação a objetos, que é como a maioria dos sistemas profissionais é construída"*

- **Por que orientação a objetos:**
  - Programação estruturada funciona bem para programas pequenos e lineares
  - Conforme o sistema cresce: mais dados, mais funções, mais relações entre eles — o código estruturado se torna difícil de organizar e manter
  - OO organiza o código em torno de entidades do mundo real — cada entidade tem seus próprios dados e comportamentos agrupados em um único lugar
  - Vantagens: organização · reutilização · manutenção facilitada · modelagem próxima da realidade

- **Comparativo: estruturado × orientado a objetos:**

  | Aspecto | Estruturado | Orientado a Objetos |
  |---------|-------------|---------------------|
  | Organização | Funções separadas dos dados | Dados e comportamentos juntos em classes |
  | Foco | Como o programa executa | Quais entidades existem e o que fazem |
  | Reutilização | Funções reutilizáveis | Classes reutilizáveis em qualquer projeto |
  | Exemplo | `calcularSalario(horas, valor)` | `funcionario.calcularSalario()` |

- **Classe — o molde:**
  - Define a estrutura e o comportamento de um tipo de objeto
  - Descreve o que o objeto **tem** (atributos) e o que o objeto **faz** (métodos)
  - A classe é o projeto — o objeto é o produto construído a partir dele
  - Analogia: a classe `Carro` é o projeto do carro · cada carro que sai da fábrica é um objeto dessa classe — todos têm marca, modelo e cor, mas com valores diferentes

  ```
  class Aluno {
      String nome;
      int idade;
      double nota;

      void exibirDados() {
          exibir("Nome: " + nome + " | Nota: " + nota);
      }
  }
  ```

- **Objeto — a instância:**
  - É a entidade concreta criada a partir de uma classe
  - Cada objeto tem sua própria cópia dos atributos com seus próprios valores
  - Criado com a palavra-chave `new`

  ```
  Aluno aluno1 = new Aluno();
  aluno1.nome = "Ana";
  aluno1.nota = 8.5;

  Aluno aluno2 = new Aluno();
  aluno2.nome = "Carlos";
  aluno2.nota = 7.0;

  aluno1.exibirDados();   // Nome: Ana | Nota: 8.5
  aluno2.exibirDados();   // Nome: Carlos | Nota: 7.0
  ```

  > Duas instâncias da mesma classe · estrutura idêntica · valores diferentes

- **Construtores:**
  - Método especial chamado automaticamente quando um objeto é criado com `new`
  - Mesmo nome da classe · sem tipo de retorno
  - Usado para inicializar os atributos do objeto no momento da criação

  ```
  class Aluno {
      String nome;
      double nota;

      Aluno(String nome, double nota) {
          this.nome = nome;
          this.nota = nota;
      }
  }

  // Criação com construtor:
  Aluno aluno1 = new Aluno("Ana", 8.5);
  ```

- **Encapsulamento:**
  - Princípio de esconder os atributos de uma classe do acesso direto externo
  - Os atributos são declarados como `private` — só a própria classe pode acessá-los diretamente
  - O acesso externo é feito por métodos públicos: **getters** (leitura) e **setters** (escrita)
  - Por que encapsular: protege os dados de modificações inválidas · controla o que pode ser lido e alterado · facilita a manutenção sem quebrar código que usa a classe

  ```
  class Produto {
      private String nome;
      private double preco;

      // Getter — leitura
      public String getNome() {
          return nome;
      }

      // Setter — escrita com validação
      public void setPreco(double preco) {
          if (preco >= 0) {
              this.preco = preco;
          } else {
              exibir("Preço inválido — deve ser maior ou igual a zero");
          }
      }
  }
  ```

- **Modificadores de acesso:**

  | Modificador | Visibilidade |
  |-------------|-------------|
  | `public` | Acessível de qualquer lugar |
  | `private` | Acessível apenas dentro da própria classe |
  | `protected` | Acessível dentro da classe e subclasses |
  | (sem modificador) | Acessível dentro do mesmo pacote |

- **Convenções de nomenclatura em OO:**
  - **Classes:** PascalCase — primeira letra de cada palavra maiúscula · `Aluno`, `ContaBancaria`, `ProdutoEstoque`
  - **Atributos e métodos:** camelCase — primeira letra minúscula · `nomeCompleto`, `calcularSaldo()`
  - **Constantes:** SNAKE_CASE maiúsculo · `TAXA_JUROS`, `LIMITE_MAXIMO`

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 07: *"Encerramos a programação estruturada — hoje abrimos a porta para o paradigma que domina o mercado: orientação a objetos"* |
| Retomada | Professor pergunta: *"Pensem em um sistema de uma escola: alunos, professores, turmas, disciplinas, notas. Como vocês organizariam isso em um programa estruturado? E se precisasse adicionar mais 10 tipos de entidade?"* — alunos percebem o problema · professor apresenta OO como a solução natural |
| Explicação | Slides — por que OO, comparativo com estruturado, classe como molde, objeto como instância, construtor, encapsulamento com private/getter/setter, modificadores de acesso, convenções de nomenclatura · demonstração ao vivo na IDE |
| Dinâmica | "Classe ou Objeto?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: classe é o molde · objeto é a instância · atributos são dados · métodos são comportamentos · encapsulamento protege com private e libera com getter/setter · Próxima SA: herança e polimorfismo |

---

## Dinâmica — "Classe ou Objeto?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar a distinção entre classe e objeto, e entre atributos e métodos, por meio da modelagem de entidades do mundo real — desenvolvendo o raciocínio de abstração que é o ponto de partida para qualquer projeto orientado a objetos.

**Materiais:** slide com as entidades projetadas · ficha de modelagem impressa (1 por grupo) · quadro branco.

**Passo a passo:**

1. **Apresentação da entidade** *(1 min por rodada)*
O professor apresenta uma entidade do mundo real. O grupo precisa: identificar se o item dado é uma classe ou um objeto · listar 3 atributos · listar 2 métodos · e criar um exemplo de instância com valores reais.

2. **Modelagem em grupo** *(8 min)*
Os grupos preenchem a ficha para cada entidade apresentada.

3. **Apresentação e debate** *(6 min)*
Os grupos compartilham suas modelagens. O professor compara as diferentes respostas e discute: *"Dois grupos modelaram a mesma entidade de formas diferentes — as duas estão certas? Quando uma seria melhor que a outra?"*

**Entidades sugeridas:**

| Entidade apresentada | É classe ou objeto? | Atributos sugeridos | Métodos sugeridos |
|----------------------|--------------------|--------------------|-------------------|
| Smartphone | Classe | marca, modelo, capacidadeBateria | ligar(), tirarFoto(), carregarBateria() |
| iPhone 15 Pro Max da Ana | Objeto da classe Smartphone | marca="Apple", modelo="15 Pro Max" | — (herda da classe) |
| Conta Bancária | Classe | numeroConta, titular, saldo | depositar(), sacar(), consultarSaldo() |
| Funcionário | Classe | nome, cargo, salario | calcularSalario(), baterPonto() |
| Pedido de delivery | Classe | numeroPedido, itens, valorTotal, status | confirmar(), cancelar(), rastrear() |
| O pedido #4872 de pizza | Objeto da classe Pedido | numeroPedido=4872, status="em preparo" | — (herda da classe) |

> **Nota:** o objetivo central é que os alunos internalizem a diferença: classe é o conceito abstrato · objeto é o concreto com valores reais. Reforçar que modelar bem as classes no início de um projeto é o que separa um sistema fácil de manter de um sistema caótico — e que essa habilidade de abstração é uma das mais valorizadas em desenvolvedores sêniores.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 07 — 01/04/2026 · Linguagem de Programação Estruturada — Parte 3 |
| Próxima SA → | SA 09 — 15/04/2026 · Linguagem de Programação Orientada a Objetos — Herança e Polimorfismo |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (para demonstração ao vivo)
- Ficha de modelagem impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
