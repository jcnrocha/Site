# UC: Fundamentos de Redes de Computadores
## Aula 04 — 1º Trimestre

---

## Tema

Tipos de Armazenamento em Redes

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é armazenamento em rede e por que ele é fundamental para o compartilhamento de dados em ambientes corporativos
- Identificar e diferenciar os principais tipos de armazenamento em rede: DAS, NAS e SAN
- Reconhecer o armazenamento em nuvem como uma evolução do armazenamento em rede — entendendo suas características, vantagens e limitações
- Relacionar cada tipo de armazenamento com o perfil de uso mais adequado: doméstico, corporativo de pequeno porte ou corporativo de grande porte
- Conectar os conceitos de armazenamento com as unidades de medida vistas nas Aulas 02 e 03

**Habilidade da matriz:** H1 — Reconhecer unidades de medida empregadas na transmissão e armazenamento de dados

---

## Conteúdo

- Retomada rápida das Aulas 02 e 03: *"Vimos as unidades de armazenamento (KB, MB, GB, TB) e as de velocidade (Mbps, Gbps). Hoje vamos entender onde e como os dados são armazenados em uma rede — e como as unidades que aprendemos se aplicam aqui"*
- **Por que o armazenamento em rede existe?**
  - Em um ambiente com múltiplos usuários, cada um com seu próprio HD local, surgem problemas:
    - Dados duplicados em vários computadores — desperdício de espaço
    - Dificuldade de compartilhar e colaborar em arquivos
    - Backup descentralizado — cada máquina precisa ser salva separadamente
    - Sem controle de versão e de acesso centralizado
  - O armazenamento em rede resolve esses problemas centralizando os dados em um único ponto acessível por todos os dispositivos da rede

- **DAS — Direct Attached Storage (Armazenamento Direto)**
  - **O que é:** dispositivo de armazenamento conectado diretamente a um único computador ou servidor — sem passar pela rede
  - **Como funciona:** HD externo, SSD externo, pen drive ou HD interno — conectado via USB, SATA, SAS ou NVMe
  - **Características:**
    - Alta velocidade de acesso — sem overhead de rede
    - Uso exclusivo do dispositivo ao qual está conectado
    - Não compartilhável diretamente com outros dispositivos na rede
    - Simples de instalar e de usar
  - **Vantagens:** baixo custo · alta velocidade · sem dependência de rede · fácil configuração
  - **Desvantagens:** não compartilhado nativamente · sem redundância nativa · escalabilidade limitada
  - **Exemplos práticos:** HD externo USB na mesa do usuário · HD interno de um computador · SSD externo para backup local
  - **Uso típico:** uso pessoal, backup local de um único computador, estações de trabalho individuais

- **NAS — Network Attached Storage (Armazenamento Conectado à Rede)**
  - **O que é:** dispositivo de armazenamento conectado à rede local (LAN) — acessível por múltiplos usuários e dispositivos simultaneamente
  - **Como funciona:** o NAS é um servidor de arquivos dedicado com sistema operacional próprio · os dispositivos da rede acessam os arquivos via protocolos de compartilhamento (SMB/CIFS para Windows, NFS para Linux, AFP para Mac)
  - **Características:**
    - Acesso simultâneo por múltiplos usuários da rede
    - Interface web de gerenciamento — sem necessidade de monitor dedicado
    - Suporte a RAID para redundância de dados
    - Pode ter 2 a dezenas de baias (slots) para HDs
  - **RAID (Redundant Array of Independent Disks):**
    - Tecnologia que combina múltiplos HDs para redundância ou desempenho
    - RAID 1: espelhamento — dados copiados em 2 HDs · se um falhar, o outro continua
    - RAID 5: distribuição com paridade — mínimo 3 HDs · tolera falha de 1 HD sem perda de dados
    - RAID 6: como o RAID 5 mas tolera falha de 2 HDs simultaneamente
  - **Vantagens:** compartilhamento centralizado · acesso simultâneo · gerenciamento simples · redundância com RAID · backup centralizado
  - **Desvantagens:** velocidade limitada pela rede (Ethernet) · custo maior que DAS · ponto único de falha se não houver redundância de hardware
  - **Exemplos práticos:** Synology DS223, QNAP TS-233, WD My Cloud EX2 Ultra
  - **Uso típico:** pequenas e médias empresas, escritórios, home office, estúdios de criação, pequenos servidores de arquivos

