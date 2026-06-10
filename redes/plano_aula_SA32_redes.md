# UC: Fundamentos de Redes de Computadores
## Aula 32 — 3º Trimestre

---

## Tema

Redes Corporativas e Infraestrutura Empresarial

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender como uma rede corporativa é organizada e quais são seus componentes principais
- Identificar os elementos de uma infraestrutura empresarial de rede: sala de servidores, cabeamento estruturado e DMZ
- Reconhecer o conceito de VLAN e sua utilidade no isolamento e organização do tráfego de rede
- Diferenciar os níveis de uma rede corporativa em camadas: acesso, distribuição e núcleo
- Relacionar os conceitos de infraestrutura corporativa com o planejamento do Projeto Integrador

**Habilidade da matriz:** H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 31: *"Vimos a infraestrutura sem fio corporativa — hoje ampliamos a visão para toda a infraestrutura de rede de uma empresa: cabeada, sem fio, servidores e segurança"*
- **Por que a infraestrutura corporativa é mais complexa que a doméstica?**
  - Uma rede doméstica serve poucos dispositivos com necessidades simples
  - Uma rede corporativa precisa garantir: disponibilidade 24/7, segurança em camadas, escalabilidade, gerenciamento centralizado e separação de tráfego por departamento ou função

- **Modelo de três camadas da rede corporativa:**
  - **Camada de Núcleo (Core Layer)**
    - O backbone da rede — responsável pelo tráfego de alta velocidade entre os demais componentes
    - Switches de núcleo de alta performance com links redundantes
    - Não conecta dispositivos finais diretamente — apenas interliga as camadas de distribuição
    - Prioridade: velocidade, baixa latência e redundância
  - **Camada de Distribuição (Distribution Layer)**
    - Interliga a camada de núcleo com as camadas de acesso
    - Aplica políticas de roteamento, ACLs (listas de controle de acesso) e QoS
    - Agrega o tráfego dos switches de acesso antes de encaminhar ao núcleo
    - Prioridade: controle de tráfego, segurança e gerenciamento
  - **Camada de Acesso (Access Layer)**
    - Conecta diretamente os dispositivos finais: computadores, impressoras, telefones IP, APs
    - Switches de acesso com portas para os dispositivos do usuário
    - Prioridade: conectividade, PoE para APs e telefones IP, controle de porta

- **Sala de Servidores (Data Room / Server Room)**
  - Ambiente físico controlado que abriga os servidores e equipamentos críticos da rede
  - Requisitos físicos:
    - **Controle de temperatura e umidade:** ar-condicionado dedicado — servidores geram muito calor
    - **No-break (UPS):** fornece energia elétrica em caso de queda — evita perda de dados
    - **Gerador:** para quedas prolongadas de energia
    - **Rack:** estrutura metálica que organiza servidores, switches e patch panels verticalmente
    - **Patch panel:** painel de conexões que organiza os cabos vindos dos pontos de rede do ambiente
    - **Controle de acesso físico:** somente pessoal autorizado entra na sala de servidores
  - Servidores típicos em uma empresa:
    - Servidor de arquivos (file server)
    - Servidor de autenticação (Active Directory / LDAP)
    - Servidor de e-mail
    - Servidor de banco de dados
    - Servidor de backup

- **Cabeamento Estruturado**
  - Sistema padronizado de cabeamento que organiza todos os cabos da rede de forma planejada e documentada
  - Baseado nas normas ABNT NBR 14565 (Brasil) e ANSI/TIA-568 (EUA)
  - Componentes do cabeamento estruturado:
    - **Ponto de telecomunicações (PT):** tomada de rede na parede onde o usuário conecta o dispositivo
    - **Cabeamento horizontal:** cabo que vai do PT ao patch panel no rack — máximo de 90 metros
    - **Patch panel:** painel de conexões que termina o cabeamento horizontal e organiza os cabos no rack
    - **Patch cord:** cabo curto que conecta o patch panel ao switch e o PT ao dispositivo final
    - **Backbone:** cabeamento que interliga os racks entre andares ou prédios — geralmente fibra óptica
  - Vantagens: organização, facilidade de manutenção, documentação e escalabilidade

