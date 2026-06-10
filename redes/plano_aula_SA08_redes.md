# UC: Fundamentos de Redes de Computadores
## Aula 08 — 1º Trimestre

---

## Tema

Componentes de Rede — Ativos e Interfaces

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são componentes ativos de rede e como eles se diferenciam dos componentes passivos vistos na Aula 07
- Identificar e diferenciar os principais ativos de rede: hub, switch, roteador, access point e modem
- Reconhecer os tipos de interfaces de rede (NIC): Ethernet, Wi-Fi, fibra óptica e USB
- Diferenciar as funções de cada ativo — entendendo o papel específico de cada equipamento na infraestrutura de rede
- Relacionar os ativos de rede com as camadas do modelo OSI em que cada um opera

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes

---

## Conteúdo

- Retomada rápida da Aula 07: *"Vimos os componentes passivos — cabos, conectores e organização. Hoje vamos conhecer os componentes ativos: os equipamentos que processam, comutam e roteiam os dados pela rede"*
- **O que são componentes ativos de rede?**
  - Componentes ativos são equipamentos que processam dados — tomam decisões sobre para onde encaminhar os pacotes, ampliam sinais ou gerenciam o tráfego da rede
  - Precisam de energia elétrica para funcionar
  - Operam em camadas específicas do modelo OSI — o que define suas capacidades e funções
  - Exemplos: hub, switch, roteador, access point, modem, firewall

- **Hub**
  - **O que é:** dispositivo de conectividade básica que conecta múltiplos dispositivos em uma rede
  - **Camada OSI:** Camada 1 — Física
  - **Como funciona:** recebe um sinal em uma porta e retransmite para TODAS as outras portas simultaneamente — sem inteligência
  - **Problema:** todos os dispositivos conectados compartilham o mesmo domínio de colisão — se dois dispositivos transmitem ao mesmo tempo, ocorre colisão e os dados precisam ser retransmitidos
  - **Half-duplex:** não consegue enviar e receber ao mesmo tempo na mesma porta
  - **Status atual:** completamente obsoleto — substituído pelo switch em todos os ambientes modernos
  - **Por que ainda estudar?** Base histórica para entender a evolução das redes e fundamento para compreender o switch

- **Switch**
  - **O que é:** dispositivo inteligente de conectividade que interliga dispositivos em uma rede local
  - **Camada OSI:** Camada 2 — Enlace de Dados (switches gerenciáveis avançados operam também na Camada 3)
  - **Como funciona:**
    - Aprende e mantém uma tabela de endereços MAC (MAC Address Table / CAM Table)
    - Quando recebe um quadro (frame), verifica o endereço MAC de destino na tabela
    - Encaminha o dado apenas para a porta correta — não para todas como o hub
    - Cada porta tem seu próprio domínio de colisão — elimina colisões entre dispositivos
  - **Full-duplex:** pode enviar e receber simultaneamente na mesma porta — dobra a largura de banda efetiva
  - **Tipos de switch:**
    - **Não gerenciável (Unmanaged):** sem configuração · plug-and-play · uso doméstico e pequenas empresas
    - **Gerenciável (Managed):** configurável via interface web ou CLI · suporte a VLANs, STP, QoS, SNMP · uso corporativo
    - **PoE (Power over Ethernet):** fornece energia elétrica pelo cabo de rede — alimenta APs, câmeras IP e telefones VoIP
    - **Layer 3 (L3 Switch):** realiza roteamento entre VLANs — combina funções de switch e roteador
  - **Vantagens sobre o hub:** elimina colisões · dedica banda por porta · suporta VLANs · full-duplex

- **Roteador (Router)**
  - **O que é:** dispositivo que interliga redes diferentes e encaminha pacotes entre elas
  - **Camada OSI:** Camada 3 — Rede
  - **Como funciona:**
    - Mantém uma tabela de roteamento com as rotas conhecidas para diferentes redes
    - Analisa o endereço IP de destino de cada pacote
    - Decide o melhor caminho para encaminhar o pacote com base nas rotas da tabela
    - Conecta a rede interna (LAN) à internet (WAN) — é o "portão de saída" da rede
  - **Funções adicionais do roteador moderno:**
    - **NAT (Network Address Translation):** traduz IPs privados para o IP público — permite que múltiplos dispositivos compartilhem um único IP público
    - **DHCP:** atribui endereços IP automaticamente aos dispositivos da rede
    - **Firewall básico:** filtra tráfego indesejado entre a rede interna e a internet
    - **DNS Relay:** repassa consultas DNS para o servidor DNS configurado
  - **Diferença para o switch:** switch opera na Camada 2 (MAC) e conecta dispositivos na mesma rede · roteador opera na Camada 3 (IP) e conecta redes diferentes
  - **Exemplos:** roteador doméstico Wi-Fi, Cisco ISR, MikroTik RouterOS, pfSense (software)

