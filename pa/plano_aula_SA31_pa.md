# UC: Programação de Aplicativos
## SA 31 — 3º Trimestre

---

## Tema

Consolidação — POO e Conexão com Banco de Dados

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Revisar e consolidar os pilares da orientação a objetos: classes, objetos, encapsulamento, herança e polimorfismo
- Aplicar POO em um sistema com múltiplas classes relacionadas, com foco em qualidade e boas práticas
- Revisar as operações CRUD completas integradas com uma hierarquia de classes
- Refatorar código com foco em DRY, encapsulamento e documentação
- Preparar a base técnica necessária para o desenvolvimento do Projeto Final

**Capacidades da matriz:** Bloco 4 e 5 da matriz · Aplicar linguagem de programação por meio da IDE · Integrar banco de dados por meio da linguagem de programação · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Contextualização da SA: *"Na SA passada revisamos ambiente e programação estruturada — hoje consolidamos os dois blocos mais pesados da UC: orientação a objetos e banco de dados juntos"*

- **Revisão — Orientação a Objetos (SAs 08, 09 e 12):**

  | Tema | Pontos-chave para revisar |
  |------|--------------------------|
  | Classe e objeto | Classe é o molde · objeto é a instância · `new` instancia · construtor inicializa |
  | Encapsulamento | `private` protege · getter lê · setter escreve com validação · `this` referencia o objeto atual |
  | Herança | `extends` herda · `super` acessa o pai · `@Override` redefine comportamento |
  | Polimorfismo | Referência pai aponta para objeto filho · lista polimórfica · método chamado é do objeto real |
  | Classes abstratas | Não instanciável · método abstrato obriga filhas a implementar |
  | Interfaces | Contrato de capacidades · `implements` · herança múltipla de contratos |

- **Revisão — Conexão com Banco de Dados (SAs 13 a 15):**

  | Tema | Pontos-chave para revisar |
  |------|--------------------------|
  | Conexão | Driver/conector · host, porta, banco, usuário, senha · `Connection` |
  | SELECT | `executeQuery()` · `ResultSet` · percorrimento com `while(rs.next())` |
  | INSERT | `executeUpdate()` · Prepared Statement · `commit()` |
  | UPDATE | `executeUpdate()` · WHERE obrigatório · verificar `rowcount` |
  | DELETE | `executeUpdate()` · WHERE obrigatório · operação irreversível |
  | Transações | `setAutoCommit(false)` · `commit()` · `rollback()` · `finally` fecha conexão |

- **Sistema prático de consolidação — Cadastro de Funcionários com BD:**
  - Projeto que integra POO + CRUD em um único sistema coeso
  - Estrutura de classes:

  ```
  Pessoa (abstrata)
  ├── nome (private) · cpf (private)
  ├── construtor(nome, cpf)
  └── exibirDados() — abstrato

  Funcionario extends Pessoa
  ├── cargo (private) · salario (private)
  ├── construtor(nome, cpf, cargo, salario)
  ├── exibirDados() — @Override
  └── calcularBonus() — retorna 10% do salário

  FuncionarioBD (classe de acesso ao banco)
  ├── inserir(Funcionario f)
  ├── buscarTodos() → List<Funcionario>
  ├── buscarPorNome(String nome) → Funcionario
  ├── atualizar(Funcionario f)
  └── remover(int id)
  ```

  - O sistema principal:
    1. Cria objetos `Funcionario` com construtor
    2. Insere no banco via `FuncionarioBD.inserir()`
    3. Busca todos e percorre com `for` chamando `exibirDados()` — polimorfismo em ação
    4. Atualiza salário de um funcionário específico
    5. Remove um funcionário pelo ID

- **Refatoração integrada — qualidade no sistema de consolidação:**
  - Aplicar DRY: método de abertura de conexão centralizado em uma classe `ConexaoDB`
  - Aplicar encapsulamento: nenhum atributo acessado diretamente fora da classe
  - Aplicar documentação: Javadoc/docstring em todos os métodos públicos
  - Aplicar tratamento de erro: try/catch/finally em todos os métodos de BD
  - Commitar cada etapa com mensagem descritiva no repositório

