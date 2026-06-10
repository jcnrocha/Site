# UC: Fundamentos de Redes de Computadores
## Aula 30 — 3º Trimestre

---

## Tema

Modelos de Rede — Cliente-Servidor e Peer-to-Peer

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que são modelos de rede e por que a escolha do modelo impacta diretamente o projeto e o desenvolvimento de sistemas
- Identificar as características, vantagens e desvantagens do modelo Cliente-Servidor
- Identificar as características, vantagens e desvantagens do modelo Peer-to-Peer (P2P)
- Diferenciar os dois modelos com base em critérios técnicos: escalabilidade, segurança, custo, gerenciamento e desempenho
- Relacionar os modelos de rede com situações reais do desenvolvimento de sistemas e do mercado de TI

**Habilidade da matriz:** H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 29: *"Vimos como as redes são estruturadas fisicamente pelas topologias — hoje vamos entender como elas funcionam do ponto de vista lógico, ou seja, como os dispositivos se relacionam entre si"*
- **O que são modelos de rede?**
  - Um modelo de rede define como os dispositivos se comunicam e quais papéis cada um desempenha na rede
  - Enquanto a topologia define a estrutura física, o modelo define a relação funcional entre os dispositivos
  - Os dois modelos principais: **Cliente-Servidor** e **Peer-to-Peer (P2P)**

- **Modelo Cliente-Servidor**
  - **Conceito:** existe uma divisão clara de papéis — um ou mais servidores oferecem recursos e serviços, e os clientes os consomem
  - **Servidor:** dispositivo dedicado que processa requisições, armazena dados e fornece serviços aos clientes · fica disponível continuamente
  - **Cliente:** dispositivo que solicita e consome os serviços do servidor · pode ser um computador, celular, tablet ou qualquer dispositivo conectado
  - **Como funciona:**
    1. Cliente envia uma requisição ao servidor (ex.: "quero acessar o arquivo X")
    2. Servidor processa a requisição e verifica permissões
    3. Servidor retorna a resposta (ex.: envia o arquivo X ao cliente)
  - **Exemplos do cotidiano:**
    - Navegar em um site: seu navegador (cliente) requisita a página ao servidor web
    - Fazer login em um sistema: o app (cliente) envia credenciais ao servidor de autenticação
    - Baixar um arquivo: cliente solicita ao servidor de arquivos
    - Assistir Netflix: app (cliente) requisita o vídeo ao servidor de streaming
    - Sistema do SENAI: computador do aluno (cliente) acessa o servidor do portal
  - **Vantagens:**
    - Gerenciamento centralizado — dados e permissões controlados em um único ponto
    - Segurança robusta — políticas de acesso aplicadas no servidor
    - Escalabilidade — novos clientes adicionados sem alterar a estrutura
    - Backup centralizado — dados do servidor são copiados em um único processo
    - Alta disponibilidade — servidores dedicados ficam no ar continuamente
  - **Desvantagens:**
    - Ponto único de falha — se o servidor cair, todos os clientes perdem o serviço
    - Custo elevado — servidores dedicados exigem hardware, licenças e manutenção
    - Dependência de infraestrutura — requer rede estável entre clientes e servidor
  - **Onde é usado:** empresas, escolas, hospitais, bancos, e-commerce, sistemas web, apps mobile — praticamente toda aplicação profissional

