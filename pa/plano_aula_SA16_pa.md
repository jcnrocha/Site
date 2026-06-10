# UC: Programação de Aplicativos
## SA 16 — 2º Trimestre

---

## Tema

Técnicas de Programação — Formatação e Documentação de Código

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Compreender a importância da formatação padronizada de código para legibilidade e manutenção
- Aplicar padrões de formatação: indentação, espaçamento, limite de linha e organização de blocos
- Utilizar ferramentas de formatação automática da IDE (Prettier, formatadores nativos) para manter o padrão
- Documentar código-fonte com comentários de linha, bloco e documentação formal (Javadoc / docstrings)
- Reconhecer a diferença entre comentário de explicação e comentário de documentação, aplicando cada um no contexto correto

**Capacidades da matriz:** 6.1 Formatação · 6.2 Documentação de código · Empregar comentários para documentação · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Retomada da SA 15: *"Encerramos o CRUD completo — a partir de agora entramos no bloco de técnicas de programação, que transforma código que funciona em código que funciona bem. Começamos com formatação e documentação"*

- **Por que formatação importa:**
  - Código é lido muito mais vezes do que é escrito — por outros desenvolvedores, por você mesmo semanas depois, por quem vai dar manutenção
  - Código mal formatado aumenta o tempo de leitura, dificulta a identificação de erros e cria conflitos desnecessários em repositórios de equipe
  - Empresas adotam guias de estilo obrigatórios: Google Java Style Guide, PEP 8 (Python), Airbnb JavaScript Style Guide
  - Formatação não é estética — é disciplina técnica

- **Padrões essenciais de formatação:**

  | Regra | Descrição | Exemplo correto |
  |-------|-----------|----------------|
  | **Indentação** | 2 ou 4 espaços por nível · nunca misturar espaços e tabs | Blocos internos sempre recuados |
  | **Chaves** | Abertura na mesma linha do comando · fechamento em linha própria | `if (cond) {` e `}` sozinho na linha |
  | **Espaçamento** | Espaço antes e depois de operadores · espaço após vírgula | `a + b` · `metodo(a, b)` |
  | **Limite de linha** | Máximo de 80 a 120 caracteres por linha | Linha longa: quebrar em múltiplas linhas |
  | **Linhas em branco** | Uma linha em branco entre métodos · duas entre classes | Separa visualmente os blocos lógicos |
  | **Nomenclatura** | camelCase para variáveis e métodos · PascalCase para classes | `calcularMedia()` · `class Aluno` |

- **Formatação automática com a IDE:**
  - **Prettier (VS Code):** formata automaticamente ao salvar · configurado na SA 04 · suporta Java, Python, JavaScript e outros
  - **Atalho manual:** `Shift+Alt+F` (Windows) ou `Shift+Option+F` (macOS) — formata o arquivo atual
  - **Configuração `editor.formatOnSave: true`:** garante formatação automática em todo salvamento
  - Ferramenta não substitui o entendimento das regras — o desenvolvedor precisa saber o padrão para revisar e corrigir quando necessário

- **Comentários de linha e de bloco:**
  - **Comentário de linha:** explica uma decisão específica · por que aquela abordagem foi escolhida · não repete o que o código já diz
  - **Comentário de bloco:** explica a lógica de uma seção mais complexa

  ```java
  // Divide por 8 para converter Mbps em MB/s
  double velocidadeMBs = velocidadeMbps / 8;

  /*
   * Percorre o vetor de trás para frente para evitar
   * reindexação ao remover elementos durante o laço
   */
  for (int i = lista.length - 1; i >= 0; i--) { ... }
  ```

  - **O que NÃO comentar:**
    ```java
    // Incrementa i em 1  ← comentário inútil — o código já diz isso
    i++;

    // Retorna a soma  ← inútil
    return a + b;
    ```

- **Documentação formal — Javadoc e docstrings:**
  - Comentários especiais que descrevem classes, métodos e parâmetros para geração automática de documentação
  - Ficam imediatamente antes da declaração da classe ou método

  ```java
  // Java — Javadoc
  /**
   * Calcula a média aritmética de duas notas.
   *
   * @param nota1 primeira nota (0.0 a 10.0)
   * @param nota2 segunda nota (0.0 a 10.0)
   * @return média das duas notas
   */
  public double calcularMedia(double nota1, double nota2) {
      return (nota1 + nota2) / 2;
  }
  ```

  ```python
  # Python — docstring
  def calcular_media(nota1: float, nota2: float) -> float:
      """
      Calcula a média aritmética de duas notas.

      Args:
          nota1: primeira nota (0.0 a 10.0)
          nota2: segunda nota (0.0 a 10.0)

      Returns:
          Média das duas notas.
      """
      return (nota1 + nota2) / 2
  ```

