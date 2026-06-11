# UC: Programação de Aplicativos
## SA 22 — 2º Trimestre

---

## Tema

Ética Profissional — Princípios da Conduta Ética

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o que é ética profissional e sua importância no contexto do desenvolvimento de sistemas
- Identificar e aplicar os princípios de sigilo, prudência, imparcialidade e honestidade no exercício da profissão
- Reconhecer situações do cotidiano do desenvolvedor que envolvem dilemas éticos e propor condutas adequadas
- Relacionar ética profissional com responsabilidade sobre dados de usuários e decisões técnicas
- Compreender as consequências profissionais e legais de condutas antiéticas em TI

**Capacidades da matriz:** 7. Ética profissional · 7.1.1 Sigilo · 7.1.2 Prudência · 7.1.3 Imparcialidade · 7.1.4 Honestidade · Apresentar comportamento ético no desenvolvimento das atividades sob sua responsabilidade

---

## Conteúdo

- Retomada da SA 21: *"Encerramos o bloco de técnicas de programação — hoje mudamos de perspectiva: saímos do código e entramos no comportamento profissional. Ética não é opcional na área de TI"*

- **O que é ética profissional:**
  - Conjunto de princípios e valores que orientam o comportamento de um profissional no exercício de sua função
  - Vai além de cumprir a lei: envolve fazer o que é correto mesmo quando ninguém está observando
  - Em TI, o desenvolvedor tem acesso a dados sensíveis, sistemas críticos e infraestruturas que afetam a vida de pessoas — a responsabilidade ética é proporcional a esse poder

- **Por que ética em TI tem peso especial:**
  - Desenvolvedores têm acesso a dados pessoais, financeiros e de saúde de usuários
  - Um bug mal tratado pode causar prejuízo financeiro ou danos à reputação de pessoas reais
  - Código malicioso ou negligente pode afetar milhares de usuários simultaneamente
  - A confiança entre cliente e desenvolvedor é a base de qualquer relação profissional em TI

- **Princípio 1 — Sigilo:**
  - O desenvolvedor tem acesso a informações confidenciais: código-fonte proprietário, dados de clientes, senhas, estratégias de negócio
  - Sigilo significa não compartilhar, não divulgar e não usar essas informações fora do contexto profissional
  - Exemplos de violação de sigilo: comentar dados de clientes em redes sociais · compartilhar código proprietário com concorrentes · acessar dados de usuários sem necessidade técnica
  - Base legal: LGPD (Lei Geral de Proteção de Dados) · contratos de confidencialidade (NDA)

- **Princípio 2 — Prudência:**
  - Agir com cuidado e responsabilidade antes de tomar decisões técnicas que possam ter consequências
  - Em TI: testar antes de colocar em produção · fazer backup antes de alterar banco de dados · revisar código antes de aprovar · comunicar riscos ao gestor antes de implementar
  - Imprudência em TI pode causar: perda de dados · indisponibilidade de sistema · vazamento de informações
  - Exemplo: executar DELETE sem WHERE em banco de produção sem backup — falta grave de prudência

- **Princípio 3 — Imparcialidade:**
  - Tomar decisões técnicas com base em critérios objetivos, não em preferências pessoais ou interesses particulares
  - Exemplos: escolher a tecnologia mais adequada para o projeto, não a que o desenvolvedor prefere pessoalmente · avaliar o código de um colega com os mesmos critérios que avalia o próprio · reportar um bug mesmo que tenha sido introduzido por você mesmo
  - No trabalho em equipe: feedback técnico honesto e construtivo sem favoritismo

- **Princípio 4 — Honestidade:**
  - Ser transparente sobre o que sabe e o que não sabe · sobre prazos reais · sobre erros cometidos
  - Exemplos de desonestidade em TI: afirmar que uma funcionalidade está pronta quando não está · esconder um bug descoberto · estimar prazo de 2 dias sabendo que levará 2 semanas · atribuir trabalho alheio como próprio
  - Honestidade constrói reputação — desonestidade destrói carreiras

- **Dilemas éticos reais em TI:**

  | Situação | Conduta antiética | Conduta ética |
  |----------|------------------|---------------|
  | Encontrou bug crítico no código de um colega próximo | Não reportar para não expor o colega | Reportar ao líder técnico com tom construtivo |
  | Cliente pediu funcionalidade que viola privacidade de usuários | Implementar porque o cliente pagou | Alertar o cliente sobre os riscos legais e recusar se necessário |
  | Prazo impossível de cumprir com qualidade | Prometer e entregar com bugs | Negociar prazo ou escopo com transparência |
  | Acesso acidental a dados pessoais de usuários | Guardar os dados por curiosidade | Ignorar e reportar o acesso acidental ao responsável |
  | Sistema em produção com falha descoberta às 23h | Ignorar e resolver amanhã (impacta usuários) | Comunicar o gestor e avaliar se é necessário intervenção imediata |

