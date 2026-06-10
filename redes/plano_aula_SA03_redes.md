# UC: Fundamentos de Redes de Computadores
## Aula 03 — 1º Trimestre

---

## Tema

Unidades de Medida — Velocidade de Transmissão

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é velocidade de transmissão de dados e por que ela é medida em bits por segundo
- Identificar e diferenciar as unidades de velocidade: bps, Kbps, Mbps, Gbps e Tbps
- Diferenciar largura de banda de velocidade real — entendendo por que a velocidade contratada nem sempre é a velocidade obtida
- Compreender os conceitos de latência e throughput — e como eles impactam a experiência do usuário em uma rede
- Relacionar as unidades de velocidade com situações práticas do cotidiano de TI e do desenvolvimento de sistemas

**Habilidade da matriz:** H1 — Reconhecer unidades de medida empregadas na transmissão e armazenamento de dados

---

## Conteúdo

- Retomada rápida da Aula 02: *"Na aula passada vimos as unidades de armazenamento — bits, bytes, KB, MB, GB e TB. Hoje vamos entender como medimos a velocidade com que esses dados viajam pela rede"*
- **O que é velocidade de transmissão?**
  - É a quantidade de dados que pode ser transmitida por um meio de comunicação em um determinado período de tempo
  - Medida em bits por segundo (bps) — não em bytes
  - Por que bits e não bytes? Porque na transmissão de dados, os bits são a unidade básica de sinalização elétrica ou óptica

- **Unidades de velocidade de transmissão:**
  - **bps (bits por segundo):** unidade base · velocidade de modems antigos de linha telefônica (56 Kbps)
  - **Kbps (Quilobits por segundo):** 1.000 bps · conexões antigas de internet discada e ADSL básico
  - **Mbps (Megabits por segundo):** 1.000.000 bps · padrão atual de planos residenciais (100 Mbps, 200 Mbps, 300 Mbps)
  - **Gbps (Gigabits por segundo):** 1.000.000.000 bps · redes corporativas, data centers, planos de fibra de alta velocidade
  - **Tbps (Terabits por segundo):** 1.000.000.000.000 bps · backbones de internet, cabos submarinos de fibra óptica

  | Unidade | Valor em bps | Equivalência | Exemplo prático |
  |---------|-------------|-------------|----------------|
  | 1 Kbps | 1.000 bps | 1.000 bits/s | Modem dial-up antigo (56 Kbps) |
  | 1 Mbps | 1.000.000 bps | 1.000 Kbps | Plano residencial básico |
  | 1 Gbps | 1.000.000.000 bps | 1.000 Mbps | Fibra óptica corporativa |
  | 1 Tbps | 1.000.000.000.000 bps | 1.000 Gbps | Cabo submarino transoceânico |

- **Diferença entre bits (b) e bytes (B) na velocidade:**
  - Velocidade de internet: anunciada em **Megabits por segundo (Mbps)** — letra minúscula "b"
  - Velocidade de transferência de arquivo: exibida em **Megabytes por segundo (MB/s)** — letra maiúscula "B"
  - Conversão: MB/s = Mbps ÷ 8 (porque 1 byte = 8 bits)
  - Exemplo prático: plano de 200 Mbps → velocidade real de download = 200 ÷ 8 = **25 MB/s**
  - Por que as operadoras anunciam em Mbps? O número parece maior — 200 Mbps soa melhor que 25 MB/s

- **Largura de Banda (Bandwidth)**
  - Capacidade máxima teórica de transmissão de um canal ou conexão
  - É o "potencial" da rede — o máximo que ela pode transmitir em condições ideais
  - Analogia: largura de banda é como a largura de uma estrada — quantos carros podem passar ao mesmo tempo
  - Unidade: Mbps ou Gbps · anunciada pelos provedores nos planos de internet

- **Velocidade Real × Velocidade Contratada**
  - A velocidade real de transmissão quase sempre é menor que a largura de banda contratada
  - **Fatores que reduzem a velocidade real:**
    - Overhead de protocolo: TCP/IP, cabeçalhos HTTP e outros protocolos consomem parte da banda
    - Congestionamento: muitos usuários usando a rede ao mesmo tempo
    - Qualidade do meio físico: cabo velho, Wi-Fi com interferência, fibra com dobra
    - Distância do servidor: servidor geograficamente distante adiciona latência
    - Limitação do dispositivo: placa de rede antiga, processador lento, memória insuficiente

- **Latência**
  - Tempo que um pacote leva para ir da origem ao destino e voltar — medido em milissegundos (ms)
  - Também chamada de RTT (Round Trip Time) — tempo de ida e volta
  - Diferente de velocidade: você pode ter alta velocidade com alta latência — ou baixa velocidade com baixa latência
  - Exemplos de latência típica:
    - Rede local (LAN): 1 a 5 ms
    - Internet via fibra (mesma cidade): 5 a 20 ms
    - Internet 4G LTE: 30 a 50 ms
    - Satélite GEO: ~600 ms
    - Satélite LEO (Starlink): 20 a 40 ms
  - **Impacto da latência:**
    - Gaming online: latência acima de 100 ms causa "lag" perceptível
    - Videoconferência: latência acima de 150 ms causa eco e dessincronização
    - Navegação web: latência alta torna páginas lentas mesmo com banda larga
    - Aplicações críticas (cirurgia remota, veículos autônomos): exigem latência abaixo de 5 ms

