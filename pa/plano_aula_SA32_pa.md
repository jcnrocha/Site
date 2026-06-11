# UC: Programação de Aplicativos
## SA 32 — 3º Trimestre

---

## Tema

Consolidação — Técnicas de Programação e Testes

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Revisar e consolidar as técnicas de programação estudadas: formatação, documentação, DRY, otimização, depuração e rastreabilidade
- Aplicar testes unitários em um projeto existente, identificando lacunas de cobertura e corrigindo-as
- Analisar a cobertura de testes de um projeto e propor novos testes para cenários não cobertos
- Integrar todas as técnicas de programação em um fluxo de desenvolvimento profissional completo
- Preparar-se tecnicamente para o Projeto Final com domínio das ferramentas de qualidade

**Capacidades da matriz:** Bloco 6 da matriz · Aplicar métodos e técnicas de programação · Utilizar a IDE para rastreabilidade do código · Utilizar a IDE para aplicação de teste unitário · Identificar erros de acordo com o requisito do programa

---

## Conteúdo

- Contextualização da SA: *"Hoje encerramos a fase de consolidação — revisamos as técnicas de programação e testes que transformam código funcional em código profissional. Depois dessa SA, começamos o Projeto Final"*

- **Revisão rápida — Técnicas de Programação (SAs 16 a 21):**

  | Técnica | Pontos-chave |
  |---------|-------------|
  | Formatação (6.1) | Indentação · espaçamento · limite de linha · `formatOnSave` · Prettier |
  | Documentação (6.2) | Comentário de linha e bloco · Javadoc/docstring · tags `@param`, `@return` |
  | Reutilização — DRY (6.3) | Uma lógica em um lugar · métodos com parâmetros · classes utilitárias |
  | Otimização (6.4) | Big O · laços aninhados = O(n²) · HashSet para busca O(1) · break no laço |
  | Depuração (6.5) | Tipos de erro · breakpoint · step over/into · painel de variáveis |
  | Rastreabilidade (6.6) | Logs por nível (DEBUG/INFO/WARN/ERROR) · estratégia de depuração em 5 passos |
  | Teste Unitário (6.7) | Padrão AAA · assertions · cobertura · cenários de borda · mocks · TDD |

- **Projeto de consolidação — aplicar testes em código existente:**
  - Professor fornece um projeto com código funcional mas sem testes e com algumas violações de boas práticas
  - Missão dos alunos: analisar o código · escrever testes unitários · identificar e corrigir violações de técnica

  ```java
  // Código fornecido para consolidação — com problemas intencionais

  public class GerenciadorPedidos {

      // Calcula o total do pedido com desconto
      public double calc(double v, double d) {
          return v - (v * d / 100);
      }

      // Verifica se pedido pode ser aprovado
      public boolean verificar(double total, int itens) {
          if (total > 0) {
              if (itens > 0) {
                  return true;
              } else {
                  return false;
              }
          }
          return false;
      }

      // Busca pedido em lista
      public int buscar(int[] ids, int alvo) {
          for (int i = 0; i < ids.length; i++) {
              for (int j = 0; j < ids.length; j++) {
                  if (ids[i] == alvo) return i;
              }
          }
          return -1;
      }
  }
  ```

  **Problemas a identificar no código:**
  - `calc` e `verificar` e `buscar` — nomes não descritivos (violação de nomenclatura)
  - `d` e `v` como parâmetros — sem significado (violação de nomenclatura)
  - `verificar` com ifs aninhados desnecessários — pode ser simplificado para uma linha
  - `buscar` com dois `for` aninhados — O(n²) desnecessário · um `for` com `break` resolve em O(n)
  - Nenhum método documentado com Javadoc/docstring
  - Nenhum teste unitário

- **Testes a escrever para o projeto de consolidação:**

  ```java
  // Testes que os alunos devem criar

  @Test
  void deveCalcularTotalComDescontoCorretamente() {
      // 100 com 10% de desconto = 90
  }

  @Test
  void deveRetornarFalsoQuandoTotalForZero() { }

  @Test
  void deveRetornarFalsoQuandoItensForZero() { }

  @Test
  void deveBuscarIdExistenteERetornarIndice() { }

  @Test
  void deveRetornarMenosUmQuandoIdNaoExistir() { }

  @Test
  void deveLancarExcecaoQuandoDescontoForMaiorQue100() {
      // cenário de borda — desconto inválido
  }
  ```

