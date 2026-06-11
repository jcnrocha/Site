# UC: Programação de Aplicativos
## SA 20 — 2º Trimestre

---

## Tema

Técnicas de Programação — Teste Unitário Parte 1

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o que é teste unitário e qual o seu papel no ciclo de desenvolvimento de software
- Identificar os frameworks de teste mais utilizados na linguagem da UC (JUnit para Java / PyTest para Python)
- Estruturar um teste unitário seguindo o padrão Arrange, Act, Assert (AAA)
- Escrever os primeiros testes unitários para métodos simples na IDE
- Reconhecer a diferença entre testar manualmente e testar de forma automatizada

**Capacidades da matriz:** 6.7 Teste Unitário · Utilizar a IDE para aplicação de teste unitário · Identificar erros de acordo com o requisito do programa

---

## Conteúdo

- Retomada da SA 19: *"Na SA passada aprendemos a encontrar erros com o depurador e logs — hoje aprendemos a prevenir erros antes que eles cheguem ao usuário: testes unitários"*

- **Por que testar:**
  - Todo código tem a chance de quebrar quando algo muda — uma alteração em um método pode quebrar outro método que dependia dele
  - Teste manual (rodar o programa e verificar visualmente) é lento, inconsistente e não escala
  - Teste automatizado: código que verifica código · roda em segundos · pode ser executado a qualquer momento · garante que nada quebrou após uma alteração

- **O que é teste unitário:**
  - Teste que verifica uma unidade isolada do código — geralmente um único método
  - Isolado: não depende de banco de dados, rede, arquivos ou outros sistemas externos
  - Automatizado: escrito uma vez e executado quantas vezes for necessário
  - Rápido: cada teste deve rodar em milissegundos

- **Frameworks de teste:**

  | Linguagem | Framework | Como adicionar |
  |-----------|-----------|----------------|
  | Java | JUnit 5 | Dependência Maven: `junit-jupiter` |
  | Python | PyTest | `pip install pytest` |
  | JavaScript | Jest | `npm install jest` |

- **Estrutura AAA — Arrange, Act, Assert:**
  - Padrão universal para organizar qualquer teste unitário
  - **Arrange (Preparar):** define os dados de entrada e configura o cenário do teste
  - **Act (Agir):** chama o método que está sendo testado
  - **Assert (Verificar):** confirma que o resultado obtido é igual ao resultado esperado

  ```java
  // Java — JUnit 5
  @Test
  void deveCalcularMediaCorretamente() {
      // Arrange
      Calculadora calc = new Calculadora();
      double nota1 = 8.0;
      double nota2 = 6.0;

      // Act
      double resultado = calc.calcularMedia(nota1, nota2);

      // Assert
      assertEquals(7.0, resultado);
  }
  ```

  ```python
  # Python — PyTest
  def test_calcular_media_corretamente():
      # Arrange
      calc = Calculadora()
      nota1 = 8.0
      nota2 = 6.0

      # Act
      resultado = calc.calcular_media(nota1, nota2)

      # Assert
      assert resultado == 7.0
  ```

- **Assertions mais usadas:**

  | Assertion | O que verifica |
  |-----------|---------------|
  | `assertEquals(esperado, obtido)` | Valor obtido é igual ao esperado |
  | `assertNotEquals(esperado, obtido)` | Valor obtido é diferente do esperado |
  | `assertTrue(condição)` | Condição é verdadeira |
  | `assertFalse(condição)` | Condição é falsa |
  | `assertNull(objeto)` | Objeto é nulo |
  | `assertNotNull(objeto)` | Objeto não é nulo |
  | `assertThrows(Exceção, código)` | Código lança a exceção esperada |

- **Convenções de nomenclatura para testes:**
  - Nome do método deve descrever o cenário testado: `deveRetornarErroQuandoNotaForNegativa`
  - Padrão: `deve[Comportamento]Quando[Condição]`
  - Classe de teste: mesmo nome da classe testada com sufixo `Test` · `CalculadoraTest`
  - Arquivo de teste separado do código principal — pasta `test` no projeto

