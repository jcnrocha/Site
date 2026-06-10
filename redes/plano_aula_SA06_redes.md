# UC: Fundamentos de Redes de Computadores
## Aula 06 — 1º Trimestre

---

## Tema

Simbologias Básicas de Rede — Parte 2

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Identificar os símbolos de meios de transmissão utilizados em diagramas de rede: enlaces cabeados, fibra óptica e conexões sem fio
- Reconhecer os símbolos de segurança de rede: firewall e DMZ
- Identificar os símbolos de conectividade ampla: nuvem, links WAN e internet
- Criar e interpretar diagramas de rede completos utilizando a simbologia padronizada corretamente
- Conectar o vocabulário visual da Aula 05 com os novos símbolos desta aula — formando um repertório completo de simbologia básica de rede

**Habilidade da matriz:** H2 — Reconhecer as simbologias básicas de rede

---

## Conteúdo

- Retomada rápida da Aula 05: *"Aprendemos os símbolos dos dispositivos principais — roteador, switch, servidor, AP e estações. Hoje completamos o vocabulário visual com meios de transmissão, segurança e conectividade ampla"*
- **Símbolos de Meios de Transmissão:**

  - **Enlace Cabeado (Ethernet / par trançado)**
    - Representação: linha sólida contínua entre dois dispositivos
    - Uso: conexão física por cabo (UTP, STP, FTP) entre switch e dispositivo, entre switch e roteador, entre patch panel e switch
    - Variações: linha simples (link único) · linha dupla (link redundante / trunk)
    - Rótulo opcional: velocidade do enlace (ex.: 1 Gbps, 10 Gbps)

  - **Enlace de Fibra Óptica**
    - Representação: linha sólida com símbolo de losango ou traço diferenciado (alguns padrões usam linha laranja ou amarela)
    - Uso: conexão de longa distância entre prédios, entre switches de núcleo, backbone entre andares
    - Diferença visual para o Ethernet: geralmente indicado por cor diferente ou rótulo "Fibra" / "FO"
    - Rótulo opcional: tipo de fibra (monomodo/multimodo) e velocidade (ex.: 10 Gbps FO)

  - **Conexão Sem Fio (Wi-Fi)**
    - Representação: linha tracejada ou ondulada entre o AP e os dispositivos sem fio
    - Uso: conectar notebooks, smartphones e tablets ao access point
    - Importante: a linha tracejada indica que não há cabo físico — o sinal viaja pelo ar
    - Rótulo opcional: SSID da rede (ex.: "CorpNet") e padrão Wi-Fi (ex.: 802.11ax)

  - **Link WAN (Wide Area Network)**
    - Representação: linha com símbolo de relâmpago (lightning bolt) ou linha tracejada mais espessa entre o roteador local e o provedor/internet
    - Uso: representa o link contratado da operadora — ADSL, FTTH, link dedicado
    - Rótulo opcional: tecnologia e velocidade (ex.: FTTH 500 Mbps)

- **Símbolos de Segurança de Rede:**

  - **Firewall**
    - Representa: dispositivo ou software que filtra e controla o tráfego entre redes
    - Símbolo: caixa com chamas ou escudo — varia conforme o padrão adotado (Cisco usa um símbolo específico)
    - Posicionamento no diagrama: entre a internet (nuvem) e a rede interna · entre a DMZ e a rede interna
    - Função no diagrama: indica onde o tráfego é inspecionado e filtrado
    - Variações: firewall de borda (perimetral), firewall interno, next-generation firewall (NGFW)

  - **DMZ — Zona Desmilitarizada**
    - Representa: segmento de rede separado que fica entre a internet e a rede interna
    - Símbolo: área delimitada por dois firewalls ou segmento sombreado com rótulo "DMZ"
    - Posicionamento: entre o firewall externo (voltado à internet) e o firewall interno (voltado à LAN)
    - Componentes típicos dentro da DMZ no diagrama: servidor web, servidor de e-mail, servidor FTP

  - **VPN (Virtual Private Network)**
    - Representa: túnel criptografado entre dois pontos pela internet
    - Símbolo: linha com cadeado ou com símbolo de túnel entre dois roteadores ou entre um roteador e um usuário remoto
    - Uso no diagrama: indica conexão segura entre filiais ou entre usuário remoto e a sede

- **Símbolos de Conectividade Ampla:**

  - **Internet / Nuvem**
    - Representa: a internet pública ou qualquer rede externa desconhecida
    - Símbolo: nuvem — o mais universalmente reconhecido em diagramas de rede
    - Posicionamento: sempre no topo ou na borda do diagrama — representa o "mundo externo"
    - Variações: nuvem pública (AWS, Azure, GCP), nuvem privada, internet pública

  - **Nuvem de Provedor (Cloud Service)**
    - Representa: serviços hospedados em provedores de nuvem (AWS, Azure, GCP)
    - Símbolo: nuvem com logotipo do provedor ou rótulo identificador
    - Uso: indicar que um servidor, banco de dados ou aplicação está hospedado na nuvem

  - **Ponto de Presença de Operadora (ISP / POP)**
    - Representa: infraestrutura do provedor de internet que conecta o cliente à internet
    - Símbolo: caixa identificada com o nome da operadora ou símbolo de "cloud" menor
    - Uso: indicar onde termina a responsabilidade do cliente e começa a responsabilidade da operadora

