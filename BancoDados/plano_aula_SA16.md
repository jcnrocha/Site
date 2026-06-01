# UC: Fundamentos de Banco de Dados
## Aula 03 — 2º Trimestre

---

## Tema

Modelo Conceitual — Entidades e Atributos

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o que é uma entidade no contexto da modelagem conceitual e como identificá-la em um domínio real
- Diferenciar os quatro tipos de atributos: simples, composto, multivalorado e derivado
- Representar entidades e atributos corretamente no Diagrama Entidade-Relacionamento (DER)
- Identificar o atributo identificador (chave) de uma entidade e justificar sua escolha
- Construir um modelo conceitual parcial a partir da descrição de um sistema real

**Habilidade da matriz:** H03 — Identificar características de modelagem de dados

---

## Conteúdo

- O que é uma entidade — definição e critérios para identificação
- Diferença entre entidade e instância (ex: a entidade CLIENTE × o cliente João Silva)
- Tipos de entidades: forte e fraca
- O que é um atributo — definição e papel na entidade
- Tipos de atributos:
  - **Simples:** valor único e indivisível (ex: `cpf`, `ano`)
  - **Composto:** formado por subatributos (ex: `endereco` → rua, número, CEP, cidade)
  - **Multivalorado:** pode ter mais de um valor por instância (ex: `telefones`)
  - **Derivado:** calculado a partir de outro atributo (ex: `idade` derivado de `data_nascimento`)
- Atributo identificador — o que é e como escolher a chave de uma entidade
- Notação do DER: retângulo para entidade, elipse para atributo, elipse dupla para multivalorado, elipse tracejada para derivado, sublinhado para identificador
- Leitura e interpretação de DERs parciais
- Exemplos práticos: sistema de biblioteca, sistema de e-commerce, sistema de chamados de TI

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada e retomada rápida da Aula 02 — pergunta oral: *"Qual a diferença entre modelo conceitual e modelo lógico?"* |
| Retomada | Professor exibe um DER simples incompleto no slide e pergunta: *"O que está faltando neste diagrama?"* — alunos identificam livremente |
| Explicação | Slides — o que é entidade, tipos de atributos com exemplos visuais, notação do DER, atributo identificador |
| Dinâmica | "Monta o DER" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: tipos de atributos e como identificar cada um · Próxima aula: DER — Relacionamentos e Cardinalidade |

---

## Dinâmica — "Monta o DER"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar os tipos de atributos e a notação do DER por meio da construção guiada de um diagrama a partir da descrição textual de um sistema real.

**Materiais:** quadro branco ou folha A4 por grupo · caneta ou marcador · slide com a descrição do sistema.

**Passo a passo:**

1. **Leitura do sistema** *(2 min)*
O professor projeta a descrição de um sistema e lê em voz alta para a turma.

**Descrição do sistema — Clínica Veterinária:**
> *"A clínica atende animais de estimação. Cada animal tem um nome, uma espécie, uma raça e uma data de nascimento. Um animal pode ter mais de um telefone de contato do tutor cadastrado. A idade do animal é calculada automaticamente pelo sistema a partir da data de nascimento. O endereço do tutor é composto por rua, número, bairro e cidade."*

2. **Construção em grupo** *(8 min)*
Cada grupo identifica a entidade principal, lista todos os atributos e classifica cada um em: simples, composto, multivalorado ou derivado. Em seguida, esboça o DER no papel ou no quadro usando a notação correta.

3. **Apresentação e correção** *(5 min)*
Dois grupos apresentam seus diagramas. O professor compara as versões, aponta diferenças e consolida a resposta correta com a notação padronizada.

**Gabarito esperado:**

| Atributo | Tipo |
|----------|------|
| `nome` | Simples |
| `especie` | Simples |
| `raca` | Simples |
| `data_nascimento` | Simples · Identificador base |
| `idade` | Derivado (calculado de `data_nascimento`) |
| `telefones_tutor` | Multivalorado |
| `endereco_tutor` | Composto (rua, número, bairro, cidade) |

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 02 — 27/05/2026 · Modelagem de Dados — Conceitos e Fases |
| Próxima aula → | Aula 04 — 10/06/2026 · DER — Relacionamentos e Cardinalidade |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 ou quadro branco por grupo (para a dinâmica)
- Marcadores ou canetas

---

## Observações do Professor