- **Erros frequentes a revisar e corrigir:**

  | Erro | Causa | Correção |
  |------|-------|----------|
  | `NullPointerException` ao chamar método | Objeto não instanciado com `new` | Verificar criação do objeto antes do uso |
  | UPDATE sem WHERE | Esquecimento da cláusula | Sempre incluir WHERE com ID ou condição específica |
  | Atributo `private` acessado diretamente | Encapsulamento violado | Usar getter/setter correspondente |
  | Conexão não fechada no `finally` | Vazamento de recurso | Sempre fechar em bloco `finally` ou try-with-resources |
  | `@Override` com assinatura errada | Parâmetro ou tipo diferente do método pai | Conferir assinatura idêntica ao método da classe pai |

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · retomada da SA 30: *"Ambiente e estruturado revisados — hoje consolidamos POO e banco de dados: os dois blocos que formam o coração do Projeto Final"* |
| Retomada | Professor projeta a estrutura de classes do sistema de consolidação e pergunta: *"Quem consegue dizer, olhando para isso, onde está o encapsulamento, a herança e o polimorfismo?"* — alunos identificam ao vivo |
| Revisão dirigida | Revisão rápida dos pontos de maior dúvida: `@Override` e polimorfismo · transações com rollback · Prepared Statement · erros frequentes |
| Prática | Alunos implementam o sistema de Cadastro de Funcionários na IDE · professor orienta e revisa ao vivo · foco em qualidade integrada: DRY, encapsulamento, documentação e commits |
| Dinâmica | "Liga o Conceito ao Código" — ver seção abaixo |
| Questionário | 5 questões objetivas + 5 questões discursivas sobre o conteúdo da SA |
| Fechamento | Resumo: POO organiza · banco persiste · os dois juntos formam qualquer sistema real · refatoração com DRY + encapsulamento + documentação é a marca do profissional · Próxima SA: consolidação de técnicas de programação e testes |

---

## Dinâmica — "Liga o Conceito ao Código"

**Duração:** 15 minutos · **Agrupamento:** grupos de 4 a 5 alunos

**Objetivo:** consolidar POO e CRUD por meio da identificação de conceitos em trechos de código reais — desenvolvendo a leitura técnica precisa que será necessária no Projeto Final e em revisões de código no mercado de trabalho.

**Materiais:** slide com os trechos de código projetados · ficha de identificação impressa (1 por grupo).

**Passo a passo:**

1. **Apresentação do trecho** *(1 min por rodada)*
O professor projeta um trecho de código. O grupo deve identificar: qual conceito está sendo demonstrado · se está correto ou tem problema · e o que melhoraria.

2. **Análise em grupo** *(8 min)*
Os grupos analisam cada trecho e preenchem a ficha com: conceito identificado, avaliação (correto/problema) e sugestão de melhoria quando necessário.

3. **Debate coletivo** *(6 min)*
O professor revela as respostas e discute as sugestões de melhoria apresentadas pelos grupos.

**Trechos para analisar:**

| Trecho | Conceito | Avaliação |
|--------|----------|-----------|
| `Pessoa p = new Funcionario("Ana", "123", "Dev", 5000)` | Polimorfismo — referência pai para objeto filho | Correto |
| `public String nome;` dentro de uma classe | Encapsulamento violado — atributo público | Problema — deve ser `private` com getter/setter |
| `UPDATE funcionarios SET salario = 6000` sem WHERE | CRUD — UPDATE sem condição | Problema crítico — atualiza todos os registros |
| `@Override public void exibirDados(String extra)` diferente do pai | Herança — tentativa de @Override com assinatura diferente | Problema — não é Override válido, é sobrecarga |
| `finally { conexao.close(); }` após try/catch | Boas práticas de CRUD — fechamento de conexão | Correto |
| Método com 60 linhas fazendo conexão + CRUD + exibição | DRY e responsabilidade única | Problema — deve ser dividido em métodos separados |

> **Nota:** reforçar que identificar conceitos em código alheio é uma habilidade cotidiana do desenvolvedor — em revisões de código (code review), em manutenção de sistemas legados e em entrevistas técnicas. Quem consegue ler código com precisão técnica e apontar melhorias com clareza é um profissional muito valorizado em qualquer equipe.

---

## Avaliação

- 5 questões objetivas — nível alto · 4 alternativas: A) B) C) D) · Gabarito alternado, sem repetição consecutiva
- 5 questões discursivas — cada uma com título explicativo antes do enunciado · Sem linhas, apenas espaço em branco com `R:`
- Gabarito em página separada — uso exclusivo do professor · Objetivas: letra correta + justificativa · Discursivas: resposta esperada com critérios de correção

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 30 — 23/09/2026 · Consolidação — Ambiente, Ferramentas e Programação Estruturada |
| Próxima SA → | SA 32 — 07/10/2026 · Consolidação — Técnicas de Programação e Testes |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Apresentação com slides
- Questionário impresso ou digital
- Computadores com VS Code, SGBD e GitHub configurados
- Projeto base do sistema de Cadastro de Funcionários preparado para a prática
- Ficha de identificação da dinâmica impressa (1 por grupo)
- Quadro branco e marcador

---

## Observações do Professor