- **Boas práticas na criação de diagramas de rede:**
  - **Hierarquia visual:** organizar do mais externo (internet) para o mais interno (dispositivos do usuário) — de cima para baixo
  - **Rótulos:** identificar todos os dispositivos com nome e função (ex.: SW-01, RTR-BORDA, SRV-WEB)
  - **Endereçamento:** indicar os IPs dos interfaces principais, especialmente do roteador e dos servidores
  - **Legenda:** incluir legenda explicando os símbolos usados quando o público não é especialista
  - **Consistência:** usar o mesmo padrão de símbolo para o mesmo tipo de dispositivo em todo o diagrama
  - **Não sobrecarregar:** diagramas muito densos são difíceis de ler — dividir em diagramas menores por nível (lógico e físico)

- **Diagrama completo comentado:**

```
          [ INTERNET / NUVEM ]
                  |
             (Link WAN)
                  |
             [ FIREWALL ]
                  |
         ┌────────┴────────┐
         |                 |
      [ DMZ ]         [ SWITCH CORE ]
    [SRV-WEB]          /    |    \
                  [SW-01] [SW-02] [SW-03]
                    |       |       |
                 [PCs]   [PCs]   [APs]---[Notebooks/Celulares]
```

  - Internet no topo representa a rede externa
  - Firewall filtra o tráfego entre internet, DMZ e rede interna
  - DMZ isola o servidor web da rede interna
  - Switch core distribui para os switches de acesso de cada andar
  - APs conectam dispositivos sem fio à rede cabeada

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada da Aula 05: *"Aprendemos os símbolos dos dispositivos — hoje completamos o vocabulário visual com meios de transmissão, firewall, DMZ e nuvem"* |
| Retomada | Professor projeta um diagrama parcial — com apenas os dispositivos (sem os enlaces e sem o firewall) — e pergunta: *"O que está faltando neste diagrama para que ele fique completo?"* — alunos respondem livremente · conectar as respostas aos novos símbolos |
| Explicação | Slides — meios de transmissão (cabeado, fibra, sem fio, WAN), firewall, DMZ, VPN, nuvem, ISP, boas práticas, diagrama completo comentado |
| Dinâmica | "Monte o Diagrama!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: linha sólida = cabo · tracejada = sem fio · nuvem = internet · chamas/escudo = firewall · DMZ entre dois firewalls · Próxima aula: Componentes de Rede — Hardware Passivo |

---

## Dinâmica — "Monte o Diagrama!"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar todo o vocabulário visual das Aulas 05 e 06, desenvolvendo a habilidade de criar e interpretar diagramas de rede completos — diretamente aplicável no Projeto Integrador, onde cada grupo precisará desenhar o diagrama da rede corporativa com simbologia correta.

**Materiais:** papel A4 ou A3 por grupo · canetas ou lápis · ou computadores com draw.io aberto.

**Passo a passo:**

1. **Recebimento do cenário** *(1 min)*
Cada grupo recebe um cartão com a descrição de uma rede simples. O desafio é desenhar o diagrama completo usando a simbologia correta — com todos os dispositivos, conexões, firewall e nuvem.

2. **Criação do diagrama** *(9 min)*
O grupo desenha o diagrama no papel ou no draw.io, usando os símbolos corretos para cada elemento descrito no cenário.

3. **Compartilhamento e correção** *(5 min)*
Cada grupo apresenta seu diagrama. O professor comenta os acertos, aponta os erros de simbologia e reforça as boas práticas.

**Cenários sugeridos:**

| Cenário para o diagrama | Elementos obrigatórios no diagrama |
|------------------------|-----------------------------------|
| Escritório com 5 PCs, 1 servidor de arquivos, 1 switch, 1 roteador, 1 firewall e acesso à internet | Nuvem (internet) · Firewall · Roteador · Switch · 5 estações · 1 servidor · enlaces cabeados |
| Empresa com Wi-Fi para funcionários — 1 AP, 3 notebooks, 1 switch, 1 roteador e 1 firewall | Nuvem · Firewall · Roteador · Switch · AP · 3 notebooks (sem fio / linha tracejada) |
| Rede com servidor web na DMZ — 1 SRV-WEB na DMZ, firewall externo, firewall interno, switch interno com 3 PCs | Nuvem · 2 Firewalls · DMZ com SRV-WEB · Switch · 3 PCs |
| Filial conectada à sede por VPN — filial com 2 PCs e roteador, sede com switch, servidor e roteador, VPN no meio | 2 Roteadores · VPN (linha com cadeado) · Nuvem no centro · Switch · Servidor · 2 PCs |

> **Nota:** o objetivo desta dinâmica é prático — os alunos criam o diagrama, não apenas identificam símbolos. Erros comuns a corrigir: usar linha sólida para conexão Wi-Fi · esquecer o firewall entre internet e rede interna · não colocar a nuvem para representar a internet · não rotular os dispositivos · esquecer a DMZ quando o cenário tem servidor web.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 05 — 18/03/2026 · Simbologias Básicas de Rede — Parte 1 |
| Próxima aula → | Aula 07 — 01/04/2026 · Componentes de Rede — Hardware Passivo |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo todos os novos símbolos em tamanho grande e o diagrama completo comentado
- Questionário impresso ou digital
- Papel A4 ou A3 e canetas/lápis para os grupos (dinâmica de criação de diagrama)
- Se possível: computadores com draw.io (app.diagrams.net) aberto para os grupos que preferirem criar o diagrama digitalmente — ferramenta gratuita e sem instalação

---

## Observações do Professor