- **Modelo Peer-to-Peer (P2P)**
  - **Conceito:** não há distinção fixa de papéis — cada dispositivo (peer) pode atuar tanto como cliente quanto como servidor simultaneamente
  - **Como funciona:** cada peer compartilha recursos diretamente com os outros peers da rede — sem um servidor central intermediando
  - **Exemplos do cotidiano:**
    - Compartilhamento de arquivos: BitTorrent — cada usuário baixa e envia partes do arquivo simultaneamente
    - Chamadas VoIP: Skype originalmente usava P2P — as chamadas passavam diretamente entre os dispositivos
    - Criptomoedas: Bitcoin e blockchain — a rede é mantida por todos os nós sem servidor central
    - Jogos multiplayer locais: LAN party — computadores se comunicam diretamente sem servidor
    - Redes domésticas simples: dois computadores compartilhando arquivos diretamente
  - **Vantagens:**
    - Baixo custo — não requer servidor dedicado
    - Simples de configurar em pequena escala
    - Sem ponto único de falha — a rede continua mesmo se alguns peers saírem
    - Escalabilidade natural — quanto mais peers, mais recursos disponíveis
  - **Desvantagens:**
    - Segurança fraca — difícil controlar quem acessa o quê
    - Gerenciamento descentralizado — difícil aplicar políticas de forma consistente
    - Desempenho variável — depende da capacidade e disponibilidade de cada peer
    - Não recomendado para ambientes corporativos com dados sensíveis

- **Comparativo direto — Cliente-Servidor × P2P:**

| Critério | Cliente-Servidor | Peer-to-Peer |
|----------|-----------------|--------------|
| Papéis | Fixos — cliente e servidor | Dinâmicos — cada peer pode ser os dois |
| Gerenciamento | Centralizado | Descentralizado |
| Segurança | Alta — controlada no servidor | Baixa — difícil de controlar |
| Custo | Alto — servidor dedicado | Baixo — sem servidor central |
| Escalabilidade | Alta — novos clientes facilmente | Limitada em ambientes corporativos |
| Ponto de falha | Servidor central | Sem ponto único de falha |
| Desempenho | Estável e previsível | Variável — depende dos peers |
| Uso típico | Empresas, sistemas web, apps | Compartilhamento de arquivos, blockchain |

- **Modelo híbrido — o melhor dos dois mundos:**
  - Muitas aplicações modernas combinam elementos dos dois modelos
  - Exemplo: WhatsApp — servidor central gerencia contatos e entrega de mensagens, mas a chamada de voz pode ser P2P direto entre os dispositivos
  - Exemplo: jogos online — servidor central gerencia salas e rankings, mas a comunicação entre jogadores próximos pode ser P2P
  - Exemplo: CDN (Content Delivery Network) — servidores distribuídos que agem de forma similar a peers para entregar conteúdo ao usuário mais próximo

- **Conexão com o desenvolvimento de sistemas:**
  - Todo sistema web usa o modelo Cliente-Servidor: navegador/app é o cliente, backend é o servidor
  - APIs REST seguem o modelo Cliente-Servidor: o app requisita dados ao servidor via HTTP
  - Ao desenvolver um sistema, o desenvolvedor decide onde a lógica fica (no cliente ou no servidor) — essa decisão define a arquitetura da aplicação
  - Sistemas distribuídos modernos (microserviços) combinam elementos dos dois modelos

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 29: *"Vimos as topologias — hoje entendemos como os dispositivos se relacionam funcionalmente na rede"* |
| Retomada | Professor pergunta: *"Quando você abre o Instagram no celular, quem é o cliente e quem é o servidor nessa comunicação? O que cada um faz?"* — alunos respondem livremente · introduzir o modelo Cliente-Servidor a partir da resposta |
| Explicação | Slides — o que são modelos de rede, Cliente-Servidor (conceito, funcionamento, exemplos, vantagens e desvantagens), P2P (conceito, funcionamento, exemplos, vantagens e desvantagens), comparativo, modelo híbrido, conexão com desenvolvimento de sistemas |
| Dinâmica | "Cliente, Servidor ou Peer?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: Cliente-Servidor para ambientes corporativos e sistemas profissionais · P2P para compartilhamento descentralizado · Híbrido nas aplicações modernas · Conexão com o Projeto Integrador: qual modelo a rede da empresa vai usar? · Próxima aula: Redes Sem Fio — Padrões e Infraestrutura |

---

