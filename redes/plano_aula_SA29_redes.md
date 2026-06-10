# UC: Fundamentos de Redes de Computadores
## Aula 29 — 3º Trimestre

---

## Tema

Topologias de Rede — Física e Lógica

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é a topologia de rede e por que ela é um elemento fundamental no projeto de infraestrutura
- Identificar e diferenciar as principais topologias físicas: Barramento, Anel, Estrela, Malha e Híbrida
- Distinguir topologia física de topologia lógica — entendendo que a forma como os cabos estão dispostos pode ser diferente de como os dados trafegam
- Reconhecer as vantagens e desvantagens de cada topologia para aplicação em cenários reais
- Relacionar a escolha da topologia com os critérios de custo, escalabilidade, tolerância a falhas e desempenho do Projeto Integrador

**Habilidade da matriz:** H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 28: *"Classificamos as redes por abrangência — PAN, LAN, MAN, WAN e GAN. Hoje vamos entender como essas redes são estruturadas internamente"*
- **O que é topologia de rede?**
  - Topologia é a forma como os dispositivos de uma rede estão organizados e interconectados entre si
  - Define o caminho que os dados percorrem de um dispositivo ao outro
  - Impacta diretamente: custo de instalação, facilidade de manutenção, escalabilidade e tolerância a falhas
- **Topologia Física × Topologia Lógica**
  - **Topologia Física:** como os cabos e dispositivos estão fisicamente dispostos e conectados no ambiente
  - **Topologia Lógica:** como os dados efetivamente trafegam pela rede — o caminho lógico dos pacotes
  - Exemplo clássico: uma rede com topologia física Estrela (todos os cabos vão ao switch) pode ter topologia lógica de Barramento (dados transmitidos para todos os dispositivos simultaneamente em redes antigas com hub)

- **Topologia Barramento (Bus)**
  - Todos os dispositivos conectados a um único cabo central (o "barramento")
  - Dados transmitidos para todos os dispositivos — apenas o destinatário processa a mensagem
  - Terminadores nas extremidades do cabo para evitar reflexão do sinal
  - **Vantagens:** simples de instalar · baixo custo de cabeamento
  - **Desvantagens:** falha no cabo central derruba toda a rede · difícil diagnóstico de problemas · desempenho cai com muitos dispositivos · colisões frequentes
  - **Status atual:** praticamente obsoleta · usada apenas em redes legadas e em estudos históricos

- **Topologia Anel (Ring)**
  - Dispositivos conectados em série formando um anel fechado
  - Dados percorrem o anel em uma direção (ou nas duas — anel duplo)
  - Token Ring: protocolo que controla o acesso ao meio — apenas quem tem o "token" transmite
  - **Vantagens:** desempenho previsível · sem colisões (com token) · boa para redes de alta carga
  - **Desvantagens:** falha em um dispositivo ou cabo pode derrubar toda a rede (anel simples) · difícil adicionar ou remover dispositivos · mais complexa que o barramento
  - **Status atual:** praticamente obsoleta em LANs · conceito ainda usado em redes de fibra óptica metropolitanas (SONET/SDH)

- **Topologia Estrela (Star)**
  - Todos os dispositivos conectados a um ponto central — switch ou hub
  - Cada dispositivo tem seu próprio cabo dedicado ao switch
  - **Vantagens:** falha em um cabo ou dispositivo não afeta os demais · fácil diagnóstico e manutenção · simples de adicionar novos dispositivos · alto desempenho com switch
  - **Desvantagens:** falha no switch central derruba toda a rede · maior quantidade de cabo necessária · custo do switch central
  - **Status atual:** topologia padrão de LANs modernas — é o que você encontra em qualquer escritório, escola ou residência com switch

- **Topologia Malha (Mesh)**
  - Cada dispositivo conectado diretamente a múltiplos outros dispositivos
  - **Malha completa (Full Mesh):** cada dispositivo conectado a TODOS os outros
  - **Malha parcial (Partial Mesh):** dispositivos conectados a alguns outros — mais prático
  - **Vantagens:** altíssima redundância · múltiplos caminhos para os dados · tolerância máxima a falhas · sem ponto único de falha
  - **Desvantagens:** custo muito elevado · grande quantidade de cabos e interfaces · complexidade de gerenciamento · impraticável em LANs grandes
  - **Status atual:** usada em backbones de redes WAN, redes militares, infraestrutura crítica e redes de data centers de alta disponibilidade

- **Topologia Híbrida (Hybrid)**
  - Combinação de duas ou mais topologias em uma única rede
  - Mais comum: Estrela-Barramento (múltiplas estrelas conectadas por um barramento) ou Estrela-Malha (núcleo em malha, acesso em estrela)
  - **Vantagens:** flexibilidade · permite combinar as vantagens de cada topologia · adapta-se a diferentes necessidades de cada setor
  - **Desvantagens:** maior complexidade de projeto e gerenciamento · custo mais elevado
  - **Status atual:** a topologia mais usada em redes corporativas e campus universitários reais

- **Comparativo geral:**

