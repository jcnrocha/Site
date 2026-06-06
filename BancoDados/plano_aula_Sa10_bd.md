# UC: Fundamentos de Banco de Dados
## SA 10 — 1º Trimestre

---

## Tema

SQL DCL + Revisão Geral · Apresentação dos Trabalhos em Grupo

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o papel do DCL dentro das categorias SQL e a importância do controle de acesso em bancos de dados
- Aplicar os comandos `GRANT` e `REVOKE` para conceder e revogar permissões a usuários do banco
- Revisar os principais conteúdos do 1º trimestre de forma integrada — conectando BD, SGBD, SQL e Normalização
- Apresentar oralmente o trabalho de pesquisa desenvolvido ao longo do trimestre com clareza e domínio do conteúdo
- Avaliar as apresentações dos colegas com base nos critérios definidos no enunciado do trabalho

**Habilidade da matriz:** H06 — Identificar linguagem de banco de dados relacionais e não-relacionais

---

## Conteúdo

- O que é DCL — Data Control Language: a linguagem de controle de acesso ao banco de dados
- Por que o controle de acesso é importante: segurança, auditoria e princípio do menor privilégio
- Tipos de permissões em um banco de dados relacional:
  - Permissões de objetos: `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, `ALTER`
  - Permissões em nível de banco de dados e de tabela
- Comando `GRANT` — conceder permissões a um usuário:
  ```sql
  GRANT SELECT, INSERT ON banco.tabela TO 'usuario'@'host';
  ```
- Comando `REVOKE` — revogar permissões de um usuário:
  ```sql
  REVOKE INSERT ON banco.tabela FROM 'usuario'@'host';
  ```
- Cenários práticos de controle de acesso em sistemas reais:
  - Usuário de leitura apenas (relatórios, dashboards)
  - Usuário de aplicação (INSERT e SELECT, sem DROP)
  - Usuário administrador (todas as permissões)
- Revisão geral do 1º trimestre: síntese dos principais conceitos de cada SA
- **Apresentação dos Trabalhos em Grupo** — cada grupo apresenta sua pesquisa para a turma

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Organização da sala para as apresentações · Apresentação da agenda da aula |
| Explicação DCL | Slides — o que é DCL, por que o controle de acesso importa, GRANT e REVOKE com exemplos práticos e cenários reais |
| Revisão Geral | Síntese rápida dos conteúdos do trimestre — professor percorre os temas de SA 01 a SA 09 em sequência, conectando os conceitos |
| Apresentações | Cada grupo apresenta seu trabalho dentro do tempo definido · Professor e turma avaliam com base nos critérios do enunciado |
| Fechamento | Feedback geral sobre as apresentações · Orientação sobre a SA 11 (prova) — conteúdo, formato e data |

---

## Dinâmica — Apresentação dos Trabalhos em Grupo

**Duração:** conforme tempo disponível após a explicação do DCL e a revisão geral · **Agrupamento:** grupos formados na SA 03

**Objetivo:** desenvolver a capacidade de comunicação oral, domínio de conteúdo e organização de apresentações técnicas — competências essenciais para o profissional de desenvolvimento de sistemas.

**Temas por grupo** (conforme definido na SA 03):

| Grupo | Tema |
|-------|------|
| 1 | Arquitetura Relacional de Banco de Dados |
| 2 | Arquitetura Não Relacional de Banco de Dados |
| 3 | Modelagem de Dados — Modelo Conceitual e ER |
| 4 | Modelo Lógico e Físico de Banco de Dados |

**Critérios de avaliação:**

| Critério | Pontos |
|----------|--------|
| Clareza e organização dos slides | 4 |
| Domínio do conteúdo na apresentação | 4 |
| Participação de todos os integrantes | 4 |
| Uso de exemplos práticos | 4 |
| Criatividade e qualidade visual | 2 |
| Citação das fontes | 2 |
| **Total** | **20** |

**Orientações para a apresentação:**
- Tempo por grupo: 10 a 15 minutos
- Todos os integrantes devem falar
- Slides mínimos: 8
- Ao final de cada apresentação: espaço de 2 minutos para perguntas da turma e do professor

---

## Avaliação

Esta aula não possui questionário individual — a avaliação formal é o Trabalho em Grupo com peso 20, conforme critérios acima. A participação oral durante a revisão geral pode ser registrada como atividade de sala.

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 09 — 15/04/2026 · SQL DML — INSERT INTO |
| Próxima aula → | SA 11 — 29/04/2026 · Prova — 1ª Avaliação Trimestral |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides do professor (DCL e revisão geral)
- Computador ou notebook disponível para os grupos projetarem seus slides
- Cabo HDMI ou acesso à TV para conexão dos notebooks dos alunos
- Ficha de avaliação dos trabalhos impressa — uma por avaliador

---

## Observações do Professor
