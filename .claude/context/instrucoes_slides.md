# Instruções Universais — slides_SA_[uc].html
**Escola:** Colégio Neiva Pavan · Prof. Julio Cesar  
**Framework:** Reveal.js 4.6.1 · 1280×720px  
**A UC, cor principal e ano serão informados no prompt**

---

## REGRAS GERAIS — NUNCA VIOLAR

- Todo conteúdo DEVE caber dentro do frame de **1280×720px**
- `font-size` nunca abaixo de **0.36em**
- Máximo **4 cards** por slide
- Máximo **5 flow-steps** por slide
- Máximo **10 linhas** de código por code-block
- Se o conteúdo não couber: **dividir em 2 slides**
- Total de slides: **sem limite máximo** — use quantos forem necessários para explicar o conteúdo com profundidade e exemplos. A estrutura fixa abaixo (capa, objetivos, percurso, dinâmica, resumo, encerramento) é obrigatória; os slides de conteúdo podem ser expandidos livremente.
- Slides de código: **apenas quando o plano de aula trouxer exemplo de código**
- **Nunca incluir datas** (dia/mês/ano) em nenhum slide — nem na capa, nem nos cards de percurso, nem no encerramento, nem no rodapé. Usar somente o número da SA (ex: `SA 14`). Isso permite reaproveitar o mesmo slide em outras turmas/anos sem precisar editar.
- **Caixa final de cada slide (`highlight-box`, `highlight-box-y`, `highlight-box-r` de fechamento — destaque, dica, conclusão, atenção)** deve ficar sempre no rodapé do slide, com o conteúdo principal (tabela/cards/código) colado logo abaixo do título, nunca flutuando no meio. A técnica certa depende do que vem antes da caixa:
  - Se o elemento anterior for **`cards-grid`, `comp-grid` ou `exemplo-flow`** (esses três já têm `flex:1 1 auto` no CSS, então crescem por conta própria): a caixa final usa só `style="margin-top:auto;"`, sem espaçador extra. **Nunca** adicionar um spacer aqui — ele competiria com o crescimento do próprio grid e voltaria a abrir vazio no meio do slide.
  - Se o elemento anterior for **`<table class="data-table">` ou `.code-block`** (nenhum dos dois cresce por padrão): inserir um espaçador explícito `<div style="flex:1 1 auto;"></div>` IMEDIATAMENTE depois do elemento e antes da caixa final, e a caixa final NÃO leva `margin-top:auto` (fica com a classe pura, sem style inline). É esse espaçador vazio que absorve o espaço sobrando e empurra a caixa para o rodapé — usar `margin-top:auto` direto na caixa nesse caso resulta em distribuição inconsistente do espaço (gera vazio tanto antes quanto depois da tabela).
  - Nunca usar valor fixo em `px` (ex: `margin-top:6px`) para esse espaçamento — sempre uma das duas técnicas acima.
  - Caixas de introdução/contexto no topo do slide (antes de cards, tabelas ou código) continuam coladas ao título, sem `margin-top:auto` e sem espaçador.
- A cor principal da UC sempre é referenciada como `var(--pa)` no CSS do template

---

## ESTRUTURA DOS SLIDES — POSIÇÕES, NÃO NÚMEROS FIXOS

**Atenção:** desde que o limite de slides foi removido, NUNCA numerar estas seções como "SLIDE 01", "SLIDE 16" etc. — a posição exata de cada bloco varia conforme a quantidade de conteúdo. As referências corretas são:

- **1º slide** → Capa
- **2º slide** → Objetivos
- **3º slide** → Percurso
- **Slides seguintes, em quantidade livre** → Conteúdo (tipos A a E, conforme o plano de aula)
- Depois do conteúdo → Dinâmica (apresentação + tabela de casos, 2 slides)
- **Penúltimo slide, sempre** → Resumo
- **Último slide, sempre** → Encerramento (independente de ser o 16º, o 18º ou o 23º slide da apresentação)

