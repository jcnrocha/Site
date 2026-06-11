# UC: Programação de Aplicativos
## SA 26 — 2º Trimestre

---

## Tema

Gestão da Qualidade — Ferramentas e Monitoramento

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de gestão da qualidade no contexto do desenvolvimento de software
- Identificar as principais ferramentas da qualidade utilizadas em projetos de TI
- Aplicar o monitoramento como prática contínua para garantir a qualidade do software em desenvolvimento e produção
- Relacionar métricas de qualidade com decisões técnicas e de processo no ciclo de desenvolvimento
- Reconhecer a diferença entre qualidade do produto (software funcionando) e qualidade do processo (como o software é desenvolvido)

**Capacidades da matriz:** 9. Gestão da Qualidade · 9.1 Ferramentas da Qualidade · 9.1.1 Monitoramento · Monitorar a execução de atividades assegurando o seu desenvolvimento

---

## Conteúdo

- Retomada da SA 25: *"Encerramos o 2º Trimestre — hoje abrimos o 3º com Gestão da Qualidade, que conecta tudo o que aprendemos até aqui: testes, depuração, documentação e profissionalismo são todos ferramentas de qualidade"*

- **O que é qualidade em software:**
  - Software de qualidade é aquele que faz o que foi especificado, sem falhas, dentro do prazo e de forma segura
  - Duas dimensões de qualidade:
    - **Qualidade do produto:** o software funciona corretamente? É seguro? É performático? É fácil de usar?
    - **Qualidade do processo:** como o software é desenvolvido? Há testes? Há revisão de código? Há documentação?
  - Produto de qualidade exige processo de qualidade — não há atalho

- **Por que qualidade importa em TI:**
  - Bug em produção pode causar perda financeira, danos à reputação e até processos legais
  - Custo de corrigir um bug aumenta exponencialmente conforme avança no ciclo: desenvolvimento → teste → produção
  - Regra geral: corrigir em desenvolvimento custa 1 · em teste custa 10 · em produção custa 100

- **Ferramentas da qualidade em TI:**

  | Ferramenta | O que é | Exemplo de uso |
  |------------|---------|----------------|
  | **Teste unitário** | Verifica unidades isoladas do código | JUnit, PyTest — já estudado nas SAs 20 e 21 |
  | **Revisão de código (Code Review)** | Análise do código por outro desenvolvedor antes de integrar | Pull Request no GitHub/GitLab |
  | **Análise estática de código** | Ferramenta que detecta problemas sem executar o código | SonarQube, ESLint, Checkstyle |
  | **Integração Contínua (CI)** | Pipeline que executa testes automaticamente a cada commit | GitHub Actions, Jenkins |
  | **Cobertura de testes** | Métrica de quanto do código é exercitado por testes | JaCoCo (Java), Coverage.py (Python) |
  | **Linter** | Detecta erros de estilo e padrão no código | Prettier, Flake8, ESLint |

- **Monitoramento — qualidade em tempo real:**
  - Monitoramento é a prática de observar o comportamento do sistema em produção continuamente
  - Não basta o sistema funcionar nos testes — precisa funcionar para os usuários reais, o tempo todo
  - O que monitorar:
    - **Disponibilidade:** o sistema está no ar? (uptime)
    - **Performance:** o sistema responde em tempo aceitável? (tempo de resposta, latência)
    - **Erros:** há exceções ou falhas ocorrendo? (taxa de erros)
    - **Uso de recursos:** CPU, memória e disco estão dentro do esperado?

- **Métricas de qualidade mais usadas:**

  | Métrica | O que mede | Como interpretar |
  |---------|-----------|-----------------|
  | **Uptime** | Percentual de tempo em que o sistema está disponível | 99,9% = ~8,7h de indisponibilidade por ano |
  | **Tempo de resposta** | Quanto tempo o sistema leva para responder a uma requisição | Acima de 3 segundos: experiência ruim para o usuário |
  | **Taxa de erros** | Percentual de requisições que resultam em erro | Acima de 1%: indica problema a investigar |
  | **Cobertura de testes** | Percentual do código coberto por testes automatizados | Abaixo de 70%: risco de regressão não detectada |
  | **Dívida técnica** | Acúmulo de decisões técnicas ruins que precisarão ser corrigidas | Alta dívida = desenvolvimento mais lento no futuro |

