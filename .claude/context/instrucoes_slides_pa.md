# Instruções — slides_SA_pa.html
**UC:** Programação de Aplicativos · Colégio Neiva Pavan · Prof. Julio Cesar  
**Cor principal:** #1A7A4A (verde terminal)  
**Framework:** Reveal.js 4.6.1 · 1280×720px

---

## REGRAS GERAIS — NUNCA VIOLAR

- Todo conteúdo DEVE caber dentro do frame de **1280×720px**
- `font-size` nunca abaixo de **0.36em**
- Máximo **4 cards** por slide
- Máximo **5 flow-steps** por slide
- Máximo **10 linhas** de código por code-block
- Se o conteúdo não couber: **dividir em 2 slides**
- Total de slides: **mínimo 16, máximo 20**
- Slides de código: **apenas quando o plano de aula trouxer exemplo de código**

---

## ESTRUTURA FIXA DOS 16 SLIDES

### SLIDE 01 — CAPA
- Classe: `slide-capa` · Transição: `zoom`
- Kicker: `SA XX · Nº Trimestre · Programação de Aplicativos`
- Título: tema principal `<br><span>subtítulo em destaque</span>`
- Descrição: 1 ou 2 linhas resumindo o tema
- Badges obrigatórios: data · módulo/bloco · Prof. Julio Cesar · Colégio Neiva Pavan · 2º Ano — TDS

---

### SLIDE 02 — OBJETIVOS
- Label: `O que você vai aprender hoje`
- Título: `🏆 Objetivos da Aula`
- Componente: `bullet-list` com **exatamente 5 itens**
- Cada item: `<strong>nome do objetivo:</strong> descrição`
- Fonte: retirar diretamente da seção "Objetivos de Aprendizagem" do plano de aula

---

### SLIDE 03 — PERCURSO
- Label: `De onde viemos e para onde vamos`
- Título: `🔗 Nosso <span>Percurso</span> até aqui`
- `highlight-box` conectando SA anterior com a de hoje (2 linhas máx)
- `cards-grid cards-3` com 3 cards:
  - Card 1: `accent-orange` · SA anterior
  - Card 2: `accent-pa` · SA hoje (destaque)
  - Card 3: `accent-green` · SA próxima

---

### SLIDES 04 ao 14 — CONTEÚDO (11 slides)

Distribuir o conteúdo do plano de aula nos 11 slides usando os tipos abaixo:

#### TIPO A — Conceito Teórico
**Use quando:** introduzir um conceito, definição ou teoria  
**Estrutura:**
1. `highlight-box` — definição/contexto (2 linhas máx)
2. `cards-grid cards-2` — 2 cards explorando o conceito
3. `highlight-box-y` — dica prática ou reforço (1 linha)

#### TIPO B — Exemplo Prático com Código
**Use quando:** mostrar código antes × depois, demonstração prática  
**Estrutura:**
1. `highlight-box-r` — explicação do problema
2. `comp-grid` com 2 `comp-col`:
   - `comp-evit` + `code-block` — código problemático (máx 8 linhas)
   - `comp-faz` + `code-block` — código correto (máx 8 linhas)
3. `highlight-box` — conclusão do que mudou

#### TIPO C — Passo a Passo
**Use quando:** sequência de etapas, processo, fluxo de trabalho  
**Estrutura:**
1. `highlight-box` — contexto do processo (1 linha)
2. `exemplo-flow` com **máx 5** `flow-step`
   - Cores: fs-p · fs-y · fs-g · fs-o · fs-b (nessa ordem)
   - Cada step: `<strong>Passo X</strong> — descrição máx 2 linhas`

#### TIPO D — Comparativo
**Use quando:** certo × errado, vantagem × desvantagem, antes × depois sem código  
**Estrutura:**
1. `comp-grid` com 2 colunas:
   - `comp-evit` — o que evitar (máx 5 comp-item)
   - `comp-faz` — o que fazer (máx 5 comp-item)
2. `highlight-box` — conclusão (1 linha)

#### TIPO E — Tabela
**Use quando:** resumo, referência rápida, múltiplos itens com atributos  
**Estrutura:**
1. `data-table` com 3 colunas e **máx 6 linhas**
2. Usar tags coloridas nas células: `tag-r` `tag-g` `tag-b` `tag-y`
3. `highlight-box` — mensagem de reforço (1 linha)

---

### SLIDE 13 — DINÂMICA (apresentação)
- Label: `Atividade prática em grupo`
- Título: `🎮 Dinâmica — <span>[Nome]</span>`
- `din-header` com nome e duração
- `exemplo-flow` com **3 steps obrigatórios**:
  - `fs-p` — Apresentação (tempo)
  - `fs-y` — Execução em grupo (tempo)
  - `fs-g` — Correção ao vivo (tempo)
- `highlight-box-y` — itens práticos que os grupos vão trabalhar

---

### SLIDE 14 — DINÂMICA (tabela de casos)
- Label: `[Nome da Dinâmica] · casos práticos`
- Título: `📋 Casos para <span>Analisar</span>`
- `data-table` com 3 colunas e **máx 5 linhas** (os casos da dinâmica)
- `highlight-box` — reforço pedagógico (1 linha)

---

### SLIDE 15 — RESUMO
- Label: `O que vimos hoje`
- Título: `📌 Resumo da Aula`
- `cards-grid cards-2` com **exatamente 4 cards**
  - Um card para cada bloco principal do conteúdo da aula
  - Cores: accent-pa · accent-yellow · accent-orange · accent-red
- `highlight-box` — mensagem central e lição mais importante da aula

---

### SLIDE 16 — ENCERRAMENTO
- Classe: `slide-enc` · Transição: `zoom`
- Label: `Até a próxima`
- Título: `🚀 O que <span>vem a seguir</span>`
- `enc-grid` com 2 cards:
  - `enc-prox` — próxima SA: número, data e tema
  - `enc-rev` — para fixar: 3 ações práticas do aluno
- `quote-box` — frase inspiracional relacionada ao tema
- Rodapé: `SA XX · Tema · Prof. Julio Cesar · Colégio Neiva Pavan · 2026`

---

## TIPOS DE SLIDE POR CONTEÚDO COMUM

| Conteúdo do plano de aula | Tipo de slide |
|---|---|
| Definição, conceito, o que é | Tipo A |
| Código antes × depois | Tipo B |
| Como fazer, etapas, processo | Tipo C |
| Certo × errado, comparativo | Tipo D |
| Tabela resumo, referência | Tipo E |
| Gargalos com código | Tipo B |
| Boas práticas | Tipo D |
| Ferramentas, recursos | Tipo A ou E |

---

## PROMPT PARA USAR NO VS CODE

```
Leia .claude/context/template_slides_pa.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_pa.md para as regras de cada slide.
Leia pa/plano_aula_SA[XX]_pa.html para o conteúdo da aula.
Crie pa/slides_SA[XX]_pa.html seguindo exatamente a estrutura
e regras dos arquivos de referência.
```
