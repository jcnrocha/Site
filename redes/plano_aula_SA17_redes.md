# UC: Fundamentos de Redes de Computadores
## Aula 17 — 2º Trimestre

---

## Tema

Tecnologias de Conexão à Internet — Parte 2

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Identificar as principais tecnologias de conexão à internet móvel e sem fio: redes 3G, 4G e 5G
- Compreender a evolução das redes móveis e o impacto de cada geração na velocidade e na latência
- Reconhecer tecnologias alternativas de acesso à internet: satélite de baixa órbita (LEO), rádio e PLC
- Diferenciar o uso de cada tecnologia de acordo com o contexto: urbano, rural, móvel ou de alta demanda
- Relacionar as tendências de conectividade — especialmente o 5G — com o impacto na infraestrutura de redes e no desenvolvimento de sistemas

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Retomada rápida da Aula 16: tecnologias cabeadas (ADSL, VDSL, HFC, FTTH) — o que já vimos
- **Redes Móveis — Evolução por Gerações**
  - O conceito de "geração" em redes móveis: cada geração representa um novo padrão de velocidade, latência e capacidade
  - **2G (GSM/GPRS/EDGE)** — contexto histórico · dados lentos · voz digital · ainda presente em áreas remotas
  - **3G (UMTS/HSPA+)**
    - Velocidades típicas: 384 Kbps a 42 Mbps (HSPA+)
    - Primeiro padrão viável para navegar na internet pelo celular
    - Desligamento progressivo no Brasil — operadoras migrando para 4G e 5G
  - **4G (LTE — Long Term Evolution)**
    - Velocidades típicas: 10 a 150 Mbps · picos de até 300 Mbps (LTE-A)
    - Latência: ~30 a 50 ms · adequada para streaming, videochamadas e aplicativos em tempo real
    - Padrão dominante atualmente no Brasil — cobertura ampla em cidades e rodovias
  - **5G (NR — New Radio)**
    - Velocidades teóricas: até 20 Gbps · velocidades reais esperadas: 1 a 4 Gbps
    - Latência ultra-baixa: ~1 ms · viabiliza aplicações críticas em tempo real
    - Três faixas de frequência: baixa (cobertura ampla), média (equilíbrio) e alta — mmWave (velocidade máxima, alcance curto)
    - Impactos: IoT em escala, veículos autônomos, cirurgias remotas, indústria 4.0, realidade aumentada/virtual
    - Expansão no Brasil: capitais e grandes cidades · ainda em implantação
- **Internet via Rádio (Wireless ISP — WISP)**
  - Transmissão de internet por antenas de rádio entre torres e receptores
  - Frequências comuns: 900 MHz, 2,4 GHz, 5,8 GHz
  - Uso típico: zonas rurais e cidades do interior sem fibra ou cabo
  - Vantagens: menor custo de implantação que fibra · Limitações: linha de visada, interferências climáticas
- **PLC — Power Line Communication**
  - Transmissão de dados pela própria rede elétrica da edificação
  - Adaptadores plugados na tomada criam uma rede cabeada usando a fiação elétrica existente
  - Velocidades: até 1 Gbps (padrão HomePlug AV2)
  - Uso típico: alternativa ao Wi-Fi em cômodos com sinal fraco · não requer novo cabeamento
  - Limitações: interferência de outros equipamentos elétricos, desempenho variável por instalação
- **Satélite de Baixa Órbita (LEO) — Revisão e aprofundamento**
  - Retomada do conceito visto na Aula 15 com foco na conectividade à internet
  - Starlink (SpaceX): constelação de satélites LEO · latência ~20–40 ms · velocidade 50–300 Mbps
  - Uso crescente em áreas rurais, embarcações, aviões e emergências
- Comparativo geral — todas as tecnologias de conexão (cabeadas e sem fio):

