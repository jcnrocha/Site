# UC: Fundamentos de Redes de Computadores
## Aula 22 — 2º Trimestre

---

## Tema

Modelo OSI — As 7 Camadas

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender a origem e o objetivo do modelo OSI — entendendo por que ele foi criado e qual problema ele resolve
- Identificar as 7 camadas do modelo OSI e a função de cada uma na comunicação em rede
- Reconhecer exemplos de protocolos e tecnologias que atuam em cada camada do modelo
- Relacionar o modelo OSI com o modelo TCP/IP visto na Aula 19 — entendendo as semelhanças e diferenças entre os dois
- Aplicar o modelo OSI como ferramenta de diagnóstico: identificar em qual camada um problema de rede pode estar ocorrendo

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores · H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 21: segurança em redes — onde o modelo OSI se encaixa na proteção de cada camada
- **Por que o modelo OSI existe**
  - Antes do OSI: cada fabricante usava seu próprio protocolo — dispositivos de marcas diferentes não se comunicavam
  - ISO (International Organization for Standardization) criou o modelo em 1984 para padronizar a comunicação
  - OSI = Open Systems Interconnection — sistemas abertos que se interconectam independente do fabricante
  - O modelo é uma referência conceitual — não é implementado diretamente, mas é usado para entender, projetar e depurar redes

- **As 7 Camadas do Modelo OSI — de baixo para cima:**

| Camada | Nome | Função principal | Exemplos |
|--------|------|-----------------|----------|
| 7 | Aplicação | Interface com o usuário e as aplicações | HTTP, HTTPS, FTP, DNS, SMTP, SSH |
| 6 | Apresentação | Tradução, criptografia e compressão dos dados | TLS/SSL, JPEG, MP4, ASCII, Unicode |
| 5 | Sessão | Estabelece, gerencia e encerra sessões de comunicação | NetBIOS, RPC, SQL Session |
| 4 | Transporte | Controle de entrega, segmentação e reassemblagem | TCP, UDP |
| 3 | Rede | Endereçamento lógico e roteamento entre redes | IP, ICMP, ARP, roteadores |
| 2 | Enlace de Dados | Endereçamento físico (MAC) e controle de acesso ao meio | Ethernet, Wi-Fi (802.11), switches |
| 1 | Física | Transmissão dos bits pelo meio físico | Cabos, fibra óptica, conectores, hubs |

- **Detalhamento de cada camada:**

  - **Camada 1 — Física**
    - Transmite bits brutos (0s e 1s) pelo meio de transmissão
    - Define voltagem, frequência, conectores e pinagem
    - Dispositivos: hubs, repetidores, cabos, fibra óptica, antenas

  - **Camada 2 — Enlace de Dados**
    - Organiza os bits em quadros (frames)
    - Endereçamento físico: endereço MAC (48 bits · ex.: 00:1A:2B:3C:4D:5E)
    - Detecção e correção de erros no enlace
    - Dispositivos: switches, bridges, placas de rede (NIC)
    - Subcamadas: LLC (controle lógico) e MAC (controle de acesso ao meio)

  - **Camada 3 — Rede**
    - Endereçamento lógico: endereço IP
    - Roteamento: determina o melhor caminho para o pacote chegar ao destino
    - Fragmentação e remontagem de pacotes
    - Dispositivos: roteadores
    - Protocolos: IPv4, IPv6, ICMP (ping), ARP

  - **Camada 4 — Transporte**
    - Segmentação dos dados em segmentos (TCP) ou datagramas (UDP)
    - Controle de fluxo, controle de erros e multiplexação por portas
    - TCP: entrega confiável · UDP: entrega rápida sem garantia

  - **Camada 5 — Sessão**
    - Gerencia o diálogo entre aplicações: abertura, manutenção e encerramento de sessões
    - Sincronização: permite retomar uma transferência interrompida do ponto onde parou
    - Menos perceptível no uso cotidiano — integrada à camada de Aplicação no TCP/IP

  - **Camada 6 — Apresentação**
    - Traduz os dados entre formatos diferentes (ex.: EBCDIC para ASCII)
    - Criptografia e descriptografia dos dados (TLS/SSL opera aqui)
    - Compressão de dados para otimizar a transmissão
    - Menos perceptível no uso cotidiano — integrada à camada de Aplicação no TCP/IP

  - **Camada 7 — Aplicação**
    - Interface direta com o usuário e as aplicações
    - Define como as aplicações se comunicam pela rede
    - Protocolos: HTTP, HTTPS, FTP, DNS, DHCP, SMTP, IMAP, SSH, Telnet

- **OSI × TCP/IP — Comparativo:**

