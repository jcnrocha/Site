# UC: Fundamentos de Redes de Computadores
## Aula 40 — 3º Trimestre

---

## Tema

Prova de Recuperação — 3º Trimestre

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Demonstrar recuperação do domínio dos conteúdos do 3º trimestre nos quais apresentou dificuldade na avaliação anterior
- Responder questões objetivas e discursivas com clareza, precisão e fundamentação técnica
- Comprovar o desenvolvimento das habilidades H3, H4 e H5 trabalhadas ao longo do trimestre
- Superar a média mínima exigida pela instituição para aprovação no 3º trimestre

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes · H4 — Identificar tipos e tecnologias de conexão a redes de computadores · H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Esta aula é destinada exclusivamente à aplicação da Prova de Recuperação do 3º Trimestre
- Não há explicação de conteúdo novo
- **Público:** alunos que não atingiram a média mínima na Aula 39 (3ª Avaliação Trimestral)
- **Cobertura da prova — conteúdos avaliados:**

| Bloco | Conteúdo | Aulas |
|-------|----------|-------|
| Classificação de Redes | PAN, LAN, MAN, WAN e GAN — abrangência, tecnologias e exemplos | 28 |
| Topologias de Rede | Barramento, Anel, Estrela, Malha e Híbrida — física × lógica | 29 |
| Modelos de Rede | Cliente-Servidor e Peer-to-Peer — características e uso típico | 30 |
| Redes Sem Fio | AP, PoE, SSID, canais, WEP → WPA3, roaming | 31 |
| Infraestrutura Corporativa | 3 camadas, cabeamento estruturado, DMZ, VLANs, STP | 32 |
| Computação em Nuvem | IaaS, PaaS, SaaS, pública, privada, híbrida | 33 |
| Diagnóstico de Redes | ping, tracert, ipconfig, nslookup, metodologia OSI | 34 |
| IoT e Tendências | IoT, 5G, SDN, Edge Computing, Zero Trust | 35 |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · identificação dos alunos em recuperação · organização da sala · distribuição das provas · instruções gerais |
| Retomada rápida | Professor faz revisão oral de 10 minutos — percorre os pontos críticos do trimestre com foco nos conteúdos que geraram mais erros na prova anterior |
| Aplicação da Prova | Alunos em recuperação respondem individualmente a prova completa — sem consulta · demais alunos podem realizar atividade complementar ou ficam em silêncio |
| Encerramento | Recolhimento das provas · orientações sobre a Aula 41 (Correção Comentada) · previsão de devolução com correção |

---

## Formato e Estrutura da Prova de Recuperação

- **Total de questões:** 10
- **Questões objetivas:** 5 — nível alto · 4 alternativas cada: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- **Questões discursivas:** 5 — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- **Consulta:** não permitida
- **Critério de correção:**
  - Objetivas: 1,0 ponto cada · total 5,0 pontos
  - Discursivas: 1,0 ponto cada · total 5,0 pontos
  - **Total: 10,0 pontos**
- **Média para aprovação:** conforme critério da instituição
- **Gabarito:** em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Questões da Prova de Recuperação

### PARTE 1 — Questões Objetivas

---

**Questão 1 — Classificação de Redes**

Uma operadora de telecomunicações instala uma rede de fibra óptica que interliga diferentes bairros de uma cidade, conectando residências, empresas e órgãos públicos em uma única infraestrutura metropolitana. Qual é o tipo de rede que melhor descreve essa infraestrutura?

- A) PAN — pois conecta dispositivos pessoais de uma única pessoa
- B) LAN — pois todos os dispositivos estão na mesma cidade
- C) MAN — pois abrange uma área metropolitana interligando múltiplas LANs
- D) GAN — pois a infraestrutura é gerenciada por uma operadora global

---

**Questão 2 — Topologias de Rede**