- **Throughput**
  - Velocidade real e efetiva de transmissão medida em condições reais de uso — sempre menor ou igual à largura de banda
  - É o que o usuário realmente experimenta ao usar a rede
  - Diferença: largura de banda é o máximo teórico · throughput é o que de fato passa pela rede
  - Analogia: largura de banda = quantidade de bombas em um posto de gasolina · throughput = quantidade de carros que realmente abasteceram em 1 hora

- **Jitter**
  - Variação da latência ao longo do tempo — instabilidade no tempo de entrega dos pacotes
  - Exemplo: pacotes chegando com 10 ms, 30 ms, 5 ms, 50 ms — em vez de consistentemente 15 ms
  - Impacto: VoIP e streaming de áudio/vídeo são muito sensíveis ao jitter — causa distorção de voz e travamentos

- **Como medir velocidade na prática:**
  - **Speedtest (speedtest.net):** mede download, upload e latência (ping)
  - **ping:** `ping 8.8.8.8` — mede latência e verifica perda de pacotes
  - **iperf3:** ferramenta técnica para medir throughput real entre dois pontos da rede

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da Aula 02: *"Convertemos bits em bytes — hoje entendemos a velocidade com que eles viajam"* |
| Retomada | Professor pergunta: *"Qual é o plano de internet que você tem em casa? É anunciado em Mbps ou em MB/s? Se é 200 Mbps, com qual velocidade você baixa um arquivo no seu gerenciador de downloads?"* — alunos respondem livremente |
| Explicação | Slides — unidades de velocidade (bps→Tbps), diferença bits × bytes na velocidade, largura de banda, velocidade real × contratada, latência, throughput, jitter, como medir |
| Dinâmica | "Quanto Tempo Demora?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: velocidade em bits (Mbps) · divide por 8 para MB/s · latência é o tempo de resposta · throughput é o que você realmente experimenta · Próxima aula: Tipos de Armazenamento em Redes |

---

## Dinâmica — "Quanto Tempo Demora?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a habilidade de aplicar as unidades de velocidade de transmissão em cálculos práticos do cotidiano de TI — conectando o conteúdo teórico com situações reais que técnicos de redes e desenvolvedores enfrentam ao dimensionar infraestrutura e estimar tempos de transferência.

**Materiais:** cartões com situações-problema — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com situações-problema envolvendo velocidade de transmissão. O desafio é calcular ou estimar a resposta e justificar o raciocínio.

2. **Resolução em grupo** *(8 min)*
O grupo discute e resolve cada situação, mostrando o raciocínio da conversão de unidades.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma resposta. O professor complementa, corrige e reforça o raciocínio por trás de cada cálculo.

**Situações sugeridas:**

| Situação-problema | Raciocínio | Resposta esperada |
|-------------------|-----------|-------------------|
| Seu plano é de 100 Mbps. Qual a velocidade de download em MB/s? | 100 ÷ 8 = 12,5 | ~12,5 MB/s |
| Você precisa baixar um arquivo de 1 GB com uma conexão de 50 Mbps. Quanto tempo demora? | 1 GB = 1.024 MB · 50 Mbps = 6,25 MB/s · 1.024 ÷ 6,25 ≈ 164 segundos | ~2 minutos e 44 segundos |
| Um servidor precisa transferir 500 MB para outro servidor em no máximo 10 segundos. Qual a largura de banda mínima necessária? | 500 MB ÷ 10 s = 50 MB/s · 50 × 8 = 400 Mbps | 400 Mbps |
| Você faz um ping para o servidor e recebe: 8 ms, 7 ms, 9 ms. O que esses números representam? | Latência (RTT) em milissegundos · média de ~8 ms | Latência baixa · conexão estável |
| Um plano de 1 Gbps é anunciado pela operadora. Qual a velocidade de download esperada em MB/s? | 1.000 Mbps ÷ 8 = 125 | ~125 MB/s |
| Dois servidores de data center trocam dados a 10 Gbps. Quanto tempo para transferir 1 TB? | 1 TB = 1.024 GB = 1.048.576 MB · 10 Gbps = 1.250 MB/s · 1.048.576 ÷ 1.250 ≈ 839 s | ~14 minutos |
| Durante um speedtest, download = 150 Mbps mas o arquivo baixa a 10 MB/s. Isso é normal? | 150 Mbps ÷ 8 = 18,75 MB/s · 10 MB/s < 18,75 MB/s · overhead e outros fatores explicam | Sim — throughput real < largura de banda |
| Um jogador reclama de "lag" — o ping dele é 250 ms. Isso é aceitável para gaming online? | Latência ideal para gaming: abaixo de 60–80 ms · 250 ms causa lag perceptível | Não — latência muito alta para gaming |

> **Nota:** o objetivo é desenvolver o raciocínio de conversão e aplicação prática: *"a operadora anuncia em Mbps — eu preciso dividir por 8 para saber quantos megabytes por segundo vou transferir de fato."* Reforçar que esse cálculo é usado no dia a dia para dimensionar links, estimar tempos de backup e especificar planos de internet para empresas.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 02 — 25/02/2026 · Unidades de Medida — Bits, Bytes e Múltiplos |
| Próxima aula → | Aula 04 — 11/03/2026 · Tipos de Armazenamento em Redes |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Cartões com as situações-problema da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: demonstração ao vivo de um teste de velocidade (Speedtest.net) e de um ping no terminal — mostrar download em Mbps e calcular ao vivo a conversão para MB/s com a turma

---

## Observações do Professor