- **Access Point (AP)**
  - **O que é:** dispositivo que cria e transmite o sinal Wi-Fi, conectando dispositivos sem fio à rede cabeada
  - **Camada OSI:** Camada 2 — Enlace de Dados
  - **Como funciona:** recebe o sinal da rede cabeada (via porta Ethernet conectada ao switch) e converte em sinal de rádio Wi-Fi para os dispositivos sem fio
  - **Diferença para o roteador doméstico Wi-Fi:**
    - Roteador doméstico: combina roteador + switch + AP em um único equipamento
    - AP corporativo: apenas o ponto de acesso sem fio — sem função de roteamento
    - Em redes corporativas, o AP é separado do roteador — cada equipamento tem sua função específica
  - **PoE:** APs corporativos são alimentados pelo próprio cabo Ethernet (PoE) — sem necessidade de tomada elétrica próxima
  - **Exemplos:** Ubiquiti UniFi AP, Cisco Meraki, TP-Link EAP

- **Modem**
  - **O que é:** dispositivo que modula e demodula sinais para transmitir dados pela linha do provedor de internet
  - **Camada OSI:** Camada 1 — Física
  - **Como funciona:** converte o sinal digital da rede interna em sinal analógico (ou de outra natureza) compatível com o meio da operadora — e vice-versa
  - **Tipos por tecnologia:**
    - **Modem ADSL:** converte sinal para linha telefônica de cobre
    - **Modem de cabo:** converte sinal para cabo coaxial (internet HFC/DOCSIS)
    - **ONT (Optical Network Terminal):** "modem" de fibra óptica — converte sinal óptico em Ethernet
    - **Modem 4G/5G:** converte sinal celular em conexão Ethernet ou Wi-Fi
  - **Em redes domésticas:** o modem geralmente é combinado com roteador e AP em um único equipamento (gateway)
  - **Em redes corporativas:** o modem é separado — conecta ao roteador de borda da empresa

- **NIC — Network Interface Card (Placa de Rede)**
  - **O que é:** componente que permite a um dispositivo se conectar à rede — pode ser integrado à placa-mãe (onboard) ou adicional (placa de expansão)
  - **Camada OSI:** Camada 2 — Enlace de Dados (endereço MAC é atribuído à NIC)
  - **Tipos de interface:**
    - **Ethernet (RJ-45):** conexão cabeada padrão — velocidades de 10/100 Mbps (Fast Ethernet), 1 Gbps (Gigabit), 10 Gbps (10G)
    - **Wi-Fi (802.11):** conexão sem fio · padrões b/g/n/ac/ax · integrada em notebooks, celulares e tablets
    - **Fibra óptica (SFP/SFP+):** interfaces de alta velocidade usadas em switches de data center · transceiver removível · velocidades de 1 Gbps a 400 Gbps
    - **USB:** adaptadores de rede USB para conexão cabeada ou Wi-Fi em dispositivos sem porta de rede integrada
  - **Endereço MAC:** identificador físico único gravado na NIC pelo fabricante · 48 bits · notação hexadecimal ex.: 00:1A:2B:3C:4D:5E · usado na Camada 2 para identificar dispositivos na rede local

- **Comparativo dos ativos — Camada OSI e função principal:**