Analise a seguinte situação: *"A rede da empresa nunca ficou completamente fora do ar — mesmo quando um dos switches falhou, os demais continuaram operando normalmente porque havia múltiplos caminhos alternativos para o tráfego."* Qual topologia de rede está descrita nessa situação?

- A) Barramento — porque todos os dispositivos compartilham o mesmo cabo
- B) Estrela — porque o switch central gerencia todos os caminhos
- C) Anel — porque o tráfego percorre um caminho circular com desvio automático
- D) Malha — porque existem múltiplas conexões redundantes entre os dispositivos

---

**Questão 3 — Redes Sem Fio**

Um técnico de redes percebe que dois access points vizinhos em um escritório estão operando no mesmo canal da faixa 2,4 GHz, causando lentidão para os usuários próximos aos dois APs. Qual é a causa do problema e como resolvê-lo?

- A) Os APs estão usando WPA2 em vez de WPA3 — atualizar o padrão de segurança resolve o problema
- B) Os APs estão causando co-channel interference — configurar canais não sobrepostos (1, 6 e 11) resolve o problema
- C) Os APs estão com PoE desativado — ativar o PoE aumenta a potência do sinal e resolve a interferência
- D) Os APs precisam de mais SSIDs configurados — criar SSIDs adicionais distribui os usuários e elimina a interferência

---

**Questão 4 — Infraestrutura Corporativa e Nuvem**

Uma empresa de médio porte mantém seus dados financeiros e de RH em servidores físicos no próprio escritório por questões de conformidade com a LGPD, mas usa a AWS para hospedar o site institucional e o sistema de e-commerce. Qual modelo de nuvem essa empresa está adotando?

- A) Nuvem pública — pois usa a AWS para os serviços principais
- B) Nuvem privada — pois tem servidores físicos próprios no escritório
- C) Nuvem híbrida — pois combina infraestrutura local com serviços de nuvem pública
- D) SaaS — pois contrata software como serviço de terceiros

---

**Questão 5 — IoT e SDN**

Uma grande empresa de telecomunicações migra sua infraestrutura de rede para um modelo onde um controlador centralizado define as regras de roteamento para todos os switches da rede, que passam a apenas encaminhar pacotes conforme as instruções recebidas. Qual tecnologia está sendo implementada?

- A) VLAN — segmentação lógica da rede por departamento
- B) SDN — Software Defined Networking, com separação do plano de controle e plano de dados
- C) DMZ — zona desmilitarizada para proteção de servidores públicos
- D) LoRaWAN — protocolo de longa distância para dispositivos IoT

---

### PARTE 2 — Questões Discursivas

---

**Questão 6 — Classificação e Topologia**

**Da PAN à GAN: A Escala das Redes**

Descreva as cinco classificações de redes por abrangência (PAN, LAN, MAN, WAN e GAN), indicando para cada uma: a abrangência geográfica típica, um exemplo real do cotidiano e uma tecnologia de conexão típica.

`R:`

---

**Questão 7 — Modelos de Rede**

**Peer-to-Peer: Quando Faz Sentido?**

Explique o modelo Peer-to-Peer (P2P), descrevendo suas características principais, vantagens e desvantagens. Cite dois exemplos reais de aplicações que utilizam P2P e explique por que esse modelo NÃO é recomendado para ambientes corporativos com dados sensíveis.

`R:`

---

**Questão 8 — Infraestrutura Corporativa**

**Cabeamento Estruturado e Sala de Servidores**

Explique o que é cabeamento estruturado e quais são seus componentes principais (ponto de telecomunicações, cabeamento horizontal, patch panel e backbone). Em seguida, descreva os requisitos mínimos de uma sala de servidores corporativa, explicando a função de cada elemento.

`R:`

---

**Questão 9 — Diagnóstico de Redes**

**Tracert: Mapeando o Caminho dos Pacotes**

Explique o que é o comando tracert (Windows) / traceroute (Linux) e como ele funciona. Descreva como interpretar o resultado — o que cada linha representa, o que significa quando aparece `* * *` em um salto e como usar essa ferramenta para identificar onde um problema de conectividade está ocorrendo.

