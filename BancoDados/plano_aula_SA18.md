# UC: Fundamentos de Banco de Dados
## Aula 05 — 2º Trimestre

---

## Tema

Modelo Lógico — Conceitos e Conversão do DER

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é o modelo lógico e qual é o seu papel na transição entre o modelo conceitual e a implementação física
- Aplicar as regras de conversão de entidades e relacionamentos do DER para o esquema lógico
- Identificar e definir chaves primárias (PK) e chaves estrangeiras (FK) no esquema lógico
- Resolver relacionamentos N:N por meio da criação de tabelas associativas
- Escrever um esquema lógico completo na notação textual padronizada a partir de um DER fornecido

**Habilidade da matriz:** H03 — Identificar características de modelagem de dados

---

## Conteúdo

- Revisão rápida: o que o modelo lógico representa e onde ele se posiciona entre o conceitual e o físico
- Regras de conversão do DER para o modelo lógico:
  - Cada entidade vira uma tabela
  - Cada atributo simples vira uma coluna
  - O atributo identificador vira a chave primária (PK)
  - Atributos compostos: cada subatributo vira uma coluna separada
  - Atributos multivalorados: viram uma tabela própria com FK para a entidade principal
- Conversão de relacionamentos por tipo de cardinalidade:
  - **1:1** — a FK vai para a tabela de participação parcial (ou para qualquer uma das duas)
  - **1:N** — a FK vai sempre para o lado N (a tabela do "muitos")
  - **N:N** — cria-se uma tabela associativa com as FKs de ambas as entidades como chave composta
- Relacionamento com atributo próprio: o atributo vai para a tabela associativa
- Notação textual do esquema lógico: `TABELA (coluna PK, coluna, coluna FK → OUTRA_TABELA)`
- Conversão completa do DER de biblioteca: do diagrama ao esquema lógico
- Diferença entre chave candidata, chave primária e chave estrangeira

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 04 — pergunta oral: *"O que acontece com um relacionamento N:N no modelo lógico?"* |
| Retomada | Professor exibe o DER completo do sistema de biblioteca construído nas aulas anteriores e pergunta: *"Como transformamos este diagrama em tabelas?"* — alunos tentam responder livremente |
| Explicação | Slides — regras de conversão por tipo de entidade e por tipo de cardinalidade, notação textual, resolução do N:N com tabela associativa |
| Dinâmica | "Converte aí!" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: as três regras de ouro da conversão (entidade → tabela, identificador → PK, lado N → FK) · Próxima aula: Modelo Físico — Restrições, Chaves e Design |

---

## Dinâmica — "Converte aí!"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar as regras de conversão do DER para o modelo lógico por meio da prática guiada de transformação de um diagrama simples em esquema textual, tomando decisões sobre PK, FK e tabelas associativas.

**Materiais:** slide ou folha com o DER do sistema de locadora · folha A4 por grupo para escrever o esquema lógico.

**Passo a passo:**

1. **Apresentação do DER** *(2 min)*
O professor projeta o DER do sistema de locadora de filmes — já conhecido da Aula 02 — agora com cardinalidades marcadas.

**DER fornecido — Sistema de Locadora:**

| Entidade / Relacionamento | Detalhes |
|---------------------------|----------|
| CLIENTE | `cpf` (identificador), `nome`, `email`, `telefones` (multivalorado) |
| FILME | `id_filme` (identificador), `titulo`, `genero`, `ano` |
| ATOR | `id_ator` (identificador), `nome`, `nacionalidade` |
| LOCACAO | relacionamento entre CLIENTE e FILME — cardinalidade 1:N (um cliente faz várias locações) · atributo: `data_locacao` |
| ELENCO | relacionamento entre FILME e ATOR — cardinalidade N:N (um filme tem vários atores; um ator aparece em vários filmes) |

2. **Conversão em grupo** *(8 min)*
Cada grupo escreve o esquema lógico completo na notação textual, tomando as seguintes decisões:
- Onde colocar a FK da LOCACAO
- Como resolver o N:N de ELENCO
- Como tratar o atributo multivalorado `telefones`

3. **Apresentação e correção** *(5 min)*
Um grupo apresenta seu esquema. O professor compara com o gabarito e discute as decisões tomadas.

**Gabarito esperado:**

```
CLIENTE (cpf PK, nome, email)

TELEFONE_CLIENTE (cpf_cliente FK → CLIENTE, telefone)

FILME (id_filme PK, titulo, genero, ano)

ATOR (id_ator PK, nome, nacionalidade)

ELENCO (id_filme FK → FILME, id_ator FK → ATOR)
  ↑ Tabela associativa — resolve o N:N entre FILME e ATOR

LOCACAO (id_locacao PK, cpf_cliente FK → CLIENTE,
         id_filme FK → FILME, data_locacao)
```

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 04 — 10/06/2026 · DER — Relacionamentos e Cardinalidade |
| Próxima aula → | Aula 06 — 24/06/2026 · Modelo Físico — Restrições, Chaves e Design |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para escrever o esquema lógico na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