- **Executando testes na IDE:**
  - VS Code com extensão de teste: botão de play ao lado de cada método de teste
  - Resultado verde: teste passou · resultado vermelho: teste falhou
  - Mensagem de falha indica: valor esperado × valor obtido — facilita a correção

- **Teste manual × teste automatizado:**

  | Aspecto | Teste manual | Teste automatizado |
  |---------|-------------|-------------------|
  | Velocidade | Lento | Milissegundos |
  | Consistência | Depende do testador | Sempre igual |
  | Reexecução | Trabalhosa | Um clique |
  | Documentação | Nenhuma | O próprio código de teste |
  | Cobertura | Limitada ao que foi verificado | Todos os cenários escritos |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 19: *"Depuramos erros existentes — hoje aprendemos a escrever código que garante que os erros não existam"* |
| Retomada | Professor pergunta: *"Depois de alterar um método, como vocês sabem que nada mais quebrou no sistema?"* — alunos respondem · professor mostra que sem testes a resposta honesta é "não sei" · apresenta teste unitário como a resposta profissional |
| Explicação | Slides — por que testar, o que é teste unitário, frameworks, padrão AAA com exemplos, assertions mais usadas, convenções de nomenclatura, como executar na IDE, comparativo manual × automatizado · demonstração ao vivo na IDE |
| Dinâmica | "Escreve o Teste" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: teste unitário verifica uma unidade isolada · AAA organiza o teste em preparar, agir e verificar · assertEquals compara resultado obtido com esperado · teste verde passa · teste vermelho indica onde corrigir · Próxima SA: Teste Unitário Parte 2 |

---

## Dinâmica — "Escreve o Teste"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** aplicar o padrão AAA escrevendo testes unitários para métodos simples — desenvolvendo a habilidade de pensar nos cenários de teste antes mesmo de escrever o código de produção, prática conhecida como TDD (Test-Driven Development).

**Materiais:** computadores com VS Code e framework de teste configurado · slide com os métodos a serem testados projetado · ficha de testes impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do método** *(1 min por rodada)*
O professor projeta a assinatura e o comportamento esperado de um método. O grupo deve escrever o teste unitário usando o padrão AAA — sem ver a implementação do método.

2. **Escrita do teste em grupo** *(8 min)*
Os grupos escrevem os testes na ficha ou diretamente na IDE, cobrindo ao menos dois cenários: o cenário feliz (entrada válida) e o cenário de borda (entrada no limite ou inválida).

3. **Execução e debate** *(6 min)*
O professor apresenta a implementação dos métodos · os grupos executam seus testes · verificam se passam ou falham · discutem os cenários que não foram cobertos.

**Métodos para testar:**

| Método | Comportamento esperado | Cenários sugeridos |
|--------|----------------------|-------------------|
| `boolean ehMaiorDeIdade(int idade)` | Retorna true se idade >= 18 | idade = 18 (limite) · idade = 17 · idade = 0 |
| `double calcularDesconto(double preco, double percentual)` | Retorna preço com desconto aplicado | preco=100, percentual=10 → 90.0 · percentual=0 → preço original |
| `String classificarNota(double nota)` | Retorna "Aprovado", "Recuperação" ou "Reprovado" | nota=7.0 · nota=5.0 · nota=4.9 |
| `boolean cpfValido(String cpf)` | Retorna true se CPF tem 11 dígitos numéricos | CPF válido · CPF com letras · CPF com menos dígitos |

> **Nota:** reforçar que escrever o teste antes de ver a implementação é uma prática avançada chamada TDD — Test-Driven Development. O teste funciona como uma especificação executável: descreve exatamente o que o método deve fazer em cada situação. Empresas que adotam TDD têm menos bugs em produção e código mais bem estruturado.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 19 — 24/06/2026 · Técnicas de Programação — Depuração e Rastreabilidade |
| Próxima SA → | SA 21 — 08/07/2026 · Técnicas de Programação — Teste Unitário Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code e framework de teste configurado (JUnit ou PyTest)
- Projeto de demonstração com métodos prontos para testar ao vivo
- Ficha de testes impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