`R:`

---

**Questão 10 — IoT e Redes do Futuro**

**O Impacto do 5G nas Redes**

Explique as três capacidades fundamentais do 5G (eMBB, URLLC e mMTC) e como cada uma viabiliza um tipo diferente de aplicação. Para cada capacidade, cite um caso de uso real que seria inviável com a tecnologia 4G atual.

`R:`

---

## Gabarito — Uso Exclusivo do Professor

### Objetivas

| Questão | Gabarito | Justificativa |
|---------|----------|---------------|
| 1 | C | MAN (Metropolitan Area Network) abrange uma cidade interligando múltiplas LANs · PAN é pessoal (poucos metros) · LAN é local (um prédio/campus) · GAN é global (mundial) · o critério é a abrangência geográfica, não quem gerencia |
| 2 | D | Múltiplos caminhos alternativos com tolerância a falha de switch = característica da topologia Malha (partial mesh) · Barramento tem ponto único de falha no cabo · Estrela tem ponto único de falha no switch central · Anel simples derruba toda a rede com falha em um nó |
| 3 | B | Co-channel interference ocorre quando APs vizinhos usam o mesmo canal — os sinais colidem e degradam o desempenho · solução: canais não sobrepostos 1, 6 e 11 na faixa 2,4 GHz · WPA2/WPA3 é padrão de segurança, não afeta interferência de canal · PoE fornece energia, não controla canal |
| 4 | C | Nuvem híbrida = combinação de infraestrutura local (on-premises) com nuvem pública · dados sensíveis no servidor físico (conformidade LGPD) + serviços na AWS = modelo híbrido clássico · não é apenas pública nem apenas privada |
| 5 | B | SDN (Software Defined Networking) = separação do plano de controle (controlador centralizado decide o roteamento) do plano de dados (switches apenas encaminham) · VLAN é segmentação lógica · DMZ é zona de segurança perimetral · LoRaWAN é protocolo IoT |

### Discursivas — Critérios de Correção

**Questão 6 — PAN à GAN**

*Resposta esperada:*
- **PAN:** poucos metros · smartwatch ↔ celular · Bluetooth/NFC
- **LAN:** prédio/campus · rede do escritório ou escola · Ethernet/Wi-Fi
- **MAN:** cidade/região · rede da prefeitura ou operadora local · fibra óptica metropolitana
- **WAN:** países/continentes · rede corporativa com filiais em estados diferentes · links MPLS/VPN de operadora
- **GAN:** mundial · a própria internet · cabos submarinos de fibra óptica e satélites

*Critérios:* cada tipo com abrangência + exemplo + tecnologia corretos (0,2 pt cada = 1,0 pt total)

---

**Questão 7 — Peer-to-Peer**

*Resposta esperada:*
- **Características:** sem servidor central · cada dispositivo (peer) é cliente e servidor simultaneamente · comunicação direta entre peers · descentralizado
- **Vantagens:** baixo custo (sem servidor dedicado) · sem ponto único de falha · escalabilidade natural · simples para redes pequenas
- **Desvantagens:** segurança fraca (difícil controlar acesso) · gerenciamento descentralizado · desempenho variável · não recomendado para dados sensíveis
- **Exemplos reais:** BitTorrent (compartilhamento de arquivos) · Bitcoin/blockchain (transações sem banco central) · jogos LAN party · Skype original
- **Por que não corporativo:** impossível aplicar políticas de segurança consistentes · sem controle centralizado de permissões · dados sensíveis ficam expostos nos peers · sem auditoria de acesso

*Critérios:* características + vantagens + desvantagens (0,4 pt) · dois exemplos válidos (0,2 pt) · justificativa para ambiente corporativo (0,4 pt)

---

**Questão 8 — Cabeamento Estruturado e Sala de Servidores**

