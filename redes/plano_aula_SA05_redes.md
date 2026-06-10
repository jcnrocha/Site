# UC: Fundamentos de Redes de Computadores
## Aula 05 — 1º Trimestre

---

## Tema

Simbologias Básicas de Rede — Parte 1

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são simbologias de rede e por que a padronização é fundamental para a comunicação técnica entre profissionais de TI
- Identificar os símbolos padrão ANSI/ISO para os principais dispositivos de rede: roteadores, switches, hubs, servidores e estações de trabalho
- Reconhecer os símbolos de conectividade básica: enlaces cabeados e pontos de acesso sem fio
- Interpretar um diagrama de rede simples — identificando os dispositivos e suas conexões a partir dos símbolos
- Iniciar a leitura de diagramas de rede com vocabulário visual padronizado

**Habilidade da matriz:** H2 — Reconhecer as simbologias básicas de rede

---

## Conteúdo

- Retomada rápida da Aula 04: *"Vimos onde os dados são armazenados em uma rede. Hoje vamos aprender como representar esses equipamentos visualmente em um diagrama — a linguagem universal dos projetos de rede"*
- **Por que simbologias padronizadas?**
  - Um diagrama de rede é como uma planta baixa de um imóvel — precisa ser compreendido por qualquer profissional, independentemente da empresa ou do país
  - Sem padronização: cada empresa usaria símbolos diferentes — comunicação confusa e documentação inutilizável por terceiros
  - Com padronização (ANSI/ISO e Cisco): um técnico no Brasil e um engenheiro na Alemanha leem o mesmo diagrama e entendem a mesma coisa
  - **Padrões existentes:**
    - **ANSI/TIA:** padrão americano — base para a maioria dos diagramas corporativos
    - **ISO/IEC:** padrão internacional
    - **Cisco:** símbolos proprietários amplamente adotados no mercado — reconhecidos mundialmente mesmo fora do ecossistema Cisco
    - **Ferramentas comuns:** draw.io (gratuito), Microsoft Visio, Lucidchart, Cisco Packet Tracer

- **Símbolos dos Principais Dispositivos de Rede — Parte 1:**

  - **Estação de Trabalho (Workstation / Desktop)**
    - Representa: computador pessoal ou estação de trabalho de um usuário
    - Símbolo: monitor com teclado ou desktop com tela
    - Função na rede: dispositivo cliente que solicita recursos — acessa arquivos, internet, impressoras
    - Variações: desktop, laptop/notebook, tablet

  - **Servidor (Server)**
    - Representa: computador dedicado que oferece serviços à rede
    - Símbolo: caixa retangular com detalhes de rack ou torre — geralmente mais robusta que a estação
    - Função na rede: armazena dados, processa requisições, oferece serviços (arquivos, e-mail, web, banco de dados)
    - Variações: servidor de arquivos, servidor web, servidor de banco de dados, servidor de e-mail

  - **Hub**
    - Representa: dispositivo de conectividade básica que conecta múltiplos dispositivos em uma rede
    - Símbolo: caixa retangular com múltiplas portas ou ícone específico
    - Função na rede: repassa os dados recebidos para TODAS as portas simultaneamente — sem inteligência
    - **Importante:** hub é considerado obsoleto — substituído pelo switch em praticamente todos os ambientes modernos
    - Diferença fundamental para o switch: hub compartilha a banda · switch dedica a banda por porta

  - **Switch**
    - Representa: dispositivo inteligente de conectividade que interliga dispositivos em uma rede local
    - Símbolo: caixa retangular com setas indicando comutação bidirecional ou ícone de switch
    - Função na rede: encaminha dados apenas para a porta de destino correto (com base no endereço MAC) — não para todas as portas como o hub
    - É o coração de qualquer LAN moderna — todo dispositivo cabeado conecta ao switch
    - Variações: switch de acesso, switch de distribuição, switch de núcleo (core), switch gerenciável (managed), switch não gerenciável (unmanaged)

  - **Roteador (Router)**
    - Representa: dispositivo que interliga redes diferentes e encaminha pacotes entre elas
    - Símbolo: círculo com setas apontando em múltiplas direções (símbolo universal de roteamento)
    - Função na rede: conecta a rede interna (LAN) à internet (WAN) · decide o melhor caminho para cada pacote · atribui IPs via DHCP em redes domésticas
    - Diferença para o switch: switch conecta dispositivos na mesma rede · roteador conecta redes diferentes
    - Exemplos: roteador doméstico Wi-Fi, roteador corporativo Cisco, MikroTik

  - **Access Point (AP) sem fio**
    - Representa: dispositivo que cria e transmite o sinal Wi-Fi para dispositivos sem fio
    - Símbolo: antenas irradiando ondas ou ícone de dispositivo com ondas
    - Função na rede: estende a rede cabeada para dispositivos sem fio (notebooks, celulares, tablets)
    - Diferença para o roteador: AP não roteia — apenas fornece acesso sem fio à rede já existente

  - **Dispositivos móveis (Smartphone e Notebook)**
    - Representam: dispositivos clientes sem fio que se conectam ao AP
    - Símbolo: ícone de smartphone ou notebook
    - Função: clientes da rede sem fio — consomem recursos como estações de trabalho

