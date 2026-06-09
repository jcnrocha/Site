# UC: Fundamentos de Redes de Computadores
## Aula 26 — 2º Trimestre

---

## Tema

Correção Comentada das Provas do 2º Trimestre

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender os erros cometidos na avaliação trimestral — identificando onde e por que errou
- Consolidar os conceitos do 2º trimestre a partir da correção detalhada de cada questão
- Reconhecer os pontos de maior dificuldade da turma e retomar os conteúdos com base no feedback coletivo
- Conectar o aprendizado do 2º trimestre com os conteúdos que serão trabalhados no 3º trimestre
- Desenvolver a capacidade de autoavaliação — identificando o próprio nível de domínio de cada habilidade

**Habilidade da matriz:** H3 · H4 — consolidação e fechamento das habilidades do 2º trimestre

---

## Conteúdo

- Esta aula é de correção comentada — não há conteúdo novo
- O foco é o feedback detalhado sobre a prova, a retomada dos conceitos que geraram mais erros e a conexão com o 3º trimestre
- **Estrutura da correção:**
  - Correção coletiva de todas as 10 questões da prova trimestral (Aula 24)
  - Para cada questão: o professor apresenta a resposta correta, explica o raciocínio e comenta os erros mais comuns cometidos pela turma
  - Espaço aberto para perguntas após cada bloco de questões

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Devolução das provas corrigidas · Apresentação da estrutura da aula · Professor registra no quadro os temas com maior índice de erro da turma |
| Correção — Objetivas | Professor corrige as 5 questões objetivas uma a uma · explica o raciocínio correto · comenta por que cada distrator (alternativa errada) é incorreto · abre para perguntas após cada questão |
| Correção — Discursivas | Professor corrige as 5 questões discursivas uma a uma · lê exemplos de respostas boas e de respostas incompletas (sem identificar os alunos) · reforça os critérios de correção · abre para perguntas |
| Retomada dirigida | Professor retoma com mais profundidade os 2 ou 3 conteúdos com maior índice de erro — usando slides ou quadro branco |
| Conexão com o 3º Trimestre | Professor apresenta o que vem a seguir: classificação de redes, topologias, modelos, IoT e Projeto Integrador · mostra como o que foi aprendido no 2º trimestre serve de base para o 3º |
| Fechamento | Espaço aberto para dúvidas finais · orientações sobre a Aula 27 (Ponte — início do 3º Trimestre) |

---

## Roteiro de Correção — Questões Objetivas da Prova (Aula 24)

> O professor usa este roteiro como guia durante a correção coletiva. Para cada questão: anuncia o gabarito, explica o raciocínio correto e comenta os distradores.

---

**Questão 1 — Gabarito: C (Fibra óptica monomodo)**

*Raciocínio:* distância de 1.200 metros está além do alcance do par trançado (máximo ~100 m para Cat6A) e do coaxial para LAN · fibra monomodo suporta dezenas de quilômetros com altíssima velocidade e imunidade total a interferências

*Erros comuns:* confundir Cat6A com fibra · não lembrar do limite de distância do par trançado

---

**Questão 2 — Gabarito: B (172.20.5.100)**

*Raciocínio:* faixas privadas RFC 1918 — Classe A: 10.x.x.x · Classe B: 172.16.x.x a 172.31.x.x · Classe C: 192.168.x.x · os demais endereços da questão são públicos e roteáveis na internet

*Erros comuns:* não memorizar as três faixas privadas · confundir 172.20.x.x como público

---

**Questão 3 — Gabarito: C (UDP — baixa latência)**

*Raciocínio:* streaming ao vivo prioriza velocidade e continuidade · um pacote perdido causa apenas uma falha visual/sonora mínima · o atraso do TCP para reenviar um pacote causaria travamento perceptível — inaceitável em tempo real

*Erros comuns:* associar streaming sempre ao TCP por ser "mais confiável" · não entender que em tempo real a perda é preferível ao atraso

---

**Questão 4 — Gabarito: D (Camada 1 — Física)**

*Raciocínio:* LED apagado + cabo desconectado = ausência de sinal físico = problema na Camada 1 · não há nem transmissão de bits, portanto as camadas superiores não chegam a ser ativadas

*Erros comuns:* confundir com Camada 2 (que trata do MAC, não do cabo em si) · não lembrar que a Camada 1 é o ponto de partida do diagnóstico OSI

---

**Questão 5 — Gabarito: D (DDoS)**

*Raciocínio:* múltiplas origens + volume massivo de requisições + objetivo de derrubar o serviço = DDoS (Distributed Denial of Service) · phishing rouba credenciais · ransomware criptografa arquivos · Man-in-the-Middle intercepta comunicação

*Erros comuns:* confundir DDoS com DoS (ataque de origem única) · não diferenciar DDoS de outros tipos de ataque

---

## Roteiro de Correção — Questões Discursivas da Prova (Aula 24)

> Para cada discursiva: o professor lê a questão, apresenta os critérios de correção, mostra um exemplo de resposta completa e comenta os erros mais frequentes.

