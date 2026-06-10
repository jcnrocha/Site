# UC: Fundamentos de Redes de Computadores
## Aula 12 — 1º Trimestre

---

## Tema

Revisão e Correção Comentada das Provas do 1º Trimestre

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender os erros cometidos na avaliação trimestral — identificando onde e por que errou
- Consolidar os conceitos do 1º trimestre a partir da correção detalhada de cada questão
- Reconhecer os pontos de maior dificuldade da turma e retomar os conteúdos com base no feedback coletivo
- Conectar o aprendizado do 1º trimestre com os conteúdos que serão trabalhados no 2º trimestre
- Desenvolver a capacidade de autoavaliação — identificando o próprio nível de domínio de cada habilidade

**Habilidade da matriz:** H1 · H2 · H3 · H4 — consolidação e fechamento das habilidades do 1º trimestre

---

## Conteúdo

- Esta aula é de correção comentada — não há conteúdo novo
- O foco é o feedback detalhado sobre a prova, a retomada dos conceitos que geraram mais erros e a conexão com o 2º trimestre
- **Estrutura da correção:**
  - Correção coletiva de todas as 10 questões da prova trimestral (Aula 10)
  - Para cada questão: o professor apresenta a resposta correta, explica o raciocínio e comenta os erros mais comuns cometidos pela turma
  - Espaço aberto para perguntas após cada bloco de questões

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Devolução das provas corrigidas · Apresentação da estrutura da aula · Professor registra no quadro os temas com maior índice de erro da turma |
| Correção — Objetivas | Professor corrige as 5 questões objetivas uma a uma · explica o raciocínio correto · comenta por que cada distrator (alternativa errada) é incorreto · abre para perguntas após cada questão |
| Correção — Discursivas | Professor corrige as 5 questões discursivas uma a uma · lê exemplos de respostas boas e de respostas incompletas (sem identificar os alunos) · reforça os critérios de correção · abre para perguntas |
| Retomada dirigida | Professor retoma com mais profundidade os 2 ou 3 conteúdos com maior índice de erro — usando slides ou quadro branco |
| Conexão com o 2º Trimestre | Professor apresenta o que vem a seguir: meios de transmissão guiados e não guiados, tecnologias de conexão, endereçamento IP, protocolos · mostra como o 1º trimestre é a base para o 2º |
| Fechamento | Espaço aberto para dúvidas finais · orientações sobre a Aula 13 (Ponte) · reconhecimento da turma pelo esforço no trimestre |

---

## Roteiro de Correção — Questões Objetivas da Prova (Aula 10)

> O professor usa este roteiro como guia durante a correção coletiva. Para cada questão: anuncia o gabarito, explica o raciocínio correto e comenta os distradores.

---

**Questão 1 — Gabarito: B (50 MB/s)**

*Raciocínio:* 400 Mbps ÷ 8 = 50 MB/s · a conversão é necessária porque 1 byte = 8 bits · as operadoras anunciam em Mbps porque o número parece maior — 400 Mbps soa melhor que 50 MB/s para o consumidor

*Erros comuns:* confundir Mbps com MB/s sem fazer a divisão por 8 · escolher a alternativa A (400 MB/s) por não lembrar da conversão · não entender por que o número anunciado é sempre maior que o que aparece no gerenciador de downloads

---

**Questão 2 — Gabarito: C (Nuvem → Firewall Externo → DMZ → Firewall Interno → Rede Interna)**

*Raciocínio:* a DMZ precisa de dois firewalls — um voltado para a internet e outro voltado para a rede interna · isso cria uma zona tampão onde servidores públicos ficam acessíveis externamente mas não têm acesso direto à rede interna · as demais opções colocam o servidor web no mesmo segmento que a rede interna ou sem proteção adequada

*Erros comuns:* não lembrar que a DMZ exige dois firewalls · escolher a alternativa D que tem apenas um firewall e coloca servidor web e rede interna no mesmo segmento · confundir a posição da DMZ no diagrama

---

**Questão 3 — Gabarito: C (I, III e IV estão corretas)**

