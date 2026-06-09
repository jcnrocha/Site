# UC: Fundamentos de Redes de Computadores
## Aula 19 — 2º Trimestre

---

## Tema

Protocolos de Rede — TCP/IP e UDP

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um protocolo de rede e por que ele é essencial para a comunicação entre dispositivos
- Identificar a estrutura e as camadas do modelo TCP/IP — entendendo a função de cada camada
- Diferenciar TCP de UDP: características, funcionamento e situações de uso de cada protocolo
- Reconhecer exemplos práticos de aplicações que usam TCP e aplicações que usam UDP no cotidiano de TI
- Relacionar o modelo TCP/IP com o funcionamento real de aplicações desenvolvidas por programadores

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- O que é um protocolo de rede — conjunto de regras que define como os dispositivos se comunicam
- Analogia: protocolo é como um idioma comum — sem ele, os dispositivos não se entendem
- **Modelo TCP/IP — As 4 Camadas**
  - Por que o modelo existe: padronizar a comunicação entre fabricantes e sistemas diferentes
  - Comparação rápida com o modelo OSI (7 camadas) — contexto para entender onde o TCP/IP se encaixa

| Camada TCP/IP | Função | Exemplos de protocolos |
|---------------|--------|------------------------|
| 4 — Aplicação | Interface com o usuário e aplicações | HTTP, HTTPS, FTP, DNS, DHCP, SMTP, SSH |
| 3 — Transporte | Controle de entrega dos dados entre hosts | TCP, UDP |
| 2 — Internet | Endereçamento e roteamento dos pacotes | IP (IPv4/IPv6), ICMP, ARP |
| 1 — Acesso à Rede | Transmissão física dos bits no meio | Ethernet, Wi-Fi, Fibra, PPP |

- **TCP — Transmission Control Protocol**
  - Protocolo orientado à conexão: estabelece uma sessão antes de transmitir dados
  - Three-Way Handshake (aperto de mão de três vias): SYN → SYN-ACK → ACK
  - Garantias do TCP:
    - **Entrega garantida** — confirma o recebimento de cada pacote (ACK)
    - **Ordem garantida** — remonta os pacotes na sequência correta
    - **Controle de fluxo** — ajusta a velocidade de envio conforme a capacidade do receptor
    - **Controle de congestionamento** — reduz a transmissão em caso de sobrecarga da rede
  - Desvantagem: overhead maior — mais lento que UDP por causa das verificações
  - Quando usar TCP: qualquer situação em que a integridade dos dados é crítica
  - Exemplos de uso: navegação web (HTTP/HTTPS), e-mail (SMTP/IMAP), transferência de arquivos (FTP), acesso remoto (SSH)

- **UDP — User Datagram Protocol**
  - Protocolo sem conexão: envia os dados sem estabelecer sessão prévia
  - Sem garantia de entrega, sem verificação de ordem, sem confirmação de recebimento
  - Vantagem: muito mais rápido e com menor latência que o TCP
  - Quando usar UDP: situações em que a velocidade é mais importante que a perfeição dos dados
  - Exemplos de uso: streaming de vídeo e áudio (YouTube, Netflix, Spotify), videoconferências (Meet, Zoom, Teams), jogos online, DNS, VoIP

- **Comparativo TCP × UDP:**

| Característica | TCP | UDP |
|----------------|-----|-----|
| Tipo de conexão | Orientado à conexão | Sem conexão |
| Entrega garantida | Sim | Não |
| Ordem dos pacotes | Garantida | Não garantida |
| Velocidade | Mais lento | Mais rápido |
| Overhead | Alto | Baixo |
| Controle de erros | Sim | Mínimo |
| Uso típico | Web, e-mail, FTP, SSH | Streaming, jogos, DNS, VoIP |

- **Portas de rede**
  - O que são portas: identificam qual aplicação/serviço está recebendo os dados no host de destino
  - Analogia: o IP é o endereço do prédio, a porta é o número do apartamento
  - Portas bem conhecidas (Well-Known Ports — 0 a 1023):

