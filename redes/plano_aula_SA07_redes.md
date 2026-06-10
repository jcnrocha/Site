# UC: Fundamentos de Redes de Computadores
## Aula 07 — 1º Trimestre

---

## Tema

Componentes de Rede — Hardware Passivo

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são componentes passivos de rede e qual é o seu papel na infraestrutura física de uma rede
- Identificar os principais tipos de cabos de rede: par trançado (categorias), fibra óptica e cabo coaxial
- Reconhecer os conectores mais comuns: RJ-45, RJ-11, SC e LC
- Identificar os componentes de organização física: patch panel, rack e organizador de cabos
- Relacionar cada componente passivo com sua função dentro da infraestrutura de cabeamento estruturado

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes

---

## Conteúdo

- Retomada rápida das Aulas 05 e 06: *"Vimos como representar os equipamentos em diagramas — hoje vamos conhecer os componentes físicos que ficam por baixo desses diagramas: os cabos, conectores e organizadores que formam a infraestrutura da rede"*
- **O que são componentes passivos de rede?**
  - Componentes passivos são elementos da infraestrutura de rede que não processam dados — eles apenas transportam, organizam ou terminam os sinais
  - Não precisam de energia elétrica para funcionar (com exceção de alguns painéis iluminados)
  - São a base física da rede — sem eles, nenhum componente ativo (switch, roteador, servidor) consegue se comunicar
  - Exemplos: cabos, conectores, patch panel, rack, organizadores de cabo

- **Cabos de Rede:**

  - **Par Trançado (Twisted Pair)**
    - O tipo de cabo mais usado em redes locais (LANs)
    - Composto de 4 pares de fios de cobre trançados entre si — o trançamento cancela interferências eletromagnéticas (crosstalk)
    - **Tipos por blindagem:**
      - **UTP (Unshielded Twisted Pair):** sem blindagem · mais barato · uso doméstico e corporativo geral
      - **STP (Shielded Twisted Pair):** blindagem individual por par · ambientes com interferência moderada
      - **FTP (Foiled Twisted Pair):** blindagem global por folha metálica · ambientes industriais
    - **Categorias (determinam velocidade e distância máxima):**

    | Categoria | Velocidade Máxima | Distância Máxima | Uso Típico |
    |-----------|------------------|-----------------|-----------|
    | Cat5e | 1 Gbps | 100 metros | Redes domésticas e pequenas empresas |
    | Cat6 | 10 Gbps | 55 metros | Escritórios e redes corporativas |
    | Cat6A | 10 Gbps | 100 metros | Data centers e ambientes de alta demanda |
    | Cat7 | 10 Gbps | 100 metros | Ambientes industriais — blindagem total |
    | Cat8 | 40 Gbps | 30 metros | Data centers de alta performance |

    - **Conector padrão:** RJ-45 — 8 pinos · encaixa em placas de rede, switches, roteadores e patch panels
    - **Padrões de crimpagem:** EIA/TIA-568A e 568B — definem a ordem das cores dos fios no conector

  - **Fibra Óptica**
    - Transmite dados por pulsos de luz em vez de sinais elétricos
    - **Monomodo (SMF — Single Mode Fiber):**
      - Núcleo estreito (~9 µm) · transmite um único raio de luz
      - Longas distâncias: dezenas de quilômetros
      - Altíssima velocidade · uso: backbones de operadoras, conexões entre prédios distantes
    - **Multimodo (MMF — Multi Mode Fiber):**
      - Núcleo mais largo (~50–62,5 µm) · transmite múltiplos raios de luz
      - Curtas distâncias: até ~500 metros
      - Alta velocidade · uso: data centers, conexões entre andares do mesmo prédio
    - **Vantagens da fibra:** imunidade total a interferências eletromagnéticas · altíssima velocidade · longa distância · sinal mais seguro (difícil interceptação)
    - **Desvantagens:** custo mais alto · instalação mais delicada · emendas exigem equipamento especializado

  - **Cabo Coaxial**
    - Estrutura em camadas: condutor central de cobre → isolante dielétrico → malha metálica → capa externa
    - Tipos comuns:
      - **RG-6:** cabo de TV a cabo e internet DOCSIS
      - **RG-58:** redes antigas (10Base2 — Thin Ethernet) — praticamente obsoleto em LANs
    - Uso atual: distribuição de TV a cabo, internet HFC, câmeras de segurança analógicas (CFTV), antenas
    - Praticamente obsoleto para LANs modernas — substituído pelo par trançado

