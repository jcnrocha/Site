# UC: Fundamentos de Redes de Computadores
## Aula 34 — 3º Trimestre

---

## Tema

Diagnóstico e Solução de Problemas em Redes

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender a metodologia de diagnóstico em camadas — usando o modelo OSI como guia para identificar onde um problema de rede está ocorrendo
- Identificar e utilizar as principais ferramentas de diagnóstico de redes: ping, tracert/traceroute, ipconfig/ifconfig e nslookup
- Reconhecer os problemas mais comuns em redes e suas causas típicas
- Aplicar boas práticas de troubleshooting de forma sistemática e eficiente
- Relacionar o diagnóstico de redes com situações reais do suporte técnico e do desenvolvimento de sistemas

**Habilidade da matriz:** H3 — Reconhecer componentes e ativos de redes · H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Retomada rápida da Aula 33: *"Vimos como a nuvem se integra à infraestrutura corporativa — hoje aprendemos a diagnosticar e resolver problemas quando algo falha nessa infraestrutura"*
- **Por que saber diagnosticar redes?**
  - Qualquer profissional de TI — desenvolvedor, analista, técnico de suporte — precisa identificar se um problema está na rede, no servidor, na aplicação ou no dispositivo do usuário
  - Um diagnóstico correto reduz o tempo de resolução e evita intervenções desnecessárias
  - Desenvolvedores que entendem de redes resolvem problemas de conexão sem precisar acionar o setor de infraestrutura a cada incidente

- **Metodologia de diagnóstico em camadas (modelo OSI):**
  - A abordagem mais eficiente é partir da Camada 1 (Física) e subir até a Camada 7 (Aplicação) — ou partir dos sintomas e identificar em qual camada o problema está
  - **Bottom-up (de baixo para cima):** começa verificando o cabo, depois o endereço IP, depois o protocolo, depois a aplicação
  - **Top-down (de cima para baixo):** começa pela aplicação e desce até o físico — útil quando o sintoma é claro (ex.: "o site não abre")
  - **Divide and conquer:** testa no meio da pilha e divide o problema em duas metades — ex.: se o ping funciona, descarta Camadas 1 a 3

  | Camada | Pergunta de diagnóstico | Ferramenta |
  |--------|------------------------|-----------|
  | 1 — Física | O cabo está conectado? O LED da placa está aceso? | Inspeção visual |
  | 2 — Enlace | O switch reconhece o dispositivo? O MAC está na tabela? | `arp -a` |
  | 3 — Rede | O dispositivo tem IP? Consegue fazer ping no gateway? | `ipconfig` / `ping` |
  | 4 — Transporte | A porta está aberta? O firewall está bloqueando? | `netstat` / `telnet` |
  | 5/6 — Sessão/Apresentação | A sessão está sendo estabelecida? Certificado válido? | Logs da aplicação |
  | 7 — Aplicação | O serviço está rodando? O DNS resolve o nome? | `nslookup` / browser |

- **Ferramentas de diagnóstico:**

  - **ping**
    - Envia pacotes ICMP Echo Request ao destino e aguarda respostas ICMP Echo Reply
    - O que verifica: conectividade IP entre origem e destino, latência (RTT — Round Trip Time) e perda de pacotes
    - Sintaxe: `ping 8.8.8.8` · `ping google.com` · `ping -t 192.168.1.1` (contínuo no Windows)
    - Interpretação dos resultados:
      - Resposta normal: conectividade OK — camadas 1 a 3 funcionando
      - Request timed out: destino não responde — pode ser firewall, cabo, IP errado ou host desligado
      - Destination host unreachable: sem rota para o destino — problema de roteamento ou gateway
      - 100% packet loss: sem conectividade — verificar camadas 1 a 3

  - **tracert / traceroute**
    - Mapeia o caminho (rota) que os pacotes percorrem da origem até o destino, mostrando cada salto (hop)
    - Sintaxe: `tracert google.com` (Windows) · `traceroute google.com` (Linux/Mac)
    - O que verifica: onde o pacote está sendo bloqueado ou atrasado no caminho
    - Interpretação: cada linha é um roteador no caminho · `* * *` indica que o roteador não responde (firewall bloqueando ICMP) · tempo alto em um salto indica gargalo naquele ponto

  - **ipconfig / ifconfig**
    - Exibe as configurações de rede do dispositivo: IP, máscara de sub-rede, gateway padrão e servidores DNS
    - Sintaxe: `ipconfig` (Windows) · `ifconfig` ou `ip addr` (Linux/Mac)
    - Comandos adicionais:
      - `ipconfig /all` — exibe informações detalhadas incluindo endereço MAC e servidores DHCP/DNS
      - `ipconfig /release` — libera o IP atual obtido por DHCP
      - `ipconfig /renew` — solicita novo IP ao servidor DHCP
      - `ipconfig /flushdns` — limpa o cache DNS local — resolve problemas de resolução de nomes desatualizada
    - O que verificar: IP na faixa correta? Gateway correto? DNS configurado?
    - IP 169.254.x.x (APIPA): indica que o DHCP não respondeu — dispositivo sem IP válido

  - **nslookup**
    - Consulta servidores DNS para resolver nomes de domínio em endereços IP
    - Sintaxe: `nslookup google.com` · `nslookup google.com 8.8.8.8` (consulta servidor específico)
    - O que verifica: o DNS está respondendo? O nome está sendo resolvido corretamente? Qual servidor DNS está sendo usado?
    - Uso prático: site não abre mas ping no IP funciona → problema de DNS · `nslookup` confirma se o nome resolve

  - **netstat**
    - Exibe conexões de rede ativas, portas abertas e tabela de roteamento
    - Sintaxe: `netstat -an` (todas as conexões) · `netstat -b` (Windows — mostra o processo de cada conexão)
    - O que verifica: quais portas estão abertas? Há conexões suspeitas? O serviço está escutando na porta correta?

  - **arp -a**
    - Exibe a tabela ARP — mapeamento entre endereços IP e endereços MAC na rede local
    - Útil para verificar se o gateway está sendo reconhecido e para identificar conflitos de IP

