# UC: Programação de Aplicativos
## SA 04 — 1º Trimestre

---

## Tema

Instalação e Configuração do Ambiente de Desenvolvimento

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Identificar os requisitos mínimos de hardware e software necessários para instalar e executar uma IDE e suas ferramentas complementares
- Realizar a instalação do VS Code e das extensões essenciais para o desenvolvimento na linguagem da UC
- Configurar o ambiente de desenvolvimento: tema, formatador automático, terminal padrão e integração com Git
- Reconhecer os parâmetros de configuração mais relevantes de uma IDE e o impacto de cada um na produtividade
- Verificar se o ambiente está corretamente configurado executando um programa simples do início ao fim

**Capacidades da matriz:** 2.2.1 Configurações · 2.2.2 Requisitos mínimos · Instalar ferramentas de acordo com requisitos de hardware, software e parâmetro de configuração

---

## Conteúdo

- Retomada rápida da SA 03: *"Na SA passada conhecemos a IDE e seus recursos — hoje vamos colocar a mão na massa: instalar, configurar e fazer o ambiente funcionar do zero"*

- **Requisitos mínimos de hardware para o ambiente de desenvolvimento:**

  | Componente | Mínimo recomendado | Por que importa |
  |------------|-------------------|-----------------|
  | Processador | Intel Core i3 / AMD Ryzen 3 (64 bits) | Compilação e execução de código exigem processamento |
  | Memória RAM | 4 GB (8 GB recomendado) | IDE + terminal + navegador consomem memória simultaneamente |
  | Armazenamento | 10 GB livres em SSD ou HD | Espaço para IDE, extensões, projetos e dependências |
  | Sistema Operacional | Windows 10/11 · Linux Ubuntu 20.04+ · macOS 10.15+ | VS Code suporta os três sistemas |
  | Conexão à internet | Necessária para baixar extensões e dependências | Gerenciadores de pacotes (pip, npm, maven) precisam de acesso à rede |

- **Requisitos mínimos de software:**
  - Sistema operacional atualizado (Windows 10 64 bits ou superior recomendado)
  - Permissão de administrador para instalar programas
  - Git instalado e configurado com nome de usuário e e-mail
  - Linguagem de programação da UC instalada (JDK para Java · Python 3.x para Python)
  - VS Code instalado

- **Roteiro de instalação — passo a passo:**
  1. **Baixar o VS Code** — acessar code.visualstudio.com · escolher o instalador correto para o sistema operacional
  2. **Instalar o VS Code** — executar o instalador · marcar as opções: *"Adicionar ao PATH"* e *"Abrir com VS Code"* no menu de contexto
  3. **Instalar a linguagem da UC** — JDK (java.sun.com) ou Python (python.org) · verificar instalação no terminal: `java -version` ou `python --version`
  4. **Instalar o Git** — git-scm.com · verificar instalação: `git --version`
  5. **Configurar o Git** — definir nome e e-mail globais:
     - `git config --global user.name "Seu Nome"`
     - `git config --global user.email "seu@email.com"`
  6. **Instalar extensões no VS Code** — abrir painel de extensões (`Ctrl+Shift+X`) · instalar: extensão da linguagem, Prettier, GitLens, Error Lens

- **Parâmetros de configuração essenciais do VS Code:**
  - **Tema de cores** — `Ctrl+K Ctrl+T` · escolher tema de alto contraste ou escuro para reduzir fadiga visual
  - **Formatação automática ao salvar** — `settings.json`: `"editor.formatOnSave": true` · mantém o código sempre organizado sem esforço manual
  - **Terminal padrão** — definir o terminal que abre com `Ctrl+'`: PowerShell (Windows) · Bash (Linux/macOS)
  - **Tamanho da fonte** — `"editor.fontSize": 14` · ajuste para conforto visual
  - **Auto Save** — `"files.autoSave": "afterDelay"` · salva automaticamente após um tempo sem digitação
  - **Régua de limite de linha** — `"editor.rulers": [80]` · linha guia visual para manter o código dentro de 80 caracteres por linha (boa prática)

- **Verificação do ambiente — como confirmar que tudo está funcionando:**
  - Abrir o VS Code · abrir o terminal integrado (`Ctrl+'`)
  - Executar `git --version` — deve retornar a versão instalada
  - Executar `java -version` ou `python --version` — deve retornar a versão da linguagem
  - Criar uma pasta de projeto · abrir no VS Code · criar um arquivo `hello.java` ou `hello.py`
  - Escrever e executar um programa simples: *"Olá, Mundo!"* — se rodar sem erros, o ambiente está pronto