### 1º SLIDE — CAPA
- Classe: `slide-capa` · Transição: `zoom` · Velocidade: `slow`
- Kicker: `SA XX · [Nº] Trimestre · [Nome da UC]`
- Título: tema principal `<br><span>subtítulo em destaque</span>`
- Descrição: 1 ou 2 linhas resumindo o tema da aula
- Badges obrigatórios:
  - `cb-pa` → SA XX (sem data)
  - `cb-yellow` → módulo ou bloco do conteúdo
  - `cb-dark` → Prof. Julio Cesar
  - `cb-dark` → Colégio Neiva Pavan
  - `cb-dark` → [Nº] Ano — TDS
- **Botão de Tela Cheia** (obrigatório, só no slide 01):
  - `<button id="btn-fullscreen" onclick="toggleFullscreen()" aria-label="Ativar tela cheia">⛶ Tela Cheia</button>` posicionado dentro de `.slide-capa`, antes de `.capa-deco`
  - CSS: `position:absolute; top:20px; right:24px; z-index:20;` com fundo translúcido, hover em `var(--pa)`, oculto em `@media print`
  - Função JS `toggleFullscreen()` chama `document.documentElement.requestFullscreen()` / `exitFullscreen()` — funciona como o modo de apresentação do PowerPoint (oculta a interface do navegador, navegação por seta/espaço já nativa do Reveal, Esc sai)
  - Comportamento aplica-se a toda a apresentação, não só ao slide 01, pois o fullscreen é do `document.documentElement`

---

### 2º SLIDE — OBJETIVOS
- Transição: `fade`
- Label: `O que você vai aprender hoje`
- Título: `🏆 Objetivos da Aula`
- Componente: `bullet-list` com **exatamente 5 itens**
- Cada item: `<strong>nome do objetivo:</strong> descrição`
- Fonte: retirar diretamente da seção "Objetivos de Aprendizagem" do plano de aula

---

### 3º SLIDE — PERCURSO
- Transição: `slide`
- Label: `De onde viemos e para onde vamos`
- Título: `🔗 Nosso <span>Percurso</span> até aqui`
- `highlight-box` conectando SA anterior com a de hoje (2 linhas máx)
- `cards-grid cards-3` com 3 cards:
  - Card 1: `accent-orange` · SA anterior — tema e resumo
  - Card 2: `accent-pa` · SA hoje — tema e destaque (cor da UC)
  - Card 3: `accent-green` · SA próxima — gancho para a próxima aula

---

### SLIDES DE CONTEÚDO — quantidade livre, entre o Percurso e a Dinâmica

Distribuir o conteúdo do plano de aula em quantos slides forem necessários para explicar com profundidade e exemplos — sem limite máximo.
Escolher o tipo correto para cada slide conforme o conteúdo:

---

#### TIPO A — Conceito Teórico
**Transição:** `convex`  
**Use quando:** introduzir um conceito, definição ou teoria  
**Estrutura:**
1. `highlight-box` — definição/contexto (2 linhas máx)
2. `cards-grid cards-2` — 2 cards explorando o conceito
3. `highlight-box-y` — dica prática ou reforço (1 linha)

---

#### TIPO B — Exemplo Prático com Código
**Transição:** `fade`  
**Use quando:** mostrar código antes × depois, demonstração prática  
**Estrutura:**
1. `highlight-box-r` — explicação do problema (por que é ruim)
2. `comp-grid` com 2 `comp-col`:
   - `comp-evit` + `code-block` — código problemático (máx 8 linhas)
   - `comp-faz` + `code-block` — código correto (máx 8 linhas)
3. `highlight-box` — conclusão do que mudou e por que é melhor

---

#### TIPO C — Passo a Passo
**Transição:** `slide`  
**Use quando:** sequência de etapas, processo, fluxo de trabalho  
**Estrutura:**
1. `highlight-box` — contexto do processo (1 linha)
2. `exemplo-flow` com **máx 5** `flow-step`
   - Cores em ordem: `fs-p` · `fs-y` · `fs-g` · `fs-o` · `fs-b`
   - Cada step: `<strong>Passo X</strong> — descrição máx 2 linhas`

---