- **Problemas mais comuns e suas causas:**

  | Sintoma | Causa mais provável | Verificação |
  |---------|-------------------|-------------|
  | Sem acesso à internet, mas rede local funciona | Gateway ou link do ISP com problema | `ping` no gateway · `tracert` para 8.8.8.8 |
  | IP 169.254.x.x no dispositivo | DHCP não respondeu | `ipconfig /release` e `/renew` · verificar servidor DHCP |
  | Site não abre, mas ping no IP funciona | Problema de DNS | `nslookup` · `ipconfig /flushdns` |
  | Lentidão em um segmento da rede | Congestionamento, cabo ruim ou duplex mismatch | `ping` com `-t` para medir perda · verificar cabo e negociação do switch |
  | Conexão cai periodicamente | Interferência (Wi-Fi), cabo com defeito ou DHCP lease expirando | Trocar cabo · verificar canal Wi-Fi · aumentar lease time do DHCP |
  | Aplicação não conecta ao servidor | Porta bloqueada por firewall | `netstat` · `telnet ip porta` · verificar regras do firewall |
  | Computador não aparece na rede | Placa de rede desabilitada, cabo ou switch com problema | Inspeção visual · `ipconfig` · verificar gerenciador de dispositivos |

- **Boas práticas de troubleshooting:**
  - **Documentar antes de mexer:** anote o que está funcionando, o que não está e o que foi alterado
  - **Um passo de cada vez:** altere apenas uma variável por vez para isolar a causa
  - **Testar do simples para o complexo:** cabo → IP → DNS → aplicação
  - **Usar ferramentas nativas antes de ferramentas externas:** ping e ipconfig antes de Wireshark
  - **Verificar o óbvio primeiro:** cabo conectado? Dispositivo ligado? Wi-Fi habilitado?
  - **Reproduzir o problema antes de resolver:** entenda exatamente quando e como o problema ocorre
  - **Registrar a solução:** documentar o problema e a solução encontrada para referência futura

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 33: *"Vimos a nuvem — hoje voltamos para o chão: quando a rede falha, como diagnosticamos e resolvemos?"* |
| Retomada | Professor pergunta: *"Quando a internet da sua casa cai, qual é a primeira coisa que você faz? Reinicia o roteador? Verifica o cabo? Liga para a operadora? Existe uma ordem lógica para isso?"* — alunos respondem livremente · conectar as respostas à metodologia bottom-up |
| Explicação | Slides — metodologia OSI para diagnóstico, ferramentas (ping, tracert, ipconfig, nslookup, netstat, arp), tabela de problemas comuns, boas práticas de troubleshooting |
| Dinâmica | "Resolva o Problema!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: diagnóstico em camadas do OSI · ping testa conectividade · tracert mapeia o caminho · ipconfig mostra a configuração · nslookup verifica o DNS · um passo de cada vez · Próxima aula: Tendências em Redes — IoT e Redes do Futuro |

---

## Dinâmica — "Resolva o Problema!"

**Duração:** 15 minutos · **Agrupamento:** grupos do Projeto Integrador (4 a 5 alunos)