- **Conectores de Rede:**

  - **RJ-45**
    - Conector padrão para cabo par trançado (UTP/STP/FTP)
    - 8 pinos · encaixa em switches, roteadores, placas de rede, patch panels e pontos de rede
    - Crimpagem: aplica o conector ao cabo usando uma ferramenta chamada alicate de crimpar
    - Padrão de cores: seguir TIA-568B (mais comum no Brasil) ou TIA-568A

  - **RJ-11**
    - Conector para linha telefônica — menor que o RJ-45 (6 pinos, usa apenas 2 ou 4)
    - Usado em conexões ADSL (modem → linha telefônica)
    - Não confundir com RJ-45 — são incompatíveis fisicamente

  - **SC (Subscriber Connector)**
    - Conector de fibra óptica quadrado com mecanismo de pressão (push-pull)
    - Uso: patch panels de fibra, ODF (Distribuidor de Fibra Óptica), equipamentos de rede de fibra
    - Vantagem: fácil de conectar e desconectar

  - **LC (Lucent Connector)**
    - Conector de fibra óptica pequeno com trava de pressão — metade do tamanho do SC
    - Uso: switches de data center, transceivers SFP, equipamentos de alta densidade
    - Padrão atual preferido em novos projetos de fibra por ser mais compacto

  - **ST (Straight Tip)**
    - Conector de fibra óptica cilíndrico com trava de baioneta (torção para travar)
    - Uso: instalações antigas de fibra óptica — ainda encontrado em ambientes legados

- **Componentes de Organização Física:**

  - **Rack (Armário de Rede)**
    - Estrutura metálica padronizada que organiza verticalmente os equipamentos de rede e servidores
    - **Unidade de medida:** U (Unit) = 1,75 polegadas de altura · um servidor ocupa 1U, 2U ou 4U
    - Tamanhos comuns: 12U (rack de parede pequeno), 24U, 42U (rack de piso padrão)
    - Tipos: rack de parede (wall mount) para ambientes menores · rack de piso (floor mount) para data centers
    - Componentes típicos dentro do rack: switches, patch panels, servidores, no-breaks (UPS), organizadores de cabo

  - **Patch Panel**
    - Painel de conexões que termina o cabeamento horizontal (que vem dos pontos de rede das salas)
    - Organiza todas as conexões de cabeamento em um único ponto no rack
    - Portas frontais: conectam ao switch via patch cord · portas traseiras: terminam o cabeamento horizontal
    - Vantagens: organização, documentação, flexibilidade (mover uma conexão sem mexer no cabeamento fixo)
    - Tamanhos: 24 portas, 48 portas — padronizados para encaixar no rack (1U ou 2U)

  - **Patch Cord**
    - Cabo curto com conectores RJ-45 em ambas as extremidades (ou LC-LC para fibra)
    - Conecta: patch panel → switch · switch → servidor · ponto de rede → computador do usuário
    - Cores diferentes para facilitar a identificação: azul (dados), amarelo (uplinks), vermelho (links críticos)
    - Comprimentos típicos: 0,5 m, 1 m, 2 m, 3 m, 5 m

  - **Organizador de Cabos (Cable Manager)**
    - Componente do rack que guia e organiza os patch cords horizontalmente ou verticalmente
    - Evita o "espaguete de cabos" que dificulta a manutenção e causa confusão
    - Tipos: organizador horizontal (1U, entre switches e patch panels) · organizador vertical (lateral do rack)

  - **Ponto de Rede (Tomada de Rede / Jack)**
    - Tomada instalada na parede onde o usuário conecta o cabo patch cord do seu dispositivo
    - Conector fêmea RJ-45 ou LC (fibra) instalado em caixa de tomada padrão
    - Termina o cabeamento horizontal que vai até o patch panel no rack
    - Identificação: cada ponto deve ser etiquetado com código único (ex.: P01, P02) correspondente à porta do patch panel

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada das Aulas 05 e 06: *"Vimos os símbolos — hoje vamos tocar nos componentes reais que ficam por trás desses símbolos"* |
| Retomada | Professor mostra (ao vivo ou em foto) um cabo UTP, um conector RJ-45 e um patch panel e pergunta: *"Alguém sabe o nome desses componentes? Alguém já viu isso antes? Onde?"* — alunos respondem livremente |
| Explicação | Slides — o que são componentes passivos, cabos (par trançado com categorias, fibra monomodo/multimodo, coaxial), conectores (RJ-45, RJ-11, SC, LC, ST), rack, patch panel, patch cord, organizador de cabos, ponto de rede |
| Dinâmica | "Identifique o Componente!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: passivos = cabos + conectores + organização · RJ-45 para par trançado · LC/SC para fibra · patch panel organiza · rack abriga · Próxima aula: Componentes Ativos e Interfaces |

