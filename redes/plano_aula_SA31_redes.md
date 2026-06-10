# UC: Fundamentos de Redes de Computadores
## Aula 31 — 3º Trimestre

---

## Tema

Redes Sem Fio — Padrões e Infraestrutura

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender a infraestrutura necessária para montar e gerenciar uma rede sem fio corporativa
- Identificar os componentes de uma rede Wi-Fi: roteadores, access points e controladores
- Reconhecer os conceitos de SSID, canais e frequências aplicados à configuração de redes sem fio
- Diferenciar os padrões de segurança Wi-Fi: WEP, WPA, WPA2 e WPA3 — entendendo a evolução e por que o WPA3 é o padrão atual
- Relacionar os conceitos de infraestrutura sem fio com o planejamento do Projeto Integrador

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores · H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 30: *"Definimos os modelos de rede — Cliente-Servidor e P2P. Hoje vamos entender como estruturar uma rede sem fio corporativa com segurança e desempenho"*
- **Por que redes sem fio corporativas são diferentes da rede doméstica?**
  - Em casa: um único roteador Wi-Fi cobre o ambiente e serve poucos dispositivos
  - Em uma empresa: múltiplos andares, salas e áreas externas exigem cobertura planejada, gerenciamento centralizado e segurança robusta
  - A rede corporativa sem fio precisa garantir: cobertura total, segurança por usuário, controle de acesso e desempenho estável para dezenas ou centenas de dispositivos simultâneos

- **Componentes de uma rede Wi-Fi corporativa:**

  - **Roteador (Router)**
    - Conecta a rede interna à internet (WAN)
    - Faz o roteamento dos pacotes entre redes diferentes
    - Em redes corporativas geralmente é separado do access point — cada equipamento tem sua função específica
    - Exemplos: roteadores Cisco, MikroTik, pfSense (software)

  - **Access Point (AP)**
    - Dispositivo que cria e transmite o sinal Wi-Fi para os dispositivos finais
    - Conectado ao switch por cabo (uplink via Ethernet — PoE)
    - Diferente do roteador: o AP não roteia — apenas fornece acesso sem fio à rede cabeada
    - **PoE (Power over Ethernet):** permite alimentar o AP com energia elétrica pelo próprio cabo de rede — sem necessidade de tomada próxima ao AP
    - Tipos de instalação: teto (ceiling mount), parede, área externa (outdoor)
    - Exemplos: Ubiquiti UniFi, Cisco Meraki, TP-Link EAP

  - **Controlador Wi-Fi (Wireless Controller)**
    - Gerencia múltiplos access points de forma centralizada
    - Permite: configuração simultânea de todos os APs, monitoramento de desempenho, roaming entre APs, políticas de segurança centralizadas
    - Pode ser físico (hardware dedicado) ou em nuvem (cloud controller)
    - Roaming: usuário se move pelo ambiente e o dispositivo passa automaticamente de um AP para outro sem perder a conexão
    - Exemplos: Ubiquiti UniFi Controller, Cisco WLC, Aruba Central

  - **Switch PoE**
    - Switch com portas que fornecem energia elétrica pelo cabo Ethernet
    - Alimenta os access points sem necessidade de fonte de energia separada
    - Simplifica a instalação: apenas um cabo do switch ao AP (dados + energia)

- **SSID — Service Set Identifier**
  - O "nome" da rede Wi-Fi visível para os dispositivos
  - Uma mesma rede pode ter múltiplos SSIDs para finalidades diferentes:
    - **SSID Corporativo:** para funcionários — acesso completo à rede interna com autenticação
    - **SSID Guest (visitantes):** para clientes e visitantes — acesso apenas à internet, isolado da rede interna
    - **SSID IoT:** para dispositivos inteligentes — isolado por segurança
  - Cada SSID pode ter sua própria senha, VLAN e políticas de acesso
  - **SSID oculto:** não aparece na lista de redes disponíveis — o usuário precisa digitar o nome manualmente · segurança por obscuridade — não é uma medida de segurança robusta