*Raciocínio:*
- I ✅ Switch opera na Camada 2, usa endereço MAC — correto
- II ❌ Hub retransmite para todas as portas causando colisões — é ineficiente, não eficiente · não aumenta o alcance
- III ✅ Patch panel é passivo e organiza o cabeamento horizontal — correto
- IV ✅ Roteador opera na Camada 3, usa endereço IP — correto

*Erros comuns:* marcar a afirmação II como correta por não lembrar que hub causa colisões · confundir o conceito de "repassar para todas as portas" com eficiência

---

**Questão 4 — Gabarito: B (NAS)**

*Raciocínio:* NAS atende todos os requisitos — conectado à LAN (acesso simultâneo por 40 usuários), suporte a RAID (redundância), gerenciamento via interface web · DAS é exclusivo de um dispositivo · SAN é cara e complexa para PME · nuvem tem latência de internet e não é ideal para acesso frequente de arquivos internos

*Erros comuns:* confundir SAN com NAS · escolher nuvem sem considerar a latência de internet para acesso frequente · não lembrar que DAS não é compartilhado

---

**Questão 5 — Gabarito: C (FTTH)**

*Raciocínio:* FTTH oferece velocidade simétrica (upload = download) — fundamental para videoconferências e upload de arquivos · baixíssima latência (~5 ms) · conexão dedicada (não compartilhada) · ADSL é assimétrico e lento · HFC tem banda compartilhada entre vizinhos · 4G tem latência variável e custo por dado

*Erros comuns:* escolher HFC por ter alta velocidade de download sem considerar a assimetria e o compartilhamento · não perceber que upload simétrico é o diferencial do FTTH para uso corporativo

---

## Roteiro de Correção — Questões Discursivas da Prova (Aula 10)

> Para cada discursiva: o professor lê a questão, apresenta os critérios de correção, mostra um exemplo de resposta completa e comenta os erros mais frequentes.

---

**Questão 6 — Dimensionando o Link**

*Pontos obrigatórios na resposta:*
- 200 GB = 204.800 MB
- Velocidade mínima: 204.800 ÷ 7.200 = ~28,4 MB/s
- Conversão: 28,4 × 8 = ~227,5 Mbps
- Plano de 200 Mbps NÃO é suficiente — 200 Mbps = 25 MB/s < 28,4 MB/s necessários
- Solução: contratar plano de pelo menos 300 Mbps simétrico

*Erros comuns:* não converter GB para MB antes de calcular · esquecer de multiplicar por 8 para converter MB/s em Mbps · concluir que 200 Mbps é suficiente sem verificar a conversão · não mencionar que o upload deve ser simétrico

---

**Questão 7 — Diagrama de Rede**

*Pontos obrigatórios na resposta:*
- Nuvem (internet) no topo com símbolo de nuvem
- Firewall externo entre internet e DMZ
- DMZ com servidor web identificado (SRV-WEB)
- Firewall interno entre DMZ e rede interna
- Switch conectando os dispositivos internos
- Servidor de arquivos interno (SRV-ARQUIVOS) conectado ao switch por linha sólida
- Access point conectado ao switch por linha sólida
- Funcionários conectados ao AP por linha tracejada (Wi-Fi)

*Erros comuns:* colocar o servidor web dentro da rede interna · usar apenas um firewall · não usar linha tracejada para a conexão Wi-Fi · não rotular os servidores · esquecer o access point para o Wi-Fi

---

**Questão 8 — Par Trançado: Categorias**

*Pontos obrigatórios na resposta:*
- Cat5e: 1 Gbps / 100 m → rede doméstica ou pequena empresa sem necessidade de alta velocidade
- Cat6: 10 Gbps / 55 m → escritório corporativo com distâncias menores que 55 m
- Cat6A: 10 Gbps / 100 m → data center ou nova instalação corporativa com distância padrão de 100 m

*Erros comuns:* confundir a distância máxima do Cat6 (55 m) com a do Cat5e e Cat6A (100 m) · não justificar a escolha de cada categoria para o cenário indicado · afirmar que Cat5e não funciona em redes corporativas

---

**Questão 9 — Switch vs. Roteador**

*Pontos obrigatórios na resposta:*
- Switch: Camada 2, endereço MAC, conecta dispositivos na mesma rede
- Roteador: Camada 3, endereço IP, conecta redes diferentes
- Roteador doméstico = All-in-One (roteador + switch + AP + modem em um único aparelho)
- Separação corporativa: desempenho, gerenciamento, segurança e escalabilidade exigem equipamentos dedicados

