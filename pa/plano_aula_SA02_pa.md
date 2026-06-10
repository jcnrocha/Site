# UC: Programação de Aplicativos
## SA 02 — 1º Trimestre

---

## Tema

Ferramentas de Desenvolvimento — Funções e Repositórios

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Identificar as principais ferramentas utilizadas no desenvolvimento de software e a função de cada uma no ciclo de desenvolvimento
- Compreender o que é um repositório de código e por que ele é indispensável no trabalho profissional
- Reconhecer o Git como sistema de controle de versão e diferenciar Git de GitHub/GitLab
- Relacionar o uso de repositórios com boas práticas de organização, rastreabilidade e trabalho em equipe
- Descrever o fluxo básico de uso de um repositório: criar, commitar e visualizar histórico de alterações

**Capacidades da matriz:** Reconhecer ferramentas para o desenvolvimento de atividades (repositório, controle de versão) · 2.1.1 Funções · 2.1.2 Repositórios

---

## Conteúdo

- Retomada rápida da SA 01: *"Na SA passada vimos o ciclo de desenvolvimento e uma visão geral das ferramentas — hoje vamos aprofundar nas ferramentas e entender como repositórios funcionam na prática"*

- **Ferramentas do ciclo de desenvolvimento e suas funções:**
  - **IDE (Integrated Development Environment)** — ambiente onde o código é escrito, executado e depurado · combina editor, terminal e depurador em um só lugar · ex: VS Code, IntelliJ, Eclipse
  - **Compilador / Interpretador** — transforma o código escrito pelo desenvolvedor em instruções que o computador entende · ex: javac (Java), python (Python)
  - **Gerenciador de dependências** — controla as bibliotecas externas que o projeto usa · ex: Maven (Java), pip (Python), npm (JavaScript)
  - **Ferramenta de teste** — automatiza a verificação se o código funciona corretamente · ex: JUnit, PyTest
  - **Repositório de código** — armazena, organiza e versiona o código do projeto · ex: GitHub, GitLab, Bitbucket
  - **Sistema de controle de versão** — registra o histórico de todas as alterações feitas no código · ex: Git, SVN

- **O que é controle de versão:**
  - Sistema que registra cada alteração feita em um arquivo ao longo do tempo
  - Permite voltar para qualquer versão anterior do código
  - Permite que múltiplos desenvolvedores trabalhem no mesmo projeto simultaneamente sem conflito
  - Responde às perguntas: *o que mudou? quem mudou? quando mudou? por quê mudou?*

- **Git — o sistema de controle de versão mais usado no mundo:**
  - Criado por Linus Torvalds em 2005 para gerenciar o desenvolvimento do kernel Linux
  - Distribuído: cada desenvolvedor tem uma cópia completa do repositório na sua máquina
  - Gratuito e open source
  - Conceitos fundamentais:
    - **Repositório (repo):** pasta do projeto com todo o histórico de versões
    - **Commit:** registro de uma alteração com mensagem descritiva — *"adicionei tela de login"*
    - **Branch:** ramificação do código para desenvolver uma funcionalidade sem afetar o principal
    - **Merge:** junção de uma branch de volta ao código principal
    - **Clone:** cópia de um repositório remoto para a máquina local

- **Git × GitHub × GitLab — qual a diferença:**
  | Ferramenta | O que é | Função |
  |------------|---------|--------|
  | **Git** | Sistema de controle de versão | Registra o histórico localmente na máquina |
  | **GitHub** | Plataforma online de repositórios | Armazena o repositório na nuvem e facilita colaboração |
  | **GitLab** | Plataforma online de repositórios | Similar ao GitHub, com foco em CI/CD e uso corporativo |
  > Git é a ferramenta · GitHub e GitLab são plataformas que hospedam repositórios Git na nuvem

- **Fluxo básico de uso de um repositório:**
  1. `git init` — inicializa um repositório na pasta do projeto
  2. Desenvolvedor escreve ou modifica código
  3. `git add` — seleciona os arquivos alterados para registrar
  4. `git commit -m "mensagem"` — registra as alterações com uma descrição
  5. `git push` — envia os commits para o repositório remoto (GitHub/GitLab)
  6. `git pull` — baixa as alterações feitas por outros desenvolvedores