## Dinâmica — "Cliente, Servidor ou Peer?"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** consolidar a diferença entre os modelos de rede por meio de situações reais do cotidiano digital, desenvolvendo o raciocínio de identificação do modelo correto — e conectando diretamente com o Projeto Integrador, onde os alunos precisarão definir o modelo de funcionamento da rede da empresa projetada.

**Materiais:** cartões com situações — um conjunto por grupo · ou slide com as situações projetadas.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com situações de uso de rede. O desafio é identificar qual modelo está em uso (Cliente-Servidor, P2P ou Híbrido) e justificar a resposta identificando quem é cliente e quem é servidor — ou se todos são peers.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cartão: identifica o modelo, os papéis de cada dispositivo e avalia se o modelo é adequado para aquela situação.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça as características de cada modelo.

**Situações sugeridas:**

| Situação | Modelo | Justificativa |
|----------|--------|---------------|
| Aluno acessa o portal do SENAI pelo navegador para ver suas notas | Cliente-Servidor | Navegador = cliente · servidor do portal = servidor · papéis fixos |
| Dois computadores compartilham arquivos diretamente via cabo de rede sem roteador | P2P | Sem servidor central · cada computador é cliente e servidor simultaneamente |
| Download de um filme via BitTorrent — você baixa e envia partes ao mesmo tempo | P2P | Cada peer baixa e distribui partes — sem servidor central de arquivos |
| App do banco no celular consulta o saldo na conta | Cliente-Servidor | App = cliente · servidor do banco = servidor · dados centralizados e seguros |
| Chamada de voz pelo WhatsApp entre dois celulares | Híbrido | Servidor gerencia a conexão inicial · chamada pode ser P2P direto entre dispositivos |
| Desenvolvedor faz uma requisição GET a uma API REST para buscar dados de produtos | Cliente-Servidor | App/Postman = cliente · servidor da API = servidor · padrão REST é Cliente-Servidor |
| Rede de criptomoedas Bitcoin — transações validadas por todos os nós da rede | P2P | Sem servidor central · cada nó valida e retransmite transações |
| Sistema de e-commerce: cliente adiciona produto ao carrinho e finaliza a compra | Cliente-Servidor | Navegador/app = cliente · servidores de catálogo, carrinho e pagamento = servidores |

> **Nota:** o objetivo é desenvolver o raciocínio: *"existe um servidor dedicado? Os papéis são fixos ou dinâmicos? Os dados ficam centralizados ou distribuídos?"* Reforçar que no Projeto Integrador a rede corporativa usará o modelo Cliente-Servidor — com servidores de arquivos, impressão e internet no centro e os computadores dos funcionários como clientes.

---

## Conexão com o Projeto Integrador

Esta aula tem conexão direta com o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- A rede corporativa do projeto seguirá o modelo **Cliente-Servidor** — padrão para ambientes empresariais
- Os alunos precisarão identificar no projeto: quais são os servidores (arquivos, impressão, internet) e quais são os clientes (computadores dos funcionários)
- A decisão de topologia (Aula 29) + modelo (Aula 30) forma a base estrutural do projeto:
  - **Topologia:** como os dispositivos estão fisicamente conectados (geralmente Estrela)
  - **Modelo:** como os dispositivos se relacionam funcionalmente (Cliente-Servidor)

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 29 — 16/09/2026 · Topologias de Rede — Física e Lógica |
| Próxima aula → | Aula 31 — 30/09/2026 · Redes Sem Fio — Padrões e Infraestrutura |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagrama visual do modelo Cliente-Servidor e do P2P
- Questionário impresso ou digital
- Cartões com as situações da dinâmica impressos (1 conjunto por grupo) ou slide com as situações
- Se possível: demonstração ao vivo — abrir o DevTools do navegador (F12 → Network) e mostrar uma requisição HTTP sendo feita ao servidor ao carregar uma página · reforça visualmente o modelo Cliente-Servidor em ação

---

## Observações do Professor