#### TIPO D — Comparativo
**Transição:** `convex`  
**Use quando:** certo × errado, vantagem × desvantagem, antes × depois sem código  
**Estrutura:**
1. `comp-grid` com 2 colunas:
   - `comp-evit` — o que evitar (máx 5 `comp-item`)
   - `comp-faz` — o que fazer (máx 5 `comp-item`)
2. `highlight-box` — conclusão (1 linha)

---

#### TIPO E — Tabela
**Transição:** `slide`  
**Use quando:** resumo, referência rápida, múltiplos itens com atributos  
**Estrutura:**
1. `data-table` com 3 colunas e **máx 6 linhas**
2. Usar tags coloridas nas células: `tag-r` `tag-g` `tag-b` `tag-y`
3. `highlight-box` — mensagem de reforço (1 linha)

---

### DINÂMICA (apresentação) — logo após os slides de conteúdo
- Transição: `zoom`
- Label: `Atividade prática em grupo`
- Título: `🎮 Dinâmica — <span>[Nome da Dinâmica]</span>`
- `din-header` com nome e duração total
- `exemplo-flow` com **exatamente 3 steps**:
  - `fs-p` — Apresentação: o que o professor projeta/explica
  - `fs-y` — Execução em grupo: tarefa principal dos alunos
  - `fs-g` — Correção ao vivo: como o professor fecha a atividade
- `highlight-box-y` — lista dos itens/casos que os grupos vão trabalhar

---

### DINÂMICA (tabela de casos) — imediatamente depois da Dinâmica (apresentação)
- Transição: `convex`
- Label: `[Nome da Dinâmica] · casos práticos`
- Título: `📋 Casos para <span>Analisar</span>`
- `data-table` com 3 colunas e **máx 5 linhas**
- `highlight-box` — reforço pedagógico (1 linha)

---

### RESUMO — penúltimo slide, sempre
- Transição: `fade`
- Label: `O que vimos hoje`
- Título: `📌 Resumo da Aula`
- `cards-grid cards-2` com **exatamente 4 cards**
  - Um card por bloco principal do conteúdo
  - Cores em ordem: `accent-pa` · `accent-yellow` · `accent-orange` · `accent-red`
- `highlight-box` — mensagem central e lição mais importante da aula

---

### ENCERRAMENTO — último slide, sempre (não tem número fixo)
- Classe: `slide-enc` · Transição: `zoom`
- Label: `Até a próxima`
- Título: `🚀 O que <span>vem a seguir</span>`
- `enc-grid` com 2 cards:
  - `enc-prox` — próxima SA: número e tema (sem data)
  - `enc-rev` — para fixar: 3 ações práticas do aluno
  - CSS: `.enc-grid { flex:1 1 auto; align-content:stretch; }` e `.enc-card { padding:16px 20px; display:flex; flex-direction:column; }` — os cards crescem para preencher o espaço vertical do slide, em vez de ficarem pequenos no topo
- `quote-box` — frase inspiracional relacionada ao tema da aula. Fica com altura natural (sem flex-grow), posicionada logo abaixo dos cards grandes, próxima ao rodapé
- Rodapé centralizado: `SA XX · [Tema] · Prof. Julio Cesar` — **sem nome da escola e sem ano/data**

---

## TABELA DE TIPOS POR CONTEÚDO

| Conteúdo do plano de aula | Tipo de slide | Transição |
|---|---|---|
| Definição, conceito, o que é | Tipo A | convex |
| Código antes × depois | Tipo B | fade |
| Como fazer, etapas, processo | Tipo C | slide |
| Certo × errado, comparativo | Tipo D | convex |
| Tabela resumo, referência | Tipo E | slide |
| Gargalos com código | Tipo B | fade |
| Boas práticas | Tipo D | convex |
| Ferramentas, recursos | Tipo A ou E | convex ou slide |
| Sintaxe de linguagem | Tipo B ou E | fade ou slide |
| Diagrama conceitual | Tipo C | slide |
| Normas, regras, legislação | Tipo E | slide |
| Protocolo, modelo de rede | Tipo C ou E | slide |