---

**Questão 6 — Wi-Fi: Frequências e Padrões**

*Pontos obrigatórios na resposta:*
- Diferença de alcance: 2,4 GHz penetra melhor obstáculos · 5 GHz tem maior velocidade mas menor alcance
- Interferência: 2,4 GHz mais suscetível (micro-ondas, outros roteadores) · 5 GHz menos congestionada
- Padrões corretos: 2,4 GHz → 802.11b/g/n · 5 GHz → 802.11a/ac/ax
- Indicação de uso: 2,4 GHz para ambientes grandes e IoT · 5 GHz para streaming e gaming

*Erros comuns:* inverter as características das frequências · não citar padrões IEEE · resposta genérica sem critério técnico

---

**Questão 7 — FTTH vs. ADSL**

*Pontos obrigatórios na resposta:*
- ADSL: par de cobre, assimétrico, até ~8 Mbps, velocidade cai com distância da central
- FTTH: fibra óptica, simétrico, 100 Mbps a 1 Gbps+, baixa latência, conexão dedicada
- Justificativa corporativa: FTTH suporta múltiplos usuários, aplicações críticas e videoconferências sem degradação

*Erros comuns:* não mencionar a assimetria do ADSL · confundir FTTH com FTTB · não justificar a escolha para uso corporativo

---

**Questão 8 — Processo DORA**

*Pontos obrigatórios na resposta:*
- **D**iscover: cliente busca servidor DHCP por broadcast
- **O**ffer: servidor oferece configuração disponível
- **R**equest: cliente solicita formalmente a oferta
- **A**cknowledge: servidor confirma e registra o lease

*Erros comuns:* inverter a ordem das etapas · não descrever o papel do cliente e do servidor · confundir DORA com o three-way handshake do TCP

---

**Questão 9 — VPN**

*Pontos obrigatórios na resposta:*
- Conceito: túnel criptografado pela internet pública
- Funcionamento: encapsulamento e criptografia dos dados antes do envio
- Cenários: home office, Wi-Fi público, interligação de filiais
- Justificativa home office: sem VPN os dados trafegam sem proteção · com VPN é equivalente a estar na rede da empresa

*Erros comuns:* confundir VPN com proxy · não explicar o mecanismo de criptografia · cenários muito vagos sem justificativa técnica

---

**Questão 10 — OSI como Diagnóstico**

*Pontos obrigatórios na resposta:*
- Ping funciona → Camadas 1, 2 e 3 estão ok
- Navegador não abre → problema na Camada 7 (Aplicação) ou possivelmente DNS (ainda Camada 7)
- Descarte das camadas inferiores justificado pelo ping
- Ação sugerida: testar DNS com nslookup · tentar IP direto no navegador

*Erros comuns:* apontar Camada 4 sem justificar · não usar o resultado do ping como evidência · não descartar as camadas inferiores com argumento técnico

---

## Retomada Dirigida — Conteúdos para Aprofundamento

> O professor escolhe os 2 ou 3 temas com maior índice de erro na turma e dedica 5 minutos extras a cada um com slides ou quadro branco.

**Sugestões de retomada (adaptar conforme desempenho real da turma):**

- **Faixas de IP privado (RFC 1918):** reescrever as três faixas no quadro e fixar com exemplos do cotidiano
- **TCP × UDP na prática:** retomar a lógica — "tempo real = UDP · integridade crítica = TCP"
- **Camadas OSI e diagnóstico:** percorrer as 7 camadas com o macete e um caso prático de diagnóstico
- **Processo DORA:** desenhar o fluxo cliente ↔ servidor no quadro passo a passo

---

## Conexão com o 3º Trimestre

> Professor apresenta brevemente o que vem a seguir — criando expectativa e mostrando como o 2º trimestre é base para o 3º.

- **O que vimos no 2º trimestre:** como os dados são transmitidos (meios), como os dispositivos se conectam (tecnologias), como são identificados (IP) e como se comunicam (protocolos e OSI)
- **O que veremos no 3º trimestre:** como as redes são classificadas e organizadas — topologias, modelos cliente-servidor e P2P, redes sem fio avançadas, redes corporativas, computação em nuvem, IoT e Projeto Integrador
- **A conexão:** sem entender protocolos e endereçamento (2º tri), não é possível projetar uma rede corporativa ou entender como os dispositivos IoT se comunicam (3º tri)

---

## Avaliação

- Esta aula não tem questionário individual
- A avaliação é formativa — o professor observa a participação, as dúvidas levantadas e o engajamento na correção
- O professor pode solicitar que os alunos registrem por escrito: *"O que eu errei e o que aprendi com a correção"* — exercício de autoavaliação (opcional)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 25 — 19/08/2026 · Prova de Recuperação — 2º Trimestre |
| Próxima aula → | Aula 27 — 02/09/2026 · Ponte — Conexão com o 3º Trimestre |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Slides com as questões da prova e gabarito comentado
- Quadro branco e marcador para retomada dirigida
- Provas corrigidas para devolução aos alunos

---

## Observações do Professor
