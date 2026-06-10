# UC: Fundamentos de Redes de Computadores
## Aula 09 — 1º Trimestre

---

## Tema

Tipos Comuns de Interfaces e Serviços de Internet

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Identificar os principais tipos de interfaces de rede utilizados no cotidiano: Ethernet, Wi-Fi, fibra óptica, USB e Bluetooth
- Reconhecer os principais serviços de acesso à internet disponíveis no Brasil: banda larga, ADSL, cabo, fibra óptica, 4G e 5G
- Diferenciar os serviços de internet quanto à velocidade, tecnologia, disponibilidade e adequação para uso residencial ou corporativo
- Realizar uma revisão integrada dos conteúdos do 1º trimestre — conectando unidades de medida, simbologias, componentes passivos e ativos em uma visão consolidada
- Preparar-se para a avaliação trimestral da Aula 10

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes · H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Retomada rápida da Aula 08: *"Conhecemos os ativos de rede — switch, roteador, AP e modem. Hoje entendemos como cada interface conecta os dispositivos à rede e quais serviços de internet estão disponíveis para usuários e empresas"*
- **Tipos Comuns de Interfaces de Rede:**

  - **Ethernet (RJ-45)**
    - Interface cabeada padrão — presente em computadores desktop, notebooks, servidores e switches
    - Velocidades: 10 Mbps (10Base-T), 100 Mbps (Fast Ethernet), 1 Gbps (Gigabit Ethernet), 10 Gbps (10GbE)
    - Vantagens: estável, alta velocidade, baixa latência, sem interferência
    - Desvantagens: requer cabo físico — limita a mobilidade do dispositivo
    - Uso típico: estações de trabalho fixas, servidores, switches, impressoras de rede

  - **Wi-Fi (IEEE 802.11)**
    - Interface sem fio padrão — integrada em notebooks, smartphones, tablets e smart TVs
    - Padrões: 802.11b/g/n (Wi-Fi 4), 802.11ac (Wi-Fi 5), 802.11ax (Wi-Fi 6/6E)
    - Vantagens: mobilidade, sem cabo, fácil de conectar novos dispositivos
    - Desvantagens: velocidade menor que Ethernet cabeada, sujeita a interferências, latência maior
    - Uso típico: dispositivos móveis, notebooks, dispositivos IoT, áreas onde cabeamento é inviável

  - **Fibra Óptica (SFP/SFP+)**
    - Interface de altíssima velocidade usada em switches de data center, roteadores corporativos e servidores
    - Transceiver (módulo) removível — inserido na porta SFP do equipamento
    - Velocidades: 1 Gbps (SFP), 10 Gbps (SFP+), 25 Gbps (SFP28), 100 Gbps (QSFP28)
    - Uso típico: conexões de backbone entre switches de núcleo, uplinks de data center, conexões de longa distância

  - **USB (Universal Serial Bus)**
    - Interface versátil para conexão de dispositivos periféricos — adaptadores de rede USB permitem adicionar conectividade a dispositivos sem porta Ethernet integrada
    - Adaptadores USB-Ethernet: adicionam porta Gigabit Ethernet a notebooks que não possuem RJ-45
    - Adaptadores USB Wi-Fi: adicionam conectividade sem fio a computadores desktop sem placa Wi-Fi integrada
    - Velocidade: limitada pelo padrão USB (USB 3.0: até 5 Gbps de transferência bruta, mas adaptadores de rede tipicamente entregam até 1 Gbps Ethernet)
    - Uso típico: solução temporária, dispositivos sem interface de rede nativa, pen drives com função de rede

  - **Bluetooth**
    - Interface sem fio de curto alcance para conexão de dispositivos pessoais
    - Alcance: até 10 metros (Classe 2) ou 100 metros (Classe 1)
    - Versões: 4.0 (BLE — baixo consumo), 5.0 (maior alcance e velocidade de até 2 Mbps)
    - Uso típico: periféricos (mouse, teclado, fone), wearables, transferência de arquivos entre dispositivos próximos
    - **Não é uma interface de rede LAN** — é uma tecnologia de rede pessoal (PAN) para curtas distâncias

  - **Tabela comparativa das interfaces:**

  | Interface | Tipo | Velocidade típica | Alcance | Uso principal |
  |-----------|------|------------------|---------|--------------|
  | Ethernet | Cabeada | 1–10 Gbps | 100 m (cabo) | Estações fixas, servidores |
  | Wi-Fi (802.11ax) | Sem fio | Até 9,6 Gbps | 30–100 m | Dispositivos móveis |
  | Fibra (SFP+) | Cabeada/óptica | 10–100 Gbps | km | Backbone e data center |
  | USB (adaptador) | Cabeada | Até 1 Gbps | — | Solução temporária |
  | Bluetooth | Sem fio | Até 2 Mbps | 10–100 m | Periféricos e wearables |

