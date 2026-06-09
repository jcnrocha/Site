# UC: Fundamentos de Redes de Computadores
## Aula 02 — 1º Trimestre

---

## Tema

Unidades de Medida — Bits, Bytes e Múltiplos

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um bit e um byte, e por que essas são as unidades fundamentais da computação
- Identificar e converter corretamente as unidades de medida de armazenamento: KB, MB, GB, TB e PB
- Diferenciar bits por segundo (bps) de bytes por segundo (B/s) — entendendo por que essa distinção importa na prática
- Reconhecer as unidades de medida de velocidade de transmissão: bps, Kbps, Mbps, Gbps e Tbps
- Relacionar as unidades de medida com situações reais do cotidiano de TI: tamanho de arquivos, velocidade de internet e capacidade de armazenamento

**Habilidade da matriz:** H1 — Reconhecer unidades de medida empregadas na transmissão e armazenamento de dados

---

## Conteúdo

- O que é um bit — a menor unidade de informação digital: 0 ou 1
- O que é um byte — agrupamento de 8 bits · origem e significado
- Por que tudo na computação começa pelo bit: processadores, memória, transmissão e armazenamento
- Unidades de medida de armazenamento:
  - **Kilobyte (KB)** — 1.024 bytes · exemplos: um arquivo de texto simples
  - **Megabyte (MB)** — 1.024 KB · exemplos: uma foto de câmera, uma música em MP3
  - **Gigabyte (GB)** — 1.024 MB · exemplos: um filme em HD, a capacidade de um pen drive
  - **Terabyte (TB)** — 1.024 GB · exemplos: HD externo, servidor de arquivos
  - **Petabyte (PB)** — 1.024 TB · exemplos: data centers, armazenamento em nuvem em escala
- Diferença entre notação decimal (fabricantes: 1 KB = 1.000 bytes) e notação binária (sistemas operacionais: 1 KB = 1.024 bytes) — por que o HD de 1 TB parece ter menos espaço no Windows
- Unidades de medida de velocidade de transmissão:
  - **bps** — bits por segundo · unidade base
  - **Kbps** — quilobits por segundo · 1.000 bps
  - **Mbps** — megabits por segundo · 1.000 Kbps · padrão atual de planos de internet
  - **Gbps** — gigabits por segundo · redes corporativas e fibra de alta velocidade
  - **Tbps** — terabits por segundo · backbones de internet e cabos submarinos
- Diferença entre bps (velocidade de transmissão) e B/s (taxa de transferência de arquivos) — por que um plano de 100 Mbps transfere ~12,5 MB/s
- Aplicações práticas: calcular tempo de download, comparar planos de internet, entender especificações de equipamentos de rede

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 01 · Apresentação do tema do dia |
| Retomada | Professor pergunta: *"Seu plano de internet é de quantos Mega? Isso significa que você baixa arquivos a essa velocidade?"* — alunos respondem livremente · Discussão sobre a diferença entre Mbps e MB/s |
| Explicação | Slides — bit, byte, unidades de armazenamento, unidades de velocidade, diferença bps × B/s, exemplos práticos |
| Dinâmica | "Quanto Pesa? Quanto Demora?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: bit é a base · KB/MB/GB/TB medem armazenamento · bps/Kbps/Mbps/Gbps medem velocidade · Próxima aula: Velocidade de Transmissão na prática |

---

## Dinâmica — "Quanto Pesa? Quanto Demora?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a habilidade de reconhecer e aplicar unidades de medida em situações reais de TI, conectando o conteúdo teórico com decisões práticas que um técnico ou desenvolvedor toma no dia a dia — como escolher um plano de internet, dimensionar um servidor ou estimar tempo de transferência de arquivos.

**Materiais:** cartões com situações-problema — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição das situações** *(1 min)*
Cada grupo recebe 4 cartões com situações-problema. O desafio é identificar a unidade correta e, em alguns casos, fazer uma estimativa rápida.

2. **Resolução em grupo** *(8 min)*
O grupo discute e responde cada situação, justificando a escolha da unidade de medida.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma resposta. O professor complementa, corrige e reforça a lógica por trás de cada conversão.

**Situações sugeridas:**

| Situação-problema | Resposta esperada |
|-------------------|-------------------|
| Um filme em Full HD tem aproximadamente 4 ___. | 4 GB |
| Seu plano de internet é de 200 Mbps. Qual a velocidade real de download em MB/s? | ~25 MB/s (200 ÷ 8) |
| Um arquivo de texto com 3 páginas tem cerca de 30 ___. | 30 KB |
| Um HD externo para backup de fotos e vídeos tem 2 ___. | 2 TB |
| A internet de um grande data center opera em velocidades de 400 ___. | 400 Gbps ou Tbps |
| Uma música em MP3 de boa qualidade tem cerca de 5 ___. | 5 MB |
| Um pen drive escolar para guardar PDFs e apresentações tem 16 ___. | 16 GB |
| Você precisa enviar um arquivo de 800 MB com uma conexão de 50 Mbps. Quanto tempo demora? | ~128 segundos (~2 min) |

> **Nota:** o foco não é memorizar tabelas de conversão, mas desenvolver o raciocínio: *"qual grandeza estou medindo — armazenamento ou velocidade? Qual unidade faz sentido aqui?"* Reforçar que técnicos de redes e desenvolvedores usam esse raciocínio para dimensionar infraestrutura, escolher equipamentos e diagnosticar problemas de desempenho.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 01 — 11/02/2026 · Apresentação da UC e Introdução às Redes de Computadores |
| Próxima aula → | Aula 03 — 04/03/2026 · Unidades de Medida — Velocidade de Transmissão |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com as situações-problema impressos (1 conjunto por grupo) ou slide com as situações

---

## Observações do Professor
