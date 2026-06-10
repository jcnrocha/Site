# UC: Fundamentos de Redes de Computadores
## Aula 37 — 3º Trimestre

---

## Tema

Apresentação do Projeto Integrador + Revisão Geral

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Apresentar o projeto de rede corporativa desenvolvido em grupo com clareza, domínio técnico e organização
- Justificar oralmente as decisões técnicas do projeto — respondendo perguntas e defendendo as escolhas realizadas
- Avaliar criticamente os projetos dos outros grupos — identificando pontos fortes e oportunidades de melhoria
- Consolidar os principais conteúdos do 3º trimestre a partir da revisão integrada realizada após as apresentações
- Preparar-se para a prova trimestral (Aula 39) com visão consolidada de todos os conteúdos

**Habilidade da matriz:** H1 · H2 · H3 · H4 · H5 — consolidação integrada de todas as habilidades da UC

---

## Conteúdo

- Esta aula tem duas partes distintas:
  - **Parte 1 (primeiro tempo):** Apresentações dos Projetos Integradores
  - **Parte 2 (segundo tempo):** Revisão Geral do 3º Trimestre

---

## PARTE 1 — Apresentações dos Projetos Integradores

### Organização das Apresentações

- **Tempo por grupo:** 10 a 12 minutos de apresentação + 3 minutos de perguntas
- **Ordem:** sorteada no início da aula
- **Quem apresenta:** todos os membros do grupo participam — cada integrante apresenta pelo menos uma parte
- **Recursos:** projetor ou TV · grupos podem usar slides, papel A3 ou ferramenta de diagrama (draw.io, Packet Tracer)

### Roteiro Sugerido para Cada Apresentação

| Etapa | Conteúdo | Tempo |
|-------|----------|-------|
| Contexto | Apresentar o cenário da empresa — quem é, quantos funcionários, quantos andares, quais necessidades | 1 min |
| Diagrama | Exibir e explicar o diagrama de rede — percorrer os componentes de fora para dentro (ISP → roteador → firewall → switch → dispositivos) | 4 min |
| Decisões técnicas | Explicar as principais decisões: topologia, VLANs, endereçamento IP, Wi-Fi e segurança | 4 min |
| Diferenciais | Apresentar itens extras: nuvem, IoT, redundância, plano de diagnóstico, visão de futuro | 2 min |
| Perguntas | Professor e colegas fazem perguntas técnicas ao grupo | 3 min |

### Perguntas Técnicas Sugeridas para o Professor

> Usar essas perguntas para aprofundar a avaliação técnica de cada grupo:

- *"Por que vocês escolheram a topologia Estrela e não a Malha para esta rede?"*
- *"Explique o endereçamento IP que vocês usaram — por que essa faixa? A máscara suporta a quantidade de hosts do cenário?"*
- *"Se o switch principal falhar, o que acontece com a rede? Há algum mecanismo de redundância?"*
- *"Por que o servidor de arquivos está dentro da rede interna e não na DMZ?"*
- *"Qual é a VLAN dos visitantes? O que eles conseguem acessar? O que eles não conseguem?"*
- *"Se um dispositivo IoT for comprometido, como a rede está protegida para que o invasor não alcance os computadores dos funcionários?"*
- *"Qual padrão de segurança Wi-Fi vocês escolheram? Por que não usar WPA2-Personal neste cenário corporativo?"*
- *"Como vocês fariam o diagnóstico se um funcionário reclamasse que não consegue acessar o servidor de arquivos?"*

### Ficha de Avaliação do Projeto (por grupo)

| Critério | Descrição | Nota (0–10) |
|----------|-----------|-------------|
| Coerência técnica | As escolhas são adequadas ao cenário? Componentes corretos? | |
| Diagrama e simbologia | Diagrama legível, completo e com simbologia correta? | |
| Endereçamento IP | Faixa correta, máscaras adequadas, hosts dimensionados? | |
| Justificativa técnica | As decisões foram explicadas com base nos conteúdos da UC? | |
| Apresentação oral | Clareza, participação de todos, domínio do conteúdo, respostas às perguntas? | |
| **Nota final** | Média ponderada dos critérios conforme definido na Aula 36 | |

---

## PARTE 2 — Revisão Geral do 3º Trimestre

### Estrutura da Revisão

- Após as apresentações, professor conduz revisão oral dos principais conteúdos do trimestre
- Foco nos tópicos com maior índice de dúvida identificado durante as apresentações e nos conteúdos de maior peso na prova

### Mapa do 3º Trimestre — Conteúdos Revisados