- **Regras de leitura de um diagrama de rede:**
  - **Linhas sólidas:** conexões cabeadas (Ethernet, fibra óptica)
  - **Linhas tracejadas ou onduladas:** conexões sem fio (Wi-Fi)
  - **Hierarquia visual:** internet/nuvem no topo → roteador → switch → dispositivos finais na base
  - **Rótulos:** identificam o nome do dispositivo, endereço IP ou função (ex.: SW-01, SRV-ARQUIVOS)
  - **Nuvem:** símbolo padrão para representar a internet ou uma rede externa desconhecida

- **Lendo um diagrama simples:**

```
          [ INTERNET / NUVEM ]
                  |
              [ ROTEADOR ]
                  |
              [ SWITCH ]
           /     |      \
    [PC-01]  [PC-02]  [SERVIDOR]
```

  - A nuvem representa a internet (rede externa)
  - O roteador conecta a rede interna à internet
  - O switch distribui as conexões internamente
  - PCs e servidor são os dispositivos finais da rede

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada da Aula 04: *"Vimos onde os dados são guardados — hoje aprendemos a representar os equipamentos de rede em diagramas padronizados"* |
| Retomada | Professor projeta um diagrama de rede simples sem legenda e pergunta: *"O que vocês conseguem identificar neste diagrama? Quais dispositivos reconhecem?"* — alunos respondem livremente · conectar as respostas aos símbolos que serão estudados |
| Explicação | Slides — por que padronizar, padrões ANSI/ISO e Cisco, símbolos de cada dispositivo (estação, servidor, hub, switch, roteador, AP, dispositivos móveis), regras de leitura, diagrama simples comentado |
| Dinâmica | "Identifique o Dispositivo!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: roteador (círculo com setas) · switch (caixa com comutação) · hub (obsoleto) · servidor (caixa robusta) · AP (ondas) · Próxima aula: Simbologias — Parte 2 (meios de transmissão, firewall, nuvem e WAN) |

---

## Dinâmica — "Identifique o Dispositivo!"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar o reconhecimento dos símbolos de rede por meio da interpretação de diagramas simples — desenvolvendo a habilidade de leitura e comunicação visual técnica que será usada no Projeto Integrador e em qualquer documentação de infraestrutura de rede.

**Materiais:** cartões com fragmentos de diagramas ou descrições de cenários — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões. Cada cartão mostra um fragmento de diagrama de rede ou descreve um cenário. O desafio é: identificar os dispositivos pelos símbolos OU escolher o símbolo correto para representar o dispositivo descrito.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica os dispositivos, descreve sua função e verifica se o símbolo está sendo usado corretamente.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça o significado de cada símbolo e sua função na rede.

**Situações sugeridas:**

| Situação / Fragmento | Resposta esperada | O que reforçar |
|----------------------|------------------|----------------|
| Símbolo de círculo com 4 setas apontando em direções diferentes | Roteador | Encaminha pacotes entre redes diferentes · gateway da rede |
| Caixa retangular com setas bidirecionais e múltiplas portas | Switch | Comuta dados apenas para a porta correta · coração da LAN |
| Símbolo com antenas irradiando ondas semicirculares | Access Point | Distribui sinal Wi-Fi · não roteia · estende a rede cabeada |
| Dispositivo no topo do diagrama com o símbolo de nuvem conectado ao roteador | Internet / Nuvem | A nuvem representa a internet ou rede externa |
| Caixa robusta identificada como "SRV-ARQUIVOS" conectada ao switch | Servidor de arquivos | Centraliza armazenamento · dispositivo que oferece serviços |
| Caixa igual ao switch mas com a legenda "Hub" — conectada a 4 PCs | Hub | Repassa dados para TODAS as portas · obsoleto · substituído pelo switch |
| Diagrama com: Nuvem → Roteador → Switch → 3 PCs e 1 Servidor | Topologia estrela básica | Hierarquia correta · switch no centro conectando todos os dispositivos finais |
| Cenário: "Preciso representar o celular de um usuário conectado ao Wi-Fi da empresa" | Smartphone conectado ao AP por linha tracejada | Dispositivo móvel + AP + conexão sem fio (tracejada) |

> **Nota:** o objetivo é desenvolver o "vocabulário visual" de redes — ao ver um símbolo, o aluno deve identificar instintivamente o dispositivo e sua função. Reforçar que esses símbolos são universais: um diagrama feito com esses padrões será lido corretamente por qualquer profissional de TI no mundo.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 04 — 11/03/2026 · Tipos de Armazenamento em Redes |
| Próxima aula → | Aula 06 — 25/03/2026 · Simbologias Básicas de Rede — Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo os símbolos em tamanho grande e um diagrama simples comentado
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: abrir o draw.io (app.diagrams.net) ao vivo e mostrar a biblioteca de símbolos de rede — demonstrar como arrastar e conectar os dispositivos em um diagrama simples em tempo real

---

## Observações do Professor
