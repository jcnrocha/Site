# UC: Fundamentos de Redes de Computadores
## Aula 33 — 3º Trimestre

---

## Tema

Computação em Nuvem e Redes

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é computação em nuvem e como ela se relaciona com a infraestrutura de redes
- Identificar e diferenciar os modelos de serviço em nuvem: IaaS, PaaS e SaaS
- Diferenciar os tipos de nuvem: pública, privada e híbrida — entendendo quando cada modelo é mais adequado
- Reconhecer os principais provedores de nuvem (AWS, Azure e GCP) e seus serviços mais relevantes para a área de redes e desenvolvimento de sistemas
- Relacionar o impacto da computação em nuvem na infraestrutura de redes corporativas e no desenvolvimento de sistemas

**Habilidade da matriz:** H5 — Reconhecer tipos e características (classificação, estrutura e modelos)

---

## Conteúdo

- Retomada rápida da Aula 32: *"Estruturamos a rede corporativa completa — hoje vamos entender como a nuvem se encaixa nessa infraestrutura e o que muda quando parte dos recursos sai do servidor físico da empresa e vai para um data center remoto"*
- **O que é computação em nuvem?**
  - Fornecimento de recursos de TI — servidores, armazenamento, redes, software — pela internet, sob demanda, com pagamento pelo uso
  - Antes da nuvem: empresa precisava comprar, instalar e manter seus próprios servidores físicos
  - Com a nuvem: empresa "aluga" recursos de um provedor e acessa tudo pela internet — sem hardware próprio
  - Características essenciais (NIST):
    - **Sob demanda (On-demand):** recursos disponíveis a qualquer momento sem intervenção humana do provedor
    - **Acesso amplo pela rede:** acessível por qualquer dispositivo com internet
    - **Pooling de recursos:** recursos compartilhados entre múltiplos clientes (multitenancy)
    - **Elasticidade rápida:** aumentar ou diminuir recursos em minutos conforme a demanda
    - **Serviço medido:** pague apenas pelo que usar

- **Modelos de Serviço em Nuvem:**

  - **IaaS — Infrastructure as a Service (Infraestrutura como Serviço)**
    - O provedor oferece: servidores virtuais, armazenamento, rede e virtualização
    - O cliente gerencia: sistema operacional, middleware, runtime, dados e aplicações
    - Analogia: você aluga o terreno e a construção — mas decora e mobilia do jeito que quiser
    - Exemplos de serviços: Amazon EC2, Azure Virtual Machines, Google Compute Engine
    - Uso típico: hospedar servidores de aplicação, banco de dados, ambientes de desenvolvimento

  - **PaaS — Platform as a Service (Plataforma como Serviço)**
    - O provedor oferece: tudo do IaaS + sistema operacional, middleware e runtime
    - O cliente gerencia: apenas os dados e as aplicações
    - Analogia: você aluga um apartamento mobiliado — só precisa levar seus pertences
    - Exemplos de serviços: AWS Elastic Beanstalk, Azure App Service, Google App Engine, Heroku
    - Uso típico: desenvolver e implantar aplicações sem se preocupar com a infraestrutura subjacente

  - **SaaS — Software as a Service (Software como Serviço)**
    - O provedor oferece: tudo — infraestrutura, plataforma e o software já pronto para uso
    - O cliente gerencia: apenas seus dados e configurações de uso
    - Analogia: você usa um hotel — tudo já está pronto, arrumado e funcionando
    - Exemplos de serviços: Google Workspace (Gmail, Drive, Docs), Microsoft 365, Salesforce, Zoom, Slack, Trello
    - Uso típico: ferramentas de produtividade, CRM, comunicação, colaboração

  - **Comparativo resumido:**

| Modelo | Cliente gerencia | Provedor gerencia | Exemplo |
|--------|-----------------|-------------------|---------|
| IaaS | SO, middleware, app, dados | Virtualização, servidores, rede | AWS EC2 |
| PaaS | Aplicação e dados | SO, middleware, runtime, infra | Heroku |
| SaaS | Apenas dados e uso | Tudo | Gmail, Office 365 |

