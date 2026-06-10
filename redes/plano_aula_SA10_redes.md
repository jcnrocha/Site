# UC: Fundamentos de Redes de Computadores
## Aula 10 — 1º Trimestre

---

## Tema

Prova — 1ª Avaliação Trimestral

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Demonstrar domínio dos conteúdos trabalhados ao longo do 1º trimestre: unidades de medida, simbologias, componentes passivos, componentes ativos, interfaces e serviços de internet
- Responder questões objetivas e discursivas com clareza, precisão e fundamentação técnica
- Aplicar o raciocínio de identificação, comparação e escolha de componentes e tecnologias em situações práticas
- Demonstrar as habilidades H1, H2, H3 e H4 desenvolvidas ao longo do trimestre

**Habilidade da matriz:** H1 — Unidades de medida · H2 — Simbologias básicas de rede · H3 — Componentes e ativos de redes · H4 — Tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Esta aula é destinada exclusivamente à aplicação da 1ª Avaliação Trimestral
- Não há explicação de conteúdo novo
- **Cobertura da prova — conteúdos avaliados:**

| Bloco | Conteúdo | Aulas |
|-------|----------|-------|
| Unidades de Medida | Bits, bytes, KB, MB, GB, TB · bps, Kbps, Mbps, Gbps · conversões · latência · throughput | 02 e 03 |
| Armazenamento em Redes | DAS, NAS, SAN e armazenamento em nuvem | 04 |
| Simbologias de Rede | Dispositivos, meios de transmissão, firewall, DMZ, nuvem, leitura e criação de diagramas | 05 e 06 |
| Componentes Passivos | Cabos (par trançado, fibra, coaxial), conectores (RJ-45, SC, LC), rack, patch panel | 07 |
| Componentes Ativos | Hub, switch, roteador, access point, modem, NIC — funções e camadas OSI | 08 |
| Interfaces e Serviços | Ethernet, Wi-Fi, fibra SFP, USB, Bluetooth · ADSL, FTTH, HFC, 4G, 5G, Satélite | 09 |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · organização da sala · distribuição das provas · instruções gerais |
| Aplicação da Prova | Alunos respondem individualmente a prova completa — sem consulta |
| Encerramento | Recolhimento das provas · orientações sobre a Aula 11 (Recuperação) · previsão de devolução com correção |

---

## Formato e Estrutura da Prova

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

## Questões da Prova

### PARTE 1 — Questões Objetivas

---

**Questão 1 — Unidades de Medida**

Um plano de internet residencial é anunciado com velocidade de 400 Mbps. Qual é a velocidade máxima de download esperada em megabytes por segundo (MB/s) e por que a velocidade anunciada pelas operadoras é sempre em Mbps e não em MB/s?

- A) 400 MB/s — porque 1 Megabit equivale a 1 Megabyte
- B) 50 MB/s — porque 1 byte equivale a 8 bits, portanto 400 ÷ 8 = 50 MB/s
- C) 3.200 MB/s — porque 1 byte equivale a 8 bits, portanto 400 × 8 = 3.200 MB/s
- D) 100 MB/s — porque a velocidade real é sempre 25% da velocidade anunciada

---

**Questão 2 — Simbologias de Rede**

Em um diagrama de rede, um técnico precisa representar a seguinte situação: *"O servidor web da empresa deve ser acessível pela internet, mas não pode ter acesso direto aos servidores internos da rede corporativa."* Qual conjunto de elementos deve aparecer obrigatoriamente no diagrama para representar essa situação corretamente?

- A) Nuvem → Switch → Servidor Web → Rede Interna
- B) Nuvem → Roteador → Servidor Web → Switch → Rede Interna
- C) Nuvem → Firewall Externo → DMZ (com Servidor Web) → Firewall Interno → Rede Interna
- D) Nuvem → Firewall → Switch → Servidor Web + Rede Interna (mesmo segmento)

