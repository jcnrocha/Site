# UC: Fundamentos de Banco de Dados
## Aula 04 — 2º Trimestre

---

## Tema

DER — Relacionamentos e Cardinalidade

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é um relacionamento no DER e como ele conecta duas entidades
- Identificar os três tipos de cardinalidade: 1:1, 1:N e N:N, e reconhecer cada um em situações reais
- Diferenciar participação total e participação parcial de uma entidade em um relacionamento
- Representar relacionamentos e cardinalidades corretamente na notação do DER
- Construir um DER completo — com entidades, atributos e relacionamentos — a partir da descrição de um sistema real

**Habilidade da matriz:** H03 — Identificar características de modelagem de dados

---

## Conteúdo

- O que é um relacionamento no DER — definição e notação (losango)
- Nome do relacionamento — como nomear de forma clara e no infinitivo (ex: *Realiza*, *Pertence*, *Possui*)
- Grau do relacionamento: unário, binário e ternário
- Cardinalidade — o que é e por que define as regras do negócio
- Tipos de cardinalidade:
  - **1:1** — um para um (ex: um funcionário possui um crachá)
  - **1:N** — um para muitos (ex: um cliente realiza vários pedidos)
  - **N:N** — muitos para muitos (ex: um aluno cursa várias disciplinas; uma disciplina tem vários alunos)
- Como ler a cardinalidade nos dois sentidos do relacionamento
- Participação total (obrigatória) × participação parcial (opcional) — notação com linha dupla e linha simples
- Relacionamento com atributo próprio — quando o relacionamento em si precisa guardar dados (ex: data do empréstimo)
- Construção de DER completo: entidades + atributos + relacionamentos + cardinalidades
- Exemplos práticos: sistema de biblioteca, sistema de chamados de TI, plataforma de cursos online

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 03 — pergunta oral: *"Qual a diferença entre atributo composto e atributo multivalorado?"* |
| Retomada | Professor exibe duas entidades no slide (CLIENTE e PEDIDO) sem relacionamento e pergunta: *"Como essas duas entidades se conectam? O que existe entre elas?"* — alunos respondem livremente |
| Explicação | Slides — o que é relacionamento, nome e grau, cardinalidade 1:1 / 1:N / N:N com exemplos visuais, participação total e parcial, relacionamento com atributo |
| Dinâmica | "Qual a Cardinalidade?" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: como ler cardinalidade nos dois sentidos · Próxima aula: Modelo Lógico — Conceitos e Conversão do DER |

---

## Dinâmica — "Qual a Cardinalidade?"

**Duração:** 15 minutos · **Agrupamento:** turma inteira — resposta individual com votação coletiva

**Objetivo:** fixar os três tipos de cardinalidade e a leitura bidirecional dos relacionamentos por meio de análise rápida de cenários do cotidiano de TI.

**Materiais:** slides com os cenários · quadro branco para registrar os votos.

**Passo a passo:**

1. **Apresentação do cenário** *(1 min por rodada)*
O professor projeta um par de entidades e a descrição da regra de negócio. A turma deve identificar a cardinalidade correta.

2. **Votação individual** *(1 min)*
Cada aluno levanta a mão para a opção que escolheu: **1:1**, **1:N** ou **N:N**. O professor registra os votos no quadro.

3. **Justificativa e consolidação** *(2 min)*
O professor escolhe um aluno de cada grupo de votos para justificar sua resposta. Em seguida, revela a cardinalidade correta e explica o raciocínio nos dois sentidos do relacionamento.

**Cenários sugeridos (6 rodadas):**

| Cenário | Entidades | Cardinalidade correta |
|---------|-----------|----------------------|
| Um usuário possui exatamente um perfil no sistema | USUARIO — PERFIL | 1:1 |
| Um desenvolvedor pode abrir vários chamados; cada chamado pertence a um único desenvolvedor | DESENVOLVEDOR — CHAMADO | 1:N |
| Um produto pode estar em vários pedidos; um pedido pode conter vários produtos | PRODUTO — PEDIDO | N:N |
| Um servidor hospeda vários sites; cada site está em um único servidor | SERVIDOR — SITE | 1:N |
| Um aluno pode se matricular em vários cursos; um curso pode ter vários alunos | ALUNO — CURSO | N:N |
| Cada empresa tem um único CNPJ cadastrado; cada CNPJ pertence a uma única empresa | EMPRESA — CNPJ | 1:1 |

> **Nota:** nos cenários N:N, o professor deve reforçar que esse tipo de relacionamento exigirá uma tabela associativa na fase do modelo lógico — criando a ponte entre as duas aulas.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 03 — 03/06/2026 · Modelo Conceitual — Entidades e Atributos |
| Próxima aula → | Aula 05 — 17/06/2026 · Modelo Lógico — Conceitos e Conversão do DER |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Quadro branco e marcador (para registrar votos da dinâmica)

---

## Observações do Professor
