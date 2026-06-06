# UC: Fundamentos de Banco de Dados
## SA 35 — 3º Trimestre

---

## Tema

Projeto Integrador — Banco de Dados Completo

---

## Objetivos de Aprendizagem

Ao final desta aula, o aluno será capaz de:

- Aplicar de forma integrada todos os conteúdos do ano: modelagem conceitual, lógica, física, normalização, SQL DDL, DML e DQL
- Elaborar o DER de um sistema real a partir de uma descrição textual de requisitos
- Converter o DER para o modelo lógico e físico, tomando decisões técnicas fundamentadas
- Escrever o script SQL completo de criação e população do banco de dados com comentários de documentação
- Construir consultas SQL com SELECT, JOIN, GROUP BY e subqueries sobre o banco criado pelo grupo

**Habilidades da matriz:** H03 · H04 · H06 · H07 · H08

---

## Conteúdo

Esta aula é dedicada ao desenvolvimento do Projeto Integrador em grupo. Não há conteúdo novo — o objetivo é consolidar e aplicar de forma autônoma tudo o que foi aprendido ao longo do ano.

**Etapas do Projeto Integrador:**

- **Etapa 1 — Modelo Conceitual:** leitura dos requisitos do cenário · identificação das entidades, atributos e relacionamentos · construção do DER com cardinalidades
- **Etapa 2 — Modelo Lógico:** conversão do DER para esquema lógico na notação textual · definição de PKs, FKs e tabelas associativas · resolução de relacionamentos N:N
- **Etapa 3 — Modelo Físico:** escrita do script SQL com `CREATE TABLE` · escolha de tipos de dados e restrições · ordem correta de criação das tabelas · documentação com comentários
- **Etapa 4 — População do Banco:** inserção de dados com `INSERT INTO` · mínimo de 5 registros por tabela principal · dados coerentes com o cenário
- **Etapa 5 — Consultas SQL:** escrita de pelo menos 5 consultas que demonstrem SELECT com WHERE, JOIN, GROUP BY, subquery e View

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · Apresentação do cenário do Projeto Integrador · Formação dos grupos · Distribuição do enunciado impresso |
| Leitura e planejamento | Grupos leem o cenário e planejam as etapas — professor circula para tirar dúvidas e validar o entendimento do escopo |
| Desenvolvimento | Grupos trabalham nas etapas do projeto — DER, modelo lógico, modelo físico, INSERT e consultas · professor acompanha e orienta cada grupo |
| Ponto de verificação | Professor solicita que cada grupo apresente o DER esboçado para validação antes de avançar para o modelo lógico |
| Fechamento | Professor informa o que deve estar pronto para apresentação na SA 36 · esclarece dúvidas finais · orienta sobre o formato da entrega |

---

## Dinâmica — Projeto Integrador em Grupo

**Duração:** aula inteira · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** integrar todos os conteúdos trabalhados ao longo do ano em um banco de dados real e completo — desde o modelo conceitual até as consultas SQL com documentação — desenvolvendo autonomia técnica e trabalho colaborativo.

**Cenário do Projeto — Sistema de Gestão de uma Academia de Musculação:**

> *"A academia CorporeFit precisa de um sistema para gerenciar seus alunos, planos de assinatura, instrutores e agendamentos de treino. Cada aluno tem um cadastro com nome, CPF, data de nascimento e e-mail. Um aluno assina um plano (mensal, trimestral ou anual) com data de início e data de vencimento. Cada plano tem um nome e um valor mensal. Os instrutores têm nome, CREF e especialidade. Um instrutor pode orientar vários alunos, e um aluno tem um único instrutor responsável. Os treinos são agendados com data, horário e duração. Um aluno pode ter vários treinos agendados, e cada treino é acompanhado por um instrutor."*

**Requisitos mínimos de entrega:**

| Etapa | Entregável mínimo |
|-------|-------------------|
| Modelo Conceitual | DER com todas as entidades, atributos identificadores e relacionamentos com cardinalidade |
| Modelo Lógico | Esquema lógico completo na notação textual com PKs, FKs e tabelas associativas |
| Modelo Físico | Script SQL com `CREATE TABLE` documentado — tipos de dados e restrições corretos |
| População | Mínimo de 5 registros por tabela principal com `INSERT INTO` |
| Consultas SQL | Mínimo de 5 consultas: 1 com JOIN, 1 com GROUP BY, 1 com subquery, 1 com View, 1 livre |

**Critérios de avaliação (Peso 20):**

| Critério | Pontos |
|----------|--------|
| Modelo Conceitual — DER correto e completo | 4 |
| Modelo Lógico e Físico — script SQL funcional e bem estruturado | 4 |
| Population e consultas SQL — dados coerentes e consultas funcionais | 4 |
| Documentação — comentários no código SQL | 4 |
| Apresentação oral — clareza, domínio e participação de todos | 4 |
| **Total** | **20** |

---

## Avaliação

Esta aula não possui questionário individual. A avaliação formal é o Projeto Integrador com peso 20, conforme critérios acima. A apresentação oral ocorrerá na SA 36.

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | SA 34 — 28/10/2026 · Documentação de Código SQL — Comentários |
| Próxima aula → | SA 36 — 11/11/2026 · Apresentação do Projeto + Revisão Geral |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Enunciado do Projeto Integrador impresso — uma cópia por aluno
- Folhas A4 para esboço do DER e modelo lógico
- Computadores ou notebooks para escrita do script SQL (se disponíveis)
- Quadro branco e marcador

---

## Observações do Professor