---

**Questão 3 — Componentes Passivos e Ativos**

Analise as afirmações abaixo sobre componentes de rede:

I. O switch opera na Camada 2 do modelo OSI e encaminha quadros com base no endereço MAC de destino.
II. O hub é mais eficiente que o switch porque repassa os dados para todas as portas simultaneamente, aumentando o alcance do sinal.
III. O patch panel é um componente passivo que organiza e termina o cabeamento horizontal no rack.
IV. O roteador conecta redes diferentes e toma decisões de encaminhamento com base no endereço IP.

Estão **corretas** apenas as afirmações:

- A) I e II
- B) II e III
- C) I, III e IV
- D) I, II, III e IV

---

**Questão 4 — Armazenamento em Redes**

Uma empresa de médio porte com 40 funcionários precisa de uma solução de armazenamento centralizado que permita acesso simultâneo por todos os usuários da rede local, tenha redundância de dados via RAID e possa ser gerenciada por interface web sem necessidade de monitor dedicado. Qual tipo de armazenamento atende melhor a esses requisitos?

- A) DAS — pois oferece alta velocidade de acesso direto para múltiplos usuários
- B) NAS — pois é conectado à rede local e suporta acesso simultâneo com gerenciamento via interface web
- C) SAN — pois é a solução mais barata e simples para pequenas e médias empresas
- D) Armazenamento em nuvem — pois elimina a necessidade de qualquer hardware local

---

**Questão 5 — Interfaces e Serviços de Internet**

Um técnico de redes precisa recomendar o serviço de internet mais adequado para uma empresa com 60 funcionários que realiza videoconferências diárias, faz upload frequente de arquivos grandes para servidores e precisa de uma conexão com velocidade simétrica (download = upload) e baixa latência. Qual serviço atende melhor a esses requisitos?

- A) ADSL — pois é amplamente disponível e de fácil instalação
- B) Internet via TV a Cabo (HFC) — pois oferece alta velocidade de download
- C) FTTH (Fibra Óptica) — pois oferece velocidade simétrica, baixa latência e conexão dedicada
- D) 4G LTE — pois oferece mobilidade e cobertura ampla em todo o Brasil

---

### PARTE 2 — Questões Discursivas

---

**Questão 6 — Unidades de Medida na Prática**

**Dimensionando o Link de Internet de uma Empresa**

Uma empresa precisa fazer backup diário de 200 GB de dados para um servidor na nuvem. O processo deve ser concluído em no máximo 2 horas (7.200 segundos). Calcule a velocidade mínima de upload necessária em MB/s e em Mbps. Mostre o raciocínio completo e explique se um plano de fibra de 200 Mbps simétrico seria suficiente para essa demanda.

`R:`

---

**Questão 7 — Simbologias e Diagrama de Rede**

**Lendo e Interpretando um Diagrama**

Descreva os elementos que devem estar presentes em um diagrama de rede completo de uma pequena empresa com: acesso à internet, um servidor de arquivos interno, uma zona DMZ com servidor web público e rede Wi-Fi para funcionários. Para cada elemento, indique o símbolo utilizado e a função que ele representa no diagrama.

`R:`

---

**Questão 8 — Componentes Passivos**

**Par Trançado: Categorias e Aplicações**

Explique a diferença entre os cabos Cat5e, Cat6 e Cat6A em relação à velocidade máxima suportada e à distância. Para cada categoria, indique um cenário de uso adequado e justifique por que a categoria escolhida é a mais indicada para aquele cenário.

`R:`

---

**Questão 9 — Componentes Ativos**

**Switch vs. Roteador: Confusão Clássica**

Explique a diferença fundamental entre um switch e um roteador, indicando: a camada do modelo OSI em que cada um opera, o tipo de endereçamento que cada um utiliza e uma situação real em que cada equipamento é necessário. Por que em uma rede doméstica o roteador Wi-Fi parece "fazer tudo", mas em uma rede corporativa esses equipamentos são separados?

