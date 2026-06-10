# UC: Programação de Aplicativos
## SA 12 — 1º Trimestre

---

## Tema

Linguagem de Programação Orientada a Objetos — Consolidação

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Consolidar os conceitos de OO aplicando-os em um projeto prático guiado de ponta a ponta
- Criar um sistema simples com múltiplas classes relacionadas por herança e encapsulamento
- Identificar e corrigir erros comuns de OO com o auxílio do depurador da IDE
- Refatorar código estruturado em código orientado a objetos, reconhecendo as vantagens da transformação
- Esclarecer dúvidas remanescentes da avaliação e da recuperação antes de avançar para o 2º Trimestre

**Capacidades da matriz:** 4. Linguagem de programação orientada a objetos · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE) · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada dirigida da SA 10 e SA 11: *"Antes de avançar, vamos fechar as lacunas — os pontos que mais apareceram como dúvida nas avaliações serão retomados aqui com exemplos práticos"*

- **Revisão rápida dos pilares da OO — na prática:**
  - **Encapsulamento:** atributos `private` + getters e setters com validação real
  - **Herança:** classe pai com atributos comuns + classes filhas com `@Override`
  - **Polimorfismo:** referência pai apontando para objetos filhos em um array

- **Erros comuns de OO e como identificá-los:**

  | Erro | Causa | Como corrigir |
  |------|-------|---------------|
  | `NullPointerException` | Objeto não foi instanciado com `new` antes do uso | Verificar se a criação do objeto foi feita corretamente |
  | `cannot find symbol` | Atributo `private` acessado diretamente de fora da classe | Usar o getter correspondente |
  | Método não sobrescrito corretamente | Falta da anotação `@Override` ou assinatura diferente | Conferir nome, parâmetros e tipo de retorno iguais ao método pai |
  | `ArrayIndexOutOfBoundsException` | Acesso a índice inexistente no vetor | Usar `.length` no laço `for` em vez de número fixo |
  | Construtor não encontrado | Chamada de `new Classe(params)` sem construtor correspondente | Criar o construtor com os parâmetros corretos ou usar o construtor padrão |

- **Projeto prático guiado — Sistema de Cadastro de Alunos:**
  - Objetivo: criar um sistema simples com as classes `Pessoa`, `Aluno` e `Professor` — aplicando encapsulamento, herança e polimorfismo
  - Estrutura do projeto:

  ```
  Pessoa (classe pai — abstrata)
  ├── nome (private) · getter/setter
  ├── cpf (private) · getter
  └── exibirDados() — abstrato

  Aluno extends Pessoa
  ├── matricula (private) · getter/setter
  ├── nota (private) · getter/setter com validação 0–10
  └── exibirDados() — @Override

  Professor extends Pessoa
  ├── disciplina (private) · getter/setter
  ├── salario (private) · getter/setter com validação > 0
  └── exibirDados() — @Override
  ```

  - Programa principal:
    - Criar 2 objetos `Aluno` e 1 objeto `Professor`
    - Armazenar em um array do tipo `Pessoa[]`
    - Percorrer o array com `for` chamando `exibirDados()` em cada objeto
    - Observar o polimorfismo em ação: cada objeto responde com sua implementação

- **Refatoração — de estruturado para OO:**
  - Professor exibe um programa estruturado simples de gerenciamento de notas
  - A turma, em conjunto, identifica o que pode ser transformado em classe, atributos e métodos
  - Refatoração ao vivo na IDE — mostrando como o código fica mais limpo, organizado e reutilizável

- **Resolução de dúvidas pós-avaliação:**
  - Professor reserva tempo para responder dúvidas específicas levantadas pelos alunos nas avaliações SA 10 e SA 11
  - Foco em questões que muitos erraram — correção coletiva sem expor individualmente

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada dos resultados das avaliações: *"Fechamos o 1º Trimestre — hoje consolidamos OO com prática e resolvemos as dúvidas que ficaram"* |
| Revisão dirigida | Revisão rápida dos erros mais comuns identificados nas avaliações · tabela de erros projetada · exemplos corrigidos ao vivo na IDE |
| Projeto prático | Desenvolvimento guiado do Sistema de Cadastro de Alunos · professor codifica ao vivo com participação da turma · alunos replicam na própria máquina |
| Dinâmica | "Refatora Aí" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: OO organiza o código em entidades com dados e comportamentos · encapsulamento protege · herança reutiliza · polimorfismo unifica · Próxima SA: conexão com banco de dados |

---

## Dinâmica — "Refatora Aí"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar a transição do paradigma estruturado para o orientado a objetos por meio da refatoração de um trecho de código — desenvolvendo a capacidade de reconhecer oportunidades de melhoria estrutural no código e aplicar os conceitos de OO em uma situação concreta.

**Materiais:** slide com o código estruturado projetado · ficha de refatoração impressa (1 por grupo) ou quadro branco.

**Passo a passo:**

1. **Apresentação do código estruturado** *(2 min)*
O professor projeta um trecho de código estruturado funcional mas desorganizado. O grupo precisa identificar: quais dados poderiam virar atributos de uma classe · quais funções poderiam virar métodos · qual seria o nome da classe · se haveria necessidade de herança.

2. **Refatoração em grupo** *(8 min)*
Os grupos reescrevem a estrutura do código em OO na ficha: nome da classe, atributos com tipos e modificadores, assinatura dos métodos. Não é necessário escrever o código completo — apenas a estrutura.

3. **Apresentação e comparação** *(5 min)*
Os grupos apresentam suas propostas de refatoração. O professor compara as estruturas e discute as diferenças de escolha.

**Código estruturado para refatorar:**

```
// Código estruturado — gerenciamento de produto

String nomeProduto = "Notebook";
double precoProduto = 3500.00;
int quantidadeEstoque = 10;

void exibirProduto(String nome, double preco, int qtd) {
    exibir("Produto: " + nome);
    exibir("Preço: R$ " + preco);
    exibir("Estoque: " + qtd + " unidades");
}

void aplicarDesconto(double preco, double percentual) {
    double novoPreco = preco - (preco * percentual / 100);
    exibir("Preço com desconto: R$ " + novoPreco);
}

void atualizarEstoque(int qtdAtual, int qtdVendida) {
    int novoEstoque = qtdAtual - qtdVendida;
    exibir("Novo estoque: " + novoEstoque);
}
```

**Resultado esperado da refatoração:**
```
class Produto {
    private String nome;
    private double preco;
    private int quantidadeEstoque;

    // construtor, getters e setters

    void exibirDados() { ... }
    void aplicarDesconto(double percentual) { ... }
    void atualizarEstoque(int qtdVendida) { ... }
}
```

> **Nota:** reforçar que refatoração é uma habilidade real e valorizada no mercado — desenvolvedores passam boa parte do tempo melhorando código existente, não apenas escrevendo código novo. Saber identificar quando e como refatorar é o que diferencia um desenvolvedor júnior de um pleno.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 11 — 29/04/2026 · Avaliação Recuperação — 1º Trimestre |
| Próxima SA → | SA 13 — 13/05/2026 · Conexão com Banco de Dados — Introdução |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado (essencial para projeto prático ao vivo)
- Ficha de refatoração impressa (1 por grupo) ou quadro branco
- Resultados das avaliações SA 10 e SA 11 para referência dos pontos de revisão

---

## Observações do Professor