- **LGPD e responsabilidade do desenvolvedor:**
  - Lei nº 13.709/2018 — regula o tratamento de dados pessoais no Brasil
  - O desenvolvedor que implementa um sistema que viola a LGPD pode ser responsabilizado
  - Princípios da LGPD que o desenvolvedor deve conhecer: finalidade, necessidade, segurança e transparência no uso de dados

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização: *"Hoje saímos do código por um momento. Vocês vão trabalhar com dados de pessoas reais, sistemas críticos e informações confidenciais — precisamos falar sobre ética"* |
| Retomada | Professor apresenta um caso real (anonimizado) de vazamento de dados causado por negligência de desenvolvedor · pergunta: *"O que o desenvolvedor deveria ter feito diferente?"* — alunos debatem livremente |
| Explicação | Slides — o que é ética profissional, por que TI tem peso especial, os quatro princípios (sigilo, prudência, imparcialidade, honestidade) com exemplos práticos, dilemas éticos reais, LGPD e responsabilidade do desenvolvedor |
| Dinâmica | "O Que Você Faria?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: sigilo protege dados e confiança · prudência evita danos · imparcialidade garante decisões justas · honestidade constrói reputação · ética em TI tem consequências legais reais · Próxima SA: Trabalho e Profissionalismo |

---

## Dinâmica — "O Que Você Faria?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver o raciocínio ético aplicado ao contexto de TI por meio da análise e debate de dilemas profissionais reais — construindo a capacidade de identificar a conduta ética adequada em situações ambíguas que o desenvolvedor encontrará no mercado de trabalho.

**Materiais:** slide com os dilemas projetados · ficha de análise impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do dilema** *(1 min por rodada)*
O professor lê um dilema ético em voz alta e projeta no slide. Cada grupo tem 2 minutos para decidir: qual a conduta ética correta · qual princípio está em jogo · o que poderia acontecer se a conduta antiética fosse adotada.

2. **Debate em grupo** *(8 min)*
Os grupos discutem e registram suas respostas na ficha.

3. **Plenária** *(6 min)*
Cada grupo apresenta sua conclusão para um dilema. O professor media o debate, apresenta diferentes perspectivas e conecta cada situação com os princípios estudados.

**Dilemas sugeridos:**

| Dilema | Princípio em jogo | Conduta ética esperada |
|--------|------------------|------------------------|
| Você encontrou a senha do banco de dados de produção anotada em um post-it na mesa do gestor. O que faz? | Sigilo · Prudência | Alertar o gestor sobre o risco de segurança e sugerir que a senha seja trocada e armazenada com segurança |
| Seu líder pediu para você estimar quanto tempo levará uma funcionalidade complexa. Você sabe que são 3 semanas, mas ele claramente quer ouvir "1 semana". O que faz? | Honestidade | Comunicar o prazo real com justificativa técnica — prazo irreal gera dívida técnica e frustração |
| Você percebeu que o sistema que está desenvolvendo coleta dados de localização dos usuários sem informá-los. O que faz? | Sigilo · Honestidade · LGPD | Alertar o gestor e o cliente sobre a violação da LGPD — não implementar sem o consentimento do usuário |
| Um colega pediu para você dar merge no código dele "rapidinho" sem revisar porque está com pressa. O que faz? | Prudência · Imparcialidade | Negar a aprovação sem revisão — código não revisado em produção é risco técnico e ético |
| Você descobriu que um sistema antigo da empresa tem uma vulnerabilidade grave que ainda não foi explorada. O que faz? | Prudência · Honestidade | Reportar imediatamente ao responsável de segurança — não esperar o incidente acontecer |

> **Nota:** não existe uma única resposta "certa" para todos os dilemas — o objetivo é o debate e a construção do raciocínio ético. Reforçar que no mercado de trabalho, a capacidade de identificar dilemas éticos e agir corretamente é tão valorizada quanto a competência técnica. Empresas sérias demitem por conduta antiética independentemente do nível técnico do profissional.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 21 — 08/07/2026 · Técnicas de Programação — Teste Unitário Parte 2 |
| Próxima SA → | SA 23 — 05/08/2026 · Trabalho e Profissionalismo |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Ficha de análise dos dilemas impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