- **Canais Wi-Fi**
  - A faixa de frequência é dividida em canais para que múltiplos roteadores/APs operem próximos sem interferir
  - **2,4 GHz:** 13 canais disponíveis · apenas 3 não sobrepostos: 1, 6 e 11
  - **5 GHz:** muito mais canais disponíveis — menos congestionamento
  - Em ambientes corporativos com múltiplos APs: cada AP deve usar um canal diferente para evitar interferência entre eles (co-channel interference)
  - Configuração recomendada: APs adjacentes em canais 1, 6 e 11 (na faixa 2,4 GHz)

- **Segurança Wi-Fi — Evolução dos Padrões:**

| Padrão | Ano | Criptografia | Status | Vulnerabilidade |
|--------|-----|-------------|--------|----------------|
| WEP | 1997 | RC4 (64/128 bits) | Obsoleto — NUNCA usar | Quebrado em minutos com ferramentas simples |
| WPA | 2003 | TKIP | Obsoleto | Vulnerável a ataques de dicionário |
| WPA2 | 2004 | AES-CCMP | Ainda aceitável | Vulnerável ao ataque KRACK (2017) |
| WPA3 | 2018 | AES-GCMP + SAE | Padrão atual recomendado | Proteção contra ataques de dicionário offline |

  - **WPA2-Personal:** senha compartilhada (PSK — Pre-Shared Key) · uso doméstico e pequenas empresas
  - **WPA2-Enterprise:** autenticação individual por usuário via servidor RADIUS · uso corporativo · cada funcionário tem seu próprio login na rede Wi-Fi
  - **WPA3-SAE (Simultaneous Authentication of Equals):** substitui o handshake de 4 vias do WPA2 · protege contra ataques de força bruta offline
  - **Wi-Fi Protected Setup (WPS):** botão de fácil configuração — DEVE ser desativado em ambientes corporativos (vulnerável)

- **Planejamento de cobertura Wi-Fi corporativa:**
  - **Site survey:** levantamento físico do ambiente antes de instalar os APs — mapeia paredes, obstáculos, interferências e áreas a cobrir
  - **Densidade de APs:** ambientes com muitos dispositivos precisam de mais APs com menor potência (cell splitting) — não de um AP com maior potência
  - **Roaming entre APs:** usuário em movimento (celular, notebook) deve passar de um AP para outro sem interrupção da conexão
  - **VLAN por SSID:** cada SSID em sua própria VLAN — isola o tráfego de visitantes do tráfego corporativo

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 30: *"Definimos o modelo Cliente-Servidor — hoje vamos ver como a rede sem fio corporativa é estruturada para suportar esse modelo com segurança"* |
| Retomada | Professor pergunta: *"Qual a diferença entre o roteador Wi-Fi da sua casa e o Wi-Fi de uma empresa grande como um shopping ou aeroporto? Por que lá o sinal é mais estável e você não precisa de senha para entrar em alguns casos?"* — alunos respondem livremente |
| Explicação | Slides — rede Wi-Fi doméstica × corporativa, componentes (roteador, AP, controlador, switch PoE), SSID e múltiplos SSIDs, canais e interferência, evolução dos padrões de segurança (WEP → WPA3), planejamento de cobertura |
| Dinâmica | "Monte a Rede Sem Fio!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: AP ≠ roteador · múltiplos SSIDs para diferentes usuários · WPA3 é o padrão atual · planejamento de cobertura evita pontos cegos · Próxima aula: Redes Corporativas e Infraestrutura Empresarial |

---

## Dinâmica — "Monte a Rede Sem Fio!"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** desenvolver o raciocínio de planejamento de infraestrutura Wi-Fi corporativa, conectando os componentes e conceitos da aula com decisões reais de projeto — preparando os grupos para incluir a solução sem fio no Projeto Integrador.