`R:`

---

**Questão 10 — Armazenamento e Serviços de Internet**

**Escolhendo a Infraestrutura Certa**

Uma startup de desenvolvimento de software com 12 desenvolvedores está montando sua infraestrutura. Eles precisam de: armazenamento centralizado para compartilhar projetos e arquivos entre a equipe, acesso remoto seguro para desenvolvedores em home office e um serviço de internet adequado para o perfil da equipe. Indique a solução de armazenamento mais adequada, justifique a escolha do serviço de internet e explique como o acesso remoto poderia ser viabilizado de forma segura.

`R:`

---

## Gabarito — Uso Exclusivo do Professor

### Objetivas

| Questão | Gabarito | Justificativa |
|---------|----------|---------------|
| 1 | B | 400 Mbps ÷ 8 = 50 MB/s · 1 byte = 8 bits · operadoras anunciam em Mbps porque o número parece maior (400 Mbps vs. 50 MB/s) e tecnicamente correto pois a medida de velocidade de rede é em bits por segundo |
| 2 | C | DMZ = segmento entre dois firewalls · servidor web na DMZ é acessível pela internet mas isolado da rede interna pelo firewall interno · as demais opções colocam o servidor web na mesma rede que os servidores internos ou sem proteção adequada |
| 3 | C | I correta: switch Camada 2, endereço MAC · II incorreta: hub é ineficiente — repassa para todas as portas causando colisões, não aumenta o alcance · III correta: patch panel é passivo, organiza o cabeamento horizontal · IV correta: roteador Camada 3, endereço IP |
| 4 | B | NAS atende todos os requisitos: conectado à LAN (acesso simultâneo), suporte a RAID, gerenciamento via interface web · DAS não compartilha com múltiplos usuários · SAN é cara e complexa demais para PME · nuvem depende de internet e tem latência maior |
| 5 | C | FTTH oferece velocidade simétrica (download = upload), baixíssima latência (~5ms), conexão dedicada e alta disponibilidade · ADSL é assimétrico e lento · HFC tem banda compartilhada entre vizinhos · 4G tem latência variável e custo por dados |

### Discursivas — Critérios de Correção

**Questão 6 — Dimensionando o Link**

*Resposta esperada:*
- 200 GB = 200 × 1.024 MB = 204.800 MB
- Velocidade mínima em MB/s: 204.800 ÷ 7.200 = ~28,4 MB/s
- Conversão para Mbps: 28,4 × 8 = ~227,5 Mbps
- Plano de 200 Mbps simétrico: NÃO seria suficiente — o upload de 200 Mbps = 25 MB/s, abaixo dos 28,4 MB/s necessários · seria necessário um plano de pelo menos 300 Mbps simétrico
- Observação: na prática, considerar overhead de protocolo (~10-15%) — o link necessário seria ainda maior

*Critérios:* cálculo correto de MB/s (0,3 pt) · conversão correta para Mbps (0,3 pt) · conclusão correta sobre o plano de 200 Mbps (0,4 pt)

---

**Questão 7 — Diagrama de Rede**

*Resposta esperada:*
- **Nuvem:** representa a internet · posicionada no topo do diagrama
- **Firewall externo:** entre a internet e a DMZ · filtra tráfego de entrada da internet
- **DMZ:** segmento com servidor web público · isolado da rede interna
- **Servidor Web (SRV-WEB):** dentro da DMZ · acessível pela internet
- **Firewall interno:** entre a DMZ e a rede interna · protege os servidores internos
- **Switch:** conecta os dispositivos internos · roteamento interno da LAN
- **Servidor de arquivos (SRV-ARQUIVOS):** conectado ao switch interno · acesso apenas pela rede interna
- **Access Point:** conectado ao switch · distribui Wi-Fi para funcionários
- **Notebooks/PCs:** conectados ao switch (cabeado) ou ao AP (sem fio)
- **Links:** linhas sólidas para Ethernet · linhas tracejadas para Wi-Fi

