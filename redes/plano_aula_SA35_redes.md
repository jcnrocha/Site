# UC: Fundamentos de Redes de Computadores
## Aula 35 — 3º Trimestre

---

## Tema

Tendências em Redes — IoT e Redes do Futuro

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é a Internet das Coisas (IoT) e como ela impacta a infraestrutura de redes
- Identificar os principais protocolos de comunicação utilizados em dispositivos IoT
- Reconhecer o conceito de SDN (Software Defined Networking) e como ele transforma o gerenciamento de redes
- Compreender o impacto do 5G na infraestrutura de redes e nas aplicações do futuro
- Relacionar as tendências de redes com oportunidades reais no mercado de trabalho para desenvolvedores e técnicos de TI

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores · H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 34: *"Aprendemos a diagnosticar e resolver problemas — hoje olhamos para o futuro: quais são as tendências que vão transformar as redes nos próximos anos?"*
- **Por que entender tendências?**
  - A infraestrutura de redes está evoluindo rapidamente — o que é tecnologia de ponta hoje será o padrão corporativo em poucos anos
  - Profissionais que antecipam essas mudanças se posicionam melhor no mercado de trabalho
  - IoT, 5G e SDN já estão presentes em projetos reais no Brasil — não são tecnologias do futuro distante

- **IoT — Internet das Coisas (Internet of Things)**
  - **Conceito:** conexão de objetos físicos do cotidiano à internet, permitindo coleta de dados, automação e controle remoto
  - Qualquer dispositivo com sensores, capacidade de processamento e conectividade pode ser um objeto IoT
  - **Escala:** em 2024 já eram mais de 15 bilhões de dispositivos IoT conectados no mundo · projeção de 30 bilhões até 2030
  - **Exemplos no cotidiano:**
    - 🏠 Casa inteligente: lâmpadas, tomadas, fechaduras, câmeras, termostatos conectados
    - 🏭 Indústria 4.0: sensores em máquinas que monitoram temperatura, vibração e consumo de energia
    - 🏥 Saúde: monitores de pressão, glicosímetros e pulseiras fitness conectados ao celular ou ao hospital
    - 🌾 Agronegócio: sensores de solo, irrigação automatizada, drones de monitoramento de lavoura
    - 🚗 Veículos conectados: carros que reportam localização, diagnóstico e telemetria em tempo real
    - 🏙️ Cidades inteligentes: semáforos adaptativos, lixeiras que avisam quando estão cheias, monitoramento de qualidade do ar

  - **Desafios do IoT para a infraestrutura de redes:**
    - **Volume:** milhares de dispositivos simultâneos em uma única rede — switches e APs precisam suportar alta densidade
    - **Segurança:** dispositivos IoT geralmente têm firmware desatualizado e senhas padrão — vetor de ataque frequente
    - **Isolamento:** VLAN IoT separada da rede corporativa — fundamental para proteger dados sensíveis
    - **Protocolos leves:** dispositivos com baixo poder de processamento precisam de protocolos eficientes

  - **Principais protocolos IoT:**

  | Protocolo | Camada | Característica principal | Uso típico |
  |-----------|--------|------------------------|-----------|
  | MQTT | Aplicação | Leve, publish-subscribe, baixo consumo | Sensores industriais, telemetria |
  | CoAP | Aplicação | Similar ao HTTP, otimizado para IoT | Dispositivos com bateria limitada |
  | Zigbee | Física/Enlace | Malha sem fio, baixo consumo, curto alcance | Casa inteligente, automação |
  | Z-Wave | Física/Enlace | Malha sem fio, menor interferência que Zigbee | Automação residencial |
  | LoRaWAN | Física/Enlace | Longo alcance, baixíssimo consumo | Agronegócio, cidades inteligentes |
  | NB-IoT | Física/Enlace | Usa rede celular, baixo consumo | Medidores inteligentes, rastreamento |