- **Serviços de Acesso à Internet:**

  - **Banda Larga por Linha Telefônica — ADSL/VDSL**
    - Usa o par de cobre da linha telefônica já instalada nas residências
    - **ADSL:** download até 8 Mbps · upload até 1 Mbps · assimétrico · em declínio
    - **VDSL:** download até 100 Mbps · upload até 50 Mbps · mais rápido que ADSL
    - Limitação: quanto mais longe da central telefônica, menor a velocidade
    - Equipamento do cliente: modem ADSL/VDSL com conector RJ-11
    - Uso típico: residências em áreas sem fibra óptica disponível

  - **Internet via TV a Cabo (HFC — Hybrid Fiber-Coaxial)**
    - Usa a infraestrutura de TV a cabo — fibra até os nós da operadora + cabo coaxial até o domicílio
    - Padrão: DOCSIS (Data Over Cable Service Interface Specification)
    - Velocidades: DOCSIS 3.0 até 1 Gbps · DOCSIS 3.1 até 10 Gbps teóricos
    - Desvantagem: banda compartilhada entre vizinhos no mesmo segmento — velocidade pode cair nos horários de pico
    - Equipamento: modem de cabo com conector coaxial (F-type)
    - Uso típico: residencial e pequenas empresas em áreas com cobertura de TV a cabo

  - **Fibra Óptica até o Domicílio (FTTH/FTTB)**
    - Tecnologia mais moderna — fibra óptica chega diretamente à residência ou ao prédio
    - **FTTH (Fiber to the Home):** fibra até dentro da residência — máximo desempenho
    - **FTTB (Fiber to the Building):** fibra até o prédio · distribuição interna por Ethernet ou coaxial
    - Velocidades: simétricas de 100 Mbps, 300 Mbps, 500 Mbps, 1 Gbps e além
    - Equipamento: ONT (Optical Network Terminal) — "modem de fibra" que converte sinal óptico em Ethernet
    - Vantagens: altíssima velocidade, baixa latência, conexão dedicada (não compartilhada), imunidade a interferências
    - **Padrão atual para novos projetos** — tecnologia que está substituindo ADSL e cabo no Brasil
    - Uso típico: residencial e corporativo — qualquer perfil de uso

  - **Internet Móvel — 4G LTE e 5G**
    - Usa a infraestrutura de redes celulares das operadoras
    - **4G LTE:** velocidades de 10 a 150 Mbps · latência de 30 a 50 ms · cobertura ampla no Brasil
    - **5G:** velocidades de 1 a 4 Gbps reais · latência de ~1 ms · expansão em capitais brasileiras
    - Equipamentos: chip SIM no smartphone · roteador 4G/5G (indoor ou outdoor) para uso residencial ou corporativo
    - Uso típico: mobilidade (smartphones) · backup de internet para empresas · áreas sem infraestrutura fixa
    - Vantagem: cobertura em locais sem cabeamento · Desvantagem: custo por GB de dados, latência variável

  - **Rádio (WISP — Wireless Internet Service Provider)**
    - Provedor regional que distribui internet por antenas de rádio instaladas em torres
    - Frequências: 900 MHz, 2,4 GHz, 5,8 GHz
    - Velocidades: 10 a 100 Mbps tipicamente
    - Uso típico: cidades do interior e zonas rurais sem fibra ou cabo disponível
    - Desvantagem: exige linha de visada entre a antena do cliente e a torre do provedor

  - **Internet via Satélite (LEO)**
    - Starlink e outros provedores LEO oferecem internet via satélites em órbita baixa
    - Velocidades: 50 a 300 Mbps · Latência: 20 a 40 ms
    - Uso típico: fazendas, áreas remotas, embarcações, locais sem qualquer outra infraestrutura
    - Desvantagem: custo do equipamento e mensalidade ainda elevados

  - **Tabela comparativa dos serviços:**

  | Serviço | Velocidade típica | Latência | Disponibilidade | Uso típico |
  |---------|------------------|----------|----------------|-----------|
  | ADSL | Até 8 Mbps | ~50 ms | Linha telefônica existente | Residencial sem fibra |
  | VDSL | Até 100 Mbps | ~20 ms | Próximo à central | Residencial/PME |
  | HFC (Cabo) | Até 1 Gbps | ~10 ms | Áreas com TV a cabo | Residencial |
  | FTTH | 100 Mbps – 1 Gbps+ | ~5 ms | Crescente no Brasil | Residencial e corporativo |
  | 4G LTE | 10–150 Mbps | ~30–50 ms | Ampla cobertura | Móvel e backup |
  | 5G | 1–4 Gbps | ~1 ms | Capitais | Alta demanda e IoT |
  | Rádio WISP | 10–100 Mbps | ~10–30 ms | Interior e rural | Cidades sem fibra |
  | Satélite LEO | 50–300 Mbps | ~20–40 ms | Global | Áreas remotas |

