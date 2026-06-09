# UC: Fundamentos de Redes de Computadores
## Aula 18 — 2º Trimestre

---

## Tema

Endereçamento IP — Conceitos Fundamentais

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um endereço IP e qual é o seu papel na comunicação entre dispositivos em uma rede
- Diferenciar IPv4 de IPv6 — entendendo por que a transição entre os dois protocolos é necessária
- Identificar a estrutura de um endereço IPv4: notação decimal pontuada, octetos e classes
- Reconhecer a diferença entre endereços IP públicos e privados — e quando cada um é utilizado
- Compreender os conceitos de máscara de sub-rede, gateway padrão, DHCP e IP fixo aplicados ao dia a dia de redes

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- O que é um endereço IP — identificador único de um dispositivo em uma rede · analogia com o CEP e número de uma casa
- Por que o IP é necessário: sem ele, os pacotes de dados não sabem para onde ir
- **IPv4**
  - Estrutura: 4 octetos separados por pontos · notação decimal · ex.: 192.168.1.10
  - Cada octeto vai de 0 a 255 — por quê? (8 bits = 2⁸ = 256 valores)
  - Total de endereços IPv4: ~4,3 bilhões (2³² = 4.294.967.296)
  - Esgotamento do IPv4: por que acabaram os endereços e o que foi feito para contornar isso
  - Classes de endereços IPv4:

| Classe | Faixa do 1º octeto | Uso típico |
|--------|-------------------|------------|
| A | 1 – 126 | Grandes redes · poucas redes, muitos hosts |
| B | 128 – 191 | Redes médias |
| C | 192 – 223 | Redes pequenas · muitas redes, poucos hosts |
| D | 224 – 239 | Multicast |
| E | 240 – 255 | Reservado / experimental |

- **Endereços IP Privados (RFC 1918)**
  - Faixas reservadas para uso interno — não roteáveis na internet pública:
    - Classe A: 10.0.0.0 – 10.255.255.255
    - Classe B: 172.16.0.0 – 172.31.255.255
    - Classe C: 192.168.0.0 – 192.168.255.255
  - Uso: redes domésticas, empresariais e laboratórios
- **Endereços IP Públicos**
  - Atribuídos por provedores (ISPs) e visíveis na internet
  - Podem ser estáticos (fixos) ou dinâmicos (mudam a cada conexão)
- **NAT (Network Address Translation)**
  - Como vários dispositivos com IP privado compartilham um único IP público
  - Solução que prolongou a vida útil do IPv4
- **IPv6**
  - Por que surgiu: esgotamento do IPv4
  - Estrutura: 128 bits · 8 grupos de 4 dígitos hexadecimais separados por dois pontos · ex.: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
  - Total de endereços: 2¹²⁸ — número praticamente inesgotável
  - Simplificação da notação: omissão de zeros · ex.: 2001:db8::8a2e:370:7334
  - Coexistência com IPv4: dual stack, tunneling e tradução
  - Por que a adoção ainda é lenta no Brasil e no mundo
- **Máscara de Sub-rede**
  - O que é e para que serve: define qual parte do IP identifica a rede e qual identifica o host
  - Exemplos comuns: 255.255.255.0 (/24), 255.255.0.0 (/16), 255.0.0.0 (/8)
  - Notação CIDR: /24, /16, /8 — leitura e interpretação
- **Gateway Padrão**
  - O que é: o "portão de saída" da rede local para outras redes e para a internet
  - Geralmente é o endereço IP do roteador
- **DHCP × IP Fixo (Estático)**
  - DHCP (Dynamic Host Configuration Protocol): servidor atribui IP automaticamente ao dispositivo
  - IP Fixo: configurado manualmente — quando usar? Servidores, impressoras, câmeras, roteadores
  - Vantagens e desvantagens de cada abordagem

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 17: *"Vimos como a internet chega até nós — agora vamos entender como cada dispositivo é identificado dentro de uma rede"* |
| Retomada | Professor pergunta: *"Alguém sabe o IP do próprio computador ou celular? Como você descobriria? O que significa aquele número 192.168.x.x que aparece nas configurações?"* — alunos respondem livremente |
| Explicação | Slides — o que é IP, IPv4 (estrutura, classes, privado × público, NAT), IPv6 (estrutura, por que existe), máscara de sub-rede, gateway, DHCP × IP fixo |
| Dinâmica | "Desvenda o Endereço" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: IP identifica o dispositivo · IPv4 esgotado, IPv6 em adoção · privado para uso interno, público para internet · DHCP automático, IP fixo para servidores · Próxima aula: Protocolos de Rede — TCP/IP e UDP |

---

## Dinâmica — "Desvenda o Endereço"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a habilidade de interpretar endereços IP, identificar se são públicos ou privados, reconhecer classes e compreender a função da máscara de sub-rede — conectando o conteúdo teórico com situações práticas que um técnico de redes encontra no dia a dia.

**Materiais:** cartões com endereços IP e situações — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com endereços IP ou situações-problema. O desafio é analisar cada endereço e responder as perguntas do cartão.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica classe, público ou privado, função e o que o endereço representa naquele contexto.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma análise. O professor complementa, corrige e reforça os conceitos de cada endereço.

**Cartões sugeridos:**

| Endereço / Situação | O que analisar | Resposta esperada |
|---------------------|----------------|-------------------|
| 192.168.0.1 | Classe? Público ou privado? O que costuma ser? | Classe C · Privado · Geralmente o gateway (roteador) da rede doméstica |
| 10.0.0.50 | Classe? Público ou privado? Onde é usado? | Classe A · Privado · Redes corporativas grandes |
| 8.8.8.8 | Público ou privado? Você reconhece esse endereço? | Público · DNS público do Google |
| 172.16.5.100 | Classe? Público ou privado? | Classe B · Privado · Faixa reservada RFC 1918 |
| 192.168.1.10 com máscara 255.255.255.0 | Qual é a rede? Quantos hosts possíveis? | Rede: 192.168.1.0 · Hosts: 254 (2⁸ – 2) |
| Dispositivo recebe 192.168.0.105 automaticamente ao conectar no Wi-Fi | Qual serviço fez isso? IP fixo ou dinâmico? | DHCP · Dinâmico |
| Servidor de arquivos configurado com 192.168.1.5 manualmente | Por que IP fixo? Qual a vantagem? | Sempre o mesmo endereço · Fácil de localizar na rede |
| 2001:db8::1 | IPv4 ou IPv6? Como identificar? | IPv6 · Presença de ":" e dígitos hexadecimais |

> **Nota:** o objetivo é desenvolver o raciocínio: *"ao ver um endereço IP, consigo identificar se é privado ou público, a qual classe pertence e o que aquilo representa na rede."* Reforçar que esse conhecimento é base para configuração de redes, diagnóstico de problemas e desenvolvimento de sistemas que se comunicam em rede.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 17 — 10/06/2026 · Tecnologias de Conexão à Internet — Parte 2 |
| Próxima aula → | Aula 19 — 24/06/2026 · Protocolos de Rede — TCP/IP e UDP |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os endereços da dinâmica impressos (1 conjunto por grupo) ou slide com os endereços
- Se possível: demonstração ao vivo — abrir o terminal e digitar `ipconfig` (Windows) ou `ifconfig` (Linux/Mac) para mostrar o IP, máscara e gateway do próprio computador da sala

---

## Observações do Professor