- **5G e o impacto nas redes**
  - **O que o 5G traz de novo além da velocidade:**
    - **eMBB (Enhanced Mobile Broadband):** velocidades de até 20 Gbps — streaming 8K, realidade virtual/aumentada
    - **URLLC (Ultra-Reliable Low-Latency Communications):** latência de ~1 ms — cirurgias remotas, veículos autônomos, controle industrial em tempo real
    - **mMTC (Massive Machine-Type Communications):** suporte a até 1 milhão de dispositivos por km² — viabiliza IoT em escala urbana
  - **Impacto na infraestrutura:**
    - **Small cells:** antenas menores e mais densas instaladas em postes, fachadas e interiores de prédios — substituem as grandes torres em áreas urbanas
    - **Edge computing:** processamento de dados próximo ao dispositivo, sem enviar tudo para a nuvem — reduz latência e economiza banda
    - **Network slicing:** divisão da rede 5G em fatias virtuais independentes para diferentes usos (slice para IoT, slice para streaming, slice para emergências)
  - **Casos de uso reais já em implantação no Brasil:**
    - Fábricas inteligentes com controle de máquinas via 5G privado
    - Telemedicina e cirurgias assistidas remotamente
    - Transmissão ao vivo de eventos em 4K/8K sem cabo
    - Veículos conectados em vias inteligentes

- **SDN — Software Defined Networking (Redes Definidas por Software)**
  - **Conceito:** separação do plano de controle (decisões de roteamento) do plano de dados (encaminhamento de pacotes)
  - Na rede tradicional: cada switch e roteador toma suas próprias decisões de forma independente e distribuída
  - No SDN: um controlador centralizado define as regras para todos os dispositivos da rede — os switches apenas encaminham os pacotes conforme instruído
  - **Benefícios:**
    - Gerenciamento centralizado de toda a rede por software
    - Programabilidade: a rede pode ser configurada via código (NetDevOps)
    - Flexibilidade: mudanças de configuração aplicadas em segundos em toda a rede
    - Visibilidade: o controlador tem visão completa de todo o tráfego da rede
    - Automação: scripts e APIs configuram a rede automaticamente
  - **Exemplos de uso:** data centers de grandes empresas (Google, Facebook), redes de operadoras, ambientes de cloud computing
  - **Ferramentas:** OpenFlow (protocolo), OpenDaylight (controlador open source), Cisco ACI, VMware NSX

- **NFV — Network Functions Virtualization (Virtualização de Funções de Rede)**
  - Funções de rede que antes exigiam hardware dedicado (firewall, load balancer, roteador) são executadas como software em servidores padrão
  - Reduz drasticamente o custo de infraestrutura de operadoras e grandes empresas
  - Complementa o SDN — SDN controla o fluxo, NFV virtualiza as funções

- **Edge Computing e a nova arquitetura de redes:**
  - Processamento de dados na borda da rede — próximo ao dispositivo que gera os dados
  - Reduz latência e o volume de dados enviados à nuvem central
  - Essencial para IoT industrial, veículos autônomos e realidade aumentada
  - Exemplo: câmera de segurança com IA que processa as imagens localmente e só envia alertas para a nuvem — não o vídeo completo

- **Segurança nas redes do futuro:**
  - **Zero Trust Network Access (ZTNA):** "nunca confie, sempre verifique" — nenhum dispositivo ou usuário é confiável por padrão, mesmo dentro da rede corporativa
  - **SASE (Secure Access Service Edge):** convergência de rede e segurança entregues como serviço na nuvem
  - **IA para segurança de redes:** detecção de anomalias e ataques em tempo real com machine learning

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 34: *"Aprendemos a diagnosticar redes — hoje olhamos para onde as redes estão indo: IoT, 5G, SDN e o que isso significa para nossa carreira"* |
| Retomada | Professor pergunta: *"Quantos dispositivos conectados à internet vocês têm em casa agora? Celular, TV, caixa de som, roteador, câmera... Isso é IoT. O que acontece com a rede quando esses dispositivos se multiplicam por mil em uma fábrica?"* — alunos respondem livremente |
| Explicação | Slides — IoT (conceito, escala, exemplos, desafios, protocolos), 5G (eMBB, URLLC, mMTC, small cells, edge computing, network slicing), SDN (plano de controle × dados, benefícios, ferramentas), NFV, Edge Computing, segurança do futuro (Zero Trust, SASE) |
| Dinâmica | "Tecnologia do Futuro ou do Presente?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: IoT = objetos conectados em escala · 5G = velocidade + latência + densidade · SDN = rede programável e centralizada · Edge = processamento na borda · Zero Trust = segurança sem perímetro fixo · Próxima aula: Projeto Integrador — Desenho de Rede Corporativa |