- **SAN — Storage Area Network (Rede de Área de Armazenamento)**
  - **O que é:** rede dedicada exclusivamente para armazenamento — separada da rede de dados convencional (LAN) · os dispositivos de armazenamento aparecem para os servidores como se fossem HDs locais
  - **Como funciona:** servidores se conectam ao storage via rede dedicada de alta velocidade (Fibre Channel ou iSCSI) · o sistema operacional do servidor enxerga o volume SAN como um disco local — não como uma pasta de rede
  - **Características:**
    - Altíssima velocidade — Fibre Channel: 8, 16 ou 32 Gbps · iSCSI: 10 Gbps ou mais
    - Baixíssima latência — essencial para bancos de dados e virtualização
    - Altamente escalável — petabytes de armazenamento
    - Gerenciamento centralizado e complexo
    - Infraestrutura dedicada — switches Fibre Channel, HBAs (Host Bus Adapters)
  - **Vantagens:** altíssimo desempenho · escalabilidade massiva · ideal para cargas críticas · redundância total
  - **Desvantagens:** custo muito elevado · complexidade de implementação e gerenciamento · requer equipe especializada
  - **Exemplos práticos:** EMC VNX, NetApp FAS, IBM FlashSystem, HPE Primera
  - **Uso típico:** grandes empresas, data centers, bancos, hospitais, sistemas críticos que exigem alta disponibilidade e desempenho

- **Comparativo DAS × NAS × SAN:**

| Critério | DAS | NAS | SAN |
|----------|-----|-----|-----|
| Conexão | Direto ao dispositivo | Rede LAN (Ethernet) | Rede dedicada (FC/iSCSI) |
| Compartilhamento | Não (apenas 1 dispositivo) | Sim (múltiplos usuários) | Sim (múltiplos servidores) |
| Velocidade | Alta (sem rede) | Média (limitada pela LAN) | Muito alta (FC/iSCSI) |
| Latência | Muito baixa | Média | Muito baixa |
| Custo | Baixo | Médio | Alto |
| Complexidade | Baixa | Média | Alta |
| Escalabilidade | Baixa | Média | Muito alta |
| Uso típico | Pessoal / estação individual | PME e escritórios | Data centers e grandes empresas |

- **Armazenamento em Nuvem**
  - **O que é:** armazenamento de dados em servidores remotos acessados pela internet — sem necessidade de hardware local dedicado
  - **Como funciona:** dados são enviados pela internet para data centers do provedor · acessíveis de qualquer dispositivo com conexão
  - **Modelos de serviço:**
    - **Pessoal/consumidor:** Google Drive, OneDrive, iCloud, Dropbox — para usuários individuais
    - **Empresarial:** Amazon S3, Azure Blob Storage, Google Cloud Storage — para aplicações e sistemas
    - **Backup em nuvem:** Backblaze, Veeam Cloud, AWS Backup — para cópias de segurança automatizadas
  - **Vantagens:** acesso de qualquer lugar · sem hardware local · escalabilidade instantânea · alta disponibilidade · backup automático
  - **Desvantagens:** dependência de internet · latência maior que armazenamento local · custo recorrente (mensalidade) · questões de privacidade e conformidade (LGPD)
  - **Comparativo com armazenamento local:**
    - Velocidade de acesso: local (DAS/NAS/SAN) >> nuvem (limitada pela banda de internet)
    - Disponibilidade fora da rede: local precisa de VPN ou acesso remoto · nuvem é nativa
    - Custo inicial: nuvem não exige hardware · local exige investimento inicial

- **Unidades de medida aplicadas ao armazenamento:**
  - Capacidade de armazenamento: medida em GB, TB e PB (visto na Aula 02)
  - Velocidade de transferência para/do armazenamento: medida em MB/s ou Gbps (visto na Aula 03)
  - Exemplo de aplicação: *"Um NAS com interface de 1 Gbps Ethernet tem velocidade máxima de ~125 MB/s · Uma SAN com link de 16 Gbps Fibre Channel tem velocidade de ~2 GB/s"*

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada das Aulas 02 e 03: *"Sabemos medir o tamanho dos dados e a velocidade com que viajam — hoje entendemos onde eles ficam guardados em uma rede"* |
| Retomada | Professor pergunta: *"Se você trabalha em uma empresa com 20 pessoas e todos precisam acessar os mesmos arquivos de clientes, como você guardaria esses arquivos? Em cada computador? Em um HD externo? Como todos acessariam ao mesmo tempo?"* — alunos respondem livremente |
| Explicação | Slides — por que armazenamento em rede, DAS, NAS (com RAID), SAN, armazenamento em nuvem, comparativo geral, unidades de medida aplicadas |
| Dinâmica | "Qual Tipo de Armazenamento Usar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: DAS = direto e exclusivo · NAS = rede e compartilhado · SAN = alta performance dedicada · Nuvem = acesso remoto e escalável · Próxima aula: Simbologias Básicas de Rede — Parte 1 |