| Dispositivo | Camada OSI | Endereçamento | Função principal |
|-------------|-----------|--------------|-----------------|
| Hub | Camada 1 — Física | Nenhum | Repassa sinal para todas as portas |
| Switch | Camada 2 — Enlace | Endereço MAC | Comuta quadros para a porta correta |
| Roteador | Camada 3 — Rede | Endereço IP | Encaminha pacotes entre redes |
| Access Point | Camada 2 — Enlace | Endereço MAC | Conecta dispositivos sem fio à rede cabeada |
| Modem | Camada 1 — Física | Nenhum (conversão) | Converte sinais entre meios diferentes |
| NIC | Camada 2 — Enlace | Endereço MAC | Interface do dispositivo com a rede |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada da Aula 07: *"Vimos os passivos — cabos e conectores. Hoje conhecemos os ativos: os equipamentos que processam e encaminham os dados"* |
| Retomada | Professor pergunta: *"Qual a diferença entre o switch e o roteador da sua casa? São o mesmo equipamento? Por que o roteador doméstico faz tudo isso em um único aparelho?"* — alunos respondem livremente · conectar as respostas à diferença funcional entre os ativos |
| Explicação | Slides — componentes ativos × passivos, hub (obsoleto), switch (MAC table, full-duplex, tipos), roteador (tabela de roteamento, NAT, DHCP), AP (corporativo × doméstico, PoE), modem (tipos por tecnologia), NIC (tipos de interface, endereço MAC), comparativo por camada OSI |
| Dinâmica | "Quem Sou Eu?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: hub obsoleto · switch Camada 2 (MAC) · roteador Camada 3 (IP) · AP conecta sem fio · modem converte sinal · NIC é a interface do dispositivo · Próxima aula: Interfaces e Serviços de Internet |

---

## Dinâmica — "Quem Sou Eu?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar o reconhecimento e a diferenciação dos ativos de rede por meio de descrições de função e características, desenvolvendo o raciocínio de identificação precisa — habilidade essencial para especificar, configurar e diagnosticar equipamentos de rede no suporte técnico e na administração de infraestrutura.

**Materiais:** cartões com descrições de características ou situações — um conjunto por grupo · ou slide com as descrições projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões. Cada cartão descreve características, funções ou uma situação de uso de um ativo de rede. O desafio é identificar qual equipamento está sendo descrito e justificar com base nas características apresentadas.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica o equipamento, confirma a camada OSI em que opera e descreve a função específica no cenário.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça as diferenças entre os equipamentos — especialmente switch × roteador, que é a confusão mais comum.

**Situações sugeridas:**

| Descrição | Equipamento | O que reforçar |
|-----------|------------|----------------|
| "Opera na Camada 2 · aprende endereços MAC · encaminha dados apenas para a porta correta · elimina colisões" | Switch | Diferença fundamental para o hub · MAC table · full-duplex |
| "Opera na Camada 3 · analisa endereços IP · conecta a rede interna à internet · atribui IPs via DHCP" | Roteador | Opera com IP, não com MAC · gateway da rede · NAT |
| "Recebe o sinal de rádio do celular e converte em conexão de internet para a rede celular da operadora" | Modem 4G/5G | Converte sinal entre meios diferentes · Camada 1 |
| "Equipamento instalado no teto do escritório · alimentado pelo próprio cabo de rede · distribui Wi-Fi" | Access Point com PoE | AP corporativo · PoE elimina necessidade de tomada · Camada 2 |
| "Repassa o sinal recebido para TODAS as portas ao mesmo tempo · causa colisões · completamente obsoleto" | Hub | Por que o hub foi substituído pelo switch · domínio de colisão |
| "Componente integrado à placa-mãe do notebook · possui endereço físico único gravado pelo fabricante · 48 bits" | NIC (placa de rede) | Endereço MAC · identificador único da interface · Camada 2 |
| "Recebe o sinal óptico da fibra da operadora e converte em sinal Ethernet para o roteador da empresa" | ONT / Modem de fibra | Conversão de sinal óptico → elétrico · Camada 1 · interface entre operadora e cliente |
| "Empresa tem 4 andares · cada andar tem switch conectado a este equipamento central que roteia o tráfego entre VLANs sem precisar de um roteador separado" | Switch Layer 3 (L3) | Switch gerenciável avançado · roteia entre VLANs · combina Camada 2 e Camada 3 |

> **Nota:** o objetivo é desenvolver o raciocínio preciso de identificação: *"qual é a camada OSI? O dispositivo usa MAC ou IP? Ele processa ou apenas repassa o sinal? Ele conecta dispositivos da mesma rede ou redes diferentes?"* Reforçar que a confusão entre switch e roteador é um dos erros mais comuns em entrevistas e provas técnicas da área de TI.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 07 — 01/04/2026 · Componentes de Rede — Hardware Passivo |
| Próxima aula → | Aula 09 — 15/04/2026 · Tipos Comuns de Interfaces e Serviços de Internet |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — com fotos reais dos equipamentos e tabela comparativa por camada OSI
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: levar para a aula um switch real (mesmo que pequeno/doméstico), um roteador e um access point para demonstração visual · mostrar a diferença física entre os equipamentos · se disponível, mostrar a tabela MAC de um switch ao vivo via interface web

---

## Observações do Professor