**Materiais:** cartões com cenários de infraestrutura Wi-Fi — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de infraestrutura Wi-Fi. O desafio é identificar o problema, propor a solução correta e justificar com base nos conceitos da aula.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica o problema ou a necessidade, decide qual componente ou configuração resolver e justifica tecnicamente.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os conceitos envolvidos.

**Cenários sugeridos:**

| Cenário / Problema | Solução correta | Justificativa |
|--------------------|----------------|---------------|
| Empresa com 3 andares — sinal do roteador no térreo não chega ao 3º andar | Instalar APs em cada andar conectados ao switch por cabo (PoE) | Um único roteador não cobre múltiplos andares em ambiente corporativo |
| TI quer que visitantes acessem a internet mas não a rede interna da empresa | Criar SSID Guest em VLAN separada da rede corporativa | Isolamento por VLAN impede que visitantes acessem servidores internos |
| Dois APs vizinhos interferem um no outro — usuários relatam lentidão | Configurar APs em canais não sobrepostos (1, 6 e 11 na faixa 2,4 GHz) | Co-channel interference reduz o desempenho — canais diferentes eliminam o problema |
| Rede Wi-Fi da empresa ainda usa WPA — auditor de segurança apontou como vulnerabilidade | Migrar para WPA2-Enterprise com servidor RADIUS ou WPA3 | WPA é obsoleto e vulnerável — WPA2/WPA3 com autenticação individual é o padrão |
| Funcionário reclama que o Wi-Fi cai toda vez que ele se move de uma sala para outra | Configurar roaming adequado entre APs com mesmo SSID e controlador centralizado | Roaming garante transição suave entre APs sem interrupção da conexão |
| Empresa quer identificar qual usuário está conectado em qual AP a qualquer momento | Implantar controlador Wi-Fi com WPA2-Enterprise e servidor RADIUS | Autenticação individual por usuário permite rastreabilidade e controle centralizado |
| TI percebeu que dispositivos IoT da fábrica estão na mesma rede dos computadores dos escritórios | Criar SSID IoT em VLAN separada com políticas de acesso restrito | Isolamento de IoT protege a rede corporativa de vulnerabilidades de dispositivos menos seguros |
| Novo funcionário reclamou que a senha do Wi-Fi foi compartilhada com ele por e-mail sem criptografia | Migrar para WPA2-Enterprise — cada usuário tem login e senha individual | PSK compartilhada é arriscada — se vazar, compromete toda a rede · autenticação individual elimina esse risco |

> **Nota:** o objetivo é desenvolver o raciocínio: *"qual componente, configuração ou padrão de segurança resolve esse problema?"* Reforçar que no Projeto Integrador os grupos precisarão decidir: quantos APs, em quais locais, com qual SSID, em qual faixa de frequência e com qual padrão de segurança.

---

## Conexão com o Projeto Integrador

Esta aula tem conexão direta com o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- Os grupos devem incluir no projeto a solução Wi-Fi da empresa:
  - Quantos APs são necessários para cobrir o ambiente?
  - Onde cada AP será instalado? (planta baixa simplificada)
  - Quantos SSIDs? Quais? (corporativo, guest, IoT?)
  - Qual padrão de segurança? (WPA2-Enterprise ou WPA3?)
  - Precisam de controlador centralizado?
- Esta aula fornece todos os elementos técnicos para essa parte do projeto

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 30 — 23/09/2026 · Modelos de Rede — Cliente-Servidor e Peer-to-Peer |
| Próxima aula → | Aula 32 — 07/10/2026 · Redes Corporativas e Infraestrutura Empresarial |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagrama de rede Wi-Fi corporativa com APs, switch PoE e controlador
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: mostrar ao vivo o painel de configuração de um roteador ou controlador Wi-Fi (ex.: UniFi Demo em unifi.ui.com) para ilustrar SSIDs, canais e políticas de segurança na prática

---

## Observações do Professor