- **Fluxo integrado de desenvolvimento profissional — revisão:**
  ```
  1. Escrever o código com nomes descritivos e formatação correta
  2. Documentar os métodos públicos com Javadoc/docstring
  3. Aplicar DRY — extrair lógica repetida para métodos reutilizáveis
  4. Verificar complexidade — substituir O(n²) por estrutura mais eficiente quando possível
  5. Escrever testes unitários — cenário feliz + cenários de borda
  6. Executar os testes — corrigir falhas
  7. Verificar cobertura — adicionar testes para linhas não cobertas
  8. Commitar com mensagem descritiva
  ```

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização: *"Última SA de consolidação — depois desta, o Projeto Final começa. Vamos fechar o ciclo com técnicas e testes aplicados em um código real com problemas reais"* |
| Retomada | Professor projeta o código do `GerenciadorPedidos` e pergunta: *"Quantos problemas vocês conseguem identificar em 2 minutos?"* — alunos listam ao vivo · professor confirma e organiza a lista no quadro |
| Prática dirigida | Alunos refatoram o código identificando e corrigindo cada problema · professor orienta passo a passo · em seguida escrevem os testes unitários e verificam a cobertura na IDE |
| Dinâmica | "Auditoria de Código" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: técnicas de programação são inseparáveis do código de qualidade · testes garantem que o código faz o que promete · o fluxo integrado é o padrão profissional · Próxima SA: Projeto Final — briefing e formação dos grupos |

---

## Dinâmica — "Auditoria de Código"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar todas as técnicas de programação estudadas por meio de uma auditoria técnica de um trecho de código — simulando o processo real de code review que desenvolvedores realizam diariamente em equipes profissionais.

**Materiais:** slide com o código para auditoria projetado · ficha de auditoria impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do código** *(2 min)*
O professor projeta um trecho de código funcional mas com múltiplos problemas de técnica. Cada grupo recebe a ficha de auditoria e deve avaliar o código em 6 dimensões.

2. **Auditoria em grupo** *(8 min)*
Os grupos analisam o código em cada dimensão, atribuem uma nota de 0 a 2 e descrevem o problema encontrado e a melhoria sugerida.

3. **Resultado e debate** *(5 min)*
Cada grupo apresenta a nota geral e o problema mais crítico identificado. O professor consolida e discute quais problemas impactam mais na manutenção real.

**Ficha de auditoria — 6 dimensões:**

| Dimensão | O que avaliar | Nota (0–2) |
|----------|--------------|------------|
| Formatação | Indentação, espaçamento, limite de linha | |
| Nomenclatura | Nomes de variáveis, métodos e classes descritivos | |
| DRY | Ausência de código repetido | |
| Complexidade | Laços e estruturas sem O(n²) desnecessário | |
| Documentação | Javadoc/docstring nos métodos públicos | |
| Testes | Presença e qualidade dos testes unitários | |

> **Pontuação:** 0 = problema grave · 1 = problema parcial · 2 = atende ao padrão · **Nota máxima: 12 pontos**

> **Nota:** reforçar que este é o formato real de uma revisão de código em empresas — desenvolvedores avaliam código alheio com critérios técnicos objetivos, não com base em preferência pessoal. Saber dar e receber feedback técnico com clareza e respeito é uma das soft skills mais valiosas em times de desenvolvimento.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 31 — 30/09/2026 · Consolidação — POO e Conexão com Banco de Dados |
| Próxima SA → | SA 33 — 14/10/2026 · Projeto Final — Apresentação e Briefing |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores com VS Code, framework de teste e extensão de cobertura configurados
- Projeto base do `GerenciadorPedidos` disponibilizado aos alunos (via repositório ou arquivo)
- Ficha de auditoria impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