| Modelo OSI | Modelo TCP/IP |
|------------|---------------|
| 7 — Aplicação | |
| 6 — Apresentação | Aplicação |
| 5 — Sessão | |
| 4 — Transporte | Transporte |
| 3 — Rede | Internet |
| 2 — Enlace de Dados | Acesso à Rede |
| 1 — Física | |

- **OSI como ferramenta de diagnóstico — "Em qual camada está o problema?"**
  - Cabo desconectado → Camada 1 (Física)
  - Switch não reconhece o dispositivo → Camada 2 (Enlace)
  - Dispositivo sem IP ou IP errado → Camada 3 (Rede)
  - Porta bloqueada pelo firewall → Camada 4 (Transporte)
  - Aplicação não responde, mas a rede está ok → Camada 7 (Aplicação)

- **Macete para memorizar as camadas (de baixo para cima):**
  - **F**ísica · **E**nlace · **R**ede · **T**ransporte · **S**essão · **A**presentação · **A**plicação
  - *"**Fui Embora, Reginaldo! Tô Sem Amor, Afinal."***

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 21: *"Vimos segurança em redes — hoje vamos entender o modelo que organiza toda a comunicação em camadas, usado para projetar e diagnosticar redes"* |
| Retomada | Professor pergunta: *"Quando a internet de um computador para de funcionar, por onde você começaria a investigar o problema? Pelo cabo? Pelo IP? Pelo navegador?"* — alunos respondem livremente · conectar as respostas às camadas do OSI |
| Explicação | Slides — origem do OSI, as 7 camadas (função, dispositivos e protocolos de cada uma), comparativo OSI × TCP/IP, OSI como ferramenta de diagnóstico, macete de memorização |
| Dinâmica | "Em Qual Camada Está o Problema?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: OSI é o modelo de referência com 7 camadas · cada camada tem função, dispositivos e protocolos específicos · TCP/IP condensa as 7 em 4 · OSI é ferramenta de diagnóstico · Próxima aula: Revisão Geral — 2º Trimestre |

---

## Dinâmica — "Em Qual Camada Está o Problema?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a habilidade de usar o modelo OSI como ferramenta prática de diagnóstico de problemas em redes, identificando em qual camada cada falha se manifesta — habilidade diretamente aplicável no suporte técnico, na administração de redes e no desenvolvimento de sistemas distribuídos.

**Materiais:** cartões com cenários de problema — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de problemas em redes. O desafio é identificar em qual camada do modelo OSI o problema está ocorrendo e justificar a resposta.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário: identifica a camada, os sintomas que confirmam o diagnóstico e o que poderia ser feito para resolver.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e reforça o raciocínio de diagnóstico por camadas.

**Cenários sugeridos:**

| Cenário / Sintoma | Camada OSI | Justificativa |
|-------------------|------------|---------------|
| Cabo de rede desconectado — LED da placa de rede apagado | Camada 1 — Física | Problema no meio físico de transmissão |
| Switch não aparece na lista de dispositivos da rede | Camada 2 — Enlace | Problema com endereço MAC ou configuração do switch |
| Computador sem endereço IP — exibe "169.254.x.x" | Camada 3 — Rede | DHCP não respondeu · endereço IP ausente ou incorreto |
| Aplicação não consegue conectar ao servidor na porta 443 | Camada 4 — Transporte | Porta bloqueada por firewall · problema no TCP |
| Dois sistemas não conseguem estabelecer uma sessão de transferência | Camada 5 — Sessão | Falha no gerenciamento da sessão de comunicação |
| Arquivo recebido está corrompido ou com caracteres errados | Camada 6 — Apresentação | Problema de codificação, compressão ou criptografia |
| Navegador retorna erro 500 — servidor com bug na aplicação | Camada 7 — Aplicação | Erro na aplicação web — rede está funcionando normalmente |
| Ping funciona, mas o site não abre no navegador | Camada 7 — Aplicação | Camadas 1 a 3 ok (ping passou) · problema no protocolo HTTP/DNS |

> **Nota:** o objetivo é desenvolver o raciocínio de diagnóstico em camadas: *"começo pela Camada 1 (o cabo está conectado?) e subo até encontrar onde o problema está."* Reforçar que esse método é usado por técnicos de suporte, administradores de rede e desenvolvedores de sistemas distribuídos no dia a dia profissional.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 21 — 08/07/2026 · Segurança Básica em Redes |
| Próxima aula → | Aula 23 — 05/08/2026 · Revisão Geral — 2º Trimestre |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: imprimir ou projetar o diagrama das 7 camadas OSI para fixar na parede durante toda a aula como material de consulta

---

## Observações do Professor
