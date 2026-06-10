# UC: Programação de Aplicativos
## SA 17 — 2º Trimestre

---

## Tema

Técnicas de Programação — Reutilização de Código

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o princípio DRY (Don't Repeat Yourself) e identificar trechos de código que violam esse princípio
- Criar funções e métodos reutilizáveis que centralizam lógica comum em um único lugar
- Utilizar bibliotecas e módulos externos para aproveitar código já desenvolvido e testado pela comunidade
- Criar componentes e classes genéricas que possam ser reaproveitados em diferentes partes do sistema
- Reconhecer o impacto da reutilização na manutenção, legibilidade e qualidade do código

**Capacidades da matriz:** 6.3 Reutilização de código · Aplicar métodos e técnicas de programação · Empregar comentários para documentação

---

## Conteúdo

- Retomada da SA 16: *"Na SA passada formatamos e documentamos o código — hoje aprendemos a não repetir código desnecessariamente, um dos princípios mais importantes da programação profissional"*

- **O problema da repetição de código:**
  - Código duplicado é um dos maiores inimigos da manutenção: quando a lógica muda, é necessário alterar em todos os lugares onde foi copiada
  - Se uma alteração for esquecida em uma cópia, o sistema passa a ter comportamentos inconsistentes — bugs difíceis de encontrar
  - Duplicação aumenta o tamanho do código sem agregar valor

  ```java
  // Código com repetição — problema
  double mediaAluno1 = (nota1A + nota1B + nota1C) / 3;
  if (mediaAluno1 >= 7.0) exibir("Aluno 1: Aprovado");

  double mediaAluno2 = (nota2A + nota2B + nota2C) / 3;
  if (mediaAluno2 >= 7.0) exibir("Aluno 2: Aprovado");

  double mediaAluno3 = (nota3A + nota3B + nota3C) / 3;
  if (mediaAluno3 >= 7.0) exibir("Aluno 3: Aprovado");
  ```

- **Princípio DRY — Don't Repeat Yourself:**
  - Cada pedaço de conhecimento ou lógica deve ter uma única representação no sistema
  - Não se trata apenas de evitar copiar e colar — trata-se de centralizar decisões de negócio
  - Oposto do DRY: WET — Write Everything Twice (ou Waste Everyone's Time)
  - Aplicar DRY: extrair a lógica repetida para um método, função ou classe reutilizável

  ```java
  // Código DRY — solução
  double calcularMedia(double n1, double n2, double n3) {
      return (n1 + n2 + n3) / 3;
  }

  void verificarAprovacao(String nome, double media) {
      if (media >= 7.0) exibir(nome + ": Aprovado");
      else exibir(nome + ": Reprovado");
  }

  // Uso:
  verificarAprovacao("Aluno 1", calcularMedia(nota1A, nota1B, nota1C));
  verificarAprovacao("Aluno 2", calcularMedia(nota2A, nota2B, nota2C));
  ```

- **Métodos e funções reutilizáveis — boas práticas:**
  - **Uma responsabilidade:** método que faz uma coisa bem feita é reutilizável · método que faz muitas coisas só serve para aquele contexto específico
  - **Parâmetros em vez de valores fixos:** usar parâmetros no lugar de valores hardcoded torna o método genérico
  - **Retorno em vez de exibição:** métodos que retornam valores são mais reutilizáveis que os que apenas exibem no console

  ```java
  // Ruim — difícil de reutilizar (exibe diretamente e usa valor fixo)
  void verificarIdade() {
      if (idade >= 18) System.out.println("Maior de idade");
  }

  // Bom — reutilizável (recebe parâmetro e retorna resultado)
  boolean ehMaiorDeIdade(int idade) {
      return idade >= 18;
  }
  ```

- **Bibliotecas e módulos externos:**
  - Código desenvolvido, testado e mantido pela comunidade que pode ser incorporado ao projeto
  - Evita reinventar a roda: não é necessário escrever do zero o que já existe e funciona bem
  - Gerenciado pelo gerenciador de dependências da linguagem: Maven/Gradle (Java) · pip (Python) · npm (JavaScript)

  | Necessidade | Biblioteca | Como adicionar |
  |-------------|-----------|----------------|
  | Manipulação de datas | `java.time` (Java nativo) | Já disponível |
  | Requisições HTTP | `requests` (Python) | `pip install requests` |
  | Validação de e-mail | `commons-validator` (Java) | Dependência Maven |
  | Geração de PDF | `reportlab` (Python) | `pip install reportlab` |
  | Manipulação de JSON | `jackson` (Java) | Dependência Maven |

- **Classes utilitárias — centralizando lógica comum:**
  - Classe criada exclusivamente para agrupar métodos estáticos reutilizáveis
  - Não representa uma entidade do negócio — representa uma coleção de ferramentas
  - Exemplos: `ValidadorUtils`, `FormatadorUtils`, `CalculadorUtils`

  ```java
  // Classe utilitária — agrupa validações reutilizáveis
  public class ValidadorUtils {

      public static boolean emailValido(String email) {
          return email != null && email.contains("@") && email.contains(".");
      }

      public static boolean cpfValido(String cpf) {
          return cpf != null && cpf.replaceAll("[^0-9]", "").length() == 11;
      }

      public static boolean notaValida(double nota) {
          return nota >= 0.0 && nota <= 10.0;
      }
  }

  // Uso em qualquer parte do sistema:
  if (ValidadorUtils.emailValido(emailDigitado)) { ... }
  if (ValidadorUtils.notaValida(notaInformada)) { ... }
  ```

- **Herança e interfaces como reutilização estrutural:**
  - Herança reutiliza atributos e métodos da classe pai em todas as filhas — evita duplicação de estrutura
  - Interfaces definem contratos reutilizados por classes diferentes — mesma assinatura, implementações distintas
  - OO aplicada corretamente é DRY aplicado na estrutura do sistema

- **Sinais de que o código precisa ser refatorado para DRY:**
  - Mesmo trecho de código aparece em dois ou mais lugares com pequenas variações
  - Ao corrigir um bug, é necessário alterar em mais de um arquivo
  - Método com mais de 30 linhas — provavelmente está fazendo mais de uma coisa
  - Classe com mais de 300 linhas — provavelmente acumula responsabilidades demais

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 16: *"Formatamos e documentamos — hoje aprendemos a não repetir código, um dos princípios que mais impacta a qualidade de um sistema a longo prazo"* |
| Retomada | Professor projeta um código com a mesma lógica de validação copiada em 4 lugares diferentes · pergunta: *"Se a regra de validação mudar, quantos lugares precisaria alterar? O que pode acontecer se esquecer de um?"* — alunos percebem o problema · professor apresenta DRY como a solução |
| Explicação | Slides — o problema da repetição, princípio DRY, métodos reutilizáveis com parâmetros e retorno, bibliotecas externas, classes utilitárias, herança como reutilização estrutural, sinais de que o código precisa de refatoração · demonstração ao vivo na IDE |
| Dinâmica | "Seca o Código" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: DRY — cada lógica em um único lugar · método reutilizável recebe parâmetros e retorna valores · biblioteca externa evita reinventar a roda · classe utilitária agrupa ferramentas comuns · Próxima SA: otimização de código |

---

## Dinâmica — "Seca o Código"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** aplicar o princípio DRY identificando e eliminando repetições em trechos de código reais — desenvolvendo o raciocínio de refatoração que os desenvolvedores usam continuamente para manter a qualidade do código ao longo do tempo.

**Materiais:** slide com o código úmido (WET) projetado · ficha de refatoração impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do código** *(2 min)*
O professor projeta um trecho de código com repetição evidente. Os grupos precisam: identificar o trecho repetido · extrair para um método reutilizável · reescrever o código principal usando o novo método.

2. **Refatoração em grupo** *(8 min)*
Os grupos reescrevem o código aplicando DRY na ficha de refatoração.

3. **Comparação e debate** *(5 min)*
Os grupos apresentam suas versões. O professor compara e discute: *"Qual versão é mais fácil de manter? O que acontece se a regra de negócio mudar?"*

**Código WET para refatorar:**

```java
// Código com repetição — WET
System.out.println("=== Relatório ===");
System.out.println("Aluno: Ana | Nota: 8.5");
double mediaAna = (8.5 + 7.0 + 9.0) / 3;
if (mediaAna >= 7.0) System.out.println("Situação: Aprovada");
else System.out.println("Situação: Reprovada");
System.out.println("-----------------");

System.out.println("=== Relatório ===");
System.out.println("Aluno: Carlos | Nota: 5.0");
double mediaCarlos = (5.0 + 4.5 + 6.0) / 3;
if (mediaCarlos >= 7.0) System.out.println("Situação: Aprovado");
else System.out.println("Situação: Reprovado");
System.out.println("-----------------");

System.out.println("=== Relatório ===");
System.out.println("Aluno: Julia | Nota: 9.5");
double mediaJulia = (9.5 + 8.0 + 10.0) / 3;
if (mediaJulia >= 7.0) System.out.println("Situação: Aprovada");
else System.out.println("Situação: Reprovada");
System.out.println("-----------------");
```

**Resultado esperado após refatoração DRY:**

```java
double calcularMedia(double n1, double n2, double n3) {
    return (n1 + n2 + n3) / 3;
}

void gerarRelatorio(String nome, double n1, double n2, double n3) {
    double media = calcularMedia(n1, n2, n3);
    System.out.println("=== Relatório ===");
    System.out.println("Aluno: " + nome + " | Média: " + media);
    System.out.println("Situação: " + (media >= 7.0 ? "Aprovado" : "Reprovado"));
    System.out.println("-----------------");
}

// Uso:
gerarRelatorio("Ana", 8.5, 7.0, 9.0);
gerarRelatorio("Carlos", 5.0, 4.5, 6.0);
gerarRelatorio("Julia", 9.5, 8.0, 10.0);
```

> **Nota:** reforçar que se a nota mínima para aprovação mudar de 7.0 para 6.5, na versão WET seriam necessárias 3 alterações — e esquecer uma causaria inconsistência. Na versão DRY: 1 alteração em um único lugar. Isso é o que DRY significa na prática.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 16 — 03/06/2026 · Técnicas de Programação — Formatação e Documentação de Código |
| Próxima SA → | SA 18 — 17/06/2026 · Técnicas de Programação — Otimização de Código |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado
- Ficha de refatoração da dinâmica impressa (1 por grupo) ou quadro branco
- Quadro branco e marcador

---

## Observações do Professor