| Aula | Data | Tema | Habilidade |
|------|------|------|------------|
| 28 | 09/09 | Classificação das Redes por Abrangência (PAN/LAN/MAN/WAN/GAN) | H5 |
| 29 | 16/09 | Topologias de Rede — Física e Lógica | H5 |
| 30 | 23/09 | Modelos de Rede — Cliente-Servidor e Peer-to-Peer | H5 |
| 31 | 30/09 | Redes Sem Fio — Padrões e Infraestrutura | H4 · H5 |
| 32 | 07/10 | Redes Corporativas e Infraestrutura Empresarial | H5 |
| 33 | 14/10 | Computação em Nuvem e Redes | H5 |
| 34 | 21/10 | Diagnóstico e Solução de Problemas em Redes | H3 · H4 |
| 35 | 28/10 | Tendências em Redes — IoT e Redes do Futuro | H4 · H5 |

### Pontos-Chave da Revisão por Bloco

- **Classificação por abrangência (Aula 28)**
  - PAN: pessoal, poucos metros, Bluetooth/NFC
  - LAN: local, prédio/campus, Ethernet/Wi-Fi
  - MAN: cidade, fibra metropolitana
  - WAN: países, links de operadoras, VPN
  - GAN: mundial, internet, cabos submarinos

- **Topologias (Aula 29)**
  - Barramento: obsoleta, ponto único de falha no cabo
  - Anel: obsoleta, token ring, falha derruba o anel
  - Estrela: padrão atual de LAN, switch central, isolamento de falhas
  - Malha: redundância total, WAN e data centers
  - Híbrida: corporativa, combina topologias por necessidade

- **Modelos de rede (Aula 30)**
  - Cliente-Servidor: papéis fixos, gerenciamento centralizado, segurança robusta
  - P2P: papéis dinâmicos, sem servidor central, baixo custo
  - Híbrido: WhatsApp, jogos online, CDN

- **Redes sem fio corporativas (Aula 31)**
  - AP ≠ roteador · PoE · controlador Wi-Fi · roaming
  - SSID corporativo × guest × IoT em VLANs separadas
  - WEP (obsoleto) → WPA → WPA2 → WPA3 (padrão atual)
  - WPA2-Enterprise com RADIUS para autenticação individual

- **Infraestrutura corporativa (Aula 32)**
  - Três camadas: núcleo (velocidade) · distribuição (controle) · acesso (conectividade)
  - Sala de servidores: rack, patch panel, UPS, controle de temperatura
  - Cabeamento estruturado: PT → cabo horizontal → patch panel → switch
  - DMZ: servidores públicos isolados entre dois firewalls
  - VLANs: segmentação lógica por departamento ou função

- **Computação em nuvem (Aula 33)**
  - IaaS: infraestrutura alugada (EC2, VMs)
  - PaaS: plataforma para desenvolver apps (Heroku, App Service)
  - SaaS: software pronto para usar (Gmail, Office 365)
  - Pública × privada × híbrida
  - Impacto: mais banda, VPN para nuvem, responsabilidade compartilhada

- **Diagnóstico de redes (Aula 34)**
  - Metodologia OSI: bottom-up, top-down, divide and conquer
  - ping: conectividade e latência
  - tracert/traceroute: mapeamento do caminho
  - ipconfig/ifconfig: configuração IP do dispositivo
  - nslookup: resolução de nomes DNS
  - IP 169.254.x.x = DHCP não respondeu

- **Tendências (Aula 35)**
  - IoT: bilhões de dispositivos · MQTT, Zigbee, LoRaWAN · VLAN IoT obrigatória
  - 5G: eMBB (velocidade) · URLLC (latência 1ms) · mMTC (densidade)
  - SDN: plano de controle separado do plano de dados · rede programável
  - Edge computing: processamento na borda · reduz latência e banda
  - Zero Trust: nunca confie, sempre verifique

---

## Organização do Tempo

| Etapa | Atividade | Tempo estimado |
|-------|-----------|----------------|
| Abertura | Chamada · sorteio da ordem de apresentação · orientações finais | 5 min |
| Apresentações | Cada grupo apresenta o Projeto Integrador | ~60 min (5 grupos × ~12 min) |
| Intervalo | Breve pausa entre as apresentações e a revisão | 5 min |
| Revisão geral | Professor conduz revisão oral dos 8 blocos do trimestre com perguntas à turma | ~25 min |
| Fechamento | Orientações sobre o formato da prova da Aula 39 · dúvidas finais | 5 min |

---

## Avaliação

- Esta aula não tem questionário individual
- A avaliação é feita pela **Ficha de Avaliação do Projeto** (seção acima)
- O professor pode solicitar autoavaliação dos grupos ao final: *"O que seu grupo faria diferente se tivesse mais tempo?"*
- A revisão oral é formativa — sem nota, mas essencial para a preparação da prova

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 36 — 04/11/2026 · Projeto Integrador — Desenho de Rede Corporativa |
| Próxima aula → | Aula 38 — 18/11/2026 · Revisão Geral — Todos os Trimestres |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Cronômetro para controle do tempo de cada apresentação
- Ficha de avaliação impressa — 1 por grupo avaliado (professor preenche durante as apresentações)
- Slides com o mapa do trimestre para a revisão (segunda parte da aula)
- Quadro branco e marcador para anotar dúvidas levantadas durante as apresentações

---

## Observações do Professor
