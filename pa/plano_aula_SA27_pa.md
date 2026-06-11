# UC: Programação de Aplicativos
## SA 27 — 2º Trimestre

---

## Tema

Gestão da Qualidade — Controle e Registro

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o conceito de controle de qualidade no desenvolvimento de software e sua diferença em relação ao monitoramento
- Aplicar práticas de controle de qualidade no ciclo de desenvolvimento: revisão de código, checklists e critérios de aceite
- Compreender a importância do registro de ocorrências e não conformidades como ferramenta de melhoria contínua
- Identificar e documentar não conformidades em um sistema com base em critérios técnicos definidos
- Relacionar controle e registro de qualidade com a cultura de melhoria contínua em equipes de desenvolvimento

**Capacidades da matriz:** 9.1.2 Controle · 9.1.3 Registro · Monitorar a execução de atividades assegurando o seu desenvolvimento · Aplicar os princípios de organização do trabalho no exercício das atividades profissionais

---

## Conteúdo

- Retomada da SA 26: *"Na SA passada aprendemos ferramentas da qualidade e monitoramento — hoje completamos o bloco com controle e registro: como garantir que os padrões sejam seguidos e que os problemas sejam documentados"*

- **Monitoramento × Controle — qual a diferença:**
  - **Monitoramento:** observar o que está acontecendo em tempo real — detectar desvios
  - **Controle:** agir sobre os desvios detectados para corrigi-los e prevenir recorrência
  - Monitoramento sem controle é inútil: detectar um problema e não agir não resolve nada
  - Ciclo completo: monitorar → detectar desvio → controlar → registrar → melhorar

- **Controle de qualidade no desenvolvimento de software:**
  - Conjunto de práticas que garantem que o código produzido atende aos padrões definidos antes de chegar ao usuário
  - Não é responsabilidade de um testador separado — é responsabilidade de todo o time de desenvolvimento
  - Principais práticas de controle:

  | Prática | Descrição | Quando aplicar |
  |---------|-----------|----------------|
  | **Revisão de código (Code Review)** | Outro desenvolvedor analisa o código antes do merge | A cada Pull Request |
  | **Critérios de aceite** | Lista do que a funcionalidade deve fazer para ser considerada pronta | Antes de iniciar o desenvolvimento |
  | **Checklist de entrega** | Lista de verificações obrigatórias antes de enviar o código | Antes de abrir o Pull Request |
  | **Análise estática** | Ferramenta automática que detecta problemas de código sem executar | A cada commit (CI pipeline) |
  | **Testes de regressão** | Reexecutar todos os testes ao integrar novo código | A cada merge na branch principal |

- **Checklist de qualidade — exemplo prático:**
  - Checklist que o desenvolvedor deve verificar antes de submeter o código para revisão

  ```
  [ ] O código compila sem erros
  [ ] Os testes unitários existentes continuam passando
  [ ] Foram escritos testes para o novo código
  [ ] A cobertura de testes não diminuiu
  [ ] O código está formatado conforme o padrão do projeto
  [ ] Os métodos públicos estão documentados (Javadoc/docstring)
  [ ] Não há código comentado desnecessariamente
  [ ] Não há credenciais ou senhas no código
  [ ] O Pull Request tem uma descrição clara do que foi alterado
  [ ] Foi testado manualmente o cenário principal e os casos de borda
  ```

- **Critérios de aceite — definindo o que é "pronto":**
  - Descrição objetiva e verificável do comportamento esperado de uma funcionalidade
  - Escritos antes do desenvolvimento — alinham expectativas entre desenvolvedor, analista e cliente
  - Formato: *"Dado [contexto], quando [ação], então [resultado esperado]"*

  ```
  Funcionalidade: Login de usuário

  Critério 1: Dado que o usuário informa e-mail e senha corretos,
              quando clica em "Entrar",
              então é redirecionado para o painel principal.

  Critério 2: Dado que o usuário informa senha incorreta,
              quando clica em "Entrar",
              então vê a mensagem "E-mail ou senha incorretos" sem revelar qual está errado.

  Critério 3: Dado que o usuário erra a senha 3 vezes consecutivas,
              quando tenta a quarta vez,
              então a conta é bloqueada por 15 minutos.
  ```

- **Registro de ocorrências e não conformidades:**
  - **Não conformidade:** qualquer situação em que o produto ou processo não atende ao padrão definido
  - Registrar não conformidades é essencial para: rastrear o histórico de problemas · identificar padrões recorrentes · embasar melhorias no processo
  - O que registrar em uma não conformidade:
    - Descrição do problema
    - Quando e onde foi identificado
    - Impacto para o usuário ou para o sistema
    - Causa raiz identificada
    - Ação corretiva aplicada
    - Responsável e prazo

