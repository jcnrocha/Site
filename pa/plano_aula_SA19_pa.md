# UC: Programação de Aplicativos
## SA 19 — 2º Trimestre

---

## Tema

Técnicas de Programação — Depuração e Rastreabilidade

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de depuração e sua importância no ciclo de desenvolvimento de software
- Utilizar as ferramentas de depuração da IDE com proficiência: breakpoints, step over, step into, step out e painel de variáveis
- Aplicar técnicas de rastreabilidade para acompanhar o fluxo de execução de um programa complexo
- Identificar e corrigir diferentes tipos de erros: sintaxe, lógica e tempo de execução
- Registrar logs de execução para rastrear o comportamento do programa em ambiente de produção

**Capacidades da matriz:** 6.5 Depuração · 6.6 Rastreabilidade · Utilizar a IDE para rastreabilidade do código · Identificar erros de acordo com o requisito do programa

---

## Conteúdo

- Retomada da SA 18: *"Na SA passada otimizamos o código para rodar mais rápido — hoje aprendemos a encontrar e corrigir problemas com precisão usando depuração e rastreabilidade"*

- **Tipos de erro em programação:**

  | Tipo | Quando ocorre | Exemplo | Como identificar |
  |------|--------------|---------|-----------------|
  | **Erro de sintaxe** | Em tempo de compilação | Falta de `;` · chave não fechada | IDE sublinha em vermelho antes de executar |
  | **Erro de lógica** | Em tempo de execução | Resultado errado · laço infinito | Programa executa mas produz resultado incorreto |
  | **Erro de execução (runtime)** | Durante a execução | `NullPointerException` · divisão por zero | Programa para abruptamente com mensagem de erro |

- **Depuração — além do print:**
  - Muitos iniciantes usam `System.out.println()` para inspecionar valores — funciona, mas é lento e deixa lixo no código
  - O depurador da IDE permite inspecionar qualquer variável em qualquer momento sem modificar o código
  - Depurar com a IDE é mais preciso, mais rápido e mais profissional

- **Ferramentas do depurador da IDE — revisão e aprofundamento:**

  | Recurso | Função | Atalho VS Code |
  |---------|--------|---------------|
  | **Breakpoint** | Marca uma linha onde a execução deve pausar | Clicar na margem esquerda da linha |
  | **Run in Debug Mode** | Inicia o programa no modo de depuração | `F5` |
  | **Step Over** | Executa a linha atual sem entrar dentro de funções chamadas | `F10` |
  | **Step Into** | Entra dentro da função chamada na linha atual | `F11` |
  | **Step Out** | Sai da função atual e retorna ao ponto de chamada | `Shift+F11` |
  | **Continue** | Continua a execução até o próximo breakpoint | `F5` |
  | **Watch** | Monitora o valor de uma expressão ou variável específica | Painel Watch |
  | **Variables** | Exibe todos os valores das variáveis no escopo atual | Painel Variables |
  | **Call Stack** | Mostra a pilha de chamadas — qual função chamou qual | Painel Call Stack |

- **Breakpoints condicionais:**
  - Breakpoint que só pausa a execução quando uma condição específica é verdadeira
  - Extremamente útil em laços com muitas iterações — pausa apenas na iteração problemática
  - Configuração: clicar com botão direito no breakpoint → Edit Breakpoint → inserir condição

  ```java
  // Sem breakpoint condicional: para nas 1000 iterações
  for (int i = 0; i < 1000; i++) {
      processar(lista[i]);   // breakpoint aqui para 1000 vezes
  }

  // Com breakpoint condicional: para apenas quando i == 537
  // Condição: i == 537
  ```

- **Rastreabilidade com logs:**
  - Em ambiente de produção o depurador não está disponível — logs são o mecanismo de rastreabilidade
  - Log: registro textual de eventos importantes durante a execução do programa
  - Níveis de log padrão:

  | Nível | Uso | Exemplo |
  |-------|-----|---------|
  | `DEBUG` | Informações detalhadas para desenvolvimento | Valores de variáveis · fluxo interno |
  | `INFO` | Eventos normais e esperados | Usuário logado · pedido criado |
  | `WARN` | Situação inesperada mas não crítica | Tentativa de login inválida |
  | `ERROR` | Erro que impede uma operação | Falha na conexão com banco · exceção não tratada |

  ```java
  // Java — logging com java.util.logging
  import java.util.logging.Logger;
  Logger logger = Logger.getLogger(MinhaClasse.class.getName());

  logger.info("Conexão com banco estabelecida");
  logger.warning("Tentativa de acesso com credenciais inválidas: " + usuario);
  logger.severe("Erro crítico ao processar pedido #" + idPedido + ": " + e.getMessage());
  ```

  ```python
  # Python — logging nativo
  import logging
  logging.basicConfig(level=logging.DEBUG)

  logging.info("Conexão com banco estabelecida")
  logging.warning(f"Tentativa inválida: {usuario}")
  logging.error(f"Erro ao processar pedido #{id_pedido}: {e}")
  ```