---

## Dinâmica — "Identifique o Componente!"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar o reconhecimento dos componentes passivos de rede por meio de descrições e situações reais, desenvolvendo a capacidade de identificar e especificar corretamente os componentes físicos de uma rede — habilidade essencial para técnicos de suporte, técnicos de redes e desenvolvedores que trabalham com infraestrutura.

**Materiais:** cartões com descrições ou situações — um conjunto por grupo · ou slide com as situações projetadas · se possível: amostras físicas dos componentes para manuseio.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com descrições de componentes ou situações de uso. O desafio é: identificar o componente descrito, nomear corretamente e indicar sua função na rede.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica o componente, descreve sua função e indica onde ele apareceria em um diagrama de rede ou em uma instalação real.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça as características de cada componente.

**Situações sugeridas:**

| Descrição / Situação | Componente | O que reforçar |
|---------------------|------------|----------------|
| "Preciso conectar 30 computadores em uma sala de aula a um switch central com cabo — qual cabo e conector usar?" | Cat6 UTP com conector RJ-45 | Cat6 é adequado para escritórios · RJ-45 é o conector padrão do par trançado |
| "Quero interligar dois prédios separados por 300 metros com alta velocidade e sem interferência elétrica" | Fibra óptica multimodo com conectores LC ou SC | Fibra para longas distâncias e imunidade a EMI · multimodo para ~300 m |
| "O técnico instalou todos os cabos das salas mas eles terminam de forma desorganizada no armário de rede" | Patch panel + organizador de cabos | Patch panel termina e organiza o cabeamento horizontal · organizador evita o espaguete |
| "O usuário conecta o notebook diretamente na tomada da parede usando um cabo curto com RJ-45 em ambas as pontas" | Patch cord / cabo patch | Cabo de conexão entre o ponto de rede e o dispositivo do usuário |
| "Preciso instalar câmeras de segurança analógicas (CFTV) em um galpão industrial" | Cabo coaxial RG-6 | Coaxial é o padrão para CFTV analógico · resistente a interferências mecânicas |
| "O armário de rede tem 42U de altura e abriga switches, patch panels e servidores organizados verticalmente" | Rack de piso (42U) | Rack organiza todos os equipamentos ativos e passivos em um único ponto físico |
| "Estou crimpando um conector no cabo de rede mas o conector tem apenas 6 pinos em vez de 8" | RJ-11 (errado para rede) — deveria ser RJ-45 | RJ-11 é para telefone · RJ-45 é para rede · são fisicamente similares mas incompatíveis |
| "O data center usa switches de alta densidade com transceivers SFP para conectar servidores por fibra" | Conectores LC (fibra) nos transceivers SFP | LC é o padrão atual em data centers por ser compacto · encaixa nos módulos SFP dos switches |

> **Nota:** se possível, levar para a aula amostras físicas dos componentes (um cabo UTP, um conector RJ-45, um patch cord, um pedaço de fibra com conector SC ou LC). O contato físico com os componentes acelera muito o aprendizado e torna a aula muito mais memorável. Muitos alunos nunca viram esses componentes de perto.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 06 — 25/03/2026 · Simbologias Básicas de Rede — Parte 2 |
| Próxima aula → | Aula 08 — 08/04/2026 · Componentes de Rede — Ativos e Interfaces |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — com fotos reais dos componentes em tamanho grande
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- **Fortemente recomendado:** amostras físicas para manuseio — cabo UTP Cat5e ou Cat6, conector RJ-45, patch cord, patch panel (mesmo que apenas o frontal), e se possível um pequeno trecho de fibra óptica com conector SC ou LC

---

## Observações do Professor