- **Ferramentas de registro em TI:**

  | Ferramenta | Uso |
  |------------|-----|
  | **GitHub Issues / GitLab Issues** | Registro de bugs, melhorias e tarefas diretamente no repositório |
  | **Jira** | Gestão de projetos e rastreamento de bugs em empresas |
  | **Trello** | Kanban visual para equipes menores |
  | **Notion** | Documentação e registro de ocorrências de forma estruturada |

- **Melhoria contínua — o ciclo PDCA aplicado a TI:**
  - **P (Plan):** planejar — definir padrões, critérios de aceite, checklist
  - **D (Do):** fazer — desenvolver seguindo os padrões
  - **C (Check):** verificar — monitorar, controlar, registrar não conformidades
  - **A (Act):** agir — corrigir os desvios e melhorar o processo para a próxima iteração

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 26: *"Monitoramos a qualidade — hoje controlamos e registramos: as práticas que fecham o ciclo de qualidade em TI"* |
| Retomada | Professor pergunta: *"Se vocês encontrassem o mesmo tipo de bug pela terceira vez no mesmo sistema, o que isso indicaria sobre o processo de desenvolvimento?"* — alunos debatem · professor conecta com a importância do registro para identificar padrões e agir na causa raiz |
| Explicação | Slides — monitoramento × controle, práticas de controle de qualidade, checklist de entrega, critérios de aceite com formato dado/quando/então, registro de não conformidades, ferramentas de registro, ciclo PDCA em TI |
| Dinâmica | "Abre o Chamado" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: controle age sobre o desvio detectado · checklist garante padrão antes do merge · critério de aceite alinha o que é "pronto" · registro documenta para melhorar · PDCA é o ciclo da melhoria contínua · Próxima SA: Modelagem de Negócios — Canvas |

---

## Dinâmica — "Abre o Chamado"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a habilidade de registrar não conformidades de forma estruturada e objetiva — simulando o processo real de abertura de chamado/issue que desenvolvedores e analistas realizam diariamente em ferramentas como GitHub Issues e Jira.

**Materiais:** slide com os cenários de não conformidade projetados · ficha de registro impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor descreve um problema encontrado em um sistema fictício. O grupo deve registrar a não conformidade de forma estruturada na ficha, preenchendo todos os campos obrigatórios.

2. **Registro em grupo** *(9 min)*
Os grupos preenchem a ficha de registro para cada cenário apresentado, incluindo: descrição, impacto, causa raiz provável, ação corretiva sugerida e prioridade.

3. **Comparação e debate** *(5 min)*
Os grupos compartilham seus registros. O professor compara a qualidade dos registros e discute: *"Um desenvolvedor que receber este chamado consegue entender e resolver o problema sem precisar perguntar nada?"*

**Cenários de não conformidade:**

| Cenário | O que registrar |
|---------|----------------|
| Sistema de cadastro aceita e-mail sem o símbolo "@" | Descrição · impacto (dados inválidos no banco) · causa provável (falta de validação) · ação (adicionar validação de e-mail antes do INSERT) |
| Página de relatório demora 12 segundos para carregar | Descrição · impacto (experiência ruim do usuário) · causa provável (consulta SQL sem índice) · ação (analisar query e adicionar índice na coluna de busca) |
| Sistema exibe mensagem de erro com stack trace para o usuário final | Descrição · impacto (exposição de informação técnica sensível) · causa provável (exceção não tratada) · ação (tratar exceção e exibir mensagem amigável) |
| Método `calcularDesconto` retorna valor negativo quando desconto > 100% | Descrição · impacto (erro de cálculo em pedidos) · causa provável (falta de validação do percentual) · ação (validar percentual entre 0 e 100 antes do cálculo) |

**Modelo de ficha de registro:**

| Campo | Preenchimento |
|-------|---------------|
| Título | Resumo curto e objetivo do problema |
| Descrição | O que acontece, em qual funcionalidade, como reproduzir |
| Impacto | Quem é afetado e qual a consequência |
| Causa raiz provável | O que no código ou processo causou o problema |
| Ação corretiva sugerida | O que deve ser feito para resolver |
| Prioridade | Crítica / Alta / Média / Baixa |
| Responsável sugerido | Quem deveria resolver |

> **Nota:** reforçar que um bom registro de não conformidade economiza tempo da equipe inteira — um chamado vago como "sistema não funciona" gera ciclos de perguntas e respostas que atrasam a resolução. Desenvolvedores que abrem chamados claros e bem documentados são muito mais valorizados porque respeitam o tempo dos colegas.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 26 — 26/08/2026 · Gestão da Qualidade — Ferramentas e Monitoramento |
| Próxima SA → | SA 28 — 09/09/2026 · Modelagem de Negócios — Introdução ao Canvas |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Ficha de registro de não conformidade impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