- **Estratégia de depuração — passo a passo profissional:**
  1. **Reproduzir o erro:** identificar exatamente quais passos causam o problema
  2. **Isolar:** descobrir em qual parte do código o erro ocorre — reduzir o escopo
  3. **Colocar breakpoint:** na linha suspeita ou antes dela
  4. **Inspecionar:** observar os valores das variáveis no momento do erro
  5. **Hipótese e correção:** formular o que está errado e corrigir
  6. **Verificar:** executar novamente para confirmar que o erro foi resolvido sem criar novos

- **Erros comuns e como rastrear cada um:**

  | Erro | Sintoma | Estratégia de depuração |
  |------|---------|------------------------|
  | `NullPointerException` | Programa para com NPE | Breakpoint na linha do erro · verificar qual objeto é null no painel Variables |
  | Resultado errado em cálculo | Valor incorreto exibido | Breakpoint antes do cálculo · inspecionar cada variável passo a passo |
  | Laço infinito | Programa trava sem resposta | Pausar execução manualmente · verificar condição de saída no painel Variables |
  | Dado não salvo no banco | Operação parece funcionar mas dado não persiste | Verificar se `commit()` está sendo chamado · log após cada operação |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 18: *"Código otimizado — hoje aprendemos a encontrar erros com precisão cirúrgica usando o depurador e logs"* |
| Retomada | Professor projeta um programa com um erro de lógica sutil que produz resultado errado · tenta encontrar o erro usando apenas `println` · depois usa o depurador e encontra em segundos · pergunta: *"Qual abordagem vocês prefeririam usar no trabalho?"* |
| Explicação | Slides — tipos de erro, ferramentas do depurador com atalhos, breakpoints condicionais, rastreabilidade com logs e níveis, estratégia de depuração passo a passo, erros comuns e como rastrear · demonstração ao vivo na IDE com programa com erro intencional |
| Dinâmica | "Caçada ao Bug" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: depurador é mais preciso que println · breakpoint pausa · step into entra · painel variables inspeciona · log registra em produção · estratégia: reproduzir → isolar → inspecionar → corrigir · Próxima SA: teste unitário parte 1 |

---

## Dinâmica — "Caçada ao Bug"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** aplicar a estratégia de depuração para encontrar e corrigir erros em programas com bugs intencionais — desenvolvendo a capacidade de raciocínio analítico e o uso prático das ferramentas de depuração da IDE.

**Materiais:** computadores com VS Code e os programas com bugs preparados · ficha de depuração impressa (1 por grupo).

**Passo a passo:**

1. **Distribuição dos programas** *(1 min)*
Cada grupo recebe um programa diferente com um bug intencional. O desafio é: identificar o tipo de erro · usar o depurador para encontrar a causa raiz · corrigir o código · descrever o processo que usaram.

2. **Depuração em grupo** *(10 min)*
Os grupos usam o depurador da IDE — breakpoints, step over/into e painel de variáveis — para encontrar e corrigir o bug. Registram na ficha: onde colocaram o breakpoint · o que observaram · qual era o erro · como corrigiram.

3. **Relato e debate** *(4 min)*
Cada grupo relata o bug que encontrou e o processo de depuração. O professor complementa com dicas adicionais de cada caso.

**Bugs sugeridos para os programas:**

| Programa | Bug intencional | Tipo de erro | O que o depurador revela |
|----------|----------------|-------------|--------------------------|
| Calculadora de média | Divisão por 2 em vez de 3 para média de 3 notas | Lógica | Valor da variável `divisor` é 2 no painel Variables |
| Busca em vetor | Condição do `for`: `i <= lista.length` em vez de `i < lista.length` | Runtime | `ArrayIndexOutOfBoundsException` na última iteração |
| Transferência bancária | `commit()` comentado — dados não são persistidos | Lógica | Banco retorna 0 linhas afetadas no log |
| Verificação de senha | `=` em vez de `==` na comparação | Lógica | Variável recebe valor em vez de comparar — sempre verdadeiro |

> **Nota:** reforçar que encontrar bugs é uma habilidade que se desenvolve com prática — quanto mais o aluno depurar, mais rápido ficará em identificar padrões de erro. No mercado, desenvolvedores que sabem depurar bem são extremamente valorizados porque reduzem o tempo de resolução de incidentes em produção.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 18 — 17/06/2026 · Técnicas de Programação — Otimização de Código |
| Próxima SA → | SA 20 — 01/07/2026 · Técnicas de Programação — Teste Unitário Parte 1 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code configurado e programas com bugs preparados
- Ficha de depuração da dinâmica impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