- **Revisão Integrada do 1º Trimestre:**
  - **H1 — Unidades de Medida:** bits, bytes, KB, MB, GB, TB · bps, Kbps, Mbps, Gbps · latência e throughput
  - **H2 — Simbologias:** roteador, switch, AP, servidor, firewall, DMZ, nuvem, enlaces cabeados e sem fio
  - **H3 — Componentes Passivos:** par trançado (Cat5e/6/6A), fibra óptica (mono/multi), coaxial · RJ-45, RJ-11, SC, LC · rack, patch panel, patch cord
  - **H3 — Componentes Ativos:** hub (obsoleto), switch (Camada 2, MAC), roteador (Camada 3, IP), AP (PoE), modem (tipos), NIC (interfaces)
  - **H4 — Serviços de Internet:** ADSL, VDSL, HFC, FTTH, 4G, 5G, Rádio, Satélite

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada da Aula 08: *"Conhecemos os ativos de rede — hoje finalizamos o 1º trimestre com interfaces e serviços de internet, e fazemos uma revisão geral antes da prova"* |
| Retomada | Professor pergunta: *"Qual serviço de internet você tem em casa? Sabe se é fibra, cabo ou ADSL? Como você descobriria? O que muda na velocidade e na qualidade entre cada um?"* — alunos respondem livremente |
| Explicação | Slides — interfaces (Ethernet, Wi-Fi, fibra SFP, USB, Bluetooth), serviços de internet (ADSL/VDSL, HFC, FTTH, 4G/5G, Rádio, Satélite LEO), tabelas comparativas |
| Revisão | Tour rápido pelos conteúdos do 1º trimestre — professor faz perguntas à turma cobrindo H1, H2, H3 e H4 · espaço para dúvidas finais antes da prova |
| Dinâmica | "Qual Interface e Qual Serviço?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo geral do 1º trimestre · orientações sobre o formato da prova da Aula 10 · encorajamento da turma |

---

## Dinâmica — "Qual Interface e Qual Serviço?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar a identificação dos tipos de interfaces de rede e serviços de internet — conectando esses conceitos com os componentes e unidades de medida vistos ao longo do trimestre e desenvolvendo o raciocínio de escolha adequada para cada perfil de usuário ou empresa.

**Materiais:** cartões com perfis e cenários — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com perfis de usuários ou cenários de infraestrutura. O desafio é indicar qual interface de rede e qual serviço de internet são mais adequados para cada perfil, justificando a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica a melhor interface e o melhor serviço, considerando velocidade, disponibilidade, mobilidade e custo.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os critérios de escolha.

**Cenários sugeridos:**

| Perfil / Cenário | Interface indicada | Serviço indicado | Justificativa |
|------------------|--------------------|-----------------|---------------|
| Desenvolvedor em home office que precisa de conexão estável para videoconferências e uploads de código | Ethernet (RJ-45) | FTTH (fibra óptica) | Estabilidade máxima · baixa latência · simétrica para upload |
| Estudante que usa notebook em vários cômodos da casa e quer mobilidade | Wi-Fi (802.11ac/ax) | FTTH ou HFC | Mobilidade sem cabo · velocidade suficiente para streaming e estudo |
| Fazendeiro em área rural sem fibra, cabo ou telefone fixo disponível | Wi-Fi (do roteador satélite) | Satélite LEO (Starlink) | Única opção viável em área remota sem infraestrutura fixa |
| Empresa de pequeno porte em cidade do interior sem cobertura de fibra ou cabo | Ethernet (switches internos) | Rádio WISP | Infraestrutura típica de provedores regionais do interior |
| Técnico de campo que precisa de internet no notebook para suporte remoto em qualquer lugar | USB Wi-Fi ou USB Ethernet | 4G LTE (roteador portátil) | Mobilidade total · cobertura em rodovias e cidades |
| Data center com servidores que precisam de uplinks de 10 Gbps entre switches | Fibra óptica (SFP+ 10G) | Link dedicado corporativo | Altíssima velocidade · baixa latência · conexão exclusiva |
| Família em apartamento com cobertura de TV a cabo mas sem fibra disponível | Wi-Fi (roteador doméstico) | HFC / DOCSIS | Infraestrutura de cabo disponível · boa velocidade para uso residencial |
| Usuário de smartwatch que sincroniza dados de saúde com o celular próximo | Bluetooth | Não se aplica (PAN) | Curta distância · baixo consumo · Bluetooth é o padrão para wearables |

> **Nota:** o objetivo é consolidar o raciocínio integrado do trimestre: *"qual é o perfil de uso? Qual interface conecta o dispositivo à rede? Qual serviço de internet atende a essa necessidade com a velocidade, latência e disponibilidade adequadas?"* Esta é uma simulação direta do tipo de raciocínio exigido na prova trimestral.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 08 — 08/04/2026 · Componentes de Rede — Ativos e Interfaces |
| Próxima aula → | Aula 10 — 22/04/2026 · Prova — 1ª Avaliação Trimestral |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo tabelas comparativas de interfaces e serviços de internet
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: demonstração ao vivo — mostrar as configurações de rede do próprio computador da sala (adaptadores, velocidade, serviço de internet) e executar um Speedtest para ilustrar os conceitos de velocidade e latência em tempo real com a turma

---

## Observações do Professor