- **Tipos de Nuvem:**

  - **Nuvem Pública**
    - Recursos compartilhados com outros clientes em data centers do provedor
    - Gerenciada e mantida pelo provedor — cliente não tem acesso físico
    - Vantagens: baixo custo inicial, elasticidade, sem manutenção de hardware
    - Desvantagens: menor controle, dados fora do ambiente da empresa, dependência do provedor
    - Exemplos: AWS, Microsoft Azure, Google Cloud Platform

  - **Nuvem Privada**
    - Infraestrutura de nuvem exclusiva de uma organização — não compartilhada
    - Pode ser hospedada no próprio data center da empresa (on-premises) ou em ambiente dedicado no provedor
    - Vantagens: controle total, maior segurança e conformidade regulatória (LGPD, HIPAA)
    - Desvantagens: custo elevado, exige equipe de TI especializada
    - Exemplos: VMware vSphere, OpenStack, Microsoft Azure Stack

  - **Nuvem Híbrida**
    - Combinação de nuvem pública e privada — integradas e orquestradas
    - Dados sensíveis na nuvem privada · recursos variáveis na nuvem pública (cloud bursting)
    - Vantagens: flexibilidade, equilíbrio entre custo e controle, migração gradual
    - Exemplos: empresa com ERP no servidor local e site na AWS · banco com dados regulatórios on-premises e IA na nuvem pública

- **Principais Provedores:**

| Provedor | Empresa | Destaque | Serviço de Rede |
|----------|---------|---------|----------------|
| AWS | Amazon | Maior do mercado (~32% share) | Amazon VPC, Route 53, CloudFront |
| Azure | Microsoft | Integração com ecossistema Microsoft | Azure Virtual Network, Azure DNS |
| GCP | Google | Forte em IA/ML e dados | Google VPC, Cloud DNS, Cloud CDN |

- **Impacto da nuvem na infraestrutura de redes corporativas:**
  - **Conexão dedicada com o provedor:** links de alta velocidade entre a empresa e o data center na nuvem (AWS Direct Connect, Azure ExpressRoute)
  - **SD-WAN (Software Defined WAN):** gerenciamento inteligente de múltiplos links WAN — otimiza o tráfego para a nuvem e para filiais
  - **VPN para nuvem:** tunelamento seguro entre a rede interna da empresa e os recursos na nuvem
  - **Latência:** dados na nuvem têm latência maior que dados no servidor local — impacta aplicações sensíveis ao tempo de resposta
  - **Largura de banda:** quanto mais serviços na nuvem, mais banda a empresa precisa contratar do ISP
  - **Segurança:** o modelo de responsabilidade compartilhada — provedor protege a infraestrutura, cliente protege os dados e as aplicações

- **Conexão com o desenvolvimento de sistemas:**
  - Todo desenvolvedor moderno trabalha com nuvem: deploy de aplicações, banco de dados gerenciado, armazenamento de arquivos, envio de e-mails, autenticação
  - **Serverless:** o desenvolvedor escreve apenas o código — a infraestrutura é gerenciada completamente pelo provedor (AWS Lambda, Azure Functions, Google Cloud Functions)
  - **Containers e Kubernetes:** empacotamento de aplicações que rodam consistentemente em qualquer ambiente de nuvem
  - **CDN (Content Delivery Network):** servidores distribuídos globalmente que entregam conteúdo ao usuário mais próximo — reduz latência em aplicações web

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 32: *"Montamos a infraestrutura corporativa completa — hoje entendemos o que muda quando parte dela vai para a nuvem"* |
| Retomada | Professor pergunta: *"Vocês usam Google Drive, Gmail ou Microsoft 365? Sabem onde os arquivos ficam guardados fisicamente? E quando uma empresa coloca seu sistema na AWS, o que exatamente ela está fazendo?"* — alunos respondem livremente |
| Explicação | Slides — o que é nuvem, IaaS × PaaS × SaaS (com analogias), nuvem pública × privada × híbrida, principais provedores, impacto na infraestrutura de redes, conexão com desenvolvimento de sistemas |
| Dinâmica | "Na Nuvem ou No Servidor?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: IaaS (infraestrutura) · PaaS (plataforma) · SaaS (software pronto) · pública (compartilhada) · privada (exclusiva) · híbrida (melhor dos dois) · nuvem exige mais banda e segurança na rede · Próxima aula: Diagnóstico e Solução de Problemas em Redes |

---

