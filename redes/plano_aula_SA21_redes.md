# UC: Fundamentos de Redes de Computadores
## Aula 21 — 2º Trimestre

---

## Tema

Segurança Básica em Redes

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender os principais conceitos de segurança em redes: confidencialidade, integridade e disponibilidade (tríade CIA)
- Identificar o que é um firewall, como ele funciona e qual é o seu papel na proteção de uma rede
- Reconhecer o conceito de VPN — entendendo como ela cria um túnel seguro de comunicação pela internet
- Identificar as principais ameaças em redes: vírus, phishing, ransomware, ataques DDoS e engenharia social
- Relacionar boas práticas de segurança com o dia a dia do desenvolvedor de sistemas e do técnico de redes

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Retomada rápida da Aula 20: protocolos de aplicação — onde as ameaças se manifestam
- **Por que segurança em redes importa**
  - Dados trafegam por redes públicas e privadas — qualquer ponto do caminho pode ser vulnerável
  - Impactos de uma violação: perda de dados, prejuízo financeiro, danos à reputação, responsabilidade legal
- **Tríade CIA — Os três pilares da segurança da informação**
  - **Confidencialidade** — somente pessoas autorizadas acessam os dados · ex.: criptografia, controle de acesso
  - **Integridade** — os dados não foram alterados indevidamente · ex.: hash, assinatura digital
  - **Disponibilidade** — o sistema está acessível quando necessário · ex.: redundância, backups, proteção contra DDoS
- **Firewall**
  - O que é: dispositivo ou software que monitora e filtra o tráfego de rede com base em regras
  - Tipos de firewall:
    - **Packet Filtering** — analisa cabeçalhos dos pacotes (IP, porta, protocolo) · mais simples
    - **Stateful Inspection** — monitora o estado das conexões · mais inteligente
    - **Next-Generation Firewall (NGFW)** — inspeção profunda de pacotes, filtro de aplicação, IPS integrado
  - Firewall de software × firewall de hardware
  - Exemplos: Windows Defender Firewall, pfSense, Fortinet, Cisco ASA
  - O que o firewall faz e o que ele NÃO faz — limitações importantes
- **VPN — Virtual Private Network**
  - O que é: cria um túnel criptografado entre dois pontos pela internet pública
  - Como funciona: os dados são encapsulados e criptografados antes de sair do dispositivo
  - Casos de uso:
    - Acesso remoto seguro a redes corporativas (home office)
    - Conexão segura entre filiais de uma empresa (site-to-site)
    - Proteção em redes Wi-Fi públicas (hotéis, aeroportos, cafés)
  - Protocolos VPN comuns: OpenVPN, WireGuard, IPSec, L2TP
  - O que a VPN protege — e o que ela não protege
- **Principais ameaças em redes:**

| Ameaça | Como funciona | Como se proteger |
|--------|---------------|-----------------|
| Vírus / Malware | Código malicioso que se instala no dispositivo | Antivírus atualizado, não executar arquivos desconhecidos |
| Phishing | E-mail ou site falso que rouba credenciais | Verificar remetente, não clicar em links suspeitos |
| Ransomware | Criptografa arquivos e exige resgate | Backup regular, não abrir anexos desconhecidos |
| Ataque DDoS | Sobrecarga de requisições para derrubar um serviço | Firewall, CDN, serviços anti-DDoS (Cloudflare) |
| Man-in-the-Middle | Interceptação da comunicação entre dois pontos | HTTPS, VPN, certificados digitais |
| Engenharia Social | Manipulação psicológica para obter informações | Treinamento e conscientização dos usuários |
| Força Bruta | Tentativa exaustiva de senhas até encontrar a correta | Senhas fortes, bloqueio após tentativas, MFA |

