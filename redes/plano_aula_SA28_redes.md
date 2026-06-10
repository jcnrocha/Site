# UC: Fundamentos de Redes de Computadores
## Aula 28 — 3º Trimestre

---

## Tema

Classificação das Redes por Abrangência

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é a classificação de redes por abrangência geográfica e por que ela é utilizada como ponto de partida para o projeto de redes
- Identificar e diferenciar os principais tipos de rede: PAN, LAN, MAN, WAN e GAN
- Reconhecer exemplos reais de cada tipo de rede no cotidiano e no contexto de desenvolvimento de sistemas
- Relacionar cada tipo de rede com os dispositivos, tecnologias e meios de transmissão tipicamente utilizados em cada abrangência
- Aplicar o conceito de classificação por abrangência como primeiro passo no planejamento do Projeto Integrador

**Habilidade da matriz:** H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 27 (Ponte): *"Na aula passada introduzimos brevemente a classificação de redes — hoje vamos aprofundar cada tipo"*
- **Por que classificar redes?**
  - A classificação por abrangência ajuda a definir: quais tecnologias usar, qual infraestrutura é necessária, qual o custo e qual a complexidade do projeto
  - É o primeiro critério que um projetista de redes utiliza ao iniciar um novo projeto
- **PAN — Personal Area Network (Rede de Área Pessoal)**
  - Abrangência: poucos metros (até ~10 m)
  - Conecta dispositivos pessoais de um único usuário
  - Tecnologias típicas: Bluetooth, NFC, infravermelho, USB
  - Exemplos: conexão entre smartwatch e celular, fone Bluetooth, teclado sem fio, pagamento por aproximação (NFC)
  - Característica principal: mobilidade e baixo consumo de energia
- **LAN — Local Area Network (Rede de Área Local)**
  - Abrangência: um único ambiente — sala, andar, prédio ou campus (até alguns km)
  - A rede mais comum no dia a dia: doméstica, corporativa e escolar
  - Tecnologias típicas: Ethernet (par trançado Cat5e/6/6A), Wi-Fi (802.11), switches e roteadores
  - Exemplos: rede do SENAI, rede de um escritório, rede doméstica com roteador Wi-Fi, laboratório de informática
  - Característica principal: alta velocidade, baixa latência, gerenciamento centralizado
- **MAN — Metropolitan Area Network (Rede de Área Metropolitana)**
  - Abrangência: uma cidade ou região metropolitana (até ~100 km)
  - Conecta múltiplas LANs dentro de uma mesma cidade ou região
  - Tecnologias típicas: fibra óptica metropolitana, WiMAX, redes de operadoras
  - Exemplos: rede que interliga todas as unidades do SENAI de uma cidade, rede de prefeitura conectando secretarias, rede de operadora distribuindo internet pela cidade
  - Característica principal: infraestrutura gerenciada por operadoras ou órgãos públicos
- **WAN — Wide Area Network (Rede de Área Ampla)**
  - Abrangência: países, continentes — longas distâncias (centenas a milhares de km)
  - Conecta múltiplas LANs e MANs separadas geograficamente
  - Tecnologias típicas: fibra óptica de longa distância, cabos submarinos, links de operadoras, MPLS, VPN
  - Exemplos: rede corporativa interligando filiais em diferentes estados ou países, conexão entre data centers de grandes empresas (Amazon, Google), links dedicados de operadoras
  - Característica principal: gerenciada por múltiplos provedores, alta latência em comparação com LAN, custos elevados
- **GAN — Global Area Network (Rede de Área Global)**
  - Abrangência: mundial — todos os continentes
  - A própria internet é o maior exemplo de GAN
  - Tecnologias típicas: cabos submarinos de fibra óptica, satélites, grandes backbones de internet
  - Exemplos: internet pública, rede global de uma multinacional, sistemas de comunicação via satélite
  - Característica principal: interconexão de todas as redes do planeta — sem uma única entidade controladora
- **Comparativo geral:**

