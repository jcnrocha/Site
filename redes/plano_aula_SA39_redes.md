# UC: Fundamentos de Redes de Computadores
## Aula 39 — 3º Trimestre

---

## Tema

Prova — 3ª Avaliação Trimestral

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Demonstrar domínio dos conteúdos trabalhados ao longo do 3º trimestre: classificação de redes, topologias, modelos, redes sem fio, infraestrutura corporativa, computação em nuvem, diagnóstico e tendências
- Responder questões objetivas e discursivas com clareza, precisão e fundamentação técnica
- Aplicar o raciocínio de projeto, diagnóstico e escolha de tecnologia em situações práticas
- Demonstrar as habilidades H3, H4 e H5 desenvolvidas ao longo do trimestre e consolidadas no Projeto Integrador

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes · H4 — Identificar tipos e tecnologias de conexão a redes de computadores · H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Esta aula é destinada exclusivamente à aplicação da 3ª Avaliação Trimestral
- Não há explicação de conteúdo novo
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
| Abertura | Chamada · organização da sala · distribuição das provas · instruções gerais |
| Aplicação da Prova | Alunos respondem individualmente a prova completa — sem consulta |
| Encerramento | Recolhimento das provas · orientações sobre a Aula 40 (Recuperação) · previsão de devolução com correção |

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

**Questão 1 — Classificação e Topologia de Redes**

Uma empresa com 3 andares conecta todos os computadores de cada andar a um switch local, e os switches de cada andar são conectados a um switch central no servidor. Qual é a topologia física dessa rede e qual é a classificação por abrangência?

- A) Topologia Anel · Classificação WAN
- B) Topologia Barramento · Classificação MAN
- C) Topologia Estrela · Classificação LAN
- D) Topologia Malha · Classificação LAN

---

**Questão 2 — Redes Sem Fio e Segurança**

O setor de TI de uma empresa precisa garantir que os dispositivos dos visitantes acessem apenas a internet, sem conseguir ver os servidores e computadores internos. Qual é a solução técnica correta?

- A) Configurar WPA3 no roteador principal com senha exclusiva para visitantes
- B) Criar um SSID Guest em uma VLAN separada, isolado da rede interna corporativa
- C) Desativar o SSID corporativo durante o horário de visitas
- D) Instalar um segundo roteador sem fio exclusivo para visitantes sem qualquer configuração de segurança

---

**Questão 3 — Computação em Nuvem**

Uma startup de 8 desenvolvedores quer hospedar sua aplicação web sem investir em servidores físicos. Eles precisam de um ambiente onde possam fazer o deploy do código sem se preocupar com sistema operacional, atualizações de servidor ou configuração de infraestrutura. Qual modelo de serviço em nuvem atende melhor essa necessidade?

- A) IaaS — pois oferece máquinas virtuais que eles configuram do zero
- B) SaaS — pois o software já vem pronto e hospedado pelo provedor
- C) PaaS — pois oferece a plataforma para deploy sem gerenciar a infraestrutura subjacente
- D) On-premises — pois garante total controle sobre o ambiente de produção

---

**Questão 4 — Diagnóstico de Redes**

Um analista de TI recebe o seguinte chamado: "Consigo fazer ping no servidor pelo IP (192.168.1.10), mas quando digito o nome do servidor (servidor-arq) no explorador de arquivos, ele não é encontrado." Com base nos sintomas, em qual camada do modelo OSI o problema está e qual ferramenta deve ser usada para confirmar o diagnóstico?

- A) Camada 1 — Física · usar ipconfig para verificar o cabo
- B) Camada 3 — Rede · usar ping para verificar a conectividade IP
- C) Camada 4 — Transporte · usar netstat para verificar as portas abertas
- D) Camada 7 — Aplicação · usar nslookup para verificar a resolução de nomes DNS

---

**Questão 5 — IoT e Tendências**

Uma indústria instalou 800 sensores em suas máquinas para monitorar temperatura e vibração em tempo real. Os sensores enviam pequenos pacotes de dados a cada 5 segundos e operam com bateria. Qual protocolo IoT é mais adequado para essa aplicação e por quê?

- A) HTTP — por ser o protocolo padrão da internet e mais compatível
- B) FTP — por ser otimizado para transferência de dados industriais
- C) MQTT — por ser leve, de baixo consumo e baseado em publish-subscribe, ideal para sensores
- D) DNS — por resolver os nomes dos sensores na rede industrial

---