*Critérios:* presença e função correta dos elementos principais (firewall, DMZ, servidor web, servidor interno, AP) — 0,2 pt cada = 1,0 pt

---

**Questão 8 — Par Trançado: Categorias**

*Resposta esperada:*
- **Cat5e:** 1 Gbps / 100 m · uso: rede doméstica ou escritório pequeno sem necessidade de alta velocidade · custo mais baixo justifica o uso quando 1 Gbps é suficiente
- **Cat6:** 10 Gbps / 55 m · uso: escritório corporativo com switches de 10 Gbps em distâncias menores que 55 m entre switch e dispositivo · melhor custo-benefício para ambientes corporativos
- **Cat6A:** 10 Gbps / 100 m · uso: data center ou novo cabeamento corporativo onde a distância padrão de 100 m precisa ser mantida com 10 Gbps · indicado para novas instalações pois garante compatibilidade futura

*Critérios:* cada categoria com velocidade + distância + cenário de uso + justificativa (0,33 pt cada ≈ 1,0 pt)

---

**Questão 9 — Switch vs. Roteador**

*Resposta esperada:*
- **Switch:** Camada 2 (Enlace) · endereço MAC · conecta dispositivos na mesma rede local · exemplo: interligar os 30 computadores de um escritório em uma LAN
- **Roteador:** Camada 3 (Rede) · endereço IP · conecta redes diferentes · exemplo: conectar a rede interna da empresa à internet
- **Roteador doméstico "faz tudo":** equipamento All-in-One que combina roteador + switch + AP + modem em um único aparelho · conveniente para uso doméstico com poucos dispositivos
- **Separação em redes corporativas:** desempenho, gerenciamento, segurança e escalabilidade exigem equipamentos dedicados · um roteador corporativo gerencia múltiplas rotas e políticas de QoS · o switch corporativo gerencia VLANs e alta densidade de portas · misturar funções em um único equipamento limita a capacidade e dificulta o gerenciamento

*Critérios:* camada OSI e endereçamento corretos (0,3 pt) · exemplos válidos (0,2 pt) · explicação do All-in-One doméstico (0,2 pt) · justificativa da separação corporativa (0,3 pt)

---

**Questão 10 — Startup de Desenvolvimento**

*Resposta esperada:*
- **Armazenamento:** NAS de médio porte (ex.: Synology com RAID 5) · compartilhamento centralizado para 12 desenvolvedores · acesso simultâneo via rede · backup automatizado · gerenciamento simples via interface web · custo compatível com startup
- **Serviço de internet:** FTTH (fibra óptica) simétrico · velocidade de upload adequada para repositórios Git, pipelines CI/CD e videoconferências · baixa latência para comunicação em tempo real · conexão estável e dedicada
- **Acesso remoto seguro:** VPN (ex.: WireGuard ou OpenVPN) instalada no roteador ou em servidor dedicado · desenvolvedores em home office conectam via VPN e acessam o NAS e os servidores internos como se estivessem na rede da empresa · alternativa: uso de VPN em nuvem (ex.: Tailscale) para simplicidade

*Critérios:* armazenamento correto com justificativa (0,35 pt) · serviço de internet correto com justificativa (0,35 pt) · solução de acesso remoto segura com explicação (0,3 pt)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 09 — 15/04/2026 · Tipos Comuns de Interfaces e Serviços de Internet |
| Próxima aula → | Aula 11 — 29/04/2026 · Prova de Recuperação — 1º Trimestre |

---

## Recursos Necessários

- Projetor ou TV (opcional — para exibir o tempo restante)
- Prova impressa — 1 cópia por aluno
- Gabarito impresso — uso exclusivo do professor
- Lista de chamada para controle de presença

---

## Observações do Professor