## Dinâmica — "Na Nuvem ou No Servidor?"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** desenvolver o raciocínio de decisão entre infraestrutura local (on-premises) e nuvem, identificando modelos de serviço e tipos de nuvem adequados para cada cenário — conectando os conceitos da aula com decisões reais que desenvolvedores e gestores de TI tomam no mercado de trabalho.

**Materiais:** cartões com cenários de decisão — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de decisão de infraestrutura. O desafio é indicar: local (on-premises), nuvem pública, nuvem privada ou híbrida — e qual modelo de serviço (IaaS, PaaS ou SaaS) se aplica.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário e decide a melhor abordagem, justificando com base em custo, segurança, controle e flexibilidade.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os critérios de decisão.

**Cenários sugeridos:**

| Cenário | Indicação | Justificativa |
|---------|-----------|---------------|
| Startup com 5 desenvolvedores precisa hospedar uma API REST sem investir em servidores | PaaS — nuvem pública (Heroku ou AWS Elastic Beanstalk) | Sem investimento inicial em hardware · escala conforme cresce · equipe foca no código |
| Hospital precisa armazenar prontuários eletrônicos com conformidade total à LGPD | Nuvem privada ou on-premises | Dados sensíveis de saúde exigem controle total e conformidade regulatória |
| Empresa usa Gmail, Google Drive e Google Meet para toda a equipe | SaaS — nuvem pública | Software já pronto e gerenciado pelo Google · sem instalação ou manutenção |
| E-commerce precisa suportar picos de tráfego no Black Friday sem manter servidores ociosos o resto do ano | Nuvem pública IaaS com elasticidade (AWS EC2 Auto Scaling) | Elasticidade da nuvem — escala automaticamente no pico e reduz fora dele |
| Banco precisa manter dados regulatórios no Brasil mas quer usar IA da Google para análise de crédito | Nuvem híbrida | Dados sensíveis on-premises (conformidade regulatória) · IA na nuvem pública (custo e capacidade) |
| Desenvolvedor quer testar um novo banco de dados sem configurar um servidor | IaaS ou PaaS — nuvem pública | Instância de banco de dados gerenciado em minutos · paga apenas pelo tempo de uso |
| Grande empresa de varejo quer entregar imagens de produto rapidamente para usuários em todo o Brasil | SaaS / CDN — nuvem pública (AWS CloudFront) | CDN distribui o conteúdo para servidores próximos ao usuário — reduz latência |
| Escola quer sistema de gestão acadêmica sem equipe de TI para manter servidores | SaaS — nuvem pública | Sistema já pronto, hospedado e mantido pelo fornecedor · sem preocupação com infraestrutura |

> **Nota:** o objetivo é desenvolver o raciocínio: *"quais são os requisitos de custo, segurança, controle e escala? A partir daí, faz mais sentido manter on-premises ou ir para a nuvem? E qual modelo de serviço?"* Reforçar que no Projeto Integrador os grupos podem propor que alguns serviços da empresa fictícia sejam hospedados na nuvem — como o e-mail corporativo (SaaS) ou o site institucional (IaaS/PaaS).

---

## Conexão com o Projeto Integrador

Esta aula amplia as possibilidades do **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37):

- Os grupos podem enriquecer o projeto incluindo serviços em nuvem:
  - **E-mail corporativo:** Google Workspace ou Microsoft 365 (SaaS) — sem necessidade de servidor de e-mail local
  - **Site institucional:** hospedado em IaaS ou PaaS na nuvem pública
  - **Backup:** armazenamento em nuvem para backup dos dados do servidor local
  - **Conexão:** VPN ou link dedicado entre a rede interna e os recursos na nuvem
- A decisão de incluir nuvem impacta o dimensionamento do link de internet da empresa — mais banda é necessária

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 32 — 07/10/2026 · Redes Corporativas e Infraestrutura Empresarial |
| Próxima aula → | Aula 34 — 21/10/2026 · Diagnóstico e Solução de Problemas em Redes |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagrama comparativo IaaS × PaaS × SaaS e diagrama de nuvem híbrida
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: demonstração ao vivo do console da AWS Free Tier ou do Google Cloud Console — mostrar a criação de uma instância de máquina virtual ou de um bucket de armazenamento em menos de 2 minutos para ilustrar a elasticidade da nuvem

---

## Observações do Professor