- **Tags Javadoc mais usadas:**

  | Tag | Uso |
  |-----|-----|
  | `@param` | Descreve um parâmetro do método |
  | `@return` | Descreve o valor retornado |
  | `@throws` | Descreve exceção que pode ser lançada |
  | `@author` | Autor da classe ou método |
  | `@version` | Versão do código |

- **Comentário vs Documentação — qual usar:**

  | Tipo | Onde usar | Quem lê |
  |------|-----------|---------|
  | Comentário de linha `//` | Dentro do método · lógica específica | Quem está lendo o código-fonte |
  | Comentário de bloco `/* */` | Seções complexas dentro do método | Quem está lendo o código-fonte |
  | Javadoc / docstring `/** */` | Antes de classes e métodos públicos | Quem usa a classe sem ver o código |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · contextualização do bloco de técnicas: *"Até aqui aprendemos a fazer o programa funcionar. A partir de agora aprendemos a fazer o programa funcionar bem — formatação, documentação, testes, depuração. Isso é o que separa o código amador do profissional"* |
| Retomada | Professor projeta dois trechos idênticos em lógica — um desformatado e sem comentários, outro bem formatado e documentado · pergunta: *"Qual deles você preferiria dar manutenção daqui a 6 meses?"* — resposta óbvia introduz o conteúdo naturalmente |
| Explicação | Slides — por que formatação importa, padrões essenciais, formatação automática com Prettier, comentários de linha e bloco (o que comentar e o que não comentar), Javadoc e docstrings com tags · demonstração ao vivo na IDE |
| Dinâmica | "Formata e Documenta" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: formatação é disciplina técnica, não estética · Prettier automatiza mas não substitui o conhecimento · comentário explica o porquê, não o quê · Javadoc documenta para quem usa a classe · Próxima SA: reutilização de código |

---

## Dinâmica — "Formata e Documenta"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** aplicar os padrões de formatação e documentação em um trecho de código real — desenvolvendo o hábito de revisar e melhorar código existente, habilidade central no trabalho diário de um desenvolvedor profissional.

**Materiais:** slide com o código desformatado e sem documentação projetado · ficha de reescrita impressa (1 por grupo) ou quadro branco.

**Passo a passo:**

1. **Apresentação do código** *(2 min)*
O professor projeta um trecho de código funcional mas completamente desformatado e sem nenhum comentário. O grupo deve: formatar o código seguindo os padrões · adicionar comentários onde fizer sentido · adicionar Javadoc ou docstring ao método.

2. **Reescrita em grupo** *(8 min)*
Os grupos reescrevem o código na ficha aplicando as melhorias de formatação e documentação.

3. **Comparação e debate** *(5 min)*
Os grupos apresentam suas versões. O professor compara as diferentes abordagens de comentário e discute: *"Algum grupo comentou algo que não precisava ser comentado? Algum grupo deixou de comentar algo importante?"*

**Código para formatar e documentar:**

```java
// Versão desformatada — sem padrão, sem documentação
public double calc(double a,double b,double c){
double s=(a+b+c)/3;
if(s>=7.0){System.out.println("aprovado");}
else if(s>=5.0){System.out.println("recuperacao");}
else{System.out.println("reprovado");}
return s;}
```

**Resultado esperado após formatação e documentação:**

```java
/**
 * Calcula a média de três notas e exibe a situação do aluno.
 *
 * @param nota1 primeira nota (0.0 a 10.0)
 * @param nota2 segunda nota (0.0 a 10.0)
 * @param nota3 terceira nota (0.0 a 10.0)
 * @return média aritmética das três notas
 */
public double calcularMedia(double nota1, double nota2, double nota3) {
    double media = (nota1 + nota2 + nota3) / 3;

    // Exibe situação conforme critério: >= 7 aprovado, >= 5 recuperação
    if (media >= 7.0) {
        System.out.println("Aprovado");
    } else if (media >= 5.0) {
        System.out.println("Recuperação");
    } else {
        System.out.println("Reprovado");
    }

    return media;
}
```

> **Nota:** reforçar que renomear `calc` para `calcularMedia` e `a`, `b`, `c` para `nota1`, `nota2`, `nota3` também faz parte da formatação — nomes descritivos são a forma mais valiosa de documentação. Código que se explica pelo nome precisa de muito menos comentário.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 15 — 27/05/2026 · Conexão com Banco de Dados — CRUD Parte 2 |
| Próxima SA → | SA 17 — 10/06/2026 · Técnicas de Programação — Reutilização de Código |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores da sala com VS Code e Prettier configurados
- Ficha de reescrita da dinâmica impressa (1 por grupo) ou quadro branco
- Quadro branco e marcador

---

## Observações do Professor
