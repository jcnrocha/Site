# UC: Programação de Aplicativos
## SA 03 — 1º Trimestre

---

## Tema

Ambiente de Desenvolvimento — IDE

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender o que é uma IDE e por que ela é a principal ferramenta do desenvolvedor no dia a dia profissional
- Identificar os recursos essenciais de uma IDE: editor de código, terminal integrado, depurador e gerenciador de extensões
- Diferenciar as principais IDEs do mercado e reconhecer qual é mais adequada para cada linguagem ou contexto
- Reconhecer como a IDE se integra com repositórios Git e outras ferramentas do ciclo de desenvolvimento
- Navegar pela interface do VS Code identificando suas principais áreas e funcionalidades

**Capacidades da matriz:** 2.1.3 IDE · Instalar ferramentas de acordo com requisitos de hardware, software e parâmetro de configuração · Aplicar linguagem de programação por meio do ambiente integrado de desenvolvimento (IDE)

---

## Conteúdo

- Retomada rápida da SA 02: *"Na SA passada vimos as ferramentas do ciclo de desenvolvimento e como repositórios funcionam — hoje vamos aprofundar na ferramenta onde o código nasce: a IDE"*

- **O que é uma IDE:**
  - Integrated Development Environment — Ambiente Integrado de Desenvolvimento
  - Reúne em um único programa tudo o que o desenvolvedor precisa para escrever, executar e testar código
  - Antes das IDEs: desenvolvedores usavam editor de texto simples + compilador no terminal separado + depurador externo — tudo separado e manual
  - A IDE integra tudo em um só lugar — aumenta produtividade e reduz erros

- **Recursos essenciais de uma IDE:**
  - **Editor de código** — área principal onde o código é escrito · destaque de sintaxe por cores (syntax highlighting) · autocompletar (IntelliSense) · indentação automática
  - **Terminal integrado** — executa comandos diretamente dentro da IDE sem sair do ambiente · compila, roda e testa sem abrir outro programa
  - **Depurador (Debugger)** — permite pausar a execução do programa em qualquer linha · inspecionar o valor das variáveis em tempo real · encontrar erros com precisão
  - **Gerenciador de extensões** — instala plugins que adicionam novas funcionalidades · suporte a novas linguagens, temas, integração com Git, formatadores de código
  - **Integração com Git** — visualiza alterações no código · faz commit, push e pull sem sair da IDE · destaca linhas modificadas, adicionadas ou removidas

- **Principais IDEs do mercado:**

  | IDE | Desenvolvida por | Melhor para | Tipo |
  |-----|-----------------|-------------|------|
  | **VS Code** | Microsoft | Múltiplas linguagens · Web · Python · JavaScript | Gratuito · open source |
  | **IntelliJ IDEA** | JetBrains | Java · Kotlin · Android | Pago (versão Community gratuita) |
  | **Eclipse** | Eclipse Foundation | Java · C/C++ · PHP | Gratuito · open source |
  | **PyCharm** | JetBrains | Python | Pago (versão Community gratuita) |
  | **Android Studio** | Google | Desenvolvimento Android | Gratuito |
  | **Xcode** | Apple | iOS · macOS · Swift | Gratuito (apenas macOS) |

- **VS Code — a IDE que usaremos nesta UC:**
  - IDE mais popular do mundo segundo a pesquisa Stack Overflow Developer Survey
  - Leve, rápido e altamente customizável
  - Suporta praticamente todas as linguagens por meio de extensões
  - Interface principal:
    - **Barra lateral esquerda** — explorador de arquivos, busca, controle de versão (Git), extensões, depurador
    - **Área do editor** — onde o código é escrito · suporta múltiplas abas · divisão de tela
    - **Terminal integrado** — abre com `Ctrl + '` · permite rodar comandos sem sair da IDE
    - **Barra de status (rodapé)** — exibe linguagem do arquivo, branch Git ativa, erros e avisos
    - **Paleta de comandos** — `Ctrl + Shift + P` · acesso rápido a qualquer função da IDE