---

## MAPEAMENTO DE UCs E TEMPLATES

| UC | Template | Ano |
|---|---|---|
| Programação de Aplicativos | `template_slides_pa.html` | 2º Ano |
| Fundamentos de TI | `template_slides_fti.html` | 2º Ano |
| Fundamentos de Banco de Dados | `template_slides_bd.html` | 2º Ano |
| Fundamentos de Redes | `template_slides_redes.html` | 2º Ano |
| Qualidade, Produtividade e Sustentabilidade | `template_slides_qps.html` | 1º Ano |
| Desenvolvimento de Projetos + SST | `template_slides_sst.html` | 1º Ano |

---

## CONFIGURAÇÃO DO Reveal.initialize — TELA CHEIA PREENCHENDO TUDO

Para que o slide ocupe 100% da tela ao ativar o botão de Tela Cheia (e não fique limitado ao tamanho nativo 1280×720 num monitor maior):

```js
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}

Reveal.initialize({
  hash: true,
  slideNumber: 'c/t',
  progress: true,
  controls: true,
  controlsTutorial: true,
  transition: 'convex',
  transitionSpeed: 'fast',
  backgroundTransition: 'fade',
  center: true,
  width: 1280,
  height: 720,
  margin: 0.04,
  minScale: 0.2,
  maxScale: 3.0,
  plugins: []
});

document.addEventListener('fullscreenchange', () => Reveal.layout());
```

- `maxScale: 3.0` (em vez de `1.0`) permite que o deck amplie além do tamanho nativo até preencher monitores grandes.
- O listener de `fullscreenchange` força `Reveal.layout()` a recalcular o tamanho exatamente no instante em que a tela cheia é ativada/desativada — sem ele, o recálculo só ocorre no resize da janela.

---

## PROMPT UNIVERSAL PARA O VS CODE

```
Leia .claude/context/template_slides_[uc].html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia [uc]/plano_aula_SA[XX]_[uc].html para o conteúdo da aula.
Crie [uc]/slides_SA[XX]_[uc].html.

UC: [Nome completo da UC]
Ano: [1º ou 2º] Ano — TDS
```

---

## EXEMPLOS DE PROMPT POR UC

**Programação de Aplicativos:**
```
Leia .claude/context/template_slides_pa.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia pa/plano_aula_SA19_pa.html para o conteúdo da aula.
Crie pa/slides_SA19_pa.html.
UC: Programação de Aplicativos · 2º Ano — TDS
```

**Fundamentos de TI:**
```
Leia .claude/context/template_slides_fti.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia fti/plano_aula_SA19_fti.html para o conteúdo da aula.
Crie fti/slides_SA19_fti.html.
UC: Fundamentos de Tecnologias da Informação · 2º Ano — TDS
```

**Banco de Dados:**
```
Leia .claude/context/template_slides_bd.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia bd/plano_aula_SA19_bd.html para o conteúdo da aula.
Crie bd/slides_SA19_bd.html.
UC: Fundamentos de Banco de Dados · 2º Ano — TDS
```

**Redes:**
```
Leia .claude/context/template_slides_redes.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia redes/plano_aula_SA19_redes.html para o conteúdo da aula.
Crie redes/slides_SA19_redes.html.
UC: Fundamentos de Redes de Computadores · 2º Ano — TDS
```

**QPS:**
```
Leia .claude/context/template_slides_qps.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia qps/plano_aula_SA19_qps.html para o conteúdo da aula.
Crie qps/slides_SA19_qps.html.
UC: Qualidade, Produtividade e Sustentabilidade · 1º Ano — TDS
```

**SST:**
```
Leia .claude/context/template_slides_sst.html para o CSS, cores e estrutura.
Leia .claude/context/instrucoes_slides_UNIVERSAL.md para as regras de cada slide.
Leia sst/plano_aula_SA19_sst.html para o conteúdo da aula.
Crie sst/slides_SA19_sst.html.
UC: Desenvolvimento de Projetos + SST · 1º Ano — TDS
```