| Porta | Protocolo | Serviço |
|-------|-----------|---------|
| 80 | TCP | HTTP |
| 443 | TCP | HTTPS |
| 21 | TCP | FTP |
| 22 | TCP | SSH |
| 25 | TCP | SMTP (e-mail) |
| 53 | UDP/TCP | DNS |
| 67/68 | UDP | DHCP |
| 3389 | TCP | RDP (Área de Trabalho Remota) |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 18: *"Vimos como os dispositivos são identificados pelo IP — hoje vamos entender como eles se comunicam usando protocolos"* |
| Retomada | Professor pergunta: *"Quando você assiste a um vídeo no YouTube e trava, o que você acha que aconteceu? E quando você baixa um arquivo e ele chega corrompido — o que falhou?"* — alunos respondem livremente |
| Explicação | Slides — o que é protocolo, modelo TCP/IP (4 camadas), TCP (handshake, garantias), UDP (sem conexão, velocidade), comparativo TCP × UDP, portas de rede |
| Dinâmica | "TCP ou UDP?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: TCP garante entrega e ordem — ideal para dados críticos · UDP é rápido — ideal para tempo real · portas identificam o serviço no destino · Próxima aula: Protocolos de Aplicação — HTTP, DNS, DHCP e FTP |

---

## Dinâmica — "TCP ou UDP?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar a diferença entre TCP e UDP por meio de situações reais do cotidiano digital, desenvolvendo o raciocínio técnico de identificação do protocolo de transporte mais adequado para cada tipo de aplicação — habilidade essencial para desenvolvedores que criam sistemas que se comunicam em rede.

**Materiais:** cartões com situações de uso — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com situações de uso de aplicações em rede. O desafio é identificar qual protocolo de transporte — TCP ou UDP — é utilizado e justificar a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada situação e decide: TCP ou UDP, por quê, e o que aconteceria se o protocolo errado fosse usado.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça o raciocínio por trás de cada escolha.

**Situações sugeridas:**

| Situação | Protocolo | Justificativa |
|----------|-----------|---------------|
| Baixar um arquivo ZIP do servidor | TCP | Qualquer bit corrompido torna o arquivo inutilizável — integridade é crítica |
| Assistir a um vídeo ao vivo no YouTube | UDP | Pequenas perdas de pacotes são aceitáveis — velocidade e continuidade são prioritárias |
| Fazer login em um servidor via SSH | TCP | Comandos precisam chegar completos e na ordem correta |
| Jogar um jogo online multiplayer em tempo real | UDP | Latência mínima é essencial — um pacote atrasado é pior que um pacote perdido |
| Enviar um e-mail com anexo importante | TCP | O e-mail e o anexo precisam chegar completos e sem erros |
| Realizar uma videochamada no Google Meet | UDP | Tempo real — é melhor perder um frame do que travar a chamada |
| Consultar o DNS para resolver um nome de domínio | UDP | Consulta rápida e simples — a aplicação reenviar se não receber resposta |
| Transferir o código-fonte de um projeto via FTP | TCP | Arquivos de código precisam chegar íntegros — um byte errado quebra o sistema |

> **Nota:** o objetivo é desenvolver o raciocínio: *"o dado que estou transmitindo pode ter perdas? A velocidade é mais crítica que a integridade? A resposta determina se uso TCP ou UDP."* Reforçar que desenvolvedores de sistemas precisam entender esse conceito ao criar aplicações que usam sockets, APIs e comunicação em rede.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 18 — 17/06/2026 · Endereçamento IP — Conceitos Fundamentais |
| Próxima aula → | Aula 20 — 01/07/2026 · Protocolos de Aplicação — HTTP, DNS, DHCP e FTP |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: demonstração ao vivo — abrir o Wireshark ou usar `netstat` no terminal para mostrar conexões TCP ativas no computador da sala

---

## Observações do Professor
