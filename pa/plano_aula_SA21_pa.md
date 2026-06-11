# UC: Programação de Aplicativos
## SA 21 — 2º Trimestre

---

## Tema

Técnicas de Programação — Teste Unitário Parte 2

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de cobertura de testes e identificar lacunas nos testes existentes
- Escrever testes unitários para métodos que integram banco de dados usando objetos simulados (mocks)
- Identificar erros no código a partir da falha de um teste, corrigindo o problema com precisão
- Aplicar boas práticas na escrita de testes: independência, clareza e cobertura de cenários de borda
- Consolidar o uso do framework de testes na IDE como parte do fluxo normal de desenvolvimento

**Capacidades da matriz:** 6.7 Teste Unitário · Utilizar a IDE para aplicação de teste unitário · Identificar erros de acordo com o requisito do programa

---

## Conteúdo

- Retomada da SA 20: *"Na SA passada escrevemos os primeiros testes com o padrão AAA — hoje aprofundamos com cobertura de testes, testes com banco de dados e boas práticas"*

- **Cobertura de testes (Code Coverage):**
  - Métrica que indica qual percentual do código é exercitado pelos testes existentes
  - Cobertura de 0%: nenhum teste · cobertura de 100%: cada linha do código é executada por ao menos um teste
  - Alta cobertura não garante ausência de bugs — mas baixa cobertura garante que existem cenários não verificados
  - Cobertura mínima recomendada em projetos profissionais: 70% a 80%
  - VS Code exibe cobertura com extensões de teste — linhas cobertas em verde · não cobertas em vermelho

- **Cenários de borda — o que não pode faltar nos testes:**
  - Cenário feliz: entrada válida e esperada — o fluxo normal
  - Cenário de borda: valores nos limites do permitido (zero, negativo, máximo, vazio, nulo)
  - Cenário de erro: entrada inválida que deve gerar exceção ou retorno específico

  ```java
  // Cobrindo três cenários para o mesmo método
  @Test
  void deveAprovarQuandoNotaForSetePontoZero() {
      assertEquals("Aprovado", calc.classificar(7.0));   // limite exato
  }

  @Test
  void deveRetornarRecuperacaoQuandoNotaForCincoPontoZero() {
      assertEquals("Recuperação", calc.classificar(5.0));
  }

  @Test
  void deveLancarExcecaoQuandoNotaForNegativa() {
      assertThrows(IllegalArgumentException.class,
          () -> calc.classificar(-1.0));
  }
  ```

- **Testes com banco de dados — o problema do isolamento:**
  - Teste unitário não deve depender de banco de dados real: banco pode estar indisponível · dados podem variar · teste fica lento
  - Solução: substituir a dependência real por um objeto simulado — **Mock**
  - Mock: objeto que imita o comportamento de uma dependência real sem executá-la de verdade
  - Framework de mock mais usado em Java: **Mockito** · em Python: `unittest.mock`

  ```java
  // Java — teste com Mock usando Mockito
  @Test
  void deveBuscarAlunoPorId() {
      // Arrange — cria o mock do repositório
      AlunoRepository repositorioMock = mock(AlunoRepository.class);
      when(repositorioMock.buscarPorId(1)).thenReturn(new Aluno("Ana", 8.5));

      AlunoService service = new AlunoService(repositorioMock);

      // Act
      Aluno resultado = service.buscarAluno(1);

      // Assert
      assertEquals("Ana", resultado.getNome());
      verify(repositorioMock).buscarPorId(1);   // confirma que o mock foi chamado
  }
  ```

  ```python
  # Python — teste com Mock
  from unittest.mock import MagicMock

  def test_buscar_aluno_por_id():
      # Arrange
      repositorio_mock = MagicMock()
      repositorio_mock.buscar_por_id.return_value = Aluno("Ana", 8.5)

      service = AlunoService(repositorio_mock)

      # Act
      resultado = service.buscar_aluno(1)

      # Assert
      assert resultado.nome == "Ana"
      repositorio_mock.buscar_por_id.assert_called_once_with(1)
  ```

- **Identificando erros a partir de falhas nos testes:**
  - Quando um teste falha, a mensagem indica: método testado · valor esperado · valor obtido
  - Fluxo de correção: ler a mensagem de falha → localizar o método com problema → corrigir → reexecutar
  - Testes que falham após uma alteração indicam que a alteração quebrou algo — **regressão**
  - Detectar regressão automaticamente é um dos maiores valores dos testes unitários

