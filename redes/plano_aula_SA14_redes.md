# UC: Fundamentos de Redes de Computadores
## Aula 14 — 2º Trimestre

---

## Tema

Meios de Transmissão Guiados

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são meios de transmissão guiados e qual é o seu papel na infraestrutura de redes
- Identificar os principais tipos de cabos utilizados em redes: par trançado, fibra óptica e cabo coaxial
- Diferenciar as categorias de cabo par trançado (Cat5e, Cat6 e Cat6A) e reconhecer suas características de velocidade e distância
- Distinguir fibra óptica monomodo de multimodo — entendendo quando cada uma é indicada
- Reconhecer as vantagens e limitações de cada meio de transmissão guiado para aplicação em projetos de redes

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes · H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- O que são meios de transmissão — conceito e função na rede
- Classificação: meios guiados (físicos) × meios não guiados (sem fio) — visão geral para contextualizar
- **Cabo Par Trançado (Twisted Pair)**
  - UTP (Unshielded Twisted Pair) — sem blindagem · uso doméstico e corporativo
  - STP (Shielded Twisted Pair) — blindagem individual por par · ambientes com interferência
  - FTP (Foiled Twisted Pair) — blindagem global por folha · uso em ambientes industriais
  - Categorias: Cat5e (até 1 Gbps / 100 m), Cat6 (até 10 Gbps / 55 m), Cat6A (até 10 Gbps / 100 m)
  - Conector padrão: RJ-45
- **Fibra Óptica**
  - Princípio de funcionamento: transmissão de dados por pulsos de luz
  - Monomodo (SMF) — núcleo estreito (~9 µm) · longas distâncias · uso em backbones e operadoras
  - Multimodo (MMF) — núcleo mais largo (~50–62,5 µm) · curtas distâncias · uso em data centers e prédios
  - Conectores comuns: SC, LC, ST
  - Vantagens: altíssima velocidade, imunidade a interferências eletromagnéticas, longa distância
- **Cabo Coaxial**
  - Estrutura: condutor central, isolante, malha metálica e capa externa
  - Uso atual: televisão a cabo, internet via cabo (DOCSIS), câmeras de segurança (CFTV)
  - Praticamente obsoleto para LANs modernas — contexto histórico e onde ainda aparece
- Comparativo geral entre os meios guiados: velocidade, distância, custo, imunidade a interferências e aplicação típica

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Apresentação do tema do dia · Conexão com o 1º trimestre: "Vocês viram componentes de rede — hoje vamos entender o fio que conecta tudo isso" |
| Retomada | Professor pergunta: *"Quando você conecta um cabo de rede no computador, o que você acha que está dentro desse cabo? Por que ele é trançado?"* — alunos respondem livremente |
| Explicação | Slides — meios guiados × não guiados, par trançado (UTP/STP/FTP e categorias), fibra óptica (monomodo × multimodo), cabo coaxial, comparativo final |
| Dinâmica | "Qual Cabo Usar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: par trançado para LANs, fibra para longas distâncias e alta velocidade, coaxial para TV e câmeras · Próxima aula: Meios de Transmissão Não Guiados |

---

## Dinâmica — "Qual Cabo Usar?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver o raciocínio técnico de escolha do meio de transmissão adequado para cada cenário, conectando as características de cada cabo com decisões reais de infraestrutura de rede que um técnico ou desenvolvedor pode encontrar no mercado de trabalho.

**Materiais:** cartões com cenários de infraestrutura — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cenários** *(1 min)*
Cada grupo recebe 4 cartões com cenários de infraestrutura de rede. O desafio é indicar qual meio de transmissão guiado é o mais adequado e justificar a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário e decide: qual cabo usar, por quê, e quais características técnicas sustentam a decisão.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e reforça os critérios técnicos de escolha.

**Cenários sugeridos:**

| Cenário | Cabo indicado | Justificativa |
|---------|---------------|---------------|
| Conectar os computadores de um escritório de 20 pessoas em um único andar | Cat5e ou Cat6 (UTP) | Baixo custo, velocidade suficiente, distâncias curtas |
| Interligar dois prédios de uma empresa separados por 500 metros | Fibra óptica monomodo | Longa distância, alta velocidade, sem interferência |
| Instalar câmeras de segurança em um galpão industrial | Cabo coaxial | Padrão do sistema CFTV, resistência, custo |
| Conectar servidores dentro de um data center com altíssima velocidade | Fibra óptica multimodo | Curta distância, altíssima taxa de transferência |
| Cabeamento de um ambiente industrial com muita interferência elétrica | STP ou FTP | Blindagem protege contra interferências eletromagnéticas |
| Levar internet de fibra da operadora até o roteador de um condomínio | Fibra óptica monomodo | Padrão FTTH, longas distâncias da operadora ao cliente |
| Conectar computadores em uma sala de aula pequena com orçamento limitado | Cat5e (UTP) | Baixo custo, fácil instalação, velocidade adequada |
| Interligar andares de um prédio corporativo com 10 Gbps | Cat6A ou Fibra multimodo | Cat6A para 100 m ou fibra para maior confiabilidade |

> **Nota:** o objetivo não é decorar especificações técnicas, mas desenvolver o raciocínio: *"qual é a distância, a velocidade necessária, o orçamento e o ambiente? A partir daí, qual cabo faz sentido?"* Reforçar que essa decisão aparece em projetos de infraestrutura, propostas comerciais e concursos da área de TI.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 13 — 13/05/2026 · Ponte — Conexão com o 2º Trimestre |
| Próxima aula → | Aula 15 — 27/05/2026 · Meios de Transmissão Não Guiados |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: amostras físicas de cabo UTP, fibra óptica e coaxial para demonstração visual em sala

---

## Observações do Professor
