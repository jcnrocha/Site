# UC: Programação de Aplicativos
## SA 34 — 3º Trimestre

---

## Tema

Projeto Final — Desenvolvimento Parte 1

---

## Objetivos de Aprendizagem

Ao final da SA, o aluno será capaz de:

- Estruturar o projeto na IDE com organização de pastas e pacotes adequada
- Modelar as classes do sistema aplicando herança, encapsulamento e construtores
- Criar e configurar o banco de dados com as tabelas necessárias para o sistema
- Implementar os primeiros módulos do aplicativo com qualidade técnica desde o início
- Realizar commits descritivos ao longo do desenvolvimento, mantendo o histórico rastreável

**Capacidades da matriz:** Integração de todas as capacidades da UC · Aplicar linguagem de programação por meio da IDE · Integrar banco de dados por meio da linguagem de programação · Aplicar métodos e técnicas de programação

---

## Conteúdo

- Contextualização: *"O briefing foi feito, os grupos estão formados e os temas definidos — hoje o sistema começa a existir. Foco em estrutura sólida desde o primeiro commit"*

- **O que deve ser entregue ao final desta SA:**

  | Entregável | Descrição |
  |------------|-----------|
  | Estrutura do projeto | Pastas organizadas · pacotes definidos · README atualizado |
  | Modelagem de classes | Ao menos 3 classes com herança e encapsulamento completo |
  | Banco de dados | Script SQL de criação das tabelas · banco rodando localmente |
  | Primeiros módulos | Ao menos a classe de conexão + INSERT + SELECT funcionando |
  | Repositório | Ao menos 3 commits descritivos com o progresso da SA |

- **Estrutura recomendada para o projeto:**

  ```
  sistema-nome-do-projeto/
  ├── src/
  │   ├── model/          → classes de entidade (Pessoa, Cliente, Produto...)
  │   ├── dao/            → classes de acesso ao banco (ClienteDAO, ProdutoDAO...)
  │   ├── service/        → regras de negócio
  │   └── util/           → classes utilitárias (ConexaoDB, ValidadorUtils...)
  ├── test/               → testes unitários
  ├── sql/
  │   └── schema.sql      → script de criação do banco
  └── README.md           → descrição do sistema, integrantes, como rodar
  ```

- **Modelagem de classes — checklist:**
  - [ ] Classe pai abstrata com atributos comuns e método abstrato
  - [ ] Ao menos duas classes filhas com `@Override` nos métodos abstratos
  - [ ] Todos os atributos `private` com getters e setters com validação
  - [ ] Construtores em todas as classes
  - [ ] Javadoc/docstring em todos os métodos públicos

- **Banco de dados — checklist:**
  - [ ] Script SQL salvo em `sql/schema.sql` e commitado
  - [ ] Tabelas criadas com tipos de dados corretos
  - [ ] Chaves primárias definidas (`PRIMARY KEY AUTO_INCREMENT`)
  - [ ] Chaves estrangeiras definidas quando houver relacionamento entre tabelas
  - [ ] Classe `ConexaoDB` criada com método estático que retorna a conexão

- **Classe DAO — padrão de acesso ao banco:**
  - DAO (Data Access Object): classe responsável por todas as operações de banco para uma entidade específica
  - Separa a lógica de negócio da lógica de acesso ao banco — princípio de responsabilidade única

  ```java
  // Exemplo de estrutura de uma classe DAO
  public class ClienteDAO {

      /**
       * Insere um novo cliente no banco de dados.
       * @param cliente objeto Cliente a ser inserido
       */
      public void inserir(Cliente cliente) {
          String sql = "INSERT INTO clientes (nome, email) VALUES (?, ?)";
          try (PreparedStatement ps = ConexaoDB.getConexao().prepareStatement(sql)) {
              ps.setString(1, cliente.getNome());
              ps.setString(2, cliente.getEmail());
              ps.executeUpdate();
          } catch (SQLException e) {
              System.err.println("Erro ao inserir cliente: " + e.getMessage());
          }
      }

      /**
       * Retorna todos os clientes cadastrados.
       * @return lista de clientes
       */
      public List<Cliente> buscarTodos() {
          List<Cliente> lista = new ArrayList<>();
          String sql = "SELECT * FROM clientes";
          // implementação...
          return lista;
      }
  }
  ```

- **Commits ao longo do desenvolvimento — padrão esperado:**

  | Momento | Exemplo de mensagem de commit |
  |---------|------------------------------|
  | Estrutura criada | `"estrutura inicial do projeto — pastas e pacotes"` |
  | Classes modeladas | `"adiciona classes Cliente e Funcionario com herança de Pessoa"` |
  | Banco criado | `"adiciona script SQL de criação das tabelas"` |
  | Conexão funcionando | `"implementa classe ConexaoDB com método getConexao"` |
  | INSERT funcionando | `"implementa ClienteDAO.inserir com Prepared Statement"` |
  | SELECT funcionando | `"implementa ClienteDAO.buscarTodos com ResultSet"` |

- **Orientações de qualidade desde o primeiro commit:**
  - Nomes de classes, métodos e variáveis descritivos desde o início — refatorar depois custa mais
  - Documentar cada método público ao escrever, não depois — documentação retroativa é sempre incompleta
  - Commit a cada funcionalidade que funciona — não acumular tudo para um commit no final da aula
  - Nenhum código comentado desnecessariamente — código morto não vai para o repositório

---

## Organização do Tempo

| Etapa | Atividade |
|-------|-----------|
| Abertura | Chamada · revisão rápida dos grupos, temas e repositórios criados na SA 33 · orientações específicas para esta SA |
| Kickoff por grupo | Professor passa 2 minutos com cada grupo revisando o Canvas e o escopo — garantindo que o que será desenvolvido é tecnicamente viável no prazo |
| Desenvolvimento orientado | Grupos desenvolvem na IDE com suporte do professor · foco na ordem: estrutura → classes → banco → conexão → primeiros módulos |
| Checkpoint intermediário | A 20 minutos do fim o professor faz uma rodada rápida verificando o progresso de cada grupo e orientando quem está travado |
| Fechamento | Cada grupo faz um commit final com o progresso da SA · professor registra o status de cada grupo para acompanhamento |

---

## Acompanhamento do Projeto — Ficha de Progresso

> Professor preenche ao final de cada SA de desenvolvimento (34, 35, 36)

| Grupo | Tema | Estrutura | Classes | Banco | CRUD | Testes | Commits | Status |
|-------|------|-----------|---------|-------|------|--------|---------|--------|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |

---

## Avaliação

- Avaliação formativa contínua ao longo do desenvolvimento
- Critérios verificados ao final desta SA:
  - Repositório atualizado com ao menos 3 commits descritivos
  - Classes modeladas com herança e encapsulamento
  - Banco de dados criado com script SQL commitado
  - INSERT e SELECT funcionando com Prepared Statement
- Avaliação somativa será aplicada na SA 38 (apresentação final) e SA 39 (avaliação do 3º Trimestre)

---

## Conexão com Conteúdos

| | Tema |
|---|------|
| ← SA anterior | SA 33 — 14/10/2026 · Projeto Final — Apresentação e Briefing |
| Próxima SA → | SA 35 — 28/10/2026 · Projeto Final — Desenvolvimento Parte 2 |

---

## Recursos Necessários

- Projetor ou TV
- Computador com HDMI
- Computadores com VS Code, SGBD e acesso ao GitHub
- Ficha de progresso por grupo (para uso do professor)
- Ficha do Canvas do projeto (cada grupo traz da SA 33)
- Quadro branco e marcador

---

## Observações do Professor