- **Boas práticas na escrita de testes:**
  - **Independência:** cada teste deve rodar sozinho sem depender de outros testes
  - **Clareza:** nome do teste descreve exatamente o que está sendo verificado
  - **Uma assertion por teste:** teste focado em um único comportamento — mais fácil de diagnosticar quando falha
  - **Dados fixos e previsíveis:** evitar dados aleatórios ou dependentes do ambiente
  - **Sem lógica nos testes:** teste com `if` ou laço é sinal de que está testando coisas demais

- **Ciclo de desenvolvimento com testes:**
  ```
  Escrever o teste → Rodar (falha — código ainda não existe) →
  Implementar o código → Rodar (passa) →
  Refatorar → Rodar (ainda passa) → próximo teste
  ```
  > Este ciclo é chamado de TDD (Test-Driven Development) — prática adotada em empresas de alta qualidade de software

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 20: *"Escrevemos os primeiros testes com AAA — hoje ampliamos a cobertura, testamos com banco simulado e consolidamos boas práticas"* |
| Retomada | Professor executa os testes da SA 20 ao vivo e exibe a cobertura de código na IDE · aponta as linhas não cobertas em vermelho · pergunta: *"O que pode acontecer nessas linhas que nenhum teste verifica?"* — alunos identificam os riscos |
| Explicação | Slides — cobertura de testes, cenários de borda, testes com mock, identificando regressão, boas práticas, ciclo TDD · demonstração ao vivo na IDE com mock e cobertura |
| Dinâmica | "Teste Que Pega" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: cobertura mede o quanto do código é testado · cenário de borda testa os limites · mock substitui dependências externas · teste que falha indica regressão · Próxima SA: Ética Profissional |

---

## Dinâmica — "Teste Que Pega"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar cobertura de testes e cenários de borda desafiando os grupos a escrever testes que detectem bugs intencionais em implementações defeituosas — desenvolvendo o raciocínio de "o que pode dar errado" que é a essência do pensamento orientado a testes.

**Materiais:** computadores com VS Code e framework configurado · slide com as implementações defeituosas projetado · ficha de testes impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação da implementação** *(1 min por rodada)*
O professor projeta uma implementação com um bug intencional. O grupo deve escrever o teste que detecta o bug — sem que o professor revele onde está o erro.

2. **Escrita e execução** *(9 min)*
Os grupos escrevem os testes e executam na IDE. O grupo que conseguir fazer o teste falhar (detectando o bug) venceu a rodada.

3. **Revelação e debate** *(5 min)*
O professor revela o bug em cada implementação · discute quais testes pegaram e quais não pegaram · reforça quais cenários de borda são mais eficazes.

**Implementações defeituosas:**

| Método | Bug intencional | Teste que detecta |
|--------|----------------|-------------------|
| `calcularMedia(n1, n2)` retorna `(n1 + n2) / 3` em vez de `/2` | Divisor errado | `assertEquals(7.0, calc.calcularMedia(8.0, 6.0))` falha → retorna 4.67 |
| `ehMaiorDeIdade(idade)` retorna `idade > 18` em vez de `>= 18` | Condição exclui o limite | `assertTrue(calc.ehMaiorDeIdade(18))` falha → retorna false |
| `aplicarDesconto(preco, pct)` retorna `preco + (preco * pct / 100)` em vez de `-` | Soma em vez de subtrai | `assertEquals(90.0, calc.aplicarDesconto(100.0, 10.0))` falha → retorna 110 |
| `contarPalavras(texto)` retorna `texto.length()` em vez de `texto.split(" ").length` | Conta caracteres em vez de palavras | `assertEquals(3, calc.contarPalavras("olá mundo aqui"))` falha |

> **Nota:** reforçar que escrever testes que "pegam" bugs requer pensar como alguém que quer quebrar o sistema — não apenas verificar o caminho feliz. Esse pensamento adversarial é exatamente o que diferencia um desenvolvedor que escreve testes eficazes de um que escreve testes que sempre passam sem verificar nada de útil.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 20 — 01/07/2026 · Técnicas de Programação — Teste Unitário Parte 1 |
| Próxima SA → | SA 22 — 29/07/2026 · Ética Profissional — Princípios da Conduta Ética |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores com VS Code e framework de teste configurado (JUnit ou PyTest)
- Extensão de cobertura de código instalada no VS Code
- Implementações defeituosas preparadas no projeto de demonstração
- Ficha de testes impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