| Tipo | Abrangência | Velocidade Típica | Exemplos de Tecnologia | Exemplos Reais |
|------|-------------|-------------------|----------------------|----------------|
| PAN | ~10 m | Baixa a média | Bluetooth, NFC | Smartwatch, fone sem fio |
| LAN | Prédio/campus | Alta (1–10 Gbps) | Ethernet, Wi-Fi | Rede escolar, escritório |
| MAN | Cidade/região | Média-alta | Fibra metro, WiMAX | Rede de prefeitura |
| WAN | Países/continentes | Média | MPLS, VPN, fibra | Rede corporativa multi-filial |
| GAN | Mundial | Variada | Cabos submarinos, satélite | Internet pública |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Conexão com a Aula 27: *"Fizemos a ponte — hoje mergulhamos na classificação de redes"* · Apresentação do tema |
| Retomada | Professor pergunta: *"A rede Wi-Fi da sua casa e a internet que você acessa por ela são o mesmo tipo de rede? O que é diferente?"* — alunos respondem livremente · conectar as respostas à diferença entre LAN e GAN |
| Explicação | Slides — por que classificar, PAN, LAN, MAN, WAN, GAN (cada um com definição, exemplos e tecnologias), comparativo geral |
| Dinâmica | "Classifique a Rede!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: PAN (pessoal) → LAN (local) → MAN (cidade) → WAN (países) → GAN (mundo) · conexão com o Projeto Integrador: *"Qual tipo de rede vocês vão projetar?"* · Próxima aula: Topologias de Rede |

---

## Dinâmica — "Classifique a Rede!"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** consolidar a classificação de redes por abrangência por meio de situações reais do cotidiano digital, desenvolvendo o raciocínio de identificação do tipo de rede a partir de suas características — habilidade diretamente aplicada no Projeto Integrador, onde os alunos precisarão definir o tipo de rede que estão projetando.

**Materiais:** cartões com descrições de redes — um conjunto por grupo · ou slide com as descrições projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com descrições de situações reais de rede. O desafio é identificar qual tipo de rede (PAN, LAN, MAN, WAN ou GAN) está sendo descrito e justificar com base na abrangência e nas tecnologias envolvidas.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica o tipo, a abrangência geográfica e as tecnologias típicas daquela rede.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça as características de cada tipo de rede.

**Cenários sugeridos:**

| Cenário | Tipo de Rede | Justificativa |
|---------|-------------|---------------|
| Seu smartwatch sincroniza dados de saúde com o celular via Bluetooth | PAN | Rede pessoal · alcance de poucos metros · tecnologia Bluetooth |
| O laboratório de informática do SENAI conecta 30 computadores em um único switch | LAN | Rede local · mesmo ambiente · Ethernet e Wi-Fi |
| A prefeitura interliga todas as suas secretarias espalhadas pela cidade com fibra óptica | MAN | Abrangência metropolitana · fibra da operadora local |
| Uma empresa conecta sua sede em São Paulo com a filial em Buenos Aires via link dedicado | WAN | Longa distância entre países · link de operadora ou VPN |
| Você acessa um servidor na Coreia do Sul pelo navegador em segundos | GAN | Rede global · cabos submarinos de fibra · internet pública |
| Um roteador Wi-Fi distribui internet para todos os cômodos de uma casa | LAN | Rede local doméstica · Wi-Fi 802.11 · alcance do prédio |
| Uma operadora de telecomunicações distribui internet por fibra óptica para bairros de uma cidade | MAN | Infraestrutura metropolitana · fibra da operadora |
| Um pagamento por aproximação (NFC) é feito na maquininha do mercado | PAN | Rede de curtíssimo alcance · NFC · comunicação pessoal |

> **Nota:** o objetivo é desenvolver o raciocínio: *"qual é a abrangência geográfica? Quem ela conecta e onde? A partir daí, qual tipo de rede é esse?"* Reforçar que no Projeto Integrador a primeira decisão que o grupo vai tomar é exatamente essa: que tipo de rede está sendo projetada?

---

## Conexão com o Projeto Integrador

Esta aula tem conexão direta com o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- A primeira decisão do projeto é definir **qual tipo de rede** a empresa fictícia vai ter
- A maioria dos cenários do projeto envolve uma **LAN** (rede interna da empresa) com conexão à internet (GAN via ISP)
- Grupos que já receberam o cenário do projeto devem começar a pensar: *"Nossa rede é uma LAN? Tem uma MAN envolvida? Como ela se conecta à internet?"*

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 27 — 02/09/2026 · Ponte — Conexão com o 3º Trimestre |
| Próxima aula → | Aula 29 — 16/09/2026 · Topologias de Rede — Física e Lógica |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: mapa do Brasil ou do mundo para ilustrar visualmente a diferença de abrangência entre LAN, MAN, WAN e GAN durante a explicação

---

## Observações do Professor
