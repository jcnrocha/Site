# UC: Fundamentos de Redes de Computadores
## Aula 41 — 3º Trimestre

---

## Tema

Correção Comentada das Provas do 3º Trimestre

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender os erros cometidos na avaliação trimestral — identificando onde e por que errou
- Consolidar os conceitos do 3º trimestre a partir da correção detalhada de cada questão
- Reconhecer os pontos de maior dificuldade coletiva e retomar os conteúdos com base no feedback do professor
- Conectar o aprendizado do 3º trimestre com a visão integrada de toda a UC
- Desenvolver a capacidade de autoavaliação — reconhecendo a própria evolução ao longo do ano letivo

**Habilidade da matriz:** H3 · H4 · H5 — consolidação e fechamento das habilidades do 3º trimestre

---

## Conteúdo

- Esta aula é de correção comentada — não há conteúdo novo
- O foco é o feedback detalhado sobre a prova, a retomada dos conceitos que geraram mais erros e a conexão com o encerramento da UC
- **Estrutura da correção:**
  - Correção coletiva de todas as 10 questões da prova trimestral (Aula 39)
  - Para cada questão: o professor apresenta a resposta correta, explica o raciocínio e comenta os erros mais comuns cometidos pela turma
  - Espaço aberto para perguntas após cada bloco de questões

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Devolução das provas corrigidas · Apresentação da estrutura da aula · Professor registra no quadro os temas com maior índice de erro da turma |
| Correção — Objetivas | Professor corrige as 5 questões objetivas uma a uma · explica o raciocínio correto · comenta por que cada distrator (alternativa errada) é incorreto · abre para perguntas após cada questão |
| Correção — Discursivas | Professor corrige as 5 questões discursivas uma a uma · lê exemplos de respostas boas e de respostas incompletas (sem identificar os alunos) · reforça os critérios de correção · abre para perguntas |
| Retomada dirigida | Professor retoma com mais profundidade os 2 ou 3 conteúdos com maior índice de erro · usa slides ou quadro branco |
| Conexão com o encerramento | Professor apresenta a visão integrada da UC: *"Vocês começaram entendendo o que é um bit — e terminaram projetando uma rede corporativa completa. Isso é a jornada da UC."* |
| Fechamento | Espaço aberto para dúvidas finais · orientações sobre a Aula 42 (Encerramento) · reconhecimento da turma pelo esforço ao longo do ano |

---

## Roteiro de Correção — Questões Objetivas da Prova (Aula 39)

> O professor usa este roteiro como guia durante a correção coletiva. Para cada questão: anuncia o gabarito, explica o raciocínio correto e comenta os distradores.

---

**Questão 1 — Gabarito: C (Topologia Estrela · Classificação LAN)**

*Raciocínio:* todos os dispositivos conectados a switches centrais por cabos individuais = topologia Estrela · ambiente interno de um único prédio = LAN · WAN e MAN são para longas distâncias entre cidades ou países · Malha exigiria múltiplas conexões redundantes entre cada switch

*Erros comuns:* confundir Estrela com Malha por ter múltiplos switches · classificar como WAN por ter 3 andares · não lembrar que LAN pode abranger um prédio inteiro

---

**Questão 2 — Gabarito: B (SSID Guest em VLAN separada)**

*Raciocínio:* SSID Guest em VLAN isolada impede acesso dos visitantes à rede interna · apenas senha WPA3 diferente não segmenta o tráfego — o visitante ainda estaria na mesma rede · segundo roteador sem segurança cria uma vulnerabilidade · desativar o SSID corporativo prejudica os funcionários

*Erros comuns:* acreditar que uma senha diferente no Wi-Fi já isola o tráfego · não entender a diferença entre autenticação (senha) e segmentação (VLAN)

---

**Questão 3 — Gabarito: C (PaaS)**