*Erros comuns:* inverter a camada OSI de switch e roteador · não explicar o roteador doméstico como All-in-One · afirmar que switch e roteador são equivalentes

---

**Questão 10 — Startup de Desenvolvimento**

*Pontos obrigatórios na resposta:*
- Armazenamento: NAS (compartilhamento entre 12 desenvolvedores, RAID, custo compatível com startup)
- Serviço de internet: FTTH simétrico (upload adequado para Git/CI/CD, baixa latência)
- Acesso remoto: VPN (WireGuard, OpenVPN ou Tailscale) — túnel seguro para home office

*Erros comuns:* indicar SAN para startup (custo incompatível) · indicar nuvem como armazenamento principal sem considerar a latência para acesso frequente · não mencionar VPN para o acesso remoto seguro

---

## Retomada Dirigida — Conteúdos para Aprofundamento

> O professor escolhe os 2 ou 3 temas com maior índice de erro e dedica 5 minutos extras a cada um.

**Sugestões de retomada (adaptar conforme desempenho real da turma):**

- **Conversão Mbps → MB/s:** escrever a fórmula no quadro · praticar com 3 exemplos rápidos com a turma: 100 Mbps, 500 Mbps e 1 Gbps → quanto em MB/s?
- **DMZ com dois firewalls:** desenhar o diagrama no quadro passo a passo · reforçar que a DMZ é um "corredor" entre dois firewalls — não apenas um segmento atrás de um firewall
- **Switch vs. Hub:** reescrever a tabela comparativa no quadro · reforçar que hub é Camada 1 e causa colisões · switch é Camada 2, usa MAC, elimina colisões · um único exercício: "se 5 computadores estão conectados a um hub e 2 transmitem ao mesmo tempo, o que acontece?"
- **NAS vs. SAN:** retomar as analogias — NAS é como uma pasta compartilhada na rede · SAN é como um HD local ultra-rápido que na verdade está em outro lugar · custo e complexidade separam os dois
- **Cat6 × Cat6A (distância):** fixar no quadro: Cat6 = 10 Gbps / 55 m · Cat6A = 10 Gbps / 100 m · para novas instalações sempre Cat6A

---

## Conexão com o 2º Trimestre

> Professor usa este momento para criar expectativa e mostrar como o 1º trimestre é base para o 2º.

**O que vimos no 1º trimestre:**
- Unidades de medida para entender velocidade e capacidade (H1)
- Simbologias para documentar e comunicar projetos (H2)
- Componentes físicos — passivos e ativos — que formam a rede (H3)
- Interfaces e serviços de internet disponíveis (H4)

**O que veremos no 2º trimestre:**
- Como os meios de transmissão funcionam em profundidade (cabos, Wi-Fi, satélite)
- Como a internet chega até nós (FTTH, HFC, 4G, 5G)
- Como os dispositivos são identificados na rede (endereçamento IP)
- Como os dados são entregues com segurança (protocolos TCP/IP, HTTP, DNS)
- Como a rede é protegida (firewall, VPN, segurança)
- O modelo OSI — o framework que organiza toda a comunicação em rede

**A conexão:** *"Vocês já conhecem os componentes — agora vão entender como eles se comunicam por dentro. É como aprender as peças de um carro no 1º trimestre e agora entender como o motor funciona."*

---

## Avaliação

- Esta aula não tem questionário individual
- A avaliação é formativa — o professor observa a participação, as dúvidas levantadas e o engajamento na correção
- O professor pode solicitar que os alunos registrem por escrito: *"O que eu errei e o que aprendi com a correção"* — exercício de autoavaliação (opcional)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 11 — 29/04/2026 · Prova de Recuperação — 1º Trimestre |
| Próxima aula → | Aula 13 — 13/05/2026 · Ponte — Conexão com o 2º Trimestre |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Slides com as questões da prova e gabarito comentado
- Quadro branco e marcador para retomada dirigida e diagramas
- Provas corrigidas para devolução aos alunos
- Terminal aberto (opcional) para demonstrações ao vivo de conversão de unidades ou diagramas no draw.io

---

## Observações do Professor