- **Erros comuns na instalação e como resolver:**
  - *"java não é reconhecido como comando"* → linguagem não foi adicionada ao PATH do sistema · refazer instalação marcando a opção correta
  - *"git não é reconhecido como comando"* → Git não foi adicionado ao PATH · reinstalar o Git marcando a opção "Add Git to PATH"
  - Extensão da linguagem não encontra o interpretador → configurar o caminho do interpretador no VS Code: `Ctrl+Shift+P` → *"Select Interpreter"*
  - VS Code lento na inicialização → muitas extensões instaladas desnecessariamente · desativar as que não estão em uso

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 03: *"Conhecemos a IDE — hoje o ambiente sai do papel e vai para a máquina de vocês"* |
| Retomada | Professor pergunta: *"Se eu pedir para vocês instalarem um programa agora, o que verificariam antes de clicar em 'Baixar'?"* — alunos respondem livremente · professor conecta as respostas com requisitos mínimos de hardware e software |
| Explicação | Slides — requisitos de hardware e software, roteiro de instalação passo a passo, parâmetros de configuração essenciais, como verificar se o ambiente está funcional |
| Dinâmica | "Ambiente no Ar" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: ambiente configurado é pré-requisito para tudo que vem a seguir · requisitos mínimos garantem que a ferramenta rode corretamente · configuração correta evita retrabalho · Próxima SA: linguagem de programação estruturada — variáveis e controle |

---

## Dinâmica — "Ambiente no Ar"

**Duração:** 15 minutos · **Agrupamento:** individual ou duplas

**Objetivo:** consolidar a instalação e configuração do ambiente por meio de um checklist prático — desenvolvendo o hábito profissional de verificar e validar o ambiente antes de iniciar um projeto, assim como um técnico faz ao preparar uma estação de trabalho para um cliente.

**Materiais:** checklist impresso ou projetado · computadores da sala com acesso à internet.

**Passo a passo:**

1. **Distribuição do checklist** *(1 min)*
Cada aluno ou dupla recebe o checklist de verificação do ambiente. O desafio é executar cada item e marcar como concluído.

2. **Execução do checklist** *(10 min)*
Os alunos seguem o checklist na própria máquina, executando os comandos de verificação no terminal do VS Code. O professor circula pela sala auxiliando quem encontrar dificuldades.

3. **Resultado e debate** *(4 min)*
O professor pergunta: *"Quem chegou no último item sem nenhum erro?"* · Para quem encontrou erros: *"Qual foi o erro? Conseguiu resolver? Como?"* — erros reais encontrados na sala viram casos de aprendizagem coletiva.

**Checklist — "Ambiente no Ar":**

| # | Verificação | Comando / Ação | Resultado esperado |
|---|-------------|---------------|-------------------|
| 1 | VS Code instalado e abrindo | Abrir o VS Code | Janela abre sem erros |
| 2 | Git instalado | `git --version` no terminal | Retorna versão do Git |
| 3 | Git configurado com nome | `git config user.name` | Retorna seu nome |
| 4 | Git configurado com e-mail | `git config user.email` | Retorna seu e-mail |
| 5 | Linguagem instalada | `java -version` ou `python --version` | Retorna versão da linguagem |
| 6 | Extensão da linguagem instalada | Abrir painel de extensões | Extensão aparece como instalada |
| 7 | Prettier instalado | Abrir painel de extensões | Prettier aparece como instalado |
| 8 | Formatação automática ativa | Salvar arquivo com código desformatado | Código é formatado automaticamente |
| 9 | Terminal integrado funcionando | `Ctrl+'` abre o terminal | Terminal abre dentro do VS Code |
| 10 | Programa "Olá, Mundo!" executando | Criar e rodar arquivo de teste | Saída exibe "Olá, Mundo!" no terminal |

> **Nota:** o checklist pode ser reaproveitado pelos alunos sempre que precisarem configurar um novo computador — reforçar que no mercado de trabalho, preparar o ambiente de desenvolvimento é a primeira tarefa de qualquer projeto novo. Desenvolvedores profissionais têm esse processo automatizado e documentado.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 03 — 04/03/2026 · Ambiente de Desenvolvimento — IDE |
| Próxima SA → | SA 05 — 18/03/2026 · Linguagem de Programação Estruturada — Parte 1 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com acesso à internet (essencial para esta SA)
- Checklist "Ambiente no Ar" impresso (1 por aluno ou dupla) ou projetado
- Arquivos de instalação disponíveis em pendrive como alternativa caso a internet esteja lenta

---

## Observações do Professor