*Raciocínio:* PaaS = plataforma pronta para deploy · desenvolvedor só sobe o código sem configurar SO, runtime ou servidor · IaaS exige configurar tudo a partir da máquina virtual · SaaS é software pronto para uso final (não para hospedar aplicações próprias) · on-premises requer hardware próprio

*Erros comuns:* confundir IaaS com PaaS · não entender que SaaS é para uso de software, não para hospedagem de sistemas próprios

---

**Questão 4 — Gabarito: D (Camada 7 — Aplicação · usar nslookup)**

*Raciocínio:* ping no IP funciona = Camadas 1 a 3 OK · falha ao usar o nome = DNS não resolve o nome = problema na Camada 7 (Aplicação) · ferramenta correta: nslookup verifica se o servidor DNS interno está resolvendo o nome · ipconfig verifica configuração IP · netstat verifica portas abertas

*Erros comuns:* apontar Camada 3 por envolver endereçamento IP · não reconhecer que resolução de nomes é função da Camada 7

---

**Questão 5 — Gabarito: C (MQTT)**

*Raciocínio:* MQTT é o protocolo padrão para IoT industrial — leve, publish-subscribe, baixo consumo · 800 sensores com bateria enviando dados a cada 5 segundos exigem protocolo eficiente e de baixo overhead · HTTP tem overhead alto demais para dispositivos com bateria · FTP é para transferência de arquivos · DNS é para resolução de nomes

*Erros comuns:* escolher HTTP por ser "padrão da internet" · não conhecer os protocolos específicos de IoT

---

## Roteiro de Correção — Questões Discursivas da Prova (Aula 39)

> Para cada discursiva: o professor lê a questão, apresenta os critérios de correção, mostra exemplo de resposta completa e comenta os erros mais frequentes.

---

**Questão 6 — Estrela × Malha**

*Pontos obrigatórios na resposta:*
- Estrela: ponto de falha no switch central · custo médio · alta escalabilidade · desempenho alto com switch · uso: LANs corporativas, escritórios
- Malha: sem ponto único de falha (full) ou reduzido (partial) · custo alto · escalabilidade baixa em LANs · uso: backbones WAN, data centers, infraestrutura crítica

*Erros comuns:* descrever Estrela como tendo múltiplos pontos de falha · confundir custo de Malha (alto) com custo de Estrela · não indicar os cenários de uso adequados para cada topologia

---

**Questão 7 — Cliente-Servidor na Prática**

*Pontos obrigatórios na resposta:*
- Cliente: inicia a comunicação, solicita recursos, pode ser qualquer dispositivo com acesso à rede
- Servidor: processa requisições, armazena dados, retorna respostas, disponível continuamente
- Comunicação: cliente requisita → servidor processa e verifica permissões → servidor responde
- Exemplos para desenvolvedor: API REST, deploy em servidor de produção, banco de dados via driver de conexão

*Erros comuns:* descrever o servidor como passivo · não citar exemplos do contexto de desenvolvimento de sistemas · confundir o modelo com P2P por mencionarem comunicação bidirecional

---

**Questão 8 — VLANs e DMZ**

*Pontos obrigatórios na resposta:*
- VLAN: segmentação lógica por departamento ou função · segurança, desempenho e organização · dispositivos em VLANs diferentes precisam de roteamento
- DMZ: segmento entre internet e rede interna · dois firewalls · servidores web, e-mail, FTP públicos · protege a rede interna mesmo se o servidor da DMZ for comprometido
- Relação: VLANs segmentam internamente · DMZ protege a fronteira com a internet · juntas formam defesa em profundidade

*Erros comuns:* descrever a DMZ como "rede pública sem proteção" · não mencionar os dois firewalls · não explicar o benefício da relação entre VLANs e DMZ

---

**Questão 9 — IP 169.254.x.x**

