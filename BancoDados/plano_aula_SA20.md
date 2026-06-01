# UC: Fundamentos de Banco de Dados
## Aula 07 — 2º Trimestre

---

## Tema

Dependência Funcional

---

## Objetivos de Aprendizagem

Ao final da aula, o aluno será capaz de:

- Compreender o conceito de dependência funcional e sua relação direta com a normalização de banco de dados
- Identificar os três tipos de dependência funcional: total, parcial e transitiva em tabelas reais
- Reconhecer as anomalias de inserção, atualização e exclusão geradas pela ausência de normalização
- Relacionar cada tipo de dependência funcional com a forma normal que o resolve
- Analisar uma tabela desnormalizada e mapear todas as dependências funcionais presentes

**Habilidade da matriz:** H04 — Identificar métodos de normalização

---

## Conteúdo

- O que é dependência funcional — definição formal e leitura: *"A determina B"* (A → B)
- Dependência funcional e chave primária — por que a PK é o ponto de partida da análise
- Tipos de dependência funcional:
  - **Total:** um atributo não-chave depende da chave primária inteira (ex: `nome_produto` depende de `id_produto`)
  - **Parcial:** um atributo não-chave depende de apenas parte de uma chave composta (ex: `nome_produto` depende só de `id_produto` em uma chave composta `id_produto + id_pedido`)
  - **Transitiva:** um atributo não-chave depende de outro atributo não-chave (ex: `nome_categoria` depende de `id_categoria`, que por sua vez depende de `id_produto`)
- Anomalias geradas pela falta de normalização:
  - **Inserção:** não é possível inserir um dado sem que outro exista (ex: não dá para cadastrar uma categoria sem ter um produto)
  - **Atualização:** a mesma informação está em múltiplas linhas — alterar uma e esquecer as outras gera inconsistência
  - **Exclusão:** ao excluir um registro, perde-se informação de outro contexto (ex: excluir o único produto de uma categoria apaga os dados da categoria)
- Relação entre dependências e formas normais:
  - Dependência parcial → violação da 2FN
  - Dependência transitiva → violação da 3FN
- Leitura e mapeamento de dependências em tabelas reais

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada, abertura da SA2 e contextualização: *"Nas aulas anteriores aprendemos a modelar. Agora vamos aprender a garantir que o modelo está correto — e isso começa entendendo dependência funcional."* |
| Retomada | Professor exibe uma tabela desnormalizada com dados repetidos e pergunta: *"O que há de errado nessa tabela?"* — alunos identificam os problemas livremente |
| Explicação | Slides — definição de dependência funcional, os três tipos com exemplos visuais, as três anomalias com cenários reais |
| Dinâmica | "Caça à Dependência" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da aula |
| Fechamento | Resumo: dependência total → ok · dependência parcial → problema de 2FN · dependência transitiva → problema de 3FN · Próxima aula: Normalização — 1FN e 2FN |

---

## Dinâmica — "Caça à Dependência"

**Duração:** 15 minutos · **Agrupamento:** grupos de 3 a 4 alunos

**Objetivo:** fixar os três tipos de dependência funcional por meio da análise de uma tabela desnormalizada real, identificando e classificando cada dependência presente antes de o professor apresentar a solução.

**Materiais:** slide ou folha com a tabela desnormalizada · folha A4 por grupo para mapear as dependências.

**Passo a passo:**

1. **Apresentação da tabela** *(2 min)*
O professor projeta a tabela abaixo e explica que ela representa um sistema de pedidos de uma loja virtual. A chave primária é composta: `id_pedido + id_produto`.

**Tabela PEDIDO_ITEM (desnormalizada):**

| id_pedido | id_produto | nome_produto | preco_produto | id_categoria | nome_categoria | qtd | id_cliente | nome_cliente | cidade_cliente |
|-----------|------------|--------------|---------------|--------------|----------------|-----|------------|--------------|----------------|
| 1 | 10 | Teclado | 150,00 | 3 | Periféricos | 2 | 5 | Ana | Curitiba |
| 1 | 12 | Mouse | 80,00 | 3 | Periféricos | 1 | 5 | Ana | Curitiba |
| 2 | 10 | Teclado | 150,00 | 3 | Periféricos | 1 | 8 | Carlos | São Paulo |

2. **Mapeamento em grupo** *(8 min)*
Cada grupo analisa a tabela e responde:
- Quais atributos têm dependência **total** da chave composta?
- Quais têm dependência **parcial** (dependem de só parte da chave)?
- Quais têm dependência **transitiva** (dependem de outro atributo não-chave)?

3. **Apresentação e correção** *(5 min)*
Os grupos compartilham suas respostas. O professor consolida o mapeamento correto.

**Gabarito esperado:**

| Atributo | Tipo de Dependência | Depende de |
|----------|---------------------|------------|
| `qtd` | Total | `id_pedido + id_produto` (chave completa) |
| `nome_produto` | Parcial | Só de `id_produto` |
| `preco_produto` | Parcial | Só de `id_produto` |
| `id_categoria` | Parcial | Só de `id_produto` |
| `nome_categoria` | Transitiva | De `id_categoria` → que depende de `id_produto` |
| `nome_cliente` | Parcial | Só de `id_cliente` → que depende de `id_pedido` |
| `cidade_cliente` | Transitiva | De `nome_cliente` → que depende de `id_cliente` |

> **Nota:** ao final da correção, o professor deve mostrar as anomalias concretas nessa tabela: *"O que acontece se o nome da categoria Periféricos mudar? Precisamos alterar quantas linhas?"* — reforçando a anomalia de atualização visualmente.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← Aula anterior | Aula 06 — 24/06/2026 · Modelo Físico — Restrições, Chaves e Design |
| Próxima aula → | Aula 08 — 08/07/2026 · Normalização — 1FN e 2FN |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com 20 slides
- Questionário impresso ou digital
- Folha A4 por grupo (para mapear as dependências na dinâmica)
- Quadro branco e marcador

---

## Observações do Professor
