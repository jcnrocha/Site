# UC: Programação de Aplicativos
## SA 28 — 3º Trimestre

---

## Tema

Modelagem de Negócios — Introdução ao Canvas

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o que é o Business Model Canvas e qual a sua origem e finalidade
- Identificar e descrever os 9 blocos do Canvas e a relação entre eles
- Reconhecer como o Canvas é utilizado no contexto de projetos de desenvolvimento de software
- Relacionar cada bloco do Canvas com decisões técnicas e de produto em um sistema
- Iniciar o preenchimento de um Canvas simples a partir de um produto de software conhecido

**Capacidades da matriz:** 10. Modelagem de Negócios · 10.1 Canvas · Aplicar os princípios de organização do trabalho no planejamento e exercício das atividades profissionais

---

## Conteúdo

- Retomada da SA 27: *"Encerramos Gestão da Qualidade — hoje abrimos o último bloco de conteúdo da UC: Modelagem de Negócios com o Canvas, que vai ser a base do Projeto Final"*

- **O que é o Business Model Canvas:**
  - Ferramenta visual criada por Alexander Osterwalder em 2010 para descrever, analisar e projetar modelos de negócio
  - Apresentado em uma única página dividida em 9 blocos — visão completa do negócio de forma rápida e clara
  - Usado por startups, empresas consolidadas e times de desenvolvimento de produto
  - Em TI: o Canvas ajuda o desenvolvedor a entender para quem está desenvolvendo, qual problema está resolvendo e como o produto gera valor — evita construir o sistema errado para o cliente certo

- **Os 9 blocos do Business Model Canvas:**

  | Bloco | Pergunta central | Descrição |
  |-------|-----------------|-----------|
  | **1. Segmentos de Clientes** | Para quem criamos valor? | Define os grupos de pessoas ou organizações que o produto atende |
  | **2. Proposta de Valor** | Que valor entregamos? | Descreve o problema que o produto resolve e o benefício que oferece |
  | **3. Canais** | Como chegamos ao cliente? | Formas de comunicar e entregar a proposta de valor (app, site, loja) |
  | **4. Relacionamento com Clientes** | Como nos relacionamos? | Tipo de interação com o cliente (suporte, self-service, comunidade) |
  | **5. Fontes de Receita** | Como geramos receita? | Como o produto ganha dinheiro (assinatura, venda, publicidade) |
  | **6. Recursos Principais** | O que precisamos para operar? | Ativos essenciais: infraestrutura, equipe, tecnologia, dados |
  | **7. Atividades-Chave** | O que fazemos de essencial? | Ações mais importantes para entregar a proposta de valor |
  | **8. Parcerias Principais** | Quem nos ajuda? | Fornecedores e parceiros estratégicos |
  | **9. Estrutura de Custos** | Quais são nossos custos? | Principais gastos para operar o modelo de negócio |

- **Estrutura visual do Canvas:**

  ```
  +------------------+----------+-------------------+----------+-------------------+
  |  8. Parcerias    |  7. Ativ.|  2. Proposta      |  4. Rel. |  1. Segmentos     |
  |  Principais      |  Chave   |  de Valor         |  Cliente |  de Clientes      |
  |                  +----------+                   +----------+                   |
  |                  |  6. Rec. |                   |  3.      |                   |
  |                  |  Princ.  |                   |  Canais  |                   |
  +------------------+----------+-------------------+----------+-------------------+
  |       9. Estrutura de Custos          |        5. Fontes de Receita            |
  +---------------------------------------+----------------------------------------+
  ```

- **Canvas aplicado a um sistema de software — exemplo iFood:**

  | Bloco | iFood |
  |-------|-------|
  | Segmentos de Clientes | Consumidores famintos · restaurantes · entregadores |
  | Proposta de Valor | Pedir comida de qualquer restaurante sem sair de casa |
  | Canais | Aplicativo mobile · site · notificações push |
  | Relacionamento | App self-service · suporte por chat · avaliações |
  | Fontes de Receita | Comissão por pedido · taxa de entrega · anúncios |
  | Recursos Principais | Plataforma tecnológica · base de dados · marca |
  | Atividades-Chave | Desenvolver e manter o app · logística de entrega · aquisição de parceiros |
  | Parcerias | Restaurantes · entregadores autônomos · meios de pagamento |
  | Estrutura de Custos | Desenvolvimento · infraestrutura · marketing · suporte |