---

## Dinâmica — "Qual Tipo de Armazenamento Usar?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver o raciocínio de escolha do tipo de armazenamento mais adequado para cada cenário, conectando as características técnicas de DAS, NAS, SAN e nuvem com decisões reais que um técnico de redes ou desenvolvedor de sistemas precisa tomar no mercado de trabalho.

**Materiais:** cartões com cenários — um conjunto por grupo · ou slide com os cenários projetados.

**Passo a passo:**

1. **Distribuição dos cartões** *(1 min)*
Cada grupo recebe 4 cartões com cenários de necessidade de armazenamento. O desafio é indicar qual tipo de armazenamento é mais adequado e justificar a escolha com base nas características técnicas.

2. **Análise em grupo** *(8 min)*
O grupo discute cada cenário e decide: qual tipo de armazenamento usar, por quê, e quais características técnicas sustentam a decisão.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta uma situação. O professor complementa, corrige e reforça os critérios técnicos de escolha.

**Cenários sugeridos:**

| Cenário | Armazenamento indicado | Justificativa |
|---------|----------------------|---------------|
| Designer gráfico que precisa de armazenamento rápido e exclusivo para seus projetos no computador pessoal | DAS (SSD externo ou HD interno) | Acesso exclusivo e de alta velocidade sem necessidade de compartilhamento |
| Escritório com 15 funcionários que precisam acessar e editar os mesmos documentos simultaneamente | NAS | Compartilhamento centralizado via LAN · múltiplos usuários simultâneos · custo acessível |
| Banco com sistema de transações que exige latência abaixo de 1 ms e alta disponibilidade 24/7 | SAN | Alta performance · baixíssima latência · redundância total · escalabilidade para grandes volumes |
| Freelancer que quer acessar seus arquivos de qualquer lugar do mundo pelo celular ou notebook | Nuvem (Google Drive, OneDrive) | Acesso remoto de qualquer dispositivo · sem hardware local · escalabilidade imediata |
| Empresa que precisa fazer backup automático e diário de 2 TB de dados sem manter hardware local | Nuvem (AWS S3, Backblaze) | Backup automatizado · sem hardware de backup local · escalabilidade e redundância do provedor |
| Data center com 500 servidores de virtualização que precisam de armazenamento centralizado e de altíssima velocidade | SAN (Fibre Channel) | Volume massivo · latência mínima · suporte a virtualização com múltiplos servidores acessando simultaneamente |
| Pequena empresa de contabilidade com 5 funcionários que quer centralizar arquivos sem gastar muito | NAS de entrada (2 baias) | Custo baixo · compartilhamento suficiente para 5 usuários · RAID 1 para redundância básica |
| Desenvolvedor que quer armazenar imagens Docker e artefatos de build para sua pipeline de CI/CD | Nuvem (AWS S3, Azure Blob) | Integração nativa com ferramentas DevOps · acesso por API · escalabilidade automática |

> **Nota:** o objetivo é desenvolver o raciocínio: *"quantos usuários precisam acessar? Qual a velocidade necessária? Há orçamento para hardware dedicado? Os dados precisam ser acessados remotamente?"* Reforçar que a escolha errada de armazenamento gera gargalos de performance, custos desnecessários ou indisponibilidade de dados.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 03 — 04/03/2026 · Unidades de Medida — Velocidade de Transmissão |
| Próxima aula → | Aula 05 — 18/03/2026 · Simbologias Básicas de Rede — Parte 1 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides — incluindo diagrama visual comparativo DAS × NAS × SAN
- Questionário impresso ou digital
- Cartões com os cenários da dinâmica impressos (1 conjunto por grupo) ou slide com os cenários
- Se possível: mostrar ao vivo a interface web de um NAS (ex.: demo online do Synology DiskStation Manager em demo.synology.com) — torna o conteúdo tangível e motivador

---

## Observações do Professor
