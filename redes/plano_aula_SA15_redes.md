# UC: Fundamentos de Redes de Computadores
## Aula 15 — 2º Trimestre

---

## Tema

Meios de Transmissão Não Guiados

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são meios de transmissão não guiados e como os dados trafegam sem um cabo físico
- Identificar os principais tipos de transmissão sem fio: Wi-Fi, Bluetooth, infravermelho e comunicação via satélite
- Reconhecer os padrões Wi-Fi (802.11 a/b/g/n/ac/ax) e suas diferenças de velocidade e frequência
- Diferenciar as faixas de frequência 2,4 GHz e 5 GHz — entendendo as vantagens e limitações de cada uma
- Identificar as principais causas de interferência em redes sem fio e como minimizá-las

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Revisão rápida: meios guiados × meios não guiados — onde paramos e o que muda agora
- O que são meios de transmissão não guiados — dados transmitidos pelo ar por meio de ondas eletromagnéticas
- **Wi-Fi (IEEE 802.11)**
  - O que é o padrão IEEE 802.11 e por que ele existe
  - Evolução dos padrões:

| Padrão | Nome | Frequência | Velocidade máxima | Lançamento |
|--------|------|------------|-------------------|------------|
| 802.11b | Wi-Fi 1 | 2,4 GHz | 11 Mbps | 1999 |
| 802.11a | Wi-Fi 2 | 5 GHz | 54 Mbps | 1999 |
| 802.11g | Wi-Fi 3 | 2,4 GHz | 54 Mbps | 2003 |
| 802.11n | Wi-Fi 4 | 2,4 e 5 GHz | 600 Mbps | 2009 |
| 802.11ac | Wi-Fi 5 | 5 GHz | 3,5 Gbps | 2013 |
| 802.11ax | Wi-Fi 6/6E | 2,4, 5 e 6 GHz | 9,6 Gbps | 2019 |

  - Frequência 2,4 GHz: maior alcance, mais interferência, paredes e obstáculos penetrados com mais facilidade
  - Frequência 5 GHz: maior velocidade, menor alcance, menos interferência, ideal para ambientes densos
  - Canais de Wi-Fi: o que são e por que a escolha do canal impacta o desempenho da rede
  - Principais fontes de interferência: micro-ondas, telefones sem fio, redes vizinhas, paredes e estruturas metálicas
- **Bluetooth**
  - Frequência: 2,4 GHz · alcance típico: até 10 metros (classe 2) ou 100 metros (classe 1)
  - Versões relevantes: 4.0 (BLE — baixo consumo), 5.0 (maior alcance e velocidade)
  - Aplicações: periféricos (teclado, mouse, fone), wearables, IoT, transferência de arquivos
- **Infravermelho (IR)**
  - Transmissão por luz infravermelha — sem fio, mas com linha de visada obrigatória
  - Alcance muito curto · praticamente obsoleto para redes · ainda presente em controles remotos
- **Comunicação via Satélite**
  - Como funciona: sinal enviado da Terra ao satélite e retransmitido ao destino
  - Órbitas: LEO (baixa — ex.: Starlink), MEO e GEO (geoestacionária)
  - Latência alta em GEO (~600 ms) × latência reduzida em LEO (~20–40 ms no Starlink)
  - Uso: áreas remotas sem infraestrutura cabeada, aviões, navios, comunicação militar
- Comparativo geral entre os meios não guiados: alcance, velocidade, interferência, custo e aplicação típica

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 14: *"Na aula passada vimos os meios com fio — hoje vamos entender como os dados viajam pelo ar"* |
| Retomada | Professor pergunta: *"Seu roteador em casa tem duas faixas — 2,4 GHz e 5 GHz. Qual você usa? Você sabe a diferença?"* — alunos respondem livremente |
| Explicação | Slides — meios não guiados, evolução do Wi-Fi, frequências 2,4 × 5 GHz, Bluetooth, infravermelho, satélite, comparativo final |
| Dinâmica | "Qual Meio Usar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: Wi-Fi para redes locais sem fio, Bluetooth para periféricos e curta distância, satélite para áreas remotas · Próxima aula: Tecnologias de Conexão à Internet — Parte 1 |

---

## Dinâmica — "Qual Meio Usar?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver o raciocínio técnico de escolha do meio de transmissão não guiado adequado para cada cenário, conectando as características de cada tecnologia sem fio com situações reais que um técnico ou desenvolvedor encontra no mercado de trabalho.

**Materiais:** cartões com cenários — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cenários** *(1 min)*
Cada grupo recebe 4 cartões com cenários de uso de tecnologia sem fio. O desafio é indicar qual meio de transmissão não guiado é o mais adequado e justificar a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário e decide: qual tecnologia usar, por quê, e quais características técnicas sustentam a decisão.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e reforça os critérios técnicos de escolha.

**Cenários sugeridos:**

| Cenário | Tecnologia indicada | Justificativa |
|---------|---------------------|---------------|
| Conectar um fone de ouvido sem fio ao celular | Bluetooth | Curta distância, baixo consumo, padrão para periféricos |
| Levar internet para uma fazenda em área rural sem fibra | Satélite (Starlink/LEO) | Único meio viável em áreas sem infraestrutura cabeada |
| Conectar notebooks de alunos em uma sala de aula | Wi-Fi 5 GHz (802.11ac) | Alta velocidade, muitos dispositivos, distância curta |
| Cobrir um galpão industrial grande com rede sem fio | Wi-Fi 2,4 GHz (802.11n) | Maior alcance, penetra obstáculos, velocidade suficiente |
| Conectar um smartwatch ao celular para sincronizar dados | Bluetooth BLE (4.0+) | Baixíssimo consumo de energia, curta distância |
| Prover internet em um avião em cruzeiro | Satélite | Único meio disponível a altitude de voo |
| Conectar dispositivos IoT espalhados por uma casa inteligente | Wi-Fi 2,4 GHz ou Bluetooth | 2,4 GHz para maior alcance · BLE para baixo consumo |
| Transmitir vídeo 4K em streaming dentro de casa sem lag | Wi-Fi 5 GHz (802.11ac/ax) | Alta velocidade, baixa interferência, ideal para streaming |

> **Nota:** o objetivo é desenvolver o raciocínio: *"qual é a distância, o ambiente, a velocidade necessária e a mobilidade exigida? A partir daí, qual tecnologia sem fio faz sentido?"* Reforçar que a escolha errada do meio sem fio é uma das causas mais comuns de problemas de desempenho em redes — e que saber diagnosticar isso é uma habilidade valorizada no mercado.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 14 — 20/05/2026 · Meios de Transmissão Guiados |
| Próxima aula → | Aula 16 — 03/06/2026 · Tecnologias de Conexão à Internet — Parte 1 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários

---

## Observações do Professor
