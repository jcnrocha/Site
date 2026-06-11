# UC: Programação de Aplicativos
## SA 29 — 3º Trimestre

---

## Tema

Modelagem de Negócios — Canvas Aplicado a Sistemas

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Aplicar o Business Model Canvas para modelar um produto de software do zero
- Descrever a proposta de valor de um aplicativo de forma clara e orientada ao usuário
- Identificar segmentos de clientes e canais adequados para um sistema de software
- Mapear fontes de receita viáveis para diferentes tipos de aplicativos
- Conectar as decisões do Canvas com escolhas técnicas de desenvolvimento do sistema

**Capacidades da matriz:** 10.1 Canvas · Aplicar os princípios de organização do trabalho no planejamento e exercício das atividades profissionais · Capacidades socioemocionais: organização e planejamento

---

## Conteúdo

- Retomada da SA 28: *"Na SA passada conhecemos os 9 blocos do Canvas — hoje aplicamos na prática para modelar um produto de software do zero, como será feito no Projeto Final"*

- **Do problema à proposta de valor:**
  - O ponto de partida de qualquer produto de software é um problema real de um grupo específico de pessoas
  - Canvas não começa pelo produto — começa pelo cliente e pelo problema que ele tem
  - Sequência correta de raciocínio:
    1. Quem é o cliente? (Segmento de Clientes)
    2. Qual problema ele tem? (base da Proposta de Valor)
    3. Como o sistema resolve esse problema? (Proposta de Valor)
    4. Como o sistema chega até ele? (Canais)
    5. Como sustenta financeiramente? (Fontes de Receita)

- **Proposta de valor — o bloco mais importante:**
  - Responde: *"Por que o cliente usaria este sistema e não outro?"*
  - Deve ser específica, clara e orientada ao benefício — não à funcionalidade
  - Diferença entre funcionalidade e proposta de valor:

  | Funcionalidade (o que faz) | Proposta de Valor (benefício real) |
  |---------------------------|-----------------------------------|
  | Cadastro de tarefas | Nunca mais esquecer um compromisso importante |
  | Relatório de vendas | Tomar decisões de negócio com dados reais em segundos |
  | Sistema de agendamento | Eliminar ligações telefônicas e reduzir faltas em consultas |
  | Controle de estoque | Nunca perder uma venda por falta de produto |

- **Segmentos de clientes em sistemas de software:**
  - Sistemas podem atender múltiplos segmentos com necessidades diferentes — cada um precisa ser descrito
  - Tipos comuns:
    - **B2C (Business to Consumer):** o sistema serve diretamente o consumidor final (ex: app de delivery)
    - **B2B (Business to Business):** o sistema serve outras empresas (ex: sistema de gestão para clínicas)
    - **B2B2C:** o sistema serve empresas que servem consumidores (ex: plataforma de e-commerce)
    - **Plataforma multilateral:** serve dois ou mais grupos interdependentes (ex: marketplace: vendedores e compradores)

- **Fontes de receita para sistemas de software:**

  | Modelo | Descrição | Exemplo |
  |--------|-----------|---------|
  | **SaaS (assinatura)** | Pagamento recorrente pelo acesso ao sistema | Spotify, Netflix, GitHub Pro |
  | **Freemium** | Versão gratuita com recursos limitados · versão paga com recursos completos | Trello, Notion, Canva |
  | **Por transação** | Cobrança sobre cada operação realizada | iFood (comissão por pedido), Mercado Pago |
  | **Licença** | Pagamento único pelo direito de uso | Microsoft Office (versão perpétua) |
  | **Publicidade** | Receita de anunciantes que pagam para exibir anúncios | Google, YouTube gratuito |
  | **Marketplace** | Comissão sobre transações entre compradores e vendedores | Airbnb, Uber, Etsy |

- **Canvas de um sistema de software — exemplo completo:**

  **Sistema:** aplicativo de controle financeiro pessoal

  | Bloco | Conteúdo |
  |-------|----------|
  | Segmentos | Jovens adultos (18–35 anos) que não controlam os próprios gastos |
  | Proposta de Valor | Entender para onde vai o dinheiro e parar de terminar o mês no negativo |
  | Canais | App mobile (iOS e Android) · notificações push · redes sociais |
  | Relacionamento | Self-service · tutoriais no app · comunidade online |
  | Fontes de Receita | Freemium: versão gratuita com limite de lançamentos · assinatura premium R$14,90/mês |
  | Recursos Principais | App mobile · banco de dados de transações · algoritmo de categorização |
  | Atividades-Chave | Desenvolver e manter o app · suporte · marketing de conteúdo financeiro |
  | Parcerias | Bancos e fintechs (integração via Open Finance) · lojas de apps |
  | Estrutura de Custos | Desenvolvimento · infraestrutura em nuvem · marketing · suporte |

