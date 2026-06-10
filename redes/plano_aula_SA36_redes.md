# UC: Fundamentos de Redes de Computadores
## Aula 36 — 3º Trimestre

---

## Tema

Projeto Integrador — Desenho de Rede Corporativa

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Aplicar de forma integrada os conhecimentos adquiridos ao longo do 3º trimestre no desenvolvimento de um projeto real de rede corporativa
- Definir e justificar tecnicamente as escolhas de topologia, modelo, endereçamento IP, meios de transmissão, solução sem fio e segurança para a rede projetada
- Elaborar o diagrama de rede com simbologia correta, incluindo todos os componentes definidos no projeto
- Desenvolver o documento de justificativa técnica das escolhas realizadas no projeto
- Trabalhar de forma colaborativa em grupo, distribuindo responsabilidades e integrando as contribuições individuais em um produto coeso

**Habilidade da matriz:** H1 · H2 · H3 · H4 · H5 — aplicação integrada de todas as habilidades da UC

---

## Conteúdo

- Esta aula é dedicada ao **desenvolvimento do Projeto Integrador** — não há conteúdo expositivo novo
- Os grupos trabalham ativamente no projeto com orientação do professor
- **Retomada da proposta do Projeto Integrador (lançado na Aula 27):**
  - Cada grupo recebeu um cenário de uma empresa fictícia e deve projetar a infraestrutura de rede completa
  - O produto final é composto de dois entregáveis:
    - **Diagrama de rede:** representação visual completa com simbologia correta de todos os componentes
    - **Documento de justificativa técnica:** explicação fundamentada de cada decisão de projeto

---

## Cenários das Empresas (sugestão — professor adapta conforme a turma)

> O professor distribui um cenário diferente para cada grupo. Os cenários abaixo são sugestões — podem ser adaptados para a realidade local.

**Cenário A — Escritório Contábil:**
Empresa com 25 funcionários em um único andar de um prédio comercial. Possui 3 departamentos: Contabilidade (10 pessoas), Administrativo (8 pessoas) e Diretoria (7 pessoas). Precisa de acesso à internet, impressoras em rede, servidor de arquivos compartilhados e Wi-Fi para notebooks e celulares. Clientes visitam o escritório eventualmente.

**Cenário B — Clínica Médica:**
Clínica com 2 andares — térreo (recepção, salas de espera e 4 consultórios) e 1º andar (administração, farmácia e arquivo). 20 computadores no total, sistema de prontuário eletrônico em servidor local, câmeras de segurança IP, Wi-Fi para pacientes na sala de espera e rede separada para equipamentos médicos.

**Cenário C — Escola Técnica:**
Instituição com 3 blocos: administrativo (15 computadores), laboratório de informática (30 computadores) e sala dos professores (10 computadores). Necessita de servidor de arquivos, internet para todos os blocos, Wi-Fi para alunos com acesso restrito, câmeras de segurança e impressoras em rede.

**Cenário D — Loja de Varejo:**
Rede com loja física (20 PDVs, 5 computadores administrativos, câmeras de segurança, Wi-Fi para clientes) e um pequeno escritório de administração no mesmo prédio (10 computadores, servidor de banco de dados do sistema de vendas). Precisa de link de internet redundante para garantir que os PDVs nunca fiquem offline.

**Cenário E — Empresa de Desenvolvimento de Software:**
Startup com 30 desenvolvedores em espaço aberto (open office), 1 sala de reuniões com sistema de videoconferência, servidor local de desenvolvimento (Git, CI/CD), acesso a serviços em nuvem (AWS, GitHub), Wi-Fi de alta velocidade em toda a área e isolamento da rede de desenvolvimento da rede administrativa.

---

## Estrutura do Projeto Integrador

### Entregável 1 — Diagrama de Rede

O diagrama deve conter obrigatoriamente:

- [ ] Representação de todos os dispositivos com simbologia correta (H2)
- [ ] Switch(es) e suas conexões com os dispositivos finais
- [ ] Roteador conectando a rede interna ao link de internet (ISP)
- [ ] Access point(s) com a localização indicada
- [ ] Servidor(es) com identificação do serviço (arquivos, DHCP, etc.)
- [ ] Firewall ou indicação de onde a segurança perimetral é aplicada
- [ ] DMZ (se o cenário tiver servidor web ou serviços públicos)
- [ ] Indicação das VLANs ou segmentos de rede
- [ ] Endereçamento IP de cada segmento (rede, máscara e gateway)
- [ ] Identificação dos meios de transmissão utilizados (cabo, fibra, Wi-Fi)

### Entregável 2 — Documento de Justificativa Técnica

O documento deve responder:

| Decisão de Projeto | Pergunta a responder |
|-------------------|---------------------|
| Tipo de rede | Qual é a classificação da rede projetada (PAN/LAN/MAN/WAN)? Por quê? |
| Topologia | Qual topologia foi escolhida? Por que ela é adequada para este cenário? |
| Modelo | Qual modelo de rede (Cliente-Servidor ou P2P)? Por quê? |
| Meios de transmissão | Quais cabos foram usados? Por que essa categoria/tipo? |
| Endereçamento IP | Qual faixa de IP? Máscaras? Quantos hosts por segmento? |
| VLANs | Quais VLANs foram criadas? Qual o critério de segmentação? |
| Wi-Fi | Quantos APs? Qual padrão? Qual SSID? Qual segurança (WPA2/WPA3)? |
| Segurança | Firewall? DMZ? Política de acesso? Padrão Wi-Fi? |
| Serviços em nuvem | Algum serviço vai para a nuvem? Qual modelo (IaaS/PaaS/SaaS)? |
| Alta disponibilidade | Há redundância? Como é garantida a continuidade do serviço? |
| Plano de diagnóstico | Quais ferramentas e procedimentos de troubleshooting para a rede? |
| Visão de futuro | A rede suporta expansão para IoT? 5G? Qual seria o próximo passo? |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Apresentação da estrutura da aula · Distribuição dos cenários (se ainda não foram entregues) · Formação ou confirmação dos grupos |
| Briefing do projeto | Professor apresenta os dois entregáveis, os critérios de avaliação e o cronograma: *"Hoje trabalhamos no projeto — na Aula 37 vocês apresentam"* · Esclarece dúvidas sobre o escopo |
| Desenvolvimento | Grupos trabalham ativamente no projeto · professor circula entre os grupos orientando, questionando e validando escolhas técnicas · Cada grupo deve sair da aula com pelo menos o diagrama iniciado e as decisões principais definidas |
| Checkpoint | Nos últimos 10 minutos: cada grupo faz um status rápido de 1 minuto — o que foi decidido, o que ainda falta · professor identifica grupos que precisam de mais orientação |
| Fechamento | Orientações finais para completar o projeto até a Aula 37 · Lembrete: apresentação na próxima aula — cada grupo terá 10 a 15 minutos |

---

## Critérios de Avaliação do Projeto

| Critério | Descrição | Peso |
|----------|-----------|------|
| Coerência técnica | As escolhas fazem sentido para o cenário? Os componentes estão corretos? | 30% |
| Simbologia e diagrama | O diagrama usa a simbologia correta? Está legível e completo? | 20% |
| Endereçamento IP | A faixa de IP é adequada? Máscaras corretas? Quantidade de hosts planejada? | 15% |
| Justificativa técnica | As decisões foram explicadas com fundamentação nos conteúdos da UC? | 20% |
| Apresentação | Clareza na comunicação · todos os membros participam · domínio do conteúdo | 15% |

---

## Orientações para o Professor

**Durante o desenvolvimento, questionar cada grupo:**
- *"Por que vocês escolheram essa topologia e não outra?"*
- *"Quantos hosts precisam nesse segmento? A máscara que vocês colocaram suporta isso?"*
- *"Onde fica o firewall no diagrama? O que ele filtra?"*
- *"O visitante vai usar qual SSID? Ele consegue acessar o servidor de arquivos por esse SSID?"*
- *"Se o switch principal cair, o que acontece? Há redundância?"*
- *"Vocês pensaram em onde colocar os servidores fisicamente? Há uma sala de servidores no cenário?"*

**Erros mais comuns a corrigir:**
- Usar IP público (ex.: 8.x.x.x) para a rede interna
- Esquecer o gateway em cada segmento
- Colocar todos os dispositivos na mesma rede sem segmentação
- Dimensionar a máscara incorretamente (poucos hosts para a quantidade de dispositivos)
- Não colocar firewall entre a internet e a rede interna
- Esquecer de segregar a rede de visitantes (SSID Guest) da rede interna

---

## Recursos Necessários

- Projetor ou TV (para apresentar os critérios e o checklist do projeto)
- Computador com HDMI
- **Para os grupos:**
  - Papel A3 ou A4 para rascunho do diagrama
  - Canetas coloridas ou lápis para o diagrama físico
  - Computadores para pesquisa e digitalização do diagrama (opcional — pode ser entregue no papel)
  - Ferramenta de diagrama (opcional): draw.io (gratuito, online), Packet Tracer (Cisco), Lucidchart ou Microsoft Visio
- Enunciado do cenário de cada grupo impresso
- Checklist de entregáveis impresso para cada grupo

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 35 — 28/10/2026 · Tendências em Redes — IoT e Redes do Futuro |
| Próxima aula → | Aula 37 — 11/11/2026 · Apresentação do Projeto + Revisão Geral |

---

## Observações do Professor