- **Por que o desenvolvedor precisa entender o Canvas:**
  - Desenvolvedor que entende o modelo de negócio toma decisões técnicas melhores
  - Exemplo: saber que a fonte de receita é assinatura mensal influencia como o sistema de pagamento é arquitetado
  - Exemplo: saber que o segmento de clientes são idosos influencia o design da interface
  - Canvas evita o maior desperdício em TI: construir a coisa certa de forma errada — ou a coisa errada de forma perfeita

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização: *"Chegamos ao último bloco da UC — Canvas e Projeto Final. O Canvas é a ferramenta que vai guiar o projeto que vamos construir juntos até o encerramento do ano"* |
| Retomada | Professor pergunta: *"Quando vocês pensam em criar um aplicativo, o que vem primeiro na cabeça? A ideia? O código? O usuário? O dinheiro?"* — alunos respondem · professor mostra que o Canvas organiza todas essas respostas em um único lugar antes de escrever uma linha de código |
| Explicação | Slides — o que é o Canvas, origem, os 9 blocos com descrição e perguntas centrais, estrutura visual, exemplo do iFood preenchido, por que o desenvolvedor precisa entender o Canvas · apresentação do Projeto Final que será construído nas próximas SAs |
| Dinâmica | "Decifra o Canvas" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: Canvas descreve o modelo de negócio em 9 blocos em uma página · proposta de valor é o coração · segmento de clientes define para quem · fontes de receita sustentam o negócio · Próxima SA: Canvas aplicado a sistemas |

---

## Dinâmica — "Decifra o Canvas"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar os 9 blocos do Canvas por meio do mapeamento de informações de aplicativos conhecidos — desenvolvendo a capacidade de leitura e interpretação de modelos de negócio, habilidade essencial para o Projeto Final das SAs seguintes.

**Materiais:** slide com os aplicativos e informações embaralhadas projetado · ficha do Canvas impressa em branco (1 por grupo).

**Passo a passo:**

1. **Apresentação do aplicativo** *(1 min)*
O professor projeta o nome de um aplicativo conhecido e uma lista de informações embaralhadas sobre ele. O grupo deve distribuir cada informação no bloco correto do Canvas.

2. **Preenchimento em grupo** *(9 min)*
Os grupos preenchem a ficha do Canvas com as informações fornecidas, discutindo em qual bloco cada item se encaixa melhor.

3. **Comparação e debate** *(5 min)*
Os grupos apresentam seus Canvas. O professor compara as diferentes interpretações e discute os casos onde a mesma informação poderia se encaixar em mais de um bloco.

**Aplicativo sugerido — Spotify:**

*Informações embaralhadas para distribuir nos blocos:*
- Ouvintes de música em todo o mundo
- Artistas e gravadoras independentes
- Acesso a milhões de músicas sem precisar comprá-las individualmente
- Aplicativo mobile e desktop
- Recomendações personalizadas com algoritmo
- Assinatura premium mensal
- Publicidade para usuários gratuitos
- Acordos com gravadoras e distribuidoras
- Infraestrutura de streaming em nuvem
- Desenvolver e manter plataforma de streaming
- Curadoria de playlists e algoritmos de recomendação
- Custo de licenciamento de músicas
- Infraestrutura de servidores

> **Nota:** reforçar que não existe uma única resposta completamente certa para o Canvas — o objetivo é o raciocínio de negócio, não a memorização. Diferentes interpretações são válidas desde que bem justificadas. O Canvas é uma ferramenta de comunicação e alinhamento, não um formulário burocrático — e é exatamente assim que será usado no Projeto Final.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 27 — 02/09/2026 · Gestão da Qualidade — Controle e Registro |
| Próxima SA → | SA 29 — 16/09/2026 · Modelagem de Negócios — Canvas Aplicado a Sistemas |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Ficha do Canvas em branco impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
