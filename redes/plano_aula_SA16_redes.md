# UC: Fundamentos de Redes de Computadores
## Aula 16 — 2º Trimestre

---

## Tema

Tecnologias de Conexão à Internet — Parte 1

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender como as tecnologias de conexão à internet evoluíram desde as linhas telefônicas até a fibra óptica
- Identificar as principais tecnologias de conexão cabeada: ADSL, VDSL, TV a cabo e fibra óptica (FTTH/FTTB)
- Diferenciar as tecnologias de acesso quanto à velocidade, custo, disponibilidade e infraestrutura necessária
- Reconhecer os conceitos de download e upload — e por que as velocidades são assimétricas na maioria dos planos residenciais
- Relacionar cada tecnologia de conexão com o perfil de uso mais adequado: residencial, corporativo ou rural

**Habilidade da matriz:** H4 — Identificar tipos e tecnologias de conexão a redes de computadores

---

## Conteúdo

- Contexto: como a internet chega até nós — da operadora ao dispositivo do usuário
- O que é um provedor de acesso à internet (ISP — Internet Service Provider)
- Conceitos fundamentais:
  - **Download** — recebimento de dados da internet para o dispositivo do usuário
  - **Upload** — envio de dados do dispositivo para a internet
  - **Assimetria** — por que a maioria dos planos residenciais tem download maior que upload
  - **Latência** — tempo que um pacote leva para ir e voltar · medida em milissegundos (ms)
- **ADSL (Asymmetric Digital Subscriber Line)**
  - Transmissão de dados pela linha telefônica de cobre já existente
  - Velocidades típicas: download até 8 Mbps · upload até 1 Mbps
  - Assimétrico por natureza — daí o "A" no nome
  - Limitação: quanto mais longe da central telefônica, menor a velocidade
  - Hoje em declínio — substituído por tecnologias mais rápidas
- **VDSL (Very High Speed DSL)**
  - Evolução do ADSL — também usa par de cobre, mas com maior frequência
  - Velocidades típicas: download até 100 Mbps · upload até 50 Mbps
  - Distância ainda é limitante — funciona melhor em curtas distâncias da central
  - Usado como solução intermediária enquanto a fibra não chega ao domicílio
- **Internet via TV a Cabo (HFC — Hybrid Fiber-Coaxial)**
  - Infraestrutura híbrida: fibra óptica até os nós da operadora + cabo coaxial até o domicílio
  - Padrão DOCSIS (Data Over Cable Service Interface Specification) — versões 3.0 e 3.1
  - Velocidades: DOCSIS 3.0 até 1 Gbps · DOCSIS 3.1 até 10 Gbps (teórico)
  - Compartilhamento de banda entre vizinhos no mesmo segmento de cabo — velocidade pode cair nos horários de pico
- **Fibra Óptica até o Domicílio**
  - **FTTH (Fiber to the Home)** — fibra chega até dentro da residência · maior velocidade e confiabilidade
  - **FTTB (Fiber to the Building)** — fibra chega até o prédio · distribuição interna por cabo de cobre ou coaxial
  - **FTTC (Fiber to the Curb)** — fibra chega até o armário na rua · últimos metros por cobre
  - Velocidades: simétricas de 100 Mbps, 300 Mbps, 500 Mbps, 1 Gbps e além
  - Vantagens: altíssima velocidade, baixa latência, imunidade a interferências, conexão dedicada
  - Tecnologia padrão atual para novos projetos residenciais e corporativos no Brasil
- Comparativo geral entre as tecnologias de conexão cabeada:

| Tecnologia | Meio físico | Velocidade típica | Latência | Disponibilidade |
|------------|-------------|-------------------|----------|-----------------|
| ADSL | Par de cobre | Até 8 Mbps | Alta (~50 ms) | Ampla (linha telefônica) |
| VDSL | Par de cobre | Até 100 Mbps | Média (~20 ms) | Média |
| TV a Cabo (HFC) | Fibra + Coaxial | Até 1 Gbps | Baixa (~10 ms) | Média-alta |
| FTTH | Fibra óptica | 100 Mbps a 1 Gbps+ | Muito baixa (~5 ms) | Crescente no Brasil |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Retomada rápida da Aula 15: *"Vimos como os dados viajam pelo ar — agora vamos entender como a internet chega fisicamente até a sua casa ou empresa"* |
| Retomada | Professor pergunta: *"Qual é a tecnologia de internet que você usa em casa? Você sabe se é fibra, cabo ou ADSL? Como você descobriria?"* — alunos respondem livremente |
| Explicação | Slides — ISP, download × upload × latência, ADSL, VDSL, TV a cabo (HFC/DOCSIS), fibra óptica (FTTH/FTTB/FTTC), comparativo final |
| Dinâmica | "Qual Tecnologia de Internet Indicar?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: ADSL e VDSL usam o cobre existente · TV a cabo usa infraestrutura HFC · FTTH é o padrão atual com melhor desempenho · Próxima aula: Tecnologias de Conexão à Internet — Parte 2 |

---

## Dinâmica — "Qual Tecnologia de Internet Indicar?"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** desenvolver o raciocínio técnico de escolha da tecnologia de conexão à internet mais adequada para cada perfil de usuário ou organização, conectando as características de cada tecnologia com decisões reais que um técnico de redes ou consultor de TI precisa tomar no mercado de trabalho.

**Materiais:** cartões com perfis de clientes — um conjunto por grupo · ou slide com os perfis projetados.

**Passo a passo:**

1. **Distribuição dos perfis** *(1 min)*
Cada grupo recebe 4 cartões com perfis de clientes ou situações reais. O desafio é indicar qual tecnologia de conexão é a mais adequada e justificar a escolha.

2. **Análise em grupo** *(8 min)*
O grupo discute cada perfil e decide: qual tecnologia indicar, por quê, e quais características técnicas sustentam a decisão.

3. **Compartilhamento** *(6 min)*
Cada grupo apresenta um perfil. O professor complementa, corrige e reforça os critérios técnicos de escolha.

**Perfis sugeridos:**

| Perfil / Situação | Tecnologia indicada | Justificativa |
|-------------------|---------------------|---------------|
| Família em cidade pequena onde só existe linha telefônica disponível | ADSL | Única opção disponível na infraestrutura existente |
| Empresa com 50 funcionários que precisam de conexão estável e simétrica | FTTH (fibra óptica) | Alta velocidade simétrica, baixa latência, conexão dedicada |
| Morador de apartamento em condomínio com infraestrutura de TV a cabo | HFC (DOCSIS 3.1) | Infraestrutura já disponível, boa velocidade para uso residencial |
| Pequena empresa em bairro onde a fibra ainda não chegou, mas há central DSL próxima | VDSL | Melhor que ADSL, disponível na infraestrutura de cobre existente |
| Provedor que vai instalar internet em um novo loteamento | FTTH | Padrão atual para novos projetos, melhor custo-benefício a longo prazo |
| Usuário que faz muitas videoconferências e uploads de arquivos grandes | FTTH (simétrico) | Upload e download iguais, baixa latência — ideal para videoconferência |
| Técnico que precisa comparar a velocidade real com a contratada | Teste de velocidade + análise da tecnologia | Verificar download, upload e latência com ferramentas como Speedtest |
| Condomínio que quer levar internet a todos os apartamentos com um único link | FTTB | Fibra até o prédio, distribuição interna por switch/roteador |

> **Nota:** o objetivo é desenvolver o raciocínio: *"qual é o perfil de uso, a infraestrutura disponível, o orçamento e a localização? A partir daí, qual tecnologia de acesso faz sentido?"* Reforçar que essa decisão aparece em projetos de infraestrutura, visitas técnicas e atendimento a clientes na área de TI.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 15 — 27/05/2026 · Meios de Transmissão Não Guiados |
| Próxima aula → | Aula 17 — 10/06/2026 · Tecnologias de Conexão à Internet — Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com os perfis da dinâmica impressos (1 conjunto por grupo) ou slide com os perfis
- Se possível: demonstração ao vivo de um teste de velocidade (Speedtest) para contextualizar download, upload e latência

---

## Observações do Professor