**Objetivo:** desenvolver o raciocínio sistemático de diagnóstico e solução de problemas em redes, aplicando as ferramentas e a metodologia da aula em cenários reais de suporte técnico — habilidade essencial para técnicos de redes e desenvolvedores que precisam identificar se um problema está na rede ou na aplicação.

**Materiais:** cartões com casos de suporte técnico — um conjunto por grupo · ou slide com os casos projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com casos de suporte técnico. O desafio é: identificar a causa provável, indicar qual ferramenta usar para confirmar o diagnóstico e propor a solução.

2. **Análise em grupo** *(8 min)*
O grupo discute cada caso: identifica a camada OSI afetada, a causa mais provável, a ferramenta de diagnóstico e a solução.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um caso. O professor complementa, corrige e reforça a metodologia de diagnóstico.

**Casos sugeridos:**

| Caso de Suporte | Causa provável | Ferramenta | Solução |
|----------------|---------------|-----------|---------|
| "Meu computador não acessa a internet, mas o colega ao lado acessa normalmente" | Problema no dispositivo — IP, DNS ou cabo do ponto específico | `ipconfig` · `ping` no gateway | Verificar IP (DHCP?), cabo e DNS do dispositivo |
| "O site da empresa não abre, mas consigo acessar outros sites normalmente" | Problema de DNS ou no servidor web da empresa | `nslookup empresa.com` · `ping ip-do-servidor` | `ipconfig /flushdns` · verificar servidor DNS · verificar servidor web |
| "A rede ficou lenta para todo mundo depois das 14h todos os dias" | Congestionamento em horário de pico — possível loop ou broadcast storm | `ping -t gateway` para medir perda · verificar switches | Identificar o switch com problema · verificar STP · verificar loops |
| "Consigo fazer ping no servidor mas a aplicação não conecta na porta 8080" | Porta 8080 bloqueada pelo firewall ou serviço não está rodando | `netstat -an` no servidor · `telnet servidor 8080` | Verificar regras do firewall · verificar se o serviço está ativo |
| "O notebook mostra IP 169.254.1.100 e não acessa a rede" | DHCP não respondeu — IP APIPA atribuído automaticamente | `ipconfig /release` e `/renew` | Verificar servidor DHCP · verificar cabo · verificar VLAN |
| "Funcionário novo não consegue acessar o compartilhamento de arquivos do servidor" | Permissão negada ou problema de DNS resolvendo o nome do servidor incorretamente | `nslookup nome-servidor` · verificar permissões | Corrigir permissão no Active Directory · verificar DNS interno |
| "Internet muito lenta somente no Wi-Fi, no cabo é normal" | Interferência no canal Wi-Fi ou muitos dispositivos no mesmo AP | `ping -t gateway` via Wi-Fi para medir RTT e perda | Trocar canal do AP · verificar densidade de dispositivos · considerar AP adicional |
| "Desenvolvedor relata que a API externa retorna timeout esporadicamente" | Problema de roteamento ou instabilidade no link WAN | `tracert api.externa.com` · `ping -t api.externa.com` | Identificar o salto com problema no tracert · contatar ISP se o problema for externo |

> **Nota:** o objetivo é desenvolver o raciocínio sistemático: *"qual é o sintoma? Em qual camada OSI esse sintoma se manifesta? Qual ferramenta confirma o diagnóstico? Qual é a solução?"* Reforçar que esse processo metódico economiza tempo e evita soluções aleatórias — "reiniciar tudo e torcer" não é diagnóstico.

---

## Conexão com o Projeto Integrador

Esta aula contribui com o **Projeto Integrador — Desenho de Rede Corporativa** (Aulas 36 e 37) de forma prática:

- Os grupos devem incluir no documento do projeto uma seção de **"Plano de Diagnóstico":**
  - Quais ferramentas serão usadas para monitorar e diagnosticar a rede projetada?
  - Quais são os pontos críticos de falha identificados no projeto?
  - Qual é o procedimento de troubleshooting para os problemas mais comuns da rede projetada?
- Essa seção demonstra maturidade técnica e visão operacional — vai além do simples diagrama de rede

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 33 — 14/10/2026 · Computação em Nuvem e Redes |
| Próxima aula → | Aula 35 — 28/10/2026 · Tendências em Redes — IoT e Redes do Futuro |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Cartões com os casos da dinâmica impressos (1 conjunto por grupo) ou slide com os casos
- **Recomendado:** demonstração ao vivo no terminal — executar `ping`, `tracert`, `ipconfig /all` e `nslookup` no computador da sala enquanto explica cada ferramenta · nada substitui ver o comando rodando em tempo real

---

## Observações do Professor