| Tecnologia | Tipo | Velocidade típica | Latência | Melhor uso |
|------------|------|-------------------|----------|------------|
| ADSL | Cabeada | Até 8 Mbps | ~50 ms | Residencial sem outra opção |
| VDSL | Cabeada | Até 100 Mbps | ~20 ms | Residencial/pequenas empresas |
| HFC (TV a Cabo) | Cabeada | Até 1 Gbps | ~10 ms | Residencial e empresarial |
| FTTH (Fibra) | Cabeada | 100 Mbps a 1 Gbps+ | ~5 ms | Residencial e corporativo |
| 4G LTE | Móvel | 10–150 Mbps | ~30–50 ms | Móvel, residencial sem fibra |
| 5G | Móvel | 1–4 Gbps | ~1 ms | Corporativo, IoT, mobilidade |
| Rádio (WISP) | Sem fio | 10–100 Mbps | ~10–30 ms | Rural e interior |
| PLC | Cabeada elétrica | Até 1 Gbps | Variável | Alternativa interna ao Wi-Fi |
| Satélite LEO | Sem fio | 50–300 Mbps | ~20–40 ms | Áreas remotas sem infraestrutura |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 16: *"Vimos as tecnologias cabeadas — hoje fechamos o bloco de conexões com redes móveis, rádio, PLC e satélite"* |
| Retomada | Professor pergunta: *"Você já usou internet 4G? Já percebeu diferença de velocidade entre 3G e 4G? Alguém já ouviu falar do 5G na prática?"* — alunos respondem livremente |
| Explicação | Slides — evolução 2G→3G→4G→5G, rádio WISP, PLC, satélite LEO, comparativo geral de todas as tecnologias |
| Dinâmica | "Conecta Aí!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: 4G para mobilidade e residencial sem fibra · 5G para alta demanda e IoT · Rádio e satélite para áreas sem infraestrutura · PLC como alternativa interna · Próxima aula: Endereçamento IP |

---

## Dinâmica — "Conecta Aí!"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar o conhecimento de todas as tecnologias de conexão à internet vistas nas Aulas 16 e 17, desenvolvendo o raciocínio técnico de escolha da solução mais adequada para cada cenário — incluindo situações que combinam tecnologias cabeadas e sem fio.

**Materiais:** cartões com cenários — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cenários** *(1 min)*
Cada grupo recebe 4 cartões com cenários variados. O desafio é indicar a tecnologia de conexão mais adequada — podendo ser cabeada ou sem fio — e justificar a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário e decide: qual tecnologia usar, por quê, e quais características técnicas sustentam a decisão.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e reforça os critérios de decisão.

**Cenários sugeridos:**

| Cenário | Tecnologia indicada | Justificativa |
|---------|---------------------|---------------|
| Agricultor em zona rural sem fibra, sem cabo e sem telefone fixo | Satélite LEO (Starlink) ou Rádio WISP | Únicas opções viáveis sem infraestrutura cabeada |
| Técnico que precisa de internet em campo para suporte remoto | 4G LTE (dados móveis) | Mobilidade, cobertura ampla em cidades e rodovias |
| Fábrica inteligente com centenas de sensores IoT em tempo real | 5G | Latência ultra-baixa, alta densidade de dispositivos conectados |
| Apartamento com sinal Wi-Fi fraco no quarto mais distante | PLC | Usa a fiação elétrica existente — sem obras, sem novo cabo |
| Hospital que precisa de conexão estável para laudos e prontuários | FTTH (fibra simétrica) | Alta disponibilidade, velocidade simétrica, baixa latência |
| Ônibus de turismo em estrada rodando entre cidades | 4G LTE com roteador embarcado | Cobertura em rodovias, mobilidade constante |
| Evento ao ar livre com 5.000 pessoas usando celular simultaneamente | 5G (small cells) | Alta densidade de conexões simultâneas, baixa latência |
| Cidade pequena do interior com antena de rádio da operadora local | Rádio WISP | Infraestrutura típica de provedores regionais no interior |

> **Nota:** o objetivo é consolidar o raciocínio de escolha de tecnologia de conexão considerando: localização, mobilidade, número de dispositivos, velocidade necessária e infraestrutura disponível. Reforçar que um bom técnico de redes conhece todas as opções — e sabe qual usar em cada situação.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 16 — 03/06/2026 · Tecnologias de Conexão à Internet — Parte 1 |
| Próxima aula → | Aula 18 — 17/06/2026 · Endereçamento IP — Conceitos Fundamentais |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: demonstração ao vivo da diferença de latência entre 4G e Wi-Fi usando ping no terminal

---

## Observações do Professor