| Topologia | Ponto de Falha | Custo | Escalabilidade | Desempenho | Uso Atual |
|-----------|---------------|-------|---------------|-----------|-----------|
| Barramento | Cabo central | Baixo | Baixa | Baixo | Obsoleta |
| Anel | Qualquer nó/cabo | Médio | Baixa | Médio | Obsoleta |
| Estrela | Switch central | Médio | Alta | Alto | Padrão LAN |
| Malha | Nenhum (full) | Alto | Baixa | Alto | WAN/DC |
| Híbrida | Variável | Alto | Alta | Alto | Corporativo |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 28: *"Classificamos as redes por abrangência — hoje vamos ver como elas são estruturadas por dentro"* |
| Retomada | Professor pergunta: *"Quando você conecta o notebook ao Wi-Fi em casa, todos os dispositivos estão ligados ao mesmo roteador. Isso lembra qual forma geométrica?"* — alunos respondem livremente · introduzir o conceito de topologia Estrela a partir da resposta |
| Explicação | Slides — o que é topologia, física × lógica, Barramento, Anel, Estrela, Malha, Híbrida (cada uma com diagrama, vantagens, desvantagens e status atual), comparativo geral |
| Dinâmica | "Qual Topologia É Essa?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: Estrela é o padrão atual de LAN · Malha para alta disponibilidade · Híbrida para redes corporativas complexas · Conexão com o Projeto Integrador: qual topologia o grupo vai usar? · Próxima aula: Modelos de Rede — Cliente-Servidor e Peer-to-Peer |

---

## Dinâmica — "Qual Topologia É Essa?"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** consolidar o reconhecimento das topologias de rede por meio de cenários e descrições reais, desenvolvendo o raciocínio de identificação e escolha de topologia — habilidade diretamente aplicada no Projeto Integrador, onde os alunos precisarão escolher e justificar a topologia da rede projetada.

**Materiais:** cartões com cenários e descrições — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários ou descrições de redes. O desafio é identificar qual topologia está sendo descrita e apontar a principal vantagem e o principal risco daquela topologia naquele cenário.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica a topologia, avalia se é a mais adequada para o cenário e propõe melhorias se necessário.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os critérios de escolha de topologia.

**Cenários sugeridos:**

| Cenário / Descrição | Topologia | Vantagem principal | Risco principal |
|--------------------|-----------|-------------------|----------------|
| Todos os computadores de um escritório conectados a um único switch central | Estrela | Isolamento de falhas — problema em um PC não afeta os outros | Falha no switch derruba toda a rede |
| Rede de um banco central interligando agências com múltiplos caminhos redundantes | Malha parcial | Alta redundância — se um link cair, o tráfego é redirecionado | Custo elevado de links e equipamentos |
| Computadores antigos conectados em série por um cabo coaxial compartilhado | Barramento | Baixo custo de cabeamento | Falha no cabo derruba todos os dispositivos |
| Uma rede universitária com vários prédios — cada prédio tem sua estrela interna, e os prédios são interligados entre si | Híbrida (Estrela-Estrela) | Flexibilidade e escalabilidade por setor | Maior complexidade de gerenciamento |
| Dispositivos industriais conectados em sequência, onde cada um retransmite o dado para o próximo | Anel | Controle de acesso ao meio sem colisões | Falha em um dispositivo pode interromper o anel |
| Roteadores de backbone da internet interligados com múltiplas conexões redundantes | Malha parcial | Tolerância a falhas máxima — a internet não tem ponto único de falha | Alta complexidade de roteamento |
| Empresa com sede e filiais — cada filial tem sua LAN em estrela, conectada à sede por link WAN | Híbrida (Estrela-WAN) | Organização por camadas — estrela local, WAN entre filiais | Dependência do link WAN para comunicação entre filiais |
| Rede doméstica com roteador Wi-Fi distribuindo sinal para celulares, notebooks e smart TVs | Estrela (sem fio) | Simples de instalar e gerenciar · fácil adicionar dispositivos | Falha no roteador derruba toda a rede doméstica |

> **Nota:** o objetivo é desenvolver o raciocínio: *"como os dispositivos estão conectados? Existe um ponto central? Os dados têm múltiplos caminhos? A topologia é adequada para o nível de disponibilidade exigido?"* Reforçar que no Projeto Integrador os grupos precisarão escolher e desenhar a topologia da rede — e justificar tecnicamente essa escolha.

---

## Conexão com o Projeto Integrador

Esta aula tem conexão direta com o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- Após esta aula, os grupos já têm os elementos para tomar a segunda grande decisão do projeto: **qual topologia usar?**
- Para a maioria dos cenários corporativos do projeto, a topologia **Estrela** será a base da LAN interna
- Grupos com cenários maiores (múltiplos andares ou filiais) devem considerar a topologia **Híbrida**
- O professor pode orientar cada grupo brevemente ao final da aula sobre qual topologia se encaixa melhor no seu cenário

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 28 — 09/09/2026 · Classificação das Redes por Abrangência |
| Próxima aula → | Aula 30 — 23/09/2026 · Modelos de Rede — Cliente-Servidor e Peer-to-Peer |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagramas visuais de cada topologia
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: papel e caneta para que os grupos esbocem a topologia do Projeto Integrador ao final da aula

---

## Observações do Professor