### PARTE 2 — Questões Discursivas

---

**Questão 6 — Topologias de Rede**

**Estrela × Malha: Quando Usar Cada Uma?**

Compare as topologias Estrela e Malha em relação a: ponto de falha, custo, escalabilidade e desempenho. Indique em qual tipo de ambiente ou situação cada topologia é mais adequada e justifique tecnicamente sua resposta.

`R:`

---

**Questão 7 — Modelos de Rede**

**Cliente-Servidor na Prática**

Explique o modelo Cliente-Servidor descrevendo: o papel do cliente, o papel do servidor e como ocorre a comunicação entre eles. Cite três exemplos reais de aplicações que utilizam esse modelo no cotidiano de um desenvolvedor de sistemas.

`R:`

---

**Questão 8 — Infraestrutura Corporativa**

**VLANs e DMZ: Segmentação e Segurança**

Explique o que são VLANs e qual é o seu papel na segmentação da rede corporativa. Em seguida, explique o conceito de DMZ e em qual situação ela deve ser utilizada. Qual é a relação entre VLANs, DMZ e a segurança da rede interna?

`R:`

---

**Questão 9 — Diagnóstico de Redes**

**Metodologia de Troubleshooting**

Um funcionário relata que seu computador mostra o endereço IP 169.254.45.10 e não consegue acessar nenhum recurso da rede. Descreva o processo de diagnóstico passo a passo para identificar e resolver esse problema, indicando quais ferramentas usar em cada etapa e o que cada resultado significa.

`R:`

---

**Questão 10 — Visão Integrada da UC**

**Da Medida ao Projeto: A Jornada da UC**

Ao longo do ano, você percorreu um caminho que começou nas unidades de medida (H1) e chegou ao projeto de uma rede corporativa completa (H1 a H5). Descreva esse caminho explicando como cada habilidade da UC se conecta com as demais e como elas se integraram no Projeto Integrador. Use exemplos concretos do projeto do seu grupo.

`R:`

---

## Gabarito — Uso Exclusivo do Professor

### Objetivas

| Questão | Gabarito | Justificativa |
|---------|----------|---------------|
| 1 | C | Todos conectados a switches centrais = topologia Estrela · ambiente dentro de um único prédio = LAN · WAN e MAN são para longas distâncias · Malha exigiria múltiplas conexões redundantes entre switches |
| 2 | B | SSID Guest em VLAN separada isola logicamente o tráfego dos visitantes da rede interna · apenas senha WPA3 não impede acesso à rede interna · segundo roteador sem segurança é uma vulnerabilidade · desativar SSID corporativo interrompe os funcionários |
| 3 | C | PaaS oferece a plataforma pronta (SO, runtime, middleware) — o desenvolvedor só faz o deploy do código · IaaS exige configurar SO e infraestrutura · SaaS é software pronto para uso final · on-premises requer hardware próprio |
| 4 | D | Ping no IP funciona = Camadas 1 a 3 OK · falha na resolução do nome = problema de DNS = Camada 7 (Aplicação) · ferramenta correta: nslookup para verificar se o servidor DNS interno resolve o nome do servidor |
| 5 | C | MQTT é o protocolo padrão para IoT industrial — leve (pacotes pequenos), publish-subscribe (eficiente para múltiplos sensores), baixo consumo de energia (ideal para bateria) · HTTP tem overhead alto · FTP é para transferência de arquivos · DNS é para resolução de nomes |

### Discursivas — Critérios de Correção

**Questão 6 — Estrela × Malha**

*Resposta esperada:*
- **Estrela:** ponto de falha no switch central · custo médio · alta escalabilidade (fácil adicionar dispositivos) · desempenho alto com switch · uso: LANs corporativas, escritórios, escolas — padrão atual
- **Malha:** sem ponto único de falha (full mesh) ou ponto de falha reduzido (partial mesh) · custo alto (muitos links e interfaces) · escalabilidade baixa em LANs grandes · desempenho alto com múltiplos caminhos · uso: backbones WAN, data centers, infraestrutura crítica que exige alta disponibilidade

*Critérios:* características corretas da Estrela (0,3 pt) · características corretas da Malha (0,3 pt) · indicação de uso adequada com justificativa (0,4 pt)

---

**Questão 7 — Cliente-Servidor na Prática**