- **Por que repositórios são indispensáveis no mercado de trabalho:**
  - Todo projeto profissional usa controle de versão — não saber Git é uma barreira de entrada
  - Repositórios públicos no GitHub funcionam como portfólio para o mercado de trabalho
  - Empresas usam repositórios para revisar código, registrar tarefas e fazer deploy automático
  - Trabalhar sem repositório é como escrever um texto importante sem salvar — risco total de perda

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 01: *"Citamos repositório e controle de versão na aula passada — hoje vamos entender como isso funciona de verdade"* |
| Retomada | Professor pergunta: *"Se você e um colega editassem o mesmo arquivo de código ao mesmo tempo e enviassem por e-mail para o professor, o que aconteceria com as alterações de cada um?"* — alunos respondem livremente · professor usa as respostas para introduzir o problema que o controle de versão resolve |
| Explicação | Slides — ferramentas do ciclo de desenvolvimento e funções, o que é controle de versão, Git e seus conceitos, diferença Git × GitHub × GitLab, fluxo básico de uso |
| Dinâmica | "Linha do Tempo do Código" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: cada ferramenta tem uma função específica no ciclo de desenvolvimento · Git registra o histórico · GitHub armazena na nuvem · commit é o registro de uma alteração · Próxima SA: IDE — o ambiente onde o código nasce |

---

## Dinâmica — "Linha do Tempo do Código"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar os conceitos de controle de versão e repositório por meio da simulação de um histórico de commits — desenvolvendo a compreensão de que cada commit é um registro rastreável de uma decisão técnica, e que isso é o que diferencia o trabalho profissional do amador.

**Materiais:** slide com o cenário projetado · quadro branco para registrar a linha do tempo · ou cartões impressos com os eventos do cenário.

**Passo a passo:**

1. **Apresentação do cenário** *(2 min)*
O professor apresenta a situação: um desenvolvedor está criando um sistema de cadastro de clientes e fez várias alterações ao longo de três dias. Os eventos estão fora de ordem.

2. **Organização em grupo** *(7 min)*
Cada grupo recebe os eventos embaralhados e precisa: organizá-los em ordem cronológica, escrever uma mensagem de commit adequada para cada evento e identificar qual alteração causou um erro no sistema.

3. **Apresentação e debate** *(6 min)*
Os grupos apresentam sua linha do tempo. O professor compara as mensagens de commit criadas por cada grupo e debate: *"Uma mensagem de commit boa ou ruim faz diferença? Por quê?"*

**Cenário — eventos para organizar:**

| Evento (fora de ordem) | Commit sugerido | Momento |
|------------------------|----------------|---------|
| Criou o arquivo principal do projeto | `"inicio do projeto - estrutura base"` | Dia 1 — manhã |
| Adicionou o formulário de cadastro com os campos nome e e-mail | `"adiciona formulário de cadastro"` | Dia 1 — tarde |
| Corrigiu erro de digitação no campo e-mail | `"corrige campo email no formulário"` | Dia 2 — manhã |
| Conectou o formulário ao banco de dados | `"integra formulário com banco de dados"` | Dia 2 — tarde |
| Testou e descobriu que dados não estavam sendo salvos | `"identifica bug no salvamento de dados"` | Dia 3 — manhã |
| Corrigiu o bug e confirmou que o cadastro funciona | `"corrige bug e valida salvamento"` | Dia 3 — tarde |

> **Nota:** reforçar que mensagens de commit vagas como *"alterações"* ou *"atualizei"* são um problema real no mercado — quando algo quebra, a equipe precisa saber exatamente o que cada commit fez para encontrar a origem do erro. Uma boa mensagem de commit é uma forma de comunicação profissional.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 01 — 11/02/2026 · Apresentação da UC e Introdução ao Ambiente de Desenvolvimento |
| Próxima SA → | SA 03 — 04/03/2026 · Ambiente de Desenvolvimento — IDE |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Quadro branco e marcador
- Cartões com os eventos da dinâmica impressos (1 conjunto por grupo) ou slide com os eventos projetados
- Acesso à internet para demonstração ao vivo de um repositório no GitHub (opcional)

---

## Observações do Professor