---

## Dinâmica — "Tecnologia do Futuro ou do Presente?"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** consolidar o entendimento das tendências de redes por meio de situações reais, desenvolvendo a capacidade de identificar qual tecnologia está sendo aplicada e qual oportunidade de mercado ela representa — conectando as tendências com o Projeto Integrador e com a visão de carreira dos alunos.

**Materiais:** cartões com cenários de tecnologia — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de uso de tecnologia. O desafio é identificar: qual tendência está sendo aplicada (IoT, 5G, SDN, Edge Computing ou Zero Trust) e qual é a oportunidade de mercado ou desafio de infraestrutura envolvido.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário: identifica a tecnologia, o benefício gerado e o impacto na infraestrutura de redes.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e conecta com oportunidades reais de mercado.

**Cenários sugeridos:**

| Cenário | Tecnologia | Impacto na rede / Oportunidade |
|---------|-----------|-------------------------------|
| Fábrica instala sensores em 500 máquinas que enviam dados de temperatura e vibração a cada 5 segundos | IoT Industrial (IIoT) + MQTT | Rede precisa de VLAN IoT, switches de alta densidade e protocolo leve como MQTT |
| Cirurgião em São Paulo opera um paciente em Manaus com braço robótico controlado remotamente | 5G URLLC | Latência de ~1 ms via 5G — impossível com 4G ou Wi-Fi convencional |
| Empresa de data center gerencia 10.000 switches via software, alterando rotas em segundos sem acessar cada equipamento | SDN com OpenFlow | Controlador centralizado — mudanças de configuração por API em toda a rede simultaneamente |
| Câmeras de segurança de um shopping processam reconhecimento facial localmente sem enviar vídeo para a nuvem | Edge Computing + IoT | Reduz latência, economiza banda e protege privacidade — processamento na borda |
| Empresa adota política de que todo acesso à rede — mesmo de funcionários internos — exige autenticação e verificação contínua | Zero Trust Network Access (ZTNA) | Elimina o conceito de "dentro da rede é seguro" — cada acesso é verificado independentemente |
| Operadora de telecomunicações substitui firewalls físicos por instâncias de software em servidores padrão | NFV | Reduz custo de hardware · funções de rede executadas como software escalável |
| Agricultor recebe alertas no celular quando o solo de sua lavoura precisa de irrigação — sensores a 15 km da sede | IoT + LoRaWAN | LoRaWAN transmite dados a longas distâncias com baixíssimo consumo — ideal para agronegócio |
| Desenvolvedor configura toda a topologia de rede de um data center escrevendo um arquivo de configuração em código | SDN + NetDevOps | Infraestrutura como código — rede programável e versionável como qualquer software |

> **Nota:** o objetivo é desenvolver a visão de mercado: *"essa tecnologia já existe e está sendo usada agora — como ela impacta a infraestrutura de redes e quais profissionais são necessários para implementá-la?"* Reforçar que IoT, 5G e SDN não são apenas tendências acadêmicas — são projetos reais que empresas brasileiras já estão implantando.

---

## Conexão com o Projeto Integrador

Esta aula enriquece o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37) com uma visão de futuro:

- Os grupos podem incluir no projeto uma seção de **"Visão de Futuro":**
  - Quais dispositivos IoT fazem sentido para a empresa projetada? (câmeras IP, sensores, impressoras inteligentes)
  - A rede projetada suporta a expansão para IoT? (VLAN IoT, switch de alta densidade)
  - O link de internet dimensionado suporta o crescimento dos serviços em nuvem e IoT?
  - Algum serviço poderia se beneficiar de Edge Computing? (processamento local de câmeras, por exemplo)
- Essa seção demonstra visão estratégica e diferencia os projetos mais completos

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 34 — 21/10/2026 · Diagnóstico e Solução de Problemas em Redes |
| Próxima aula → | Aula 36 — 04/11/2026 · Projeto Integrador — Desenho de Rede Corporativa |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo infográficos de IoT em escala, diagrama de arquitetura SDN e comparativo 4G × 5G
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: mostrar ao vivo um dashboard de dispositivos IoT (ex.: plataforma ThingSpeak ou Node-RED) ou uma demonstração de automação residencial com assistente de voz — torna o conteúdo tangível e motivador para os alunos

---

## Observações do Professor