- **Extensões essenciais para começar:**
  - **GitLens** — visualiza histórico de commits diretamente no código
  - **Prettier** — formata o código automaticamente ao salvar
  - **Error Lens** — destaca erros e avisos inline, na própria linha do código
  - **Live Share** — programação colaborativa em tempo real com outro desenvolvedor
  - Extensão da linguagem escolhida para a UC (Python, Java ou outra conforme definição do professor)

- **IDE × Editor de texto simples — por que a diferença importa:**
  - Notepad, Bloco de Notas: apenas texto · sem destaque de sintaxe · sem autocompletar · sem depurador
  - IDE: ambiente profissional completo · detecta erros antes de executar · aumenta produtividade
  - Analogia: escrever código no Bloco de Notas é como operar uma máquina profissional sem painel de controle — tecnicamente possível, praticamente inviável em projetos reais

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 02: *"Vimos que a IDE é uma das ferramentas do ciclo de desenvolvimento — hoje vamos entrar de cabeça nela"* |
| Retomada | Professor pergunta: *"Alguém já abriu o Bloco de Notas para escrever alguma coisa que precisava de organização? O que faltou nele?"* — alunos respondem livremente · professor usa as respostas para introduzir o que a IDE resolve |
| Explicação | Slides — o que é IDE, recursos essenciais (editor, terminal, depurador, extensões, Git), comparativo das principais IDEs, tour pela interface do VS Code |
| Dinâmica | "Caça ao Recurso" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: IDE reúne tudo em um lugar · VS Code é a mais usada no mercado · terminal integrado + depurador + Git são os recursos que fazem diferença no dia a dia · Próxima SA: instalação e configuração do ambiente |

---

## Dinâmica — "Caça ao Recurso"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar os recursos da IDE por meio da identificação e localização de funcionalidades em capturas de tela ou na própria IDE — desenvolvendo familiaridade com o ambiente que será usado ao longo de toda a UC.

**Materiais:** slide com capturas de tela do VS Code com áreas numeradas e sem legenda · ou acesso ao VS Code instalado nos computadores da sala.

**Passo a passo:**

1. **Apresentação do desafio** *(1 min)*
O professor projeta uma captura de tela do VS Code com 8 elementos numerados e sem identificação. Cada grupo recebe uma ficha com os nomes dos recursos para associar.

2. **Identificação em grupo** *(7 min)*
Os grupos associam cada número ao recurso correspondente e registram para que serve cada um, com suas próprias palavras.

3. **Correção e debate** *(7 min)*
O professor revela as respostas e usa cada item como gancho para reforçar o conteúdo: *"Este aqui é o terminal integrado — qual a vantagem de ele estar dentro da IDE?"*

**Elementos para identificar na captura de tela:**

| Número | Elemento | Para que serve |
|--------|----------|---------------|
| 1 | Explorador de arquivos (barra lateral) | Navegar pela estrutura de pastas e arquivos do projeto |
| 2 | Aba do editor de código | Área onde o código é escrito — suporta múltiplas abas abertas |
| 3 | Destaque de sintaxe (cores no código) | Facilita a leitura diferenciando palavras-chave, variáveis e strings |
| 4 | Terminal integrado (parte inferior) | Executa comandos sem sair da IDE |
| 5 | Ícone de controle de versão (Git) | Visualiza e gerencia alterações no repositório |
| 6 | Barra de status (rodapé) | Exibe linguagem ativa, branch Git, erros e avisos |
| 7 | Ícone de extensões | Instala e gerencia plugins e extensões da IDE |
| 8 | Indicador de erros e avisos | Mostra a quantidade de erros e alertas no código atual |

> **Nota:** se os computadores da sala tiverem o VS Code instalado, a dinâmica pode ser feita ao vivo — cada grupo abre a IDE e localiza os elementos na própria tela, tornando a atividade ainda mais prática. O professor circula pelos grupos orientando a navegação.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 02 — 25/02/2026 · Ferramentas de Desenvolvimento — Funções e Repositórios |
| Próxima SA → | SA 04 — 11/03/2026 · Instalação e Configuração do Ambiente |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Quadro branco e marcador
- Capturas de tela do VS Code impressas ou projetadas para a dinâmica (1 por grupo)
- VS Code instalado nos computadores da sala (recomendado para a versão ao vivo da dinâmica)

---

## Observações do Professor