- **Decisões técnicas influenciadas pelo Canvas:**
  - **Segmento jovem mobile-first** → priorizar app mobile responsivo, não sistema desktop
  - **Fonte de receita freemium** → sistema deve ter controle de plano e bloqueio de funcionalidades premium
  - **Parceria com bancos via Open Finance** → necessidade de integração com APIs externas
  - **Self-service como relacionamento** → interface deve ser intuitiva sem necessidade de treinamento
  - O Canvas evita decisões técnicas desconectadas do negócio — cada escolha de arquitetura tem uma razão de negócio por trás

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 28: *"Conhecemos os 9 blocos — hoje preenchemos um Canvas completo para um sistema de software e conectamos cada bloco com decisões técnicas reais"* |
| Retomada | Professor pergunta: *"Se vocês fossem criar um aplicativo amanhã, qual problema resolveriam? Para quem?"* — cada aluno responde em 30 segundos · professor usa as respostas para mostrar que todo mundo já pensa em Canvas naturalmente, só não sabia o nome |
| Explicação | Slides — do problema à proposta de valor, diferença entre funcionalidade e valor, segmentos B2C/B2B/multilateral, modelos de receita para software, Canvas completo do app financeiro, decisões técnicas influenciadas pelo Canvas · apresentação do briefing do Projeto Final |
| Dinâmica | "Canvas ao Vivo" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: Canvas começa pelo cliente e pelo problema · proposta de valor é o benefício, não a funcionalidade · modelo de receita define a arquitetura · Canvas conecta negócio e tecnologia · Próxima SA: consolidação e revisão geral |

---

## Dinâmica — "Canvas ao Vivo"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** criar um Canvas completo para um sistema de software proposto pelo próprio grupo — desenvolvendo o raciocínio integrado de negócio e tecnologia que será usado diretamente no Projeto Final das SAs 33 a 38.

**Materiais:** ficha do Canvas em branco impressa (1 por grupo) · post-its ou canetas coloridas · quadro branco ou parede para fixar os Canvas.

**Passo a passo:**

1. **Escolha do sistema** *(1 min)*
Cada grupo escolhe um tipo de sistema simples para modelar. O professor sugere opções caso o grupo não tenha ideia própria.

2. **Preenchimento do Canvas** *(9 min)*
Os grupos preenchem os 9 blocos do Canvas para o sistema escolhido, começando sempre pelo Segmento de Clientes e pela Proposta de Valor.

3. **Apresentação rápida** *(5 min)*
Cada grupo apresenta em 1 minuto: quem é o cliente, qual o problema resolvido e como o sistema gera receita. Professor faz uma pergunta desafiadora para cada grupo.

**Sistemas sugeridos para a dinâmica:**

| Sistema | Público sugerido |
|---------|-----------------|
| App de agendamento de serviços (cabelereiro, dentista) | B2C e B2B |
| Sistema de controle de estoque para pequeno comércio | B2B |
| Plataforma de caronas entre alunos de faculdade | B2C multilateral |
| App de gestão de tarefas domésticas em família | B2C |
| Sistema de reserva de quadras esportivas | B2C e B2B |

> **Nota:** reforçar que este exercício é um ensaio do Projeto Final — os grupos que se saírem bem aqui terão muito mais facilidade nas SAs 33 a 38. Encorajar os alunos a escolher um sistema que realmente gostariam de construir — a motivação pelo tema faz diferença na qualidade do projeto entregue.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 28 — 09/09/2026 · Modelagem de Negócios — Introdução ao Canvas |
| Próxima SA → | SA 30 — 23/09/2026 · Consolidação — Ambiente, Ferramentas e Programação Estruturada |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Ficha do Canvas em branco impressa (1 por grupo)
- Post-its coloridos ou canetas coloridas para preenchimento visual
- Quadro branco e marcador

---

## Observações do Professor