*Resposta esperada:*
- **Cliente:** dispositivo que solicita recursos ou serviços ao servidor · inicia a comunicação · pode ser navegador, app mobile, sistema desktop
- **Servidor:** dispositivo dedicado que processa requisições, armazena dados e retorna respostas · fica disponível continuamente · gerencia permissões e segurança
- **Comunicação:** cliente envia requisição → servidor processa e verifica permissões → servidor retorna resposta ao cliente
- **Exemplos para desenvolvedor:** requisição GET/POST a uma API REST · deploy de aplicação em servidor de produção · acesso ao banco de dados via driver de conexão · autenticação via servidor LDAP/OAuth

*Critérios:* papel do cliente (0,2 pt) · papel do servidor (0,2 pt) · fluxo de comunicação (0,2 pt) · três exemplos válidos (0,4 pt)

---

**Questão 8 — VLANs e DMZ**

*Resposta esperada:*
- **VLANs:** segmentação lógica da rede física em múltiplas redes virtuais independentes · dispositivos na mesma VLAN comunicam-se diretamente · entre VLANs é necessário roteamento (switch L3) · benefícios: segurança por departamento, redução de broadcast, organização e flexibilidade
- **DMZ:** segmento de rede entre a internet (WAN) e a rede interna (LAN) · abriga servidores que precisam ser acessíveis pela internet (web, e-mail, FTP) · dois firewalls: externo (internet → DMZ) e interno (DMZ → LAN) · se o servidor da DMZ for comprometido, o invasor ainda enfrenta o firewall interno
- **Relação:** VLANs segmentam a rede interna por função/departamento · DMZ isola os servidores públicos da rede interna · juntas, criam múltiplas camadas de segurança — defesa em profundidade

*Critérios:* conceito e benefícios de VLANs (0,3 pt) · conceito e funcionamento da DMZ (0,4 pt) · relação entre os dois conceitos (0,3 pt)

---

**Questão 9 — Diagnóstico: IP 169.254.x.x**

*Resposta esperada:*
- IP 169.254.x.x = APIPA (Automatic Private IP Addressing) — o DHCP não respondeu e o sistema operacional atribuiu um IP automático de link-local
- **Passo 1 — Verificar a configuração atual:** `ipconfig /all` — confirmar o IP 169.254.x.x, verificar se o adaptador de rede está ativo e se o servidor DHCP está configurado
- **Passo 2 — Tentar renovar o IP:** `ipconfig /release` seguido de `ipconfig /renew` — se renovar com sucesso, o problema era temporário no DHCP
- **Passo 3 — Verificar a conectividade física:** inspecionar o cabo e o LED do switch · se não renovar, verificar se o cabo está conectado corretamente e se a porta do switch está ativa
- **Passo 4 — Verificar o servidor DHCP:** verificar se o serviço DHCP está rodando no servidor · verificar se há endereços disponíveis no pool DHCP · verificar a VLAN do dispositivo

*Critérios:* identificação correta do APIPA (0,2 pt) · passo a passo lógico com ferramentas corretas (0,5 pt) · causas e verificações corretas (0,3 pt)

---

**Questão 10 — Visão Integrada da UC**

*Resposta esperada (resposta aberta — avaliar coerência e integração):*
- **H1:** unidades de medida definiram o dimensionamento de banda do projeto (link de internet, velocidade dos cabos)
- **H2:** simbologias permitiram desenhar o diagrama de rede com representação padronizada de cada componente
- **H3:** componentes físicos escolhidos no projeto (switches, APs, patch panel, rack, servidores)
- **H4:** tecnologias de conexão definidas (FTTH para o link, Cat6A para o cabeamento interno, Wi-Fi 802.11ax, WPA3)
- **H5:** estrutura da rede definida (LAN corporativa, topologia Estrela/Híbrida, modelo Cliente-Servidor, VLANs, DMZ, camadas de infraestrutura)
- O aluno deve usar exemplos específicos do projeto do seu grupo para ilustrar cada conexão

*Critérios:* identificação das 5 habilidades com descrição correta (0,5 pt) · conexão entre as habilidades com lógica progressiva (0,3 pt) · exemplos concretos do projeto (0,2 pt)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 38 — 18/11/2026 · Revisão Geral — Todos os Trimestres |
| Próxima aula → | Aula 40 — 02/12/2026 · Prova de Recuperação — 3º Trimestre |

---

## Recursos Necessários

- Projetor ou TV (opcional — para exibir o tempo restante)
- Prova impressa — 1 cópia por aluno
- Gabarito impresso — uso exclusivo do professor
- Lista de chamada para controle de presença

---

## Observações do Professor