- **DMZ — Demilitarized Zone (Zona Desmilitarizada)**
  - Segmento de rede separado que fica entre a rede interna (LAN) e a internet (WAN)
  - Abriga servidores que precisam ser acessíveis pela internet mas que não devem ter acesso direto à rede interna
  - Servidores típicos na DMZ: servidor web, servidor de e-mail, servidor FTP público, servidor DNS
  - Como funciona:
    - Firewall externo: filtra o tráfego entre a internet e a DMZ
    - Firewall interno: filtra o tráfego entre a DMZ e a rede interna
    - Se um servidor da DMZ for comprometido, o invasor ainda precisa superar o firewall interno para acessar a rede corporativa
  - Analogia: a DMZ é como a recepção de um prédio — visitantes entram na recepção, mas não têm acesso direto aos escritórios internos

- **VLANs — Virtual Local Area Networks**
  - Segmentação lógica da rede física em múltiplas redes virtuais independentes
  - Dispositivos na mesma VLAN comunicam-se diretamente · dispositivos em VLANs diferentes precisam passar por um roteador ou switch L3
  - Por que usar VLANs:
    - **Segurança:** isola o tráfego de diferentes departamentos — financeiro não acessa rede de produção
    - **Desempenho:** reduz o domínio de broadcast — menos tráfego desnecessário em cada segmento
    - **Organização:** cada departamento ou função em sua própria VLAN
    - **Flexibilidade:** reorganização lógica sem mexer no cabeamento físico
  - Exemplos de VLANs em uma empresa:

| VLAN ID | Nome | Dispositivos |
|---------|------|-------------|
| VLAN 10 | Administração | Computadores do RH, Financeiro e Diretoria |
| VLAN 20 | Produção | Computadores do setor produtivo |
| VLAN 30 | TI | Computadores e servidores da equipe de TI |
| VLAN 40 | Wi-Fi Corporativo | Notebooks e celulares dos funcionários |
| VLAN 50 | Guest | Dispositivos de visitantes |
| VLAN 60 | IoT | Câmeras, sensores e dispositivos inteligentes |
| VLAN 99 | Gerenciamento | Switches e APs — acesso apenas da TI |

- **Alta disponibilidade em redes corporativas:**
  - **Redundância de links:** dois cabos entre switches críticos — se um cair, o outro assume
  - **STP (Spanning Tree Protocol):** evita loops na rede quando há links redundantes
  - **Balanceamento de carga:** distribui o tráfego entre múltiplos links ativos simultaneamente
  - **Failover:** troca automática para o link reserva em caso de falha — sem intervenção manual

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 31: *"Estruturamos a rede sem fio — hoje montamos o quadro completo da infraestrutura corporativa: cabeamento, servidores, DMZ e VLANs"* |
| Retomada | Professor pergunta: *"Se você fosse o responsável pela TI de uma empresa com 100 funcionários em 3 andares, como organizaria a rede para que o financeiro não acesse os arquivos da produção e vice-versa? E como garantiria que o site da empresa fique acessível pela internet sem expor os servidores internos?"* — alunos respondem livremente |
| Explicação | Slides — modelo de três camadas (núcleo, distribuição, acesso), sala de servidores, cabeamento estruturado, DMZ, VLANs com tabela de exemplos, alta disponibilidade |
| Dinâmica | "Projete a Infraestrutura!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: três camadas organizam o tráfego · cabeamento estruturado é a base física · DMZ protege os servidores públicos · VLANs segmentam logicamente a rede · Conexão com o Projeto Integrador: aplicar esses conceitos no projeto · Próxima aula: Computação em Nuvem e Redes |

---

## Dinâmica — "Projete a Infraestrutura!"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** desenvolver o raciocínio de projeto de infraestrutura corporativa, integrando os conceitos de VLANs, DMZ, cabeamento estruturado e sala de servidores em cenários reais — preparando diretamente os grupos para o Projeto Integrador.