- **Boas práticas de segurança para desenvolvedores e técnicos:**
  - Usar HTTPS em todas as aplicações web
  - Nunca armazenar senhas em texto puro — sempre usar hash (bcrypt, Argon2)
  - Validar e sanitizar todas as entradas do usuário — prevenir SQL Injection e XSS
  - Manter sistemas e dependências sempre atualizados
  - Usar autenticação multifator (MFA) em sistemas críticos
  - Realizar backups regulares e testá-los periodicamente
  - Aplicar o princípio do menor privilégio — dar apenas as permissões necessárias

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 20: *"Vimos os protocolos de aplicação — hoje vamos entender como proteger o tráfego que passa por esses protocolos"* |
| Retomada | Professor pergunta: *"Alguém já recebeu um e-mail suspeito pedindo para clicar em um link? Ou já ouviu falar de empresa que teve dados sequestrados por ransomware? O que vocês fariam para se proteger?"* — alunos respondem livremente |
| Explicação | Slides — tríade CIA, firewall (tipos e limites), VPN (funcionamento e casos de uso), principais ameaças, boas práticas para desenvolvedores |
| Dinâmica | "Ameaça ou Proteção?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: CIA é a base da segurança · firewall filtra o tráfego · VPN cria túnel seguro · ameaças são variadas — defesa é em camadas · Próxima aula: Modelo OSI — As 7 Camadas |

---

## Dinâmica — "Ameaça ou Proteção?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver a capacidade de identificar ameaças e medidas de proteção em cenários reais de segurança em redes, conectando o conteúdo teórico com situações que desenvolvedores, técnicos e usuários comuns enfrentam no dia a dia — e reforçando que segurança é responsabilidade de todos na cadeia de TI.

**Materiais:** cartões com cenários — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de segurança. O desafio é identificar: qual ameaça está presente (ou qual proteção está sendo usada) e o que deve ser feito.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário: identifica a ameaça ou proteção, avalia o risco e propõe uma ação.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um cenário. O professor complementa, corrige e reforça os conceitos de segurança envolvidos.

**Cenários sugeridos:**

| Cenário | Ameaça / Proteção | O que fazer |
|---------|-------------------|-------------|
| Funcionário recebe e-mail do "banco" pedindo para atualizar a senha clicando em um link | Phishing | Não clicar · verificar o remetente · reportar ao setor de TI |
| Site da empresa ficou fora do ar após receber milhões de requisições simultâneas | Ataque DDoS | Ativar serviço anti-DDoS · bloquear IPs suspeitos no firewall |
| Desenvolvedor armazenou senhas dos usuários em texto puro no banco de dados | Má prática de segurança | Usar hash seguro (bcrypt/Argon2) · nunca armazenar senha em texto puro |
| Colaborador em home office acessa o sistema interno da empresa com segurança | VPN | Prática correta — túnel criptografado protege os dados em trânsito |
| Arquivos do servidor foram criptografados e apareceu mensagem pedindo pagamento | Ransomware | Isolar o sistema da rede · acionar backup · não pagar o resgate |
| Regra no firewall bloqueia todo tráfego na porta 23 (Telnet) | Proteção por firewall | Prática correta — Telnet é inseguro, deve ser substituído por SSH (porta 22) |
| Usuário conecta ao Wi-Fi público do aeroporto e acessa o sistema bancário sem VPN | Man-in-the-Middle | Usar VPN antes de acessar dados sensíveis em redes públicas |
| Sistema web não valida os dados do formulário de login | Vulnerabilidade — SQL Injection | Sanitizar e validar todas as entradas · usar prepared statements |

> **Nota:** o objetivo é desenvolver o raciocínio: *"consigo identificar uma ameaça quando a vejo? Sei qual proteção aplicar em cada situação?"* Reforçar que segurança não é responsabilidade apenas do setor de TI — desenvolvedores que escrevem código inseguro criam vulnerabilidades, e usuários que clicam em links suspeitos abrem brechas. Segurança é cultura.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 20 — 01/07/2026 · Protocolos de Aplicação — HTTP, DNS, DHCP e FTP |
| Próxima aula → | Aula 22 — 29/07/2026 · Modelo OSI — As 7 Camadas |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: demonstração ao vivo — mostrar o cabeçalho de um e-mail de phishing real (anonimizado) para ilustrar como identificar remetentes falsos

---

## Observações do Professor