*Resposta esperada:*
- **Cabeamento estruturado:** sistema padronizado e documentado de cabeamento de rede (ABNT NBR 14565 / ANSI/TIA-568)
  - PT (Ponto de Telecomunicações): tomada na parede onde o dispositivo conecta
  - Cabeamento horizontal: cabo do PT ao patch panel · máximo 90 metros
  - Patch panel: painel que termina o cabeamento horizontal e organiza as conexões no rack
  - Backbone: cabeamento entre andares/prédios · geralmente fibra óptica
- **Sala de servidores:**
  - Rack: estrutura que organiza servidores e equipamentos verticalmente
  - Ar-condicionado dedicado: controle de temperatura (servidores geram muito calor)
  - No-break (UPS): energia imediata em caso de queda — evita perda de dados
  - Gerador: para quedas prolongadas de energia
  - Controle de acesso físico: apenas pessoal autorizado

*Critérios:* componentes do cabeamento estruturado (0,5 pt) · requisitos da sala de servidores com função de cada elemento (0,5 pt)

---

**Questão 9 — Tracert/Traceroute**

*Resposta esperada:*
- **O que é:** ferramenta que mapeia o caminho (rota) dos pacotes da origem ao destino, identificando cada roteador intermediário (hop/salto)
- **Como funciona:** envia pacotes com TTL crescente (1, 2, 3...) · cada roteador decrementa o TTL · quando TTL chega a 0, o roteador envia uma mensagem ICMP de volta · assim o tracert descobre cada salto no caminho
- **Interpretação:**
  - Cada linha = um roteador no caminho (endereço IP + tempo de resposta em ms)
  - `* * *` = o roteador não responde ao ICMP (firewall bloqueando) — não significa necessariamente problema
  - Tempo alto em um salto = gargalo ou problema de latência naquele ponto da rota
  - Onde o tracert para = onde o pacote está sendo bloqueado ou perdido
- **Uso no diagnóstico:** site fora do ar → tracert mostra até qual salto o pacote chega → identifica se o problema é no link local, no ISP ou no servidor de destino

*Critérios:* definição correta (0,2 pt) · funcionamento com TTL (0,2 pt) · interpretação correta de cada linha e `* * *` (0,4 pt) · uso no diagnóstico (0,2 pt)

---

**Questão 10 — Três Capacidades do 5G**

*Resposta esperada:*
- **eMBB (Enhanced Mobile Broadband):** velocidades de até 20 Gbps · para aplicações que exigem altíssima largura de banda · caso de uso: streaming de vídeo 8K em tempo real ou realidade virtual imersiva — inviável com 4G (máximo ~150 Mbps real)
- **URLLC (Ultra-Reliable Low-Latency Communications):** latência de ~1 ms com altíssima confiabilidade · para aplicações críticas em tempo real · caso de uso: cirurgia remota com braço robótico ou controle de veículo autônomo — 4G tem latência de 30–50 ms, inaceitável para controle em tempo real
- **mMTC (Massive Machine-Type Communications):** suporte a até 1 milhão de dispositivos por km² · para IoT em escala urbana · caso de uso: cidade inteligente com sensores em cada semáforo, lixeira, poste e veículo simultaneamente — 4G não suporta essa densidade de dispositivos

*Critérios:* cada capacidade com definição correta + caso de uso válido + justificativa de por que 4G não atende (0,33 pt cada ≈ 1,0 pt total)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 39 — 25/11/2026 · Prova — 3ª Avaliação Trimestral |
| Próxima aula → | Aula 41 — 09/12/2026 · Correção Comentada das Provas do 3º Trimestre |

---

## Recursos Necessários

- Projetor ou TV (opcional — para exibir o tempo restante ou revisão oral inicial)
- Prova de recuperação impressa — 1 cópia por aluno em recuperação
- Gabarito impresso — uso exclusivo do professor
- Lista de chamada com identificação dos alunos em recuperação
- Atividade complementar impressa para os demais alunos (opcional)

---

## Observações do Professor
