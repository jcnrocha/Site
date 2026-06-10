# UC: Programação de Aplicativos
## SA 09 — 1º Trimestre

---

## Tema

Linguagem de Programação Orientada a Objetos — Herança e Polimorfismo

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de herança e como ele permite reutilizar e especializar classes existentes
- Criar uma hierarquia de classes utilizando herança, identificando classe pai e classes filhas
- Compreender o conceito de polimorfismo e como ele permite tratar objetos de tipos diferentes de forma uniforme
- Diferenciar classes abstratas de interfaces e reconhecer quando usar cada uma
- Aplicar herança e polimorfismo em programas práticos na IDE, consolidando os pilares da OO

**Capacidades da matriz:** 4. Linguagem de programação orientada a objetos · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE) · Reconhecer especificações técnicas e paradigmas de linguagem de programação

---

## Conteúdo

- Retomada rápida da SA 08: *"Na SA passada aprendemos classes, objetos, construtores e encapsulamento — hoje completamos os pilares da OO com herança e polimorfismo"*

- **Herança — reutilizando e especializando classes:**
  - Mecanismo que permite que uma classe (filha) herde atributos e métodos de outra classe (pai)
  - A classe filha recebe tudo que a classe pai tem e pode adicionar ou modificar comportamentos
  - Palavra-chave: `extends`
  - Relação semântica: classe filha **é um tipo de** classe pai · `Cachorro` é um tipo de `Animal`
  - Evita duplicação de código — atributos e métodos comuns ficam na classe pai e são herdados automaticamente

  ```
  class Animal {
      String nome;
      int idade;

      void comer() {
          exibir(nome + " está comendo");
      }
  }

  class Cachorro extends Animal {
      String raca;

      void latir() {
          exibir(nome + " está latindo: Au au!");
      }
  }

  // Uso:
  Cachorro dog = new Cachorro();
  dog.nome = "Rex";       // herdado de Animal
  dog.raca = "Labrador";  // próprio de Cachorro
  dog.comer();            // método herdado
  dog.latir();            // método próprio
  ```

- **A palavra-chave `super`:**
  - Usada dentro da classe filha para acessar atributos e métodos da classe pai
  - Muito usada em construtores para reaproveitar a inicialização da classe pai

  ```
  class Animal {
      String nome;
      Animal(String nome) {
          this.nome = nome;
      }
  }

  class Gato extends Animal {
      String cor;
      Gato(String nome, String cor) {
          super(nome);       // chama o construtor de Animal
          this.cor = cor;
      }
  }
  ```

- **Sobrescrita de método (Override):**
  - A classe filha pode redefinir um método herdado da classe pai com comportamento específico
  - Anotação `@Override` indica que o método está sendo sobrescrito — boa prática obrigatória
  - O método na classe filha substitui o da classe pai quando chamado em um objeto filha

  ```
  class Animal {
      void emitirSom() {
          exibir("Som genérico de animal");
      }
  }

  class Gato extends Animal {
      @Override
      void emitirSom() {
          exibir("Miau!");
      }
  }

  class Cachorro extends Animal {
      @Override
      void emitirSom() {
          exibir("Au au!");
      }
  }
  ```

- **Polimorfismo — muitas formas, uma interface:**
  - Capacidade de tratar objetos de classes diferentes de forma uniforme por meio de uma referência comum
  - Um objeto filha pode ser referenciado pelo tipo da classe pai
  - O método chamado é sempre o da classe real do objeto — não o da referência

  ```
  Animal a1 = new Gato();
  Animal a2 = new Cachorro();

  a1.emitirSom();   // exibe: Miau!       — método do Gato
  a2.emitirSom();   // exibe: Au au!      — método do Cachorro
  ```

  - Benefício prático: listas de objetos de tipos diferentes podem ser processadas com o mesmo código

  ```
  Animal[] animais = { new Gato(), new Cachorro(), new Gato() };
  for (Animal a : animais) {
      a.emitirSom();   // cada objeto responde com seu próprio comportamento
  }
  ```

- **Classes abstratas:**
  - Classe que não pode ser instanciada diretamente — existe apenas para ser herdada
  - Pode conter métodos abstratos (sem implementação) que as filhas são obrigadas a implementar
  - Usada quando há comportamento comum entre as filhas, mas a classe pai por si só não faz sentido existir como objeto

  ```
  abstract class Forma {
      abstract double calcularArea();   // obriga filhas a implementar

      void exibirArea() {
          exibir("Área: " + calcularArea());
      }
  }

  class Circulo extends Forma {
      double raio;
      Circulo(double raio) { this.raio = raio; }

      @Override
      double calcularArea() {
          return 3.14 * raio * raio;
      }
  }
  ```