- **Ferramentas de monitoramento:**
  - **Logs estruturados:** registros de eventos do sistema para análise posterior
  - **Dashboards:** painéis visuais com métricas em tempo real (ex: Grafana, Datadog)
  - **Alertas:** notificações automáticas quando uma métrica ultrapassa um limite (ex: taxa de erros > 2%)
  - **APM (Application Performance Monitoring):** rastreamento do desempenho de cada componente do sistema

- **Conexão com o que já foi estudado:**
  - Testes unitários (SA 20 e 21) → ferramenta de qualidade do processo
  - Depuração e logs (SA 19) → base do monitoramento em produção
  - Documentação (SA 16) → qualidade da manutenção futura
  - Ética e profissionalismo (SA 22 e 23) → postura que sustenta a cultura de qualidade

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização do 3º Trimestre: *"Entramos na reta final da UC — Gestão da Qualidade conecta tudo que aprendemos até aqui em um processo profissional completo"* |
| Retomada | Professor pergunta: *"Quando vocês usam um aplicativo que trava ou demora muito, o que pensam da empresa que o desenvolveu? Essa percepção é sobre qualidade — e ela começa no código"* — alunos compartilham experiências · professor conecta com as dimensões de qualidade |
| Explicação | Slides — qualidade do produto × qualidade do processo, custo do bug por fase, ferramentas da qualidade, monitoramento e o que monitorar, métricas principais, ferramentas de monitoramento, conexão com conteúdos anteriores |
| Dinâmica | "Diagnóstico de Qualidade" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: qualidade é processo e produto · corrigir cedo custa menos · monitoramento detecta problemas antes do usuário · métricas orientam decisões · Próxima SA: Controle e Registro da Qualidade |

---

## Dinâmica — "Diagnóstico de Qualidade"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** aplicar as ferramentas e métricas de qualidade na análise de um sistema fictício com problemas reais — desenvolvendo a capacidade de identificar lacunas de qualidade e propor ações de melhoria, habilidade diretamente aplicável em qualquer projeto profissional.

**Materiais:** slide com o relatório do sistema fictício projetado · ficha de diagnóstico impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do cenário** *(2 min)*
O professor projeta o relatório de um sistema em produção com indicadores abaixo do esperado. Os grupos precisam: identificar os problemas · classificar por gravidade · propor as ferramentas e ações para cada problema.

2. **Diagnóstico em grupo** *(8 min)*
Os grupos analisam o relatório, preenchem a ficha com diagnóstico e proposta de ação para cada indicador problemático.

3. **Apresentação e debate** *(5 min)*
Os grupos apresentam seus diagnósticos. O professor compara as propostas e discute qual seria a prioridade de ação em um cenário real.

**Relatório do sistema fictício:**

| Indicador | Valor atual | Referência saudável | Status |
|-----------|------------|---------------------|--------|
| Uptime | 97,5% | ≥ 99,5% | ⚠️ Crítico |
| Tempo de resposta médio | 4,2 segundos | ≤ 2 segundos | ⚠️ Crítico |
| Taxa de erros | 3,8% | ≤ 1% | ⚠️ Crítico |
| Cobertura de testes | 35% | ≥ 70% | ⚠️ Crítico |
| Revisão de código | Não praticada | Obrigatória antes do merge | ❌ Ausente |
| Documentação dos métodos | 20% dos métodos documentados | ≥ 80% | ❌ Insuficiente |
| Alertas de monitoramento | Nenhum configurado | Configurados para métricas críticas | ❌ Ausente |

**Perguntas para guiar o diagnóstico:**
- Qual problema representa o maior risco imediato para os usuários?
- Qual ferramenta de qualidade resolveria mais de um problema ao mesmo tempo?
- Se você fosse o líder técnico deste sistema, qual seria a primeira ação a tomar?

> **Nota:** reforçar que este relatório representa situações reais de sistemas em empresas de médio porte que cresceram rápido sem investir em qualidade desde o início. O custo de resolver todos esses problemas agora é muito maior do que teria sido se as boas práticas tivessem sido adotadas desde o começo. Qualidade é mais barata quando é construída do que quando é consertada.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 25 — 19/08/2026 · Avaliação Recuperação — 2º Trimestre |
| Próxima SA → | SA 27 — 02/09/2026 · Gestão da Qualidade — Controle e Registro |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Ficha de diagnóstico da dinâmica impressa (1 por grupo) ou slide projetado
- Quadro branco e marcador

---

## Observações do Professor
