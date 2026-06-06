# UC: Fundamentos de Banco de Dados
## SA 07 — 1º Trimestre

---

## Tema

Ferramentas de Banco de Dados

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Identificar as principais ferramentas de administração e manipulação de bancos de dados do mercado
- Reconhecer a função de cada ferramenta e com qual SGBD ela se relaciona
- Diferenciar ferramentas de interface gráfica (GUI) de ferramentas de linha de comando (CLI)
- Compreender como as ferramentas se conectam ao SGBD e facilitam o trabalho do desenvolvedor
- Relacionar a escolha da ferramenta ao contexto do projeto e ao SGBD utilizado

**Habilidade da matriz:** H07 — Identificar ferramentas de manipulação de banco de dados

---

## Conteúdo

- Por que usar ferramentas de banco de dados: produtividade, visualização, gerenciamento e documentação
- Diferença entre GUI (interface gráfica) e CLI (linha de comando) — vantagens e limitações de cada abordagem
- Ferramentas por SGBD:
  - **MySQL Workbench** — ferramenta oficial do MySQL · modelagem visual de banco de dados · editor SQL · administração do servidor · criação de diagramas ER
  - **pgAdmin** — ferramenta oficial do PostgreSQL · interface web · gerenciamento de objetos · editor de queries · monitoramento
  - **MongoDB Compass** — ferramenta oficial do MongoDB · visualização de documentos · editor de queries · análise de índices · exportação de dados
  - **DBeaver** — ferramenta multi-SGBD · suporta MySQL, PostgreSQL, SQLite, MongoDB, Oracle e outros · editor SQL avançado · visualização de dados · gratuita
  - **TablePlus** — multi-SGBD · interface moderna e intuitiva · muito usada por desenvolvedores · versão gratuita limitada
  - **SQLite Browser (DB Browser for SQLite)** — ferramenta específica para SQLite · leve e simples · ideal para projetos mobile e desktop
- Linha de comando: quando e por que usar — automação, scripts, ambientes de servidor sem interface gráfica
- Como conectar uma ferramenta a um banco de dados: host, porta, usuário, senha e nome do banco
- Parâmetros de conexão padrão dos principais SGBDs:
  - MySQL: porta 3306
  - PostgreSQL: porta 5432
  - MongoDB: porta 27017
  - SQLite: arquivo local — sem servidor

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da SA 06 — pergunta oral: *"Quais são as quatro categorias da linguagem SQL?"* |
| Retomada | Professor pergunta: *"Se vocês fossem trabalhar hoje como desenvolvedores e precisassem abrir e visualizar um banco de dados, o que usariam?"* — alunos respondem livremente · identificar o que já conhecem |
| Explicação | Slides — por que usar ferramentas, GUI x CLI, ferramentas por SGBD com demonstração visual das interfaces, parâmetros de conexão |
| Dinâmica | "Quem Sou Eu? — Round Ferramentas" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: cada SGBD tem sua ferramenta oficial · DBeaver é a opção multi-SGBD mais usada por desenvolvedores · Próxima aula: SQL DDL — CREATE TABLE |

---

## Dinâmica — "Quem Sou Eu? — Round Ferramentas"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** fixar as características e os contextos de uso das principais ferramentas de banco de dados por meio de um jogo de identificação por pistas, reativando o formato já conhecido da SA 05 com novo conteúdo.

**Materiais:** cartões com as pistas impressos — um conjunto por grupo · ou slides com as pistas projetadas.

**Passo a passo:**

1. **Leitura das pistas** *(1 min por rodada)*
O professor lê as pistas em ordem crescente de especificidade. Os grupos tentam identificar a ferramenta após cada pista.

2. **Resposta em grupo** *(1 min)*
O grupo que identificar primeiro levanta a mão e responde. Acertou na primeira pista: 3 pontos · na segunda: 2 pontos · na terceira: 1 ponto.

3. **Consolidação** *(1 min)*
O professor confirma a resposta e reforça as características da ferramenta identificada.

**Ferramentas sugeridas (5 rodadas):**

| Rodada | Pista 1 | Pista 2 | Pista 3 | Resposta |
|--------|---------|---------|---------|----------|
| 1 | Sou uma ferramenta gráfica oficial de um dos SGBDs mais usados no mundo | Permito modelar visualmente o banco de dados e criar diagramas ER | Sou da Oracle e meu nome tem a ver com o banco que gerencio e com uma bancada de trabalho | MySQL Workbench |
| 2 | Sou gratuita e consigo me conectar a quase qualquer banco de dados do mercado | Tenho suporte a mais de 80 SGBDs diferentes em uma única interface | Meu nome vem de um personagem dos desenhos animados e meu logo é um castor | DBeaver |
| 3 | Sou a ferramenta oficial de um banco de dados que guarda documentos JSON | Permito visualizar, filtrar e editar documentos diretamente pela interface | Meu nome tem a ver com a palavra "bússola" e sou feita pela mesma empresa do meu SGBD | MongoDB Compass |
| 4 | Sou leve, simples e não preciso de servidor para funcionar | Sou ideal para projetos de aplicativos mobile que precisam de um banco local | Meu nome tem a ver com navegar em um banco de dados que cabe em um arquivo | DB Browser for SQLite |
| 5 | Sou a ferramenta oficial de administração de um banco de dados open source muito robusto | Funciono como uma aplicação web que roda no navegador | Meu nome começa com "pg" — a sigla do banco de dados que gerencio | pgAdmin |

> **Nota:** ao final da dinâmica, projetar a tabela resumo com as 5 ferramentas, seus SGBDs correspondentes e seus casos de uso — reforçando a associação que será necessária nas próximas aulas práticas.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 06 — 25/03/2026 · SQL e NoSQL |
| Próxima aula → | SA 08 — 08/04/2026 · SQL DDL — CREATE TABLE |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Cartões com as pistas da dinâmica impressos (1 conjunto por grupo) ou slides com as pistas
- Quadro branco e marcador (para registrar pontuação dos grupos)

---

## Observações do Professor