**Materiais:** cartões com cenários corporativos — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com situações de infraestrutura corporativa. O desafio é identificar o problema, propor a solução correta e justificar tecnicamente.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão e propõe a solução baseada nos conceitos da aula.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os conceitos envolvidos.

**Cenários sugeridos:**

| Cenário / Problema | Solução correta | Justificativa |
|--------------------|----------------|---------------|
| Funcionário do RH acessou por engano arquivos confidenciais do setor financeiro na rede | Criar VLANs separadas para RH e Financeiro com políticas de acesso entre elas | Isolamento lógico por VLAN impede acesso indevido entre departamentos |
| Servidor web da empresa precisa ser acessado pela internet mas não pode ver os servidores internos | Colocar o servidor web na DMZ com firewall entre DMZ e rede interna | DMZ isola servidores públicos da rede interna — mesmo que o servidor seja comprometido, a rede interna está protegida |
| Empresa cresceu e o rack está com cabos totalmente desorganizados — manutenção é lenta e arriscada | Implementar cabeamento estruturado com patch panel, etiquetagem e documentação | Cabeamento estruturado padroniza e documenta cada ponto de rede — manutenção rápida e segura |
| Switch do andar térreo falhou e toda a empresa perdeu a rede | Implementar redundância de links com STP entre switches críticos | Links redundantes com STP garantem failover automático sem interrupção da rede |
| Dispositivos IoT (câmeras e sensores) estão na mesma rede dos computadores da diretoria | Criar VLAN IoT separada com acesso restrito aos sistemas internos | Dispositivos IoT têm segurança mais fraca — isolamento protege dados sensíveis da diretoria |
| TI precisa gerenciar os switches remotamente mas não quer que essa porta de gerenciamento seja acessível por funcionários | Criar VLAN de gerenciamento (ex.: VLAN 99) acessível apenas pela equipe de TI | VLAN de gerenciamento isola o acesso administrativo aos equipamentos de rede |
| Sala de servidores está sujeita a quedas de energia frequentes — houve perda de dados | Instalar no-break (UPS) e gerador com transferência automática | UPS garante energia imediata · gerador sustenta por períodos prolongados · evita perda de dados e danos ao hardware |
| Nova empresa com 50 funcionários em 2 andares — TI quer saber por onde começar a projetar a rede | Definir: topologia Estrela, 3 camadas (núcleo/distribuição/acesso), VLANs por departamento, sala de servidores com rack, cabeamento estruturado e AP por andar | Sequência lógica de projeto corporativo — da estrutura física ao segmento lógico |

> **Nota:** o objetivo é desenvolver o raciocínio integrado: *"qual problema de infraestrutura está sendo descrito? Qual conceito — VLAN, DMZ, cabeamento, redundância — resolve esse problema?"* Esta dinâmica é um ensaio direto para o Projeto Integrador — cada decisão aqui será replicada no projeto dos grupos.

---

## Conexão com o Projeto Integrador

Esta aula é a mais diretamente conectada ao **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- Após esta aula, os grupos têm todos os elementos técnicos para estruturar o projeto completo:
  - **Aula 28:** tipo de rede (LAN corporativa)
  - **Aula 29:** topologia (Estrela / Híbrida)
  - **Aula 30:** modelo (Cliente-Servidor)
  - **Aula 31:** solução sem fio (APs, SSIDs, WPA3)
  - **Aula 32:** infraestrutura completa (VLANs, DMZ, cabeamento, sala de servidores)
- O professor pode orientar os grupos a começar a montar o diagrama da rede corporativa do projeto ainda nesta semana

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 31 — 30/09/2026 · Redes Sem Fio — Padrões e Infraestrutura |
| Próxima aula → | Aula 33 — 14/10/2026 · Computação em Nuvem e Redes |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagrama completo de rede corporativa com três camadas, DMZ, VLANs e sala de servidores
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: papel A3 e canetas coloridas para que os grupos comecem a esboçar o diagrama do Projeto Integrador ao final da aula

---

## Observações do Professor