*Pontos obrigatórios na resposta:*
- IP 169.254.x.x = APIPA — DHCP não respondeu, sistema atribuiu IP de link-local automaticamente
- Passo 1: `ipconfig /all` — confirmar APIPA e verificar adaptador de rede ativo
- Passo 2: `ipconfig /release` e `/renew` — tentar renovar o IP via DHCP
- Passo 3: verificar cabo e LED do switch — conectividade física
- Passo 4: verificar servidor DHCP — serviço ativo, pool de endereços disponível, VLAN correta

*Erros comuns:* não identificar o APIPA como ausência de resposta do DHCP · não mencionar a ordem correta dos passos · pular direto para o servidor DHCP sem verificar o cabo primeiro

---

**Questão 10 — Visão Integrada da UC**

*Pontos a avaliar na resposta:*
- Identificação clara das 5 habilidades (H1 a H5) com descrição do que cada uma representa
- Conexão lógica e progressiva entre as habilidades — como cada uma constrói sobre a anterior
- Exemplos concretos e específicos do projeto do próprio grupo — não genéricos
- Reflexão sobre a jornada: como a UC foi construída de forma integrada e coerente

*Erros comuns:* listar as habilidades sem conectá-las · usar exemplos genéricos sem mencionar o projeto do grupo · não demonstrar compreensão da progressão H1→H2→H3→H4→H5

---

## Retomada Dirigida — Conteúdos para Aprofundamento

> O professor escolhe os 2 ou 3 temas com maior índice de erro na turma e dedica 5 minutos extras a cada um com slides ou quadro branco.

**Sugestões de retomada (adaptar conforme desempenho real da turma):**

- **SSID + VLAN:** reforçar que senha diferente ≠ isolamento de rede · VLAN é a única forma de segmentar logicamente o tráfego
- **IaaS × PaaS × SaaS:** retomar as analogias (terreno/apartamento/hotel) e listar exemplos reais de cada modelo
- **Diagnóstico com nslookup:** demonstrar ao vivo no terminal — executar `nslookup` e mostrar o resultado para a turma
- **APIPA e DHCP:** desenhar no quadro o processo DORA e mostrar o que acontece quando o servidor não responde
- **Topologia Malha × Estrela:** desenhar os dois diagramas lado a lado no quadro com os pontos de falha marcados

---

## Conexão com o Encerramento da UC

> Professor usa este momento para fazer uma síntese motivacional da jornada da turma ao longo do ano.

**A jornada da UC em uma frase por trimestre:**

- **1º Trimestre:** *"Vocês aprenderam a linguagem das redes — o que é um bit, como nomear um componente e qual cabo usar."*
- **2º Trimestre:** *"Vocês entenderam como as redes funcionam por dentro — protocolos, endereçamento IP, segurança e o modelo OSI."*
- **3º Trimestre:** *"Vocês projetaram uma rede do zero — escolhendo topologia, segmentando com VLANs, dimensionando a infraestrutura e pensando no futuro com IoT e nuvem."*

**O que fica depois desta UC:**
- A capacidade de entender e diagnosticar uma rede quando ela falha
- A base técnica para as próximas UCs do curso que dependem de redes (sistemas distribuídos, desenvolvimento web, segurança da informação)
- O raciocínio de projeto: *"qual problema preciso resolver? Qual tecnologia resolve isso de forma eficiente e segura?"*

---

## Avaliação

- Esta aula não tem questionário individual
- A avaliação é formativa — o professor observa a participação, as dúvidas levantadas e o engajamento na correção
- O professor pode solicitar que os alunos registrem por escrito: *"O que aprendi com a correção desta prova que levarei para as próximas UCs?"* — exercício de autoavaliação final (opcional)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 40 — 02/12/2026 · Prova de Recuperação — 3º Trimestre |
| Próxima aula → | Aula 42 — 16/12/2026 · Encerramento da UC |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Slides com as questões da prova e gabarito comentado
- Quadro branco e marcador para retomada dirigida e diagramas
- Provas corrigidas para devolução aos alunos
- Terminal aberto para demonstrações ao vivo (nslookup, ipconfig) se necessário

---

## Observações do Professor