- **Interfaces:**
  - Contrato que define quais métodos uma classe deve implementar — sem implementação própria
  - Uma classe pode implementar múltiplas interfaces (diferente da herança — só uma classe pai)
  - Palavra-chave: `implements`

  ```
  interface Voavel {
      void voar();
  }

  interface Nadavel {
      void nadar();
  }

  class Pato extends Animal implements Voavel, Nadavel {
      @Override
      public void voar() { exibir("Pato voando..."); }

      @Override
      public void nadar() { exibir("Pato nadando..."); }
  }
  ```

- **Comparativo: herança × classe abstrata × interface:**

  | Recurso | Quando usar | Permite instanciar? | Herança múltipla? |
  |---------|-------------|--------------------|--------------------|
  | Classe comum | Entidade concreta com comportamento próprio | Sim | Não |
  | Classe abstrata | Base com comportamento parcial — não faz sentido sozinha | Não | Não |
  | Interface | Contrato de capacidades sem implementação | Não | Sim |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 08: *"Já temos classes, objetos e encapsulamento — hoje adicionamos herança e polimorfismo e os quatro pilares da OO estarão completos"* |
| Retomada | Professor projeta três classes quase idênticas: `Funcionario`, `Gerente` e `Diretor` — todas com os mesmos atributos `nome`, `salario` e método `trabalhar()` copiados · pergunta: *"O que há de errado com esse código?"* — alunos identificam a repetição · professor apresenta herança como a solução |
| Explicação | Slides — herança com `extends`, `super`, sobrescrita com `@Override`, polimorfismo com referência pai, lista polimórfica, classes abstratas, interfaces, comparativo · demonstração ao vivo na IDE |
| Dinâmica | "Monta a Hierarquia" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: herança evita repetição com `extends` · `@Override` redefine comportamento · polimorfismo trata diferentes objetos com a mesma referência · classe abstrata é base sem instância · interface é contrato de capacidades · Próxima SA: Avaliação do 1º Trimestre |

---

## Dinâmica — "Monta a Hierarquia"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar herança, polimorfismo e classes abstratas por meio da construção de uma hierarquia de classes a partir de um conjunto de entidades — desenvolvendo o raciocínio de abstração e especialização que é a base do design orientado a objetos.

**Materiais:** cartões com as entidades e atributos impressos (1 conjunto por grupo) · ou slide com as entidades projetadas · folha para desenhar a hierarquia.

**Passo a passo:**

1. **Distribuição das entidades** *(1 min)*
Cada grupo recebe um conjunto de entidades misturadas. O desafio é organizá-las em uma hierarquia de herança: identificar a classe pai, as classes filhas, os atributos comuns e os específicos.

2. **Montagem da hierarquia** *(8 min)*
Os grupos desenham a hierarquia em forma de árvore, indicando: qual classe é pai · quais são filhas · quais atributos e métodos ficam na classe pai · quais são específicos de cada filha · se alguma classe deveria ser abstrata.

3. **Apresentação e debate** *(6 min)*
Cada grupo apresenta sua hierarquia. O professor compara as estruturas e discute as diferenças: *"Por que esse grupo colocou `calcularSalario` na classe pai e esse outro colocou nas filhas? Qual decisão é melhor e por quê?"*

**Conjunto de entidades para organizar:**

| Entidade | Atributos sugeridos | Métodos sugeridos |
|----------|--------------------|--------------------|
| Funcionario (pai — abstrato) | nome, cpf, salarioBase | calcularSalario(), registrarPonto() |
| Vendedor (filha) | comissao, metaMensal | calcularSalario() com comissão |
| Gerente (filha) | bonus, equipe | calcularSalario() com bônus, gerenciarEquipe() |
| Estagiario (filha) | bolsaAuxilio, cursoFaculdade | calcularSalario() apenas bolsa |
| Diretor (filha) | participacaoLucros, numeroFuncionarios | calcularSalario() com participação nos lucros |

**Resultado esperado da hierarquia:**
```
        Funcionario (abstrata)
       /       |        \       \
 Vendedor  Gerente  Estagiario  Diretor
```
> Atributos `nome`, `cpf`, `salarioBase` e método `registrarPonto()` ficam em `Funcionario` · `calcularSalario()` é abstrato em `Funcionario` e implementado diferente em cada filha — demonstração perfeita de polimorfismo.

> **Nota:** reforçar que esta hierarquia é um modelo real de sistema de RH — exatamente o tipo de estrutura que os alunos vão encontrar ou criar em estágio e no primeiro emprego. A decisão de onde colocar cada atributo e método não é arbitrária: reflete o que é comum a todos (classe pai) e o que é específico de cada tipo (classe filha).

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 08 — 08/04/2026 · Linguagem de Programação Orientada a Objetos — Introdução |
| Próxima SA → | SA 10 — 22/04/2026 · Avaliação — 1º Trimestre |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (para demonstração ao vivo)
- Cartões com as entidades da dinâmica impressos (1 conjunto por grupo) ou slide projetado
- Folha em branco para desenhar a hierarquia (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
